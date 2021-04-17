# -*- coding: utf-8 -*-
{
    'name': "Voiture",


    'description': "Agence de location des voitures",

    'author': "Tima Messadi",
   

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/voiture.xml',
        'views/personne.xml',
        'views/location.xml',
        'views/facture.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}