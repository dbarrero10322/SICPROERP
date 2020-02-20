# Copyright 2019 Camptocamp


{
    'name': 'SICPRO - Id de Procesos',
    'summary': 'Módulo para agregar campo id a la compañia',
    'version': '1.0',
    'category': 'Aplicaciones',
    'summary': """Este modulo agrega a la compañia el campo de id para su identificación en futuras acciones""",
    'author': 'Daniel Barrero Reyes',
    'website': 'https://www.facebook.com/daniel.barrero.1253',
    'license': 'AGPL-3',
    'sequence': 2,

    'depends': [
        'base',
        'web',
    ],
    'data': [
        'views/res_company_view.xml',
    ],
    'installable': True,
    'application': True,
}
