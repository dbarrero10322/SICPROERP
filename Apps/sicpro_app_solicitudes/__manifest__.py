# -*- coding: utf-8 -*-
{
    'name': 'SICPRO - APP: Solicitudes',
    'summary': 'Aplicación de Solicitudes',
    'version': '1.0',
    'category': 'Aplicaciones',
    'summary': """Esta aplicación se encargara de todo el control de las 
    solicitudes de trabajos""",
    'author': 'Daniel Barrero Reyes',
    'website': 'https://www.facebook.com/daniel.barrero.1253',
    'license': 'AGPL-3',
    'sequence': 1,
    'depends': ['base','sicpro_modulo_nomencladores','sicpro_app_proyectos','mail',],

    'data': [
        'security/solicitudes_security.xml',
        'security/ir.model.access.csv',
        'views/app_solicitudes_general.xml',
        'views/app_solicitudes_inversionistas.xml',

    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'images': [],
}