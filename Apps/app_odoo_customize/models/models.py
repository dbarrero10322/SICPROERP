# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Module(models.Model):
    _inherit = 'ir.module.module'

    def module_multi_uninstall(self):
        modules = self.browse(self.env.context.get('active_ids'))
        [module.button_immediate_uninstall() for module in modules if module not in ['base', 'web']]

