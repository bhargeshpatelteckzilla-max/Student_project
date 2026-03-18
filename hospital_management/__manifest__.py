{
    'name': 'Hospital Management',
    'version': '19.0.1.0.0',
    'summary': 'Manage patients and appointments with wizard and report',
    'category': 'Healthcare',
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/patient_views.xml',
        'views/appointment_views.xml',
        'views/wizard_views.xml',

        # ✅ FIXED ORDER
        'reports/appointment_report_template.xml',
        'reports/appointment_report.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}