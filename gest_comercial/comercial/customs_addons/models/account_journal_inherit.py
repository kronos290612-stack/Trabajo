from odoo import models, fields, api

class AccountJournalInherit(models.Model):
    _inherit = 'account.journal'

    # Métodos para los 4 botones del dashboard
    def action_control_comercial(self):
        """Abrir vista de Opción 1"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Control Comercial',
            'res_model': 'tu.modelo.1',
            'view_mode': 'tree,form',
            'target': 'current',
        }

    def action_solicitud(self):
        """Abrir vista de Opción 2"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Solicitud',
            'res_model': 'tu.modelo.2',
            'view_mode': 'tree,form',
            'target': 'current',
        }

    def action_contol_documentos(self):
        """Abrir vista de Opción 3"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Control de Documentos',
            'res_model': 'tu.modelo.3',
            'view_mode': 'tree,form',
            'target': 'current',
        }

    def action_p_entrega(self):
        """Abrir vista de Opción 4"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Próxima Entrega',
            'res_model': 'tu.modelo.4',
            'view_mode': 'tree,form',
            'target': 'current',
        }