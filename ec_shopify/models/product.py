# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

from odoo import models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def write(self, vals):
        if 'active' in vals.keys():
            shopify_product_template_obj = self.env['shopify.product.template.ec']
            for template in self:
                shopify_templates = shopify_product_template_obj.search(
                    [('product_tmpl_id', '=', template.id)])
                if vals.get('active'):
                    shopify_templates = shopify_product_template_obj.search(
                        [('product_tmpl_id', '=', template.id), ('active', '=', False)])
                shopify_templates.write({'active': vals.get('active')})
        res = super(ProductTemplate, self).write(vals)
        return res


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def write(self, vals):
        if 'active' in vals.keys():
            shopify_product_product_obj = self.env['shopify.product.product.ec']
            for product in self:
                shopify_product = shopify_product_product_obj.search(
                    [('product_id', '=', product.id)])
                if vals.get('active'):
                    shopify_product = shopify_product_product_obj.search(
                        [('product_id', '=', product.id), ('active', '=', False)])
                shopify_product.write({'active': vals.get('active')})
        res = super(ProductProduct, self).write(vals)
        return res
