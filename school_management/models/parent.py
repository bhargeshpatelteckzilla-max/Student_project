from odoo import models, fields

class Parent(models.Model):
    _name = 'school.parent'
    _description = 'Parent'

    name = fields.Char(string="Parent Name", required=True)
    phone = fields.Char(string="Phone")
    relation = fields.Selection([
        ('father', 'Father'),
        ('mother', 'Mother'),
        ('guardian', 'Guardian')
    ], string="Relation")

    student_id = fields.Many2one('school.student', string="Student")