# -*- coding: utf-8 -*-

{
    'name': 'SICPRO - Personalización Avanzada',
    'version': '1.0',
    'author': 'Daniel Barrero Reyes',
    'category': 'Herramientas',
    'website': 'https://www.facebook.com/daniel.barrero.1253',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': """Personalización del módulo SICPRO.""",
    'description': """Este módulo permite personalizar SICPRO ERP""",
    'images': [],
    'depends': [
        'base_setup',
        'web',
        'mail',
        'iap',
        # 'digest',
        # when enterprise
        # 'web_mobile'
    ],
    'data': [
        'views/app_odoo_customize_views.xml',
        'views/app_theme_config_settings_views.xml',
        'views/res_config_settings_views.xml',
        'views/ir_model_views.xml',
        'views/ir_views.xml',
        # data
        'data/ir_config_parameter.xml',
        'data/ir_module_module.xml',
        # 'data/digest_template_data.xml',
        'data/res_company_data.xml',
        'data/res_groups.xml',
        'security/ir.model.access.csv',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'demo': [],
    'test': [],
    'css': [],
    'js': [],
    # 'pre_init_hook': 'pre_init_hook',
    # 'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': True,
    'auto_install': False,
}
