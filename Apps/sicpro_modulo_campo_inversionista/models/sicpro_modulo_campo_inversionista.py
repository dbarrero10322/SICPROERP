# -*- coding: utf-8 -*-


from odoo import fields, models


class ModuloCampoInversionista(models.Model):
    _inherit = 'res.users'

    inversionista = fields.Boolean(string="Inversionista", default='False')


