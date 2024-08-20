{
    'name': 'Real Estate',
    'version': '1.0.0',
    'category': 'estate',
    'author': 'Ray',
    'sequence': -100,
    'summary': 'Real Estate',
    'description': """Real Estate""",
    'depends': ['mail', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_view.xml',
        'views/menu.xml',
        'views/estate_property_type_view.xml',
        'views/estate_property_tag_view.xml',
        'views/estate_property_offer_view.xml',

    ],
    'demo': [],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
