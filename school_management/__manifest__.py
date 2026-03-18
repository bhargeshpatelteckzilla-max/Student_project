{
    'name': 'School Management',
    'version': '1.0',
    'summary': 'Basic School Management System',
    'depends': ['base','website'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_report.xml',
        'views/student_views.xml',
        'views/teacher_views.xml',
        'views/class_views.xml',
        'wizard/parent_wizard_views.xml',
        'views/student_templates.xml',

        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}