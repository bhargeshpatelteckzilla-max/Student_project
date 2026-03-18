from odoo import models, fields

class Teacher(models.Model):
    _name = 'school.teacher'
    _description = 'Teacher'

    name = fields.Char(string="Name", required=True)
    subject = fields.Char(string="Subject")

    class_ids = fields.One2many(
        'school.class',
        'teacher_id',
        string="Classes"
    )