{
    'name': 'Custom Dark Mode',
    'version': '1.0',
    'category': 'Customization',
    'summary': 'Custom dark mode for Odoo',
    'depends': ['web'],
    'data': [
        'views/assets.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'custom_dark_mode/static/src/css/dark_mode.css',
        ],
    },
}
