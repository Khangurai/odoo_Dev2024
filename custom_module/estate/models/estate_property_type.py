from odoo import models, fields, api

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real Estate Property Type"
    _order = 'sequence, name asc'  # Sequence first, then name for secondary sorting

    name = fields.Char(required=True)
    sequence = fields.Integer(default=10)
    property_ids = fields.One2many('estate.property', 'property_type_id', string='Properties')

    _sql_constraints = [
        ('name', 'unique(name)', 'Property type name must be unique.'),

    ]
    offer_ids = fields.One2many(
        comodel_name='estate.property.offer',
        inverse_name='property_type_id',
        string='Offers'
    )

    offer_count = fields.Integer(
        string='Offer Count',
        compute = '_compute_offer_count'
    )

    has_offers = fields.Boolean(
        string='Has Offers',
        compute='_compute_has_offers'
    )

    @api.depends('offer_count')
    def _compute_has_offers(self):
        for record in self:
            record.has_offers = record.offer_count > 0

    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)