# -*- encoding: utf-8 -*-


{
    'name': 'SICPRO - Campo Mail/User',
    'summary': 'Módulo para agregar campo de correo',
    'version': '1.0',
    'category': 'Aplicaciones',
    'summary': """Este modulo agrega al usuario el campo de correo separandolo del username""",
    'author': 'Daniel Barrero Reyes',
    'website': 'https://www.facebook.com/daniel.barrero.1253',
    'license': 'AGPL-3',
    'sequence': 2,

    'depends': [
        'base',
        'web',
    ],
    'data': [
        'views/res_users_view.xml',
        #'views/login_layout.xml',
    ],
    'installable': True,
    'application': True,
}
