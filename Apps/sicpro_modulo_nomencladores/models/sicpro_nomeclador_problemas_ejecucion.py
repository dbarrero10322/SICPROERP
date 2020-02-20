# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EstadosProblemasEjecucion(models.Model):
    _name = 'sicpro.nomenclador.problemas.ejecucion'
    _description = 'Problemas en la Ejecución'

    name = fields.Char(required=True, string='Problemas')
    company_id = fields.Many2one(comodel_name="res.company", string="Proceso", required=True, )
    active = fields.Boolean(string="Activo", default=True, )