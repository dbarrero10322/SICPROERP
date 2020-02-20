# -*- coding: utf-8 -*-

{
    'name': 'SICPRO - APP: Clientes',
    'summary': 'Aplicación de Clientes',
    'version': '1.0',
    'category': 'Aplicaciones',
    'summary': """Esta aplicación le ofrece una vista rápida de su directorio de clientes, 
                   accesible desde su página de inicio.""",
    'author': 'Daniel Barrero Reyes',
    'website': 'https://www.facebook.com/daniel.barrero.1253',
    'license': 'AGPL-3',
    'sequence': 1,
    'depends': ['base','sicpro_modulo_nomencladores','mail',],

    'data': [
        'security/clientes_security.xml',
        'security/ir.model.access.csv',
        'views/clientes.xml',
        'views/etiquetas.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'images': [],
}