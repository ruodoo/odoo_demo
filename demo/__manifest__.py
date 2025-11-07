{
    'name': 'Demo App',
    'version': '1.0',
    'summary': 'A minimal demo app for Odoo',
    'description': 'This is a minimal demo app for Odoo.',
    'author': 'xdo',
    'depends': ['base'],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'data': [
        'data/hobbies.xml',
        'data/ir.model.access.csv',
        'data/views.xml',
    ],
}