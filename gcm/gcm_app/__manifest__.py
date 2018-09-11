# -*- coding: utf-8 -*-
{
    'name': "GCM",

    'summary': """
        Gestion des contrats de maintenance""",

    'description': """
        Ce module consiste à gérer les contrats de maintenance.\n
        un contrat de maintenance est structuré de cette façon: \n
        - Client\n
        - date de signature\n
        - date d'expiration\n
        - objet\n
        - prix et mode de paiement\n
        - obligations client\n
        - obligations prestataire\n
        - responsabilité\n
        
        les champs 'obligations clients','obligations prestataire' et 'responsabilité' sont à choix multiple, on peut utiliser les données qu'on déjà entrer à la creation d'un nouveau contrat.
        
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','contacts','account','project'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/templates.xml',
        'views/views.xml',
        'views/records.xml',
        'data/sequence.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': 'True'
}