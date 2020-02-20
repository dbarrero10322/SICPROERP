# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EstadosMunicipios(models.Model):
    _name = 'sicpro.nomenclador.municipio'
    _description = 'Municipios'

    name = fields.Char(required=True, string='Municipio')
    provincia = fields.Many2one(comodel_name="sicpro.nomenclador.provincia", string="Provincia", required=True,)
    active = fields.Boolean(string="Activo", default=True, )