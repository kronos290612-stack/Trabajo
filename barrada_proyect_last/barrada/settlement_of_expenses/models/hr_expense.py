# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class HrExpense(models.Model):
    _inherit = 'hr.expense'

    verified = fields.Boolean(
        string='Verified', default=False,
        help='Check to view total verified expenses')

    real_expenses = fields.Monetary(
        string='Real Expenses',
        help='Enter the actual amount spent',
        tracking=True)

    supporting_documents = fields.Binary(
        string='Supporting Documents',
        help='Please Only Allowed Formats (PDF, JPG, JPEG or PNG)',
        tracking=False)

    refund = fields.Monetary(
        string='Refund',
        #compute='_compute_diferenc',
        store=True,
        readonly=True,
        help='Negative: employee owes money to the company\nPositive: company owes money to employee'
    )



