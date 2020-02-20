# -*- coding: utf-8 -*-

from odoo import fields, models


class MailTemplate(models.Model):

    _inherit = 'mail.template'

    company_id = fields.Many2one(
        'res.company',
        'Company',
        default=lambda self: self.env['res.company']._company_default_get(
            'mail.template'
        ),
        ondelete="set null",
    )
