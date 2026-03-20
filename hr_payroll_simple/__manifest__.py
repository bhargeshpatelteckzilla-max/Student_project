{
    'name': 'Simple HR Payroll',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Automated payroll based on attendance',
    'depends': ['hr', 'hr_attendance','hr_payroll'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'report/payslip_report.xml',

        'data/salary_rules.xml',
        'views/hr_payslip_views.xml',

    ],
    'installable': True,
    'application': True,
}