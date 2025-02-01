# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.
from odoo import models, fields


class CommonLogLineEpt(models.Model):
    _name = "common.log.lines.ec"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Common log line"

    product_id = fields.Many2one('product.product', 'Product')
    order_ref = fields.Char('Order Reference')
    default_code = fields.Char('SKU')
    log_book_id = fields.Many2one('common.log.book.ec', ondelete="cascade")
    message = fields.Text()
    model_id = fields.Many2one("ir.model", string="Model")
    res_id = fields.Integer("Record ID")
    mismatch_details = fields.Boolean(string='Mismatch Detail', help="Mismatch Detail of process order")
    file_name = fields.Char()
    sale_order_id = fields.Many2one(comodel_name='sale.order', string='Sale Order')
    log_line_type = fields.Selection(selection=[('success', 'Success'), ('fail', 'Fail')], default='fail')
    operation_type = fields.Selection([('import', 'Import'), ('export', 'Export')], string="Operation")
    module = fields.Selection([('amazon_ec', 'Amazon Connector'),
                               ('woocommerce_ec', 'Woocommerce Connector'),
                               ('ec_shopify', 'Shopify Connector'),
                               ('magento_ec', 'Magento Connector'),
                               ('bol_ec', 'Bol Connector'),
                               ('ebay_ec', 'Ebay Connector'),
                               ('amz_vendor_central', 'Amazon Vendor Central'),
                               ('tpw_ec', '3PL Connector'),
                               ('walmart_ec', 'Walmart Connector')])

    def create_common_log_line_ec(self, **kwargs):
        """
        It is use to create log lines.
        @param : **kwargs, Pass the argument like, self.env['common.log.lines.ec'].create_common_log_line_ec(
        log_book_id=1, message=message, mismatch=True, log_line_type='fail', model_name = 'sale.order')
        """
        values = {}
        for key, value in kwargs.items():
            if hasattr(self, key):
                values.update({key: value})
        if kwargs.get('model_name'):
            model = self._get_model_id(kwargs.get('model_name'))
            values.update({'model_id': model.id})
        return self.create(values)

    def _get_model_id(self, model_name):
        """
        It is use to get the model id
        @param :  model_name : Name of the model
        """
        ir_model_obj = self.env['ir.model']
        return ir_model_obj.sudo().search([('model', '=', model_name)])
