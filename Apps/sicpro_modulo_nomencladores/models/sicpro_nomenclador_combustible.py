# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EstadosCombustible(models.Model):
    _name = 'sicpro.nomenclador.combustible'
    _description = 'Tipo de Combustible'

    name = fields.Char(required=True, string='Combustible')
    precio = fields.Float(string="Precio",  required=False, )
    active = fields.Boolean(string="Activo", default=True, )