# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Hotel Management',
    'version': '1.0.0',
    'category': 'Hotel',
    'author': 'tripleP',
    'sequence': -100,
    'summary': 'Hotel Management System',
    'description': """Hospital Management System""",
    'depends': ['mail', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/cancel_appointment_view.xml',
        'views/menu.xml',
        'views/guest_view.xml',
        'views/female_guest_view.xml',
        'views/male_guest_view.xml',
        'views/appointment_view.xml',
        'views/guest_tag_view.xml',
        'wizard/cancel_appointment_view.xml',
        'data/guest_tag_data.xml',
        'data/guest.tag.csv',
        'data/guest_tag_data.xml',
        'data/sequence_data.xml',
        'views/playground_view.xml'

    ],
    'demo': [],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
