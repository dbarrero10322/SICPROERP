# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EstadosTiposPasjes(models.Model):
    _name = 'sicpro.nomenclador.tipos.pasajes'
    _description = 'Tipos de Ordenes'

    name = fields.Char(required=True, string='Tipo')
    company_id = fields.Many2one(comodel_name="res.company", string="Proceso", required=True, )
    active = fields.Boolean(string="Activo", default=True, )