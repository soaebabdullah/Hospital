{
    'name': 'Hospital Management',
    'version': '13.0.1.0.0',
    'category': 'Tools',
    'summery': 'Module for managing the Hospitals',
    'sequence': '10',
    'license': 'AGPL-3',
    'author': 'Odoo Mates',
    'maintainer': 'Odoo Mates',
    'website': 'odoomates.com',
    'depends': ['sale'],
    'demo': [],
    'data': [
        'views/patient.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'reports/report.xml',
        'reports/patient_card.xml',

    ],
    'installable': True,
    'applicating': True,
    'auto_install': False,

}
