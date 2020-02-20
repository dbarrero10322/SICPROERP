# -*- coding: utf-8 -*-

{
     'name': 'SICPRO - Registros de Auditoria',
    'summary': 'Módulo para la auditoria del sistema',
    'version': '1.0',
    'category': 'Herramientas',
    'summary': """Este módulo se encargara de auditar todas las acciones de la aplicación.""",
    'author': 'Daniel Barrero Reyes',
    'website': 'https://www.facebook.com/daniel.barrero.1253',
    'license': 'AGPL-3',
    'sequence': 2,
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_cron.xml',
        'views/auditlog_view.xml',
        'views/http_session_view.xml',
        'views/http_request_view.xml',
    ],
    'application': True,
    'installable': True,
}
