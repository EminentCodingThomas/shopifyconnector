{
    # App information
    'name': 'Shopify Odoo Connector',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Odoo - Shopify Connector',
    'license': 'OPL-1',

    # Author
    'author': 'Eminent Coding',
    'website': 'https://www.eminentcoding.be/',
    'maintainer': 'Eminent Coding BV',

    # Dependencies
    'depends': ['shopify_lib'],

    # Views
    'init_xml': [],
    'data': [
        'security/group.xml',
        'security/ir.model.access.csv',
        'view/instance_view.xml',
        'wizard/res_config_view.xml',
        'data/import_order_status.xml',
        'data/ir_sequence_data.xml',
        'data/ir_cron_data.xml',
        'data/product_data.xml',
        'data/ir_attachment_data.xml',
        'wizard/process_import_export_view.xml',
        'view/product_template_view.xml',
        'view/product_product_view.xml',
        'view/payment_gateway_view.xml',
        'wizard/queue_process_wizard_view.xml',
        'view/order_data_queue_ec.xml',
        'view/product_data_queue_view.xml',
        'view/customer_data_queue_ec.xml',
        'view/customer_data_queue_line_ec.xml',
        'view/location_ec.xml',
        'view/sale_order_view.xml',
        'view/res_partner_view.xml',
        'view/sale_workflow_config_view.xml',
        'view/stock_picking_view.xml',
        'wizard/cron_configuration_ec.xml',
        'wizard/cancel_refund_order_wizard_view.xml',
        'wizard/shopify_onboarding_confirmation_ec_view.xml',
        'wizard/basic_configuration_onboarding.xml',
        'wizard/financial_status_onboarding_view.xml',
        'view/acc_invoice_view.xml',
        'report/sale_report_view.xml',
        'view/log_book_view.xml',
        'view/shopify_instances_onboarding_panel_view.xml',
        'view/dashboard_view.xml',
        'view/order_data_queue_line_ec.xml',
        'view/product_data_queue_line_view.xml',
        'view/product_image_ec.xml',
        "wizard/prepare_product_for_export.xml",
        # 'view/shopify_payout_report_ec.xml',
        'wizard/instance_configuration_wizard.xml',
        'view/delivery_carrier_view.xml',
        'view/export_stock_queue_view.xml',
        'view/export_stock_queue_line_view.xml',
    ],
    'demo_xml': [],
    # cloc settings
    'cloc_exclude': ["shopify/**/*", "**/*.xml", ],

    # Odoo Store Specific
    'images': ['static/description/Shopify_Odoo_App_v16_Video.gif'],
    "description": """
          Shopify,
          Amazon,
          Woo,
          Woocommerce,
          woo-commerce,
          Shopify Connector
          """,

    'installable': True,
    'auto_install': False,
    'application': True,
    'currency': 'EUR',
    # 'assets': {
    #     'web.assets_backend': [
    #         'ec_shopify/static/src/js/shopify_button_collapse.js',
    #         'ec_shopify/static/src/css/shopify_base.css',
    #     ],
    # },
}
