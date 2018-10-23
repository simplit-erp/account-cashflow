# -*- coding: utf-8 -*-
{
    'name': "Account Cashflow",

    'summary': """
        Basic Cashflow Managment
        """,

    'description': """
        Manage the cashflow base on accounting
    """,

    'author': "Simplit S.A.",
    'website': "http://www.simplit.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Accounting &amp; Finance',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account_invoicing'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
