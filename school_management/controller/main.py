from odoo import http
from odoo.http import request

class SchoolController(http.Controller):

    @http.route('/students', type='http', auth='public', website=True)
    def student_list(self, **kwargs):
        students = request.env['school.student'].sudo().search([])

        return request.render(
            'school_management.student_list_template',
            {'students': students}
        )