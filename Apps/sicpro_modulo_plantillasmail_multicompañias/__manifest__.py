# Copyright 2017 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'SICPRO - Mail Template multi-Compañias',
    'summary': 'Módulo para agregar campo multicompañia',
    'version': '1.0',
    'category': 'Aplicaciones',
    'summary': """Este modulo agrega a las plantillas de correo el campo de compañias.""",
    'author': 'Daniel Barrero Reyes',
    'website': 'https://www.facebook.com/daniel.barrero.1253',
    'license': 'AGPL-3',
    'sequence': 2,
    'depends': ['mail'],
    'post_init_hook': 'post_init_hook',
    'data': [
        'security/mail_template.xml',
        'views/mail_template.xml'
    ],
    'installable': True,
    'application': True,
}
