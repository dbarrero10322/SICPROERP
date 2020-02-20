# -*- coding: utf-8 -*-


{
    'name': 'SICPRO - Automatización Ext.',
    'summary': 'Módulo para extender la automatización',
    'version': '1.0',
    'category': 'Herramientas',
    'summary': """Este módulo se encargara de ampliar el acceso a la 
                automatización.""",
    'author': 'Daniel Barrero Reyes',
    'website': 'https://www.facebook.com/daniel.barrero.1253',
    'license': 'AGPL-3',
    'sequence': 2,

    "depends": [
        "base_automation",'sicpro_modulo_nomencladores',"smile_log",
    ],

    "data": [
        "security/ir.model.access.csv",
        "data/ir_cron_data.xml",
        "views/ir_actions.xml",
        "views/ir_model_methods_view.xml",
        "views/base_automation_view.xml",
    ],
    "auto_install": False,
    "installable": True,
    "application": True,
}
