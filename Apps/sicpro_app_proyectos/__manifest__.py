# -*- coding: utf-8 -*-
{
    'name': 'SICPRO - APP: Proyectos',
    'summary': 'Aplicación de Proyectos',
    'version': '1.0',
    'category': 'Aplicaciones',
    'summary': """Esta aplicación se encargara de todo el control de la 
    documentación de los proyectos""",
    'author': 'Daniel Barrero Reyes',
    'website': 'https://www.facebook.com/daniel.barrero.1253',
    'license': 'AGPL-3',
    'sequence': 1,
    'depends': ['base','sicpro_modulo_nomencladores','mail',],

    'data': [
        'security/proyecto_security.xml',
        'security/ir.model.access.csv',
        'views/app_proyectos_general.xml',

    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'images': [],
}