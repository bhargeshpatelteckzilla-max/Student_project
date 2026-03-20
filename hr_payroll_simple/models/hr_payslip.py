from odoo import models, fields, api

class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    attendance_line_ids = fields.One2many(
        'hr.payslip.attendance.line',
        'payslip_id',
        string='Attendance Details'
    )
    total_attendance_hours = fields.Float(
        string='Total Attendance Hours',
        compute='_compute_attendance_hours',
        store=True
    )

    @api.depends('date_from', 'date_to', 'employee_id')
    def _compute_attendance_hours(self):
        for slip in self:
            if slip.employee_id and slip.date_from and slip.date_to:
                # Fetch attendances within the period
                attendances = self.env['hr.attendance'].search([
                    ('employee_id', '=', slip.employee_id.id),
                    ('check_in', '>=', slip.date_from),
                    ('check_out', '<=', slip.date_to),
                ])
                total = sum(attendance.worked_hours for attendance in attendances)
                slip.total_attendance_hours = total

                # Create detailed lines (optional)
                slip.attendance_line_ids.unlink()
                for att in attendances:
                    self.env['hr.payslip.attendance.line'].create({
                        'payslip_id': slip.id,
                        'attendance_id': att.id,
                        'hours': att.worked_hours,
                        'date': att.check_in.date(),
                    })
            else:
                slip.total_attendance_hours = 0.0

    def compute_sheet(self):
        """Override to ensure our custom salary rule is processed."""
        res = super().compute_sheet()
        # If you want to add a line manually instead of using a salary rule,
        # you can do it here. But we recommend using a salary rule (see below).
        return res


class HrPayslipAttendanceLine(models.Model):
    _name = 'hr.payslip.attendance.line'
    _description = 'Payslip Attendance Line'

    payslip_id = fields.Many2one('hr.payslip', string='Payslip', ondelete='cascade')
    attendance_id = fields.Many2one('hr.attendance', string='Attendance')
    hours = fields.Float(string='Hours')
    date = fields.Date(string='Date')