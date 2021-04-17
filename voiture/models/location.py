from odoo import api, fields, models
from odoo.exceptions import Warning
class location(models.Model):
	_name = "location"
	_description = 'liste des voiture'

	id_location = fields.Integer(string="Identifiant de location",required=True)
	date_location = fields.Date("Date de location")
	date_retour = fields.Date("Date retour")
	voiture_id = fields.Many2one('voiture')
	personne_id = fields.Many2one('personne')
	facture_id = fields.Many2one('facture')
	prix_voiture_jour = fields.Monetary('Prix du voiture/jour', 'currency_id')
	currency_id = fields.Many2one('res_currency')
	duree_location = fields.Char(compute='_compute_duree')
	prix_total = fields.Monetary(string="prix", compute='_compute_prix_total')


	@api.one
	def _compute_duree(self):
		dure = self.date_retour - self.date_location
		self.duree_location = dure

	@api.one
	def _compute_prix_total(self):
		total = self.duree_location * self.prix_voiture_jour
		self.prix_total = total

	
		


	#def check_date(self):
		#if self.date_retour <= self.date_location:
			#raise Warning("Vérifier la date")
	
