# -*- encoding: utf-8 -*-
{
    'name': 'SICPRO - Numeración de Lista',
    'version': '1.0',
    'summary': """Numera los datos de la vista lisata""",
    'description': """Este módulo se encarga de autoenumerar los datos de las vistas de árbol o tree""",
    'category': 'Herramientas',
    'author': 'Daniel Barrero Reyes',
    'website': "https://www.facebook.com/daniel.barrero.1253",
    'license': 'AGPL-3',
    'sequence': 2,

    "depends": ['web'],
    'data': [
             'views/listview_templates.xml',
             ],
    "images": [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
