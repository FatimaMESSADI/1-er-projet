from odoo import api, fields, models
 
class facture(models.Model):
	_name = "facture"
	_rec_name = "id_facture"
	_description = "la facture"

	id_facture = fields.Char("Identifiant")
	description = fields.Text("Description")
	personne_id = fields.Many2one('personne')