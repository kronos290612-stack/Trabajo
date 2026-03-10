# -*- coding: utf-8 -*-
from odoo import fields, models

#Adicionar en setting 	Diario de reintegro
class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    # Campo para el diario de reintegro (ventas)
    expense_reimbursement_journal_id = fields.Many2one(
        'account.journal',
        string='Reimbursement Log',
        config_parameter='hr_expense.reimbursement_journal_id',
        readonly=False,
        domain="[('type', '=', 'sale'), ('company_id', '=', company_id)]",
        help='Default accounting journal for expense reimbursement.'
    )
