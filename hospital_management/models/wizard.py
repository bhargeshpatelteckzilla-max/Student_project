from odoo import models, fields, api

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