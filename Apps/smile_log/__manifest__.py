# -*- coding: utf-8 -*-


{
    'name': 'SICPRO - Registros Log',
    'summary': 'Módulo para registrar los Long',
    'version': '1.0',
    'category': 'Herramientas',
    'summary': """Este módulo se encargara de todo el control del archivo logs 
    de la aplicación.""",
    'author': 'Daniel Barrero Reyes',
    'website': 'https://www.facebook.com/daniel.barrero.1253',
    'license': 'AGPL-3',
    'sequence': 2,

    "depends": ['base','sicpro_modulo_nomencladores'],
    "data": [
        "security/smile_log_security.xml",
        "security/ir.model.access.csv",
        "views/smile_log_view.xml",
    ],
    "installable": True,
    'application': True,
    "active": False,
}
