# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EstadosOrdenes(models.Model):
    _name = 'sicpro.nomenclador.especialidad'
    _description = 'Especialidades'

    name = fields.Char(required=True, string='Especialidad')
    codigo = fields.Integer(string="Código", required=True, )
    letra = fields.Char(string="Letra", required=True,)
    company_id = fields.Many2one(comodel_name="res.company", string="Proceso", required=True, )
    active = fields.Boolean(string="Activo", default=True, )