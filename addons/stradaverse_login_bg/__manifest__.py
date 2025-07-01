# -*- coding: utf-8 -*-

{
    'name': "Stradaverse Login Background Image",
    'version': '16.0.0.0',
    'summary': """Set background image in login page.""",
    'description': """Set background image in Login page.""",
    'license': 'OPL-1',
    'website': "https://www.stradaverse.ai/",
    'author': 'Stradaverse',
    'category': '',
    'depends': ['base', 'portal'],
    'data': [
        'views/res_company.xml',
        'views/webclient_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'stradaverse_login_bg/static/src/scss/stradaverse_login.scss',
        ],
    },
    'sequence': 1,
    "application": True,
    "installable": True,
    'auto_install': True
}
