from odoo import models, fields

class ParentWizard(models.TransientModel):
    _name = 'parent.wizard'
    _description = 'Parent Wizard'

    name = fields.Char(string="Parent Name", required=True)
    phone = fields.Char(string="Phone")
    relation = fields.Selection([
        ('father', 'Father'),
        ('mother', 'Mother'),
        ('guardian', 'Guardian')
    ], string="Relation")

    def action_add_parent(self):
        student_id = self.env.context.get('active_id')

        self.env['school.parent'].create({
            'name': self.name,
            'phone': self.phone,
            'relation': self.relation,
            'student_id': student_id
        })