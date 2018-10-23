# -*- coding: utf-8 -*-

from odoo import models, fields, api

import logging

_logger = logging.getLogger(__name__)

class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    date_cashflow = fields.Date(string='Cashflow Date', required=False)
    
    @api.onchange('date_due')
    def _onchange_date_due(self):
        self.date_cashflow = self.date_due



