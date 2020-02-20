# -*- coding: utf-8 -*-
from odoo import models, fields, api


class dbrmodulehistorial(models.Model):
    _name = 'dbr.module.historial'

    TYPES = [
        ('install', 'Instalado'),
        ('upgrade', 'Actualizado'),
        ('uninstall', 'Desintalado'),
    ]

    module_name = fields.Char(required=True, string='Módulo')
    type = fields.Selection(TYPES, required=True, string='Acción')
    user_id = fields.Many2one('res.users', string='Autor', required=True)


class IrModuleModule(models.Model):
    _inherit = 'ir.module.module'

    def _button_immediate_function(self, function):
        res = super(IrModuleModule, self)._button_immediate_function(function)
        for module in self:
            action_type = {
                'button_install': 'install',
                'button_upgrade': 'upgrade',
                'button_uninstall': 'uninstall',
            }.get(function.__name__)

            if action_type:
                self.env['dbr.module.historial'].sudo().create({
                    'module_name': module.name,
                    'type': action_type,
                    'user_id': self._uid,
                })
        return res
