# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EstadosMeses(models.Model):
    _name = 'sicpro.nomenclador.meses'
    _description = 'Meses'

    name = fields.Char(required=True, string='Mes')
    codigo_mes= fields.Integer(string="Código Mes", required=True, )
    active = fields.Boolean(string="Activo", default=True, )