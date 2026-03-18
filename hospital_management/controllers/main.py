from odoo import http
from odoo.http import request


class HospitalController(http.Controller):

    @http.route('/hospital/appointments', type='http', auth='user', website=True)
    def list_appointments(self, **kwargs):
        appointments = request.env['hospital.appointment'].sudo().search([])

        return request.render('hospital_management.appointment_page', {
            'appointments': appointments
        })