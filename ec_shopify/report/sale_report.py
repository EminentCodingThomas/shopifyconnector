# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

from odoo import fields, models
import odoo


class SaleReport(models.Model):
    _inherit = "sale.report"

    shopify_instance_id = fields.Many2one("shopify.instance.ept", "Shopify Instance", copy=False, readonly=True)

    def _select_additional_fields(self):
        res = super()._select_additional_fields()
        res['shopify_instance_id'] = "s.shopify_instance_id"
        return res

    def _group_by_sale(self):
        res = super()._group_by_sale()
        res += """,
            s.shopify_instance_id"""
        return res

    def shopify_sale_report(self):
        version_info = odoo.service.common.exp_version()
        if version_info.get('server_version') == '16.0':
            action = self.env.ref('ec_shopify.shopify_action_order_report_all').sudo().read()[0]
        else:
            action = self.env.ref('ec_shopify.shopify_sale_report_action_dashboard').sudo().read()[0]

        return action
