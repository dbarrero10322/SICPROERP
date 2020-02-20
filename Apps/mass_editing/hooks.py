# -*- coding: utf-8 -*-

from odoo.api import Environment, SUPERUSER_ID


def uninstall_hook(cr, registry):
    """Delete the actions that were created with mass_editing when
    the module is uninstalled"""
    env = Environment(cr, SUPERUSER_ID, {})
    env['ir.actions.act_window'].search([
        ('res_model', '=', 'mass.editing.wizard')
    ]).unlink()
    return True
