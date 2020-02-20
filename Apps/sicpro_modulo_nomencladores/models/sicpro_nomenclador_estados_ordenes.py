# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EstadosOrdenes(models.Model):
    _name = 'sicpro.nomenclador.estados.ordenes'
    _description = 'Meses'

    name = fields.Char(required=True, string='Estado')
    descripcion = fields.Char(string="Descripción", required=True, )
    company_id = fields.Many2one(comodel_name="res.company", string="Proceso", required=True, )
    active = fields.Boolean(string="Activo", default=True, )