# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EstadosProvicias(models.Model):
    _name = 'sicpro.nomenclador.provincia'
    _description = 'Provincias'

    name = fields.Char(required=True, string='Provincia')
    abreviatura = fields.Char(string="Abreviatura", required=True,)
    territorio = fields.Char(string="Territorio", required=True, )
    active = fields.Boolean(string="Activo", default=True, )