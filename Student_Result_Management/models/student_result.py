from odoo import models, fields, api

class StudentResult(models.Model):
    _name = 'student.result'
    _description = 'Student Result'

    student_id = fields.Many2one('res.partner', string="Student")
    guardian_id = fields.Many2one('res.partner', string="Guardian")
    student_class = fields.Char(string="Class")

    marks_ids = fields.One2many('student.marks', 'result_id', string="Marks")

    percentage = fields.Float(string="Percentage", compute="_compute_result", store=True)
    result = fields.Selection([
        ('pass', 'Pass'),
        ('fail', 'Fail'),
        ('atkt', 'ATKT')
    ], compute="_compute_result", store=True)

    grade = fields.Char(string="Grade", compute="_compute_result", store=True)

    @api.depends('marks_ids.marks', 'marks_ids.pass_status')
    def _compute_result(self):
        for rec in self:
            total = sum(rec.marks_ids.mapped('marks'))
            subjects = len(rec.marks_ids)

            fail_count = len(rec.marks_ids.filtered(lambda x: not x.pass_status))

            rec.percentage = (total / (subjects * 100)) * 100 if subjects else 0

            # Result Logic
            if fail_count == 0:
                rec.result = 'pass'
            elif 1 <= fail_count <= 3:
                rec.result = 'atkt'
            else:
                rec.result = 'fail'

            # Grade Logic (only if pass)
            if rec.result == 'pass':
                if rec.percentage >= 95:
                    rec.grade = 'A+'
                elif rec.percentage >= 90:
                    rec.grade = 'A'
                elif rec.percentage >= 80:
                    rec.grade = 'B+'
                elif rec.percentage >= 70:
                    rec.grade = 'B'
                elif rec.percentage >= 60:
                    rec.grade = 'C+'
                elif rec.percentage >= 40:
                    rec.grade = 'C'
                else:
                    rec.grade = ''
            else:
                rec.grade = ''


class StudentMarks(models.Model):
    _name = 'student.marks'
    _description = 'Student Marks'

    result_id = fields.Many2one('student.result', string="Result")

    subject = fields.Char(string="Subject")
    marks = fields.Float(string="Marks")

    pass_status = fields.Boolean(string="Pass", compute="_compute_pass", store=True)

    @api.depends('marks')
    def _compute_pass(self):
        for rec in self:
            rec.pass_status = rec.marks >= 32