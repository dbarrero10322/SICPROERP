# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EstadosCuentasContables(models.Model):
    _name = 'sicpro.nomenclador.cuentas.contables'
    _description = 'Cuentas Contables'

    name = fields.Char(required=True, string='Cuentas')
    descripcion = fields.Char(string="Descripción", required=True,)
    active = fields.Boolean(string="Activo", default=True, )