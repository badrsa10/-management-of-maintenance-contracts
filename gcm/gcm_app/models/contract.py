# -*- coding: utf-8 -*-

from odoo import models, fields, api

#***Contract's object***#
class object(models.Model):
    _inherit = 'project.project'
    # object_id = fields.Integer(string = 'Object')

#***object's tasks***#
class task(models.Model):
    _inherit = 'project.task'

#***contract's Client***#
class client(models.Model):
    _inherit = 'res.partner'

    # client_id = fields.Integer()

#***contract's payement***#
class payment(models.Model):
    _inherit = 'account.payment'

#***Obligations Client***#
class obligation_clt(models.Model):
    _name = 'contract.obligclt'

    name = fields.Char(string="Obligation client",required=True)

#***Obligations Prestataire***#
class obligation_prest(models.Model):
    _name = 'contract.obliprest'

    name = fields.Char(string="Obligation prestataire", required=True)

#***Responsabilité***#
class responsabilite(models.Model):
    _name = 'contract.responsability'

    name = fields.Char(string="responsability", required=True)

#***contract***#
class contract(models.Model):
    _name = 'contract.contract'
    # _inherit = ['res.partner', 'account.payement']

    # ___Contract ID___#
    my_seq = fields.Char('Sequence',readonly=True)

    #___Dates___#
    starting_date = fields.Date(string="date of contract", required=True)
    deadline_date = fields.Date(string="deadline", required=True)

    #___Agreements___#
    obligclt_id = fields.Many2many('contract.obligclt',string="Obligations Client")#,default=lambda self: self.env['contract.obligclt'].search([]))
    obligpres_id = fields.Many2many('contract.obliprest',string="Obligations prestataire")#,default=lambda self: self.env['contract.obliprest'].search([]))
    responsability_id = fields.Many2many('contract.responsability',string="Responsabilities")#,default=lambda self: self.env['contract.responsability'].search([]))

    #___Object___#
    object_id = fields.Many2one('project.project',string="Object")#,default=lambda self: self.env['project.project'].search([]),required=True)

    #___Client___#
    client_id = fields.Many2one('res.partner',string="Client")#,default=lambda self: self.env['res.partner'].search([]),required=True)

    #___Payment___#
    payment_id = fields.Many2one('account.payment', string="Payment")#, default=lambda self: self.env['account.payment'].search([]),required=True)

    @api.model
    def create(self, vals):
        vals['my_seq'] = self.env['ir.sequence'].next_by_code('contract.contract')
        return super(contract, self).create(vals)
