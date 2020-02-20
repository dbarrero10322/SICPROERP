# -*- coding: utf-8 -*-

{
    'name': 'SICPRO - Notificaciones',
    'summary': 'Notificaciones a los usuarios',
    'version': '1.0',
    'category': 'Herramientas',
    'summary': """Este módulo envia los avisos de notificaciones ante eventos 
                a todos los usuarios""",
    'author': 'Daniel Barrero Reyes',
    'website': 'https://www.facebook.com/daniel.barrero.1253',
    'license': 'AGPL-3',
    'sequence': 2,

    'depends': [
        'sicpro_modulo_nomencladores',
        'web',
        'bus',
        'base',
    ],
    'data': [
        'views/web_notify.xml'
    ],
    'demo': [
        'views/res_users_demo.xml'
    ],
    'installable': True,
    'application': True,
}
