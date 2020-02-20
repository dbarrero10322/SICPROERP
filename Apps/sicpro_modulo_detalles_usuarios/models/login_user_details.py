# -*- coding: utf-8 -*-


import logging
from itertools import chain
from odoo.http import request
from odoo import models, fields, api

_logger = logging.getLogger(__name__)
USER_PRIVATE_FIELDS = ['password']
concat = chain.from_iterable


class LoginUserDetail(models.Model):
    _inherit = 'res.users'

    @api.model
    def _check_credentials(self, password):
        result = super(LoginUserDetail, self)._check_credentials(password)
        ip_address = request.httprequest.environ['REMOTE_ADDR']
        vals = {'name': self.name,
                'ip_address': ip_address
                }
        self.env['login.detail'].sudo().create(vals)
        return result


class LoginUpdate(models.Model):
    _name = 'login.detail'

    name = fields.Char(string="Nombre de usuario")
    date_time = fields.Datetime(string="Fecha y hora de inicio de sesión", default=lambda self: fields.datetime.now())
    ip_address = fields.Char(string="Dirección IP")
