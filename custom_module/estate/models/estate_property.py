from datetime import datetime, timedelta
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

# add_function = lambda x, y: x + y

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"
    _rec_name = 'title'
    _order = 'id desc'

    # Basic Property Information
    title = fields.Char(required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="PostCode")
    date_availability = fields.Date(string="Available From", copy=False, default=fields.Datetime.now)
    expected_price = fields.Float(string="Expected Price", required=True)
    selling_price = fields.Float(string="Selling Price", readonly=True, copy=False)
    bedrooms = fields.Integer(string="Bedrooms", default=2)
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden Area (sqm)")
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
    ], string="Garden Orientation")

    state = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('cancel', 'Cancel')
    ], default='new', string="Status", readonly=True)

    # Relationships
    property_type_id = fields.Many2one('estate.property.type', string='Property Type')
    buyer_id = fields.Many2one('res.partner', string='Buyer', copy=False)
    salesperson_id = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.user)

    best_price = fields.Float(string='Best Price', readonly=True, compute="_compute_best_price", store=True)
    total_area = fields.Integer(string="Total Area(sqm)", readonly=True, compute="_compute_total_area", store=True)

    tag_ids = fields.Many2many('estate.property.tag', string='Tags')
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string='Offers')

    min_date = fields.Date(string="Min Date", compute='_compute_min_date', store=True)

    is_accepted = fields.Boolean(string="Is Accepted", compute="_compute_is_accepted")

    def _compute_is_accepted(self):
        # add_function(1,2)pip
        for rec in self:
            rec.is_accepted = bool(rec.offer_ids.filtered(lambda x: x.status == 'accepted'))
        #     accept_list =[]
        #     if rec.status== 'accepted':
        #         accept_list.append(rec)

    @api.depends('create_date')
    def _compute_min_date(self):
        for record in self:
            record.min_date = (datetime.today() - timedelta(days=90)).date()
    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids')
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(record.offer_ids.mapped('price')) if record.offer_ids else 0

    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = 0
            self.garden_orientation = False

    def action_new(self):
        self.state = 'new'

    def action_offer_received(self):
        import pdb; pdb.set_trace()
        self.state = 'offer_received'

    def action_offer_accepted(self):
        self.state = 'offer_accepted'

    def action_sold(self):
        if self.state == 'cancel':
            raise ValidationError(_('Sorry, cancelled record cannot be sold'))
        self.state = 'sold'

    def action_cancel(self):
        self.state = 'cancel'

    @api.constrains('expected_price', 'selling_price')
    def _check_positive_prices(self):
        if self.expected_price <= 0:
            raise ValidationError("The expected price must be strictly positive.")
        if self.selling_price is not None and self.selling_price < 0:
            raise ValidationError("The selling price must be positive.")

    @api.constrains('selling_price', 'expected_price')
    def _check_selling_price(self):
        if self.selling_price > 0 and self.selling_price < 0.9 * self.expected_price:
            raise ValidationError(
                _("The selling price cannot be lower than 90% of the expected price. Please adjust the selling price.")
            )

    @api.ondelete(at_uninstall=False)
    def _prevent_deletion_if_not_new_or_canceled(self):
        if self.state not in ['new', 'cancel']:
            raise ValidationError(
                _("You cannot delete a property unless its state is 'New' or 'Canceled'.")
            )
