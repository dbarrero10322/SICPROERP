# -*- coding: utf-8 -*-

{
    'name': 'SICPRO - Registros de Usuario',
    'version': '1.0',
    'summary': """Detalles del usuario de inicio de sesión y dirección IP""",
    'description': """Este módulo registra la información de inicio de sesión del usuario""",
    'category': 'Herramientas',
    'author': 'Daniel Barrero Reyes',
    'website': "https://www.facebook.com/daniel.barrero.1253",
    'license': 'AGPL-3',
    'sequence': 2,
    'depends': ['web'],

    'data': [
        'security/ir.model.access.csv',
        'views/login_user_views.xml'],
    'demo': [],
    'images': [],
    'qweb': [],

    'installable': True,
    'auto_install': False,
    'application': True,
}