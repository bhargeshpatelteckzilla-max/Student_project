import io
import base64
import xlsxwriter

def action_print_excel(self):
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
        'res_model': self._name,
    })

    return {
        'type': 'ir.actions.act_url',
        'url': f'/web/content/{attachment.id}?download=true',
        'target': 'self',
    }