# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.
{
    'name': 'Shopify Library',
    'version': '1.0',
    'category': 'Sales',
    'license': 'OPL-1',
    'author': 'Eminent Coding',
    'website': 'https://www.eminentcoding.be/',
    'maintainer': 'Eminent Coding BV',
    'summary': """Develop generalize method to process different operations & auto workflow process to manage
    order process automatically.""",
    'depends': ['delivery'],
    'data': ['security/ir.model.access.csv',
             'data/ir_sequence.xml',
             'data/ir_cron.xml',
             'data/digest_data.xml',
             'views/stock_quant_package_view.xml',
             'views/log_book_view.xml',
             'views/account_fiscal_view.xml',
             'views/common_product_image_ec.xml',
             'views/product_view.xml',
             'views/product_template.xml',
             'views/sale_order_view.xml',
             'views/sale_workflow_process_view.xml',
             'data/automatic_workflow_data.xml',
             'views/common_log_lines_ec.xml',
             'views/digest_views.xml',
             'views/delivery_carrier_view.xml',
             'views/res_partner_view.xml',
             'wizard/stock_return_picking.xml',
             ],
    'installable': True,
    'currency': 'EUR',
    'images': ['static/description/Common-Connector-Library-Cover.jpg'],
    # cloc settings
    'cloc_exclude': ['**/*.xml', ],
    'assets': {
        'web.assets_backend': [
            '/shopify_lib/static/src/scss/graph_widget_ec.scss',
            '/shopify_lib/static/src/scss/on_boarding_wizards.css',
            '/shopify_lib/static/src/scss/queue_line_dashboard.scss',
            '/shopify_lib/static/src/js/graph_widget_ec.js',
            # '/shopify_lib/static/src/js/queue_line_dashboard.js',
            '/shopify_lib/static/src/xml/dashboard_widget.xml',
            # '/shopify_lib/static/src/xml/queue_line_dashboard.xml'
        ],
    },
}

