# -*- coding: utf-8 -*-

{
    "name": "SICPRO - Tema Sicpro Erp",
    "summary": "Tema para la plataforma SICPRO ERP",
    "version": "1.0",
    "category": "Temas",
    "website": 'https://www.facebook.com/daniel.barrero.1253',
	"description": """Tema Backend para la aplicación SICPRO ERP""",
	'images':['images/screen.png'],
    'author': 'Daniel Barrero Reyes',
    'license': 'LGPL-3',
    'sequence': 2,
    'installable': True,
    'application': True,
    'auto_install': False,
    "depends": [
        'web',
        'ow_web_responsive',
    ],
    "data": [
        'views/assets.xml',
		'views/res_company_view.xml',
    ],
}

