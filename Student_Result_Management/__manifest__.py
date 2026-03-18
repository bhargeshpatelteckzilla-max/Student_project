{
    'name': 'Student Result Management',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'report/student_result_report.xml',
        'report/student_result_template.xml',
        'views/student_result_views.xml',


    ],
    'installable': True,
    'application': True,
}