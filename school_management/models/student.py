from odoo import models, fields

class Student(models.Model):
    _name = 'school.student'
    _description = 'Student'

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string="Gender")

    class_id = fields.Many2one('school.class', string="Class")

    parent_ids = fields.One2many(
        'school.parent',
        'student_id',
        string="Parents"
    )

    def action_open_parent_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Add Parent',
            'res_model': 'parent.wizard',
            'view_mode': 'form',
            'target': 'new',
        }