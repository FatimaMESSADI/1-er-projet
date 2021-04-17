# -*- coding: utf-8 -*-

from odoo import api, exceptions, fields, models
class voiture(models.Model):
    _name = "voiture"
    _rec_name = "modèle"
    _description = "location des voitures"

    modèle = fields.Char(string="Modèle de voiture")
    série = fields.Char(string="Série")
    matricule = fields.Text()
    image = fields.Binary('photo de voiture')
    dis = fields.Boolean(default=True)

    def is_dispo(self):
    	self.dis = False


