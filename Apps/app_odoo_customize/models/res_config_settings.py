# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    app_system_name = fields.Char('Nombre del sistema', help="Configurar el nombre del sistema, que reemplaza a Odoo")
    app_show_lang = fields.Boolean('Mostrar Selector de Lenguajes',
                                   help="Cuando se habilita, el usuario puede cambiar rápidamente el idioma en el menú del usuario")
    app_show_debug = fields.Boolean('Mostrar depuración rápida',
                                    help="Cuando se habilita, todos los usuarios pueden ver el menú de depuración")
    app_show_documentation = fields.Boolean('Mostrar documentación',
                                            help="Cuando se habilita, el usuario puede visitar el manual del usuario")
    app_show_documentation_dev = fields.Boolean('Mostrar documentación del desarrollador',
                                                help="Cuando se habilita, el usuario puede visitar la documentación de desarrollo")
    app_show_support = fields.Boolean('Mostrar soporte',
                                      help="Cuando se habilita, el usuario puede visitar su sitio de soporte")
    app_show_account = fields.Boolean('Mostrar mi cuenta',
                                      help="Cuando se habilita, el usuario puede iniciar sesión en su sitio web")
    app_show_enterprise = fields.Boolean('Mostrar etiqueta de empresa',
                                         help="Desmarque para ocultar la etiqueta Enterprise")
    app_show_share = fields.Boolean('Mostrar panel de control compartido',
                                    help="Desmarque para ocultar el Panel de control de Odoo Share")
    app_show_poweredby = fields.Boolean('Mostrar Desarrollado por Odoo',
                                        help="Desmarque para ocultar el texto Desarrollado por")
    group_show_author_in_apps = fields.Boolean(string="Mostrar autor en el Panel de aplicaciones",
                                               implied_group='app_odoo_customize.group_show_author_in_apps',
                                               help="Desmarque para ocultar el autor y el sitio web en el panel de aplicaciones")

    app_documentation_url = fields.Char('URL de documentación')
    app_documentation_dev_url = fields.Char('URL de documentación del desarrollador')
    app_support_url = fields.Char('Url de soporte')
    app_account_title = fields.Char('Título de mi cuenta')
    app_account_url = fields.Char('Mi URL de mi cuenta')
    app_enterprise_url = fields.Char('Personalizar URL del módulo (por ejemplo, Enterprise)')

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        ir_config = self.env['ir.config_parameter'].sudo()
        app_system_name = ir_config.get_param('app_system_name', default='Personalizar')

        app_show_lang = True if ir_config.get_param('app_show_lang') == "True" else False
        app_show_debug = True if ir_config.get_param('app_show_debug') == "True" else False
        app_show_documentation = True if ir_config.get_param('app_show_documentation') == "True" else False
        app_show_documentation_dev = True if ir_config.get_param('app_show_documentation_dev') == "True" else False
        app_show_support = True if ir_config.get_param('app_show_support') == "True" else False
        app_show_account = True if ir_config.get_param('app_show_account') == "True" else False
        app_show_enterprise = True if ir_config.get_param('app_show_enterprise') == "True" else False
        app_show_share = True if ir_config.get_param('app_show_share') == "True" else False
        app_show_poweredby = True if ir_config.get_param('app_show_poweredby') == "True" else False

        app_documentation_url = ir_config.get_param('app_documentation_url',
                                                    default='#')
        app_documentation_dev_url = ir_config.get_param('app_documentation_dev_url',
                                                        default='#')
        app_support_url = ir_config.get_param('app_support_url', default='#')
        app_account_title = ir_config.get_param('app_account_title', default='Mi cuenta SICPRO')
        app_account_url = ir_config.get_param('app_account_url', default='#')
        app_enterprise_url = ir_config.get_param('app_enterprise_url', default='#')
        res.update(
            app_system_name=app_system_name,
            app_show_lang=app_show_lang,
            app_show_debug=app_show_debug,
            app_show_documentation=app_show_documentation,
            app_show_documentation_dev=app_show_documentation_dev,
            app_show_support=app_show_support,
            app_show_account=app_show_account,
            app_show_enterprise=app_show_enterprise,
            app_show_share=app_show_share,
            app_show_poweredby=app_show_poweredby,

            app_documentation_url=app_documentation_url,
            app_documentation_dev_url=app_documentation_dev_url,
            app_support_url=app_support_url,
            app_account_title=app_account_title,
            app_account_url=app_account_url,
            app_enterprise_url=app_enterprise_url
        )
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        ir_config = self.env['ir.config_parameter'].sudo()
        ir_config.set_param("app_system_name", self.app_system_name or "")
        ir_config.set_param("app_show_lang", self.app_show_lang or "False")
        ir_config.set_param("app_show_debug", self.app_show_debug or "False")
        ir_config.set_param("app_show_documentation", self.app_show_documentation or "False")
        ir_config.set_param("app_show_documentation_dev", self.app_show_documentation_dev or "False")
        ir_config.set_param("app_show_support", self.app_show_support or "False")
        ir_config.set_param("app_show_account", self.app_show_account or "False")
        ir_config.set_param("app_show_enterprise", self.app_show_enterprise or "False")
        ir_config.set_param("app_show_share", self.app_show_share or "False")
        ir_config.set_param("app_show_poweredby", self.app_show_poweredby or "False")

        ir_config.set_param("app_documentation_url",
                            self.app_documentation_url or "#")
        ir_config.set_param("app_documentation_dev_url",
                            self.app_documentation_dev_url or "#")
        ir_config.set_param("app_support_url", self.app_support_url or "#")
        ir_config.set_param("app_account_title", self.app_account_title or "Mi cuenta SICPRO")
        ir_config.set_param("app_account_url", self.app_account_url or "#")
        ir_config.set_param("app_enterprise_url", self.app_enterprise_url or "#")

    def set_module_url(self):
        sql = "UPDATE ir_module_module SET website = '%s' WHERE license like '%s' and website <> ''" % (self.app_enterprise_url, 'OEEL%')
        try:
            self._cr.execute(sql)
            self._cr.commit()
        except Exception as e:
            pass

    def remove_sales(self):
        to_removes = [

            ['sale.order.line', ],
            ['sale.order', ],

            ['sale.commission.line', ],

        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
                    self._cr.commit()
            # 更新序号
            seqs = self.env['ir.sequence'].search([('code', 'like', 'sale%')])
            for seq in seqs:
                seq.write({
                    'number_next': 1,
                })
        except Exception as e:
            raise Warning(e)
        return True

    def remove_product(self):
        to_removes = [
            # 清除产品数据
            ['product.product', ],
            ['product.template', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
                    self._cr.commit()
            # 更新序号,针对自动产品编号
            seqs = self.env['ir.sequence'].search([('code', '=', 'product.product')])
            for seq in seqs:
                seq.write({
                    'number_next': 1,
                })
        except Exception as e:
            pass  # raise Warning(e)
        return True

    def remove_product_attribute(self):
        to_removes = [
            # 清除产品属性
            ['product.attribute.value', ],
            ['product.attribute', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
                    self._cr.commit()
        except Exception as e:
            pass  # raise Warning(e)
        return True

    def remove_pos(self):
        to_removes = [
            # 清除POS单据
            ['pos.payment', ],
            ['pos.order.line', ],
            ['pos.order', ],
            ['pos.session', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
                    self._cr.commit()

            seqs = self.env['ir.sequence'].search([('code', 'like', 'pos.%')])
            for seq in seqs:
                seq.write({
                    'number_next': 1,
                })

            statement = self.env['account.bank.statement'].search([])
            for s in statement:
                s._end_balance()

        except Exception as e:
            pass  # raise Warning(e)
        return True

    def remove_purchase(self):
        to_removes = [
            # 清除采购单据
            ['purchase.order.line', ],
            ['purchase.order', ],
            ['purchase.requisition.line', ],
            ['purchase.requisition', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
                    self._cr.commit()
            # 更新序号
            seqs = self.env['ir.sequence'].search([('code', 'like', 'purchase.%')])
            for seq in seqs:
                seq.write({
                    'number_next': 1,
                })
            self._cr.execute(sql)
            self._cr.commit()
        except Exception as e:
            pass  # raise Warning(e)
        return True

    def remove_expense(self):
        to_removes = [
            # 清除
            ['hr.expense.sheet', ],
            ['hr.expense', ],
            ['hr.payslip', ],
            ['hr.payslip.run', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
                    self._cr.commit()
            # 更新序号
            seqs = self.env['ir.sequence'].search([
                ('code', 'like', 'hr.expense.%')])
            for seq in seqs:
                seq.write({
                    'number_next': 1,
                })
            self._cr.execute(sql)
            self._cr.commit()
        except Exception as e:
            pass  # raise Warning(e)
        return True

    def remove_mrp(self):
        to_removes = [
            # 清除生产单据
            ['mrp.workcenter.productivity', ],
            ['mrp.workorder', ],
            ['mrp.production.workcenter.line', ],
            ['change.production.qty', ],
            ['mrp.production', ],
            ['mrp.production.product.line', ],
            ['mrp.unbuild', ],
            ['change.production.qty', ],
            ['sale.forecast.indirect', ],
            ['sale.forecast', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
                    self._cr.commit()
            # 更新序号
            seqs = self.env['ir.sequence'].search([('code', 'like', 'mrp.%')])
            for seq in seqs:
                seq.write({
                    'number_next': 1,
                })
        except Exception as e:
            pass  # raise Warning(e)
        return True

    def remove_mrp_bom(self):
        to_removes = [
            # 清除生产BOM
            ['mrp.bom.line', ],
            ['mrp.bom', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
                    self._cr.commit()
        except Exception as e:
            pass  # raise Warning(e)
        return True

    def remove_inventory(self):
        to_removes = [
            # 清除库存单据
            ['stock.quant', ],
            ['stock.move.line', ],
            ['stock.package.level', ],
            ['stock.quantity.history', ],
            ['stock.quant.package', ],
            ['stock.move', ],
            # ['stock.pack.operation', ],
            ['stock.picking', ],
            ['stock.scrap', ],
            ['stock.picking.batch', ],
            ['stock.inventory.line', ],
            ['stock.inventory', ],
            ['stock.valuation.layer', ],
            ['stock.production.lot', ],
            # ['stock.fixed.putaway.strat', ],
            ['procurement.group', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
                    self._cr.commit()
            # 更新序号
            seqs = self.env['ir.sequence'].search([
                '|', ('code', 'like', 'stock.%'),
                '|', ('code', 'like', 'picking.%'),
                '|', ('prefix', '=', 'WH/IN/'),
                '|', ('prefix', '=', 'WH/INT/'),
                '|', ('prefix', '=', 'WH/OUT/'),
                '|', ('prefix', '=', 'WH/PACK/'),
                ('prefix', '=', 'WH/PICK/')
            ])
            for seq in seqs:
                seq.write({
                    'number_next': 1,
                })
        except Exception as e:
            pass  # raise Warning(e)
        return True

    def remove_account(self):
        to_removes = [
            # 清除财务会计单据
            ['payment.transaction', ],
            ['account.voucher.line', ],
            ['account.voucher', ],
            ['account.bank.statement.line', ],
            ['account.payment', ],
            ['account.analytic.line', ],
            ['account.analytic.account', ],
            ['account.invoice.line', ],
            ['account.invoice.refund', ],
            ['account.invoice', ],
            ['account.partial.reconcile', ],
            ['account.move.line', ],
            ['hr.expense.sheet', ],
            ['account.move', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
                    self._cr.commit()

                    # 更新序号
                    seqs = self.env['ir.sequence'].search([
                        '|', ('code', 'like', 'account.%'),
                        '|', ('prefix', 'like', 'BNK1/'),
                        '|', ('prefix', 'like', 'CSH1/'),
                        '|', ('prefix', 'like', 'INV/'),
                        '|', ('prefix', 'like', 'EXCH/'),
                        '|', ('prefix', 'like', 'MISC/'),
                        '|', ('prefix', 'like', '账单/'),
                        ('prefix', 'like', '杂项/')
                    ])
                    for seq in seqs:
                        seq.write({
                            'number_next': 1,
                        })
        except Exception as e:
            pass  # raise Warning(e)
        return True

    def remove_account_chart(self):
        to_removes = [
            # 清除财务科目，用于重设
            ['res.partner.bank', ],
            ['res.bank', ],
            ['account.move.line'],
            ['account.invoice'],
            ['account.payment'],
            ['account.bank.statement', ],
            ['account.tax.account.tag', ],
            ['account.tax', ],
            ['account.tax', ],
            ['account.account.account.tag', ],
            ['wizard_multi_charts_accounts'],
            ['account.account', ],
            ['account.journal', ],
        ]
        # todo: 要做 remove_hr，因为工资表会用到 account
        # 更新account关联，很多是多公司字段，故只存在 ir_property，故在原模型，只能用update
        try:
            # reset default tax，不管多公司
            field1 = self.env['ir.model.fields']._get('product.template', "taxes_id").id
            field2 = self.env['ir.model.fields']._get('product.template', "supplier_taxes_id").id

            sql = ("delete from ir_default where field_id = %s or field_id = %s") % (field1, field2)
            self._cr.execute(sql)
            self._cr.commit()
        except Exception as e:
            pass  # raise Warning(e)
        try:
            rec = self.env['res.partner'].search([])
            for r in rec:
                r.write({
                    'property_account_receivable_id': None,
                    'property_account_payable_id': None,
                })
        except Exception as e:
            pass  # raise Warning(e)
        try:
            rec = self.env['product.category'].search([])
            for r in rec:
                r.write({
                    'property_account_income_categ_id': None,
                    'property_account_expense_categ_id': None,
                    'property_account_creditor_price_difference_categ': None,
                    'property_stock_account_input_categ_id': None,
                    'property_stock_account_output_categ_id': None,
                    'property_stock_valuation_account_id': None,
                })
        except Exception as e:
            pass  # raise Warning(e)
        try:
            rec = self.env['stock.location'].search([])
            for r in rec:
                r.write({
                    'valuation_in_account_id': None,
                    'valuation_out_account_id': None,
                })
        except Exception as e:
            pass  # raise Warning(e)

        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
                    self._cr.commit()


            sql = "update res_company set chart_template_id=null;"
            self._cr.execute(sql)
            self._cr.commit()
            # 更新序号
        except Exception as e:
            pass

        return True

    def remove_project(self):
        to_removes = [
            # 清除项目
            ['account.analytic.line', ],
            ['project.task', ],
            ['project.forecast', ],
            ['project.project', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
                    self._cr.commit()
            # 更新序号
        except Exception as e:
            pass  # raise Warning(e)
        return True

    def remove_website(self):
        to_removes = [
            # 清除网站数据，w, w_blog
            ['blog.tag.category', ],
            ['blog.tag', ],
            ['blog.post', ],
            ['blog.blog', ],
            ['website.published.multi.mixin', ],
            ['website.published.mixin', ],
            ['website.multi.mixin', ],
            ['website.redirect', ],
            ['website.seo.metadata', ],
            ['website.page', ],
            ['website.menu', ],
            ['website', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj and obj._table:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
                    self._cr.commit()
        except Exception as e:
            pass  # raise Warning(e)
        return True

    def remove_message(self):
        to_removes = [
            # 清除消息数据
            ['mail.message', ],
            ['mail.followers', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj and obj._table:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
                    self._cr.commit()
        except Exception as e:
            pass  # raise Warning(e)
        return True

    def remove_workflow(self):
        to_removes = [
            # 清除工作流
            ['wkf.workitem', ],
            ['wkf.instance', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj and obj._table:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
                    self._cr.commit()

        except Exception as e:
            pass  # raise Warning(e)
        return True

    def remove_all_biz(self):
        try:
            self.remove_account()
            self.remove_inventory()
            self.remove_mrp()
            self.remove_purchase()
            self.remove_sales()
            self.remove_project()
            self.remove_pos()
            self.remove_expense()
            self.remove_message()
        except Exception as e:
            pass  # raise Warning(e)
        return True
