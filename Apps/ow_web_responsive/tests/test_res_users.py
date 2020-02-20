# -*- coding: utf-8 -*-

from odoo.tests import common


class TestResUsers(common.TransactionCase):

    def test_chatter_position_wr(self):
        user_public = self.env.ref('base.public_user')

        self.assertEqual(user_public.chatter_position, 'normal')
        user_public.sudo(user_public).write({
            'chatter_position': 'sided',
        })
        self.assertEqual(user_public.chatter_position, 'sided')
