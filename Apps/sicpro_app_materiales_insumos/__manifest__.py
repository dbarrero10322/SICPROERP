# -*- coding: utf-8 -*-

{
    'name': 'SICPRO - APP: Materiales e Insumos',
    'summary': 'Aplicación de Materiales e Insumos',
    'version': '1.0',
    'category': 'Aplicaciones',
    'summary': """Esta aplicación le ofrece un control de los Materiales e Insumos que se utilizan en los procesos.""",
    'author': 'Daniel Barrero Reyes',
    'website': 'https://www.facebook.com/daniel.barrero.1253',
    'license': 'AGPL-3',
    'sequence': 1,
    'depends': ['base','sicpro_modulo_nomencladores','mail',],

    'data': [
        #'security/clientes_security.xml',
        #'security/ir.model.access.csv',
        #'views/clientes.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'images': [],
}