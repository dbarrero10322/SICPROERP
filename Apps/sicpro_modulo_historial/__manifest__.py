# -*- coding: utf-8 -*-
{
    'name': 'SICPRO - Historial de Aplicaciones',
    'version': '1.0',
    'summary': """Visualización del historial de instalación / desinstalación / actualización de los módulos""",
    'description': """Visualización del historial de instalación / desinstalación / actualización de los módulos""",
    'category': 'Herramientas',
    'author': 'Daniel Barrero Reyes',
    'website': "https://www.facebook.com/daniel.barrero.1253",
    'license': 'AGPL-3',
    'sequence': 2,
    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/dbr_module_historial_view.xml',
    ],
    'demo': [

    ],
    'images': [],
    'qweb': [],

    'installable': True,
    'auto_install': False,
    'application': True,
}
