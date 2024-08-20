from odoo import models, fields, api
from datetime import timedelta
from odoo.exceptions import UserError, ValidationError

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Property Offer"
    _order = 'price desc'


    property_id = fields.Many2one('estate.property', string='Properties', readonly=True)
    price = fields.Float(string="Price")
    status = fields.Selection([
        ('accepted', 'Accepted'),
        ('refused', 'Refused')
    ])
    partner_id = fields.Many2one('res.partner', string="Partner")

    validity = fields.Integer(string="Validity(days)", default=7)
    date_deadline = fields.Date(string="Deadline",
                                compute="_compute_date_deadline",
                                inverse="_inverse_date_deadline",
                                store=True)

    duration = fields.Integer(string="Duration (Days)", compute="_compute_duration", store=True)

    property_type_id = fields.Many2one(
        related='property_id.property_type_id',
        string="Property Type")

    @api.depends('date_deadline', 'create_date')
    def _compute_duration(self):
        for record in self:
            if record.create_date and record.date_deadline:
                create_date = record.create_date.date()
                duration = (record.date_deadline - create_date).days
                record.duration = duration
            else:
                record.duration = 0

    def action_accept(self):
        self.status = 'accepted'
        self.property_id.selling_price = self.price

    def action_refuse(self):
        self.status = 'refused'

    @api.depends('create_date', 'validity')
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + timedelta(days=record.validity)
            else:
                record.date_deadline = fields.Date.today() + timedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            if record.create_date and record.date_deadline:
                create_date = record.create_date.date()
                duration = (record.date_deadline - create_date).days
                record.duration = duration

    @api.constrains('offer_amount')
    def _check_positive_offer_amount(self):
        for record in self:
            if record.offer_amount <= 0:
                raise ValidationError("The offer amount must be strictly positive.")

    @api.model
    def create(self, vals):
        property = self.env['estate.property'].browse(vals['property_id'])

        existing_offers = self.search([('property_id', '=', vals['property_id'])])
        if existing_offers and vals['price'] <= max(existing_offers.mapped('price')):
            raise UserError("You cannot create an offer with an amount lower than an existing offer.")

        property.state = 'offer_received'

        offer = super(EstatePropertyOffer, self).create(vals)
        return offer
