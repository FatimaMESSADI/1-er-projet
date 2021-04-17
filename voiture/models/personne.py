from odoo import api, fields, models
from odoo.exceptions import Warning


class personne(models.Model):
	_name = "personne"
	_rec_name = "identifiant"
	_description = "la personne qui va louer une voiture"

	identifiant = fields.Char("Identifiant de client")
	nom = fields.Char("Nom")
	prénom = fields.Char("Prénom")
	Date_naissance = fields.Date("Date de naissance")
	num_carte_identité = fields.Char("Numéro de carte d'identité")

	@api.multi
	def check_num_card(self):
		self.ensure_one()
		digits = [int(x) for x in self.num_carte_identité if x.isdigit()]
		if len(digits) >= 5:
			raise Warning('numéro de carte non valide')
