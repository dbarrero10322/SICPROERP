# -*- coding: utf-8 -*-

from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    chatter_position = fields.Selection([
        ('normal', 'Normal'),
        ('sided', 'Sided'),
    ], string="Chatter Position", default='normal')

    def __init__(self, pool, cr):
        """  Anulación de __init__ para agregar derechos de acceso.
        Los derechos de acceso están deshabilitados de forma predeterminada, pero se permiten en algunos
        campos definidos en self.SELF_ {READ / WRITE} ABLE_FIELDS.
                """
        super(ResUsers, self).__init__(pool, cr)
        # duplicate list to avoid modifying the original reference
        type(self).SELF_WRITEABLE_FIELDS = list(self.SELF_WRITEABLE_FIELDS)
        type(self).SELF_WRITEABLE_FIELDS.extend(['chatter_position'])
        # duplicate list to avoid modifying the original reference
        type(self).SELF_READABLE_FIELDS = list(self.SELF_READABLE_FIELDS)
        type(self).SELF_READABLE_FIELDS.extend(['chatter_position'])
