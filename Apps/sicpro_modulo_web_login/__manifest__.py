# -*- encoding: utf-8 -*-

{
    'name': 'SICPRO - Login Screen',
    'summary': 'Configurar login de inicio',
    'version': '1.0',
    'category': 'Herramientas',
    'summary': """Crear una nueva configuración del login para SICPRO ERP""",
    'author': 'Daniel Barrero Reyes',
    'website': 'https://www.facebook.com/daniel.barrero.1253',
    'license': 'AGPL-3',
    'sequence': 2,
    'depends': [],
    'data': [
        'data/ir_config_parameter.xml',
        'templates/website_templates.xml',
        'templates/webclient_templates.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'images': [],
}
