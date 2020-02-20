# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EstadosTiposOrdenes(models.Model):
    _name = 'sicpro.nomenclador.tipos.ordenes'
    _description = 'Tipos de Ordenes'

    name = fields.Char(required=True, string='Tipo')
    codigo = fields.Char(string="Código", required=True, )
    company_id = fields.Many2one(comodel_name="res.company", string="Proceso", required=True, )
    active = fields.Boolean(string="Activo", default=True, )