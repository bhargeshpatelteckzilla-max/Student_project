from odoo import models, fields, api
import io
import base64
import xlsxwriter
class HospitalAppointmentReportWizard(models.TransientModel):
    _name = 'hospital.appointment.report.wizard'
    _description = 'Appointment Report Wizard'

    date_from = fields.Datetime(string='From', required=True)
    date_to = fields.Datetime(string='To', required=True)
    doctor_id = fields.Many2one('res.users', string='Doctor', domain=[('share', '=', False)])

    def action_print_report(self):
        """Called when the 'Print' button is clicked. Returns the report action."""
        return self.env.ref('hospital_management.action_report_appointment').report_action(self)

    def get_appointments(self):
        """Returns appointments matching the wizard filters."""
        domain = [
            ('date', '>=', self.date_from),
            ('date', '<=', self.date_to),
        ]
        if self.doctor_id:
            domain.append(('doctor_id', '=', self.doctor_id.id))
        return self.env['hospital.appointment'].search(domain)

    def action_print_excel(self):  # ✅ inside class
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet('Appointments')

        bold = workbook.add_format({'bold': True})

        # Headers
        sheet.write(0, 0, 'Patient', bold)
        sheet.write(0, 1, 'Doctor', bold)
        sheet.write(0, 2, 'Date', bold)
        sheet.write(0, 3, 'Status', bold)
        sheet.write(0, 4, 'Notes', bold)

        row = 1
        appointments = self.get_appointments()

        for app in appointments:
            sheet.write(row, 0, app.patient_id.name)
            sheet.write(row, 1, app.doctor_id.name)
            sheet.write(row, 2, str(app.date))
            sheet.write(row, 3, app.state)
            sheet.write(row, 4, app.notes or '')
            row += 1

        workbook.close()
        output.seek(0)

        file_data = base64.b64encode(output.read())

        attachment = self.env['ir.attachment'].create({
            'name': 'Appointment_Report.xlsx',
            'type': 'binary',
            'datas': file_data,
            'mimetype': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        })

        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/content/{attachment.id}?download=true',
            'target': 'new',  # 🔥 IMPORTANT FIX
        }