# How To Inherit And Add Field To A Model

in sale_order_view.xml
```xml
<odoo>
    <data>
        <record id="view_order_form_inherit" model="ir.ui.view">
            <field name="name">sale.order.inherit</field>
            <field name="model">sale.order</field>
            <field name="inherit_id" ref="sale.view_order_form"/>
            <field name="arch" type="xml">
                <xpath expr="//field[@name='payment_term_id']" position="before">
                    <field name="confirmed_user_id"/>
                </xpath>
            </field>
        </record>
    </data>
</odoo>

```
sale_order.py
```python
from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'


    name = fields.Char(string='Name', required=True)

    confirmed_user_id = fields.Many2one('res.users', string='Confirmed User')

```


check in sale order module

----------

