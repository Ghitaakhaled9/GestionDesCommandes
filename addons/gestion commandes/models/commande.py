from odoo import models, fields

class GestionCommandes(models.Model):
    _name = 'gestion.commandes'
    _description = 'Gestion des Commandes'

    # Définition des champs
    name = fields.Char(string='Nom de la commande', required=True)
    date_commande = fields.Datetime(string='Date de la commande', default=fields.Datetime.now)
    client_id = fields.Many2one('res.partner', string='Client', required=True)
    total = fields.Float(string='Total', required=True)
    status = fields.Selection([
        ('draft', 'Brouillon'),
        ('confirmed', 'Confirmée'),
        ('done', 'Livrée')
    ], default='draft', string='Statut')

    def action_create(self):
        """Méthode qui sera appelée pour ajouter une nouvelle commande"""
        self.create({
            'name': 'Nouvelle commande',  # Nom par défaut
            'date_commande': fields.Datetime.now(),
            'client_id': self.client_id.id,  # Client par défaut
            'total': 0.0,  # Valeur initiale pour le total
            'status': 'draft',
        })
