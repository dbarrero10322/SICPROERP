# -*- coding: utf-8 -*-

{
    "name": "Dependency for sicpro_modulo_temavisual",
    "summary": "Dependency for sicpro_modulo_temavisual. This module will be obsolete when web_responsive v13 is available in the Odoo Appstore.",
    "version": "13.0.1.0.0",
    "category": "Hidden",
    "website": "https://github.com/OCA/web",
    "author": "LasLabs, Tecnativa, "
              "Odoo Community Association (OCA)",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        'web',
        'mail',
    ],
    "data": [
        'views/assets.xml',
        'views/res_users.xml',
        'views/web.xml',
    ],
    'qweb': [
        'static/src/xml/apps.xml',
        'static/src/xml/form_view.xml',
        'static/src/xml/navbar.xml',
    ],
}
