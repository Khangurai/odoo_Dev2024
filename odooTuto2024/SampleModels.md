# to create models
- models folder >>>>>> guest_tag.py
- models folder >>>>>> init.py import guest_tag
- guest_tag_view.xml
- menu.xml >>>>>> add menu items
- manifest.py add path 


guest_tag.py
```python
from odoo import api, fields, models

class GuestTag(models.Model):
    _name = 'guest.tag'
    _description = 'Guest Tag'

    name = fields.Char(string='Name', tracking=True)
    ref = fields.Char(string='Reference')
    active = fields.Boolean(string='Active', default=True)
    color = fields.Integer(string='Color')
    color2 = fields.Char(string='Color2')

```


guest_tag_view.xml
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <record id="view_guest_tag_tree" model="ir.ui.view">
        <field name="name">guest.tag.tree</field>
        <field name="model">guest.tag</field>
        <field name="arch" type="xml">
            <!--sample = "1"-->
            <tree>
                <field name="name" string="Name"/>
                <field name="ref"/>
                <field name="color" widget="color_picker"/>
            </tree>
        </field>
    </record>

    <record id="view_guest_tag_form" model="ir.ui.view">
        <field name="name">guest.tag.form</field>
        <field name="model">guest.tag</field>
        <field name="arch" type="xml">
            <form>
                <sheet>
                    <group>
                        <field name="name"/>
                        <field name="active" invisible="1"/>
                    </group>
                    <group>
                        <field name="color" widget="color_picker"/>
                        <field name="color2" widget="color"/>
                        <field name="active" widget="boolean_toggle"/>
                    </group>
                </sheet>
            </form>
        </field>
    </record>

    <record id="action_guest_tag" model="ir.actions.act_window">
        <field name="name">Guest Tag</field>
        <field name="type">ir.actions.act_window</field>
        <field name="res_model">guest.tag</field>
        <field name="view_mode">tree,form</field>
        <field name="context">{'search_default_group_by_gender': 1, 'search_default_filter_male': 1}</field>
        <field name="help" type="html">
            <p class="o_view_nocontent_smiling_face">
                Create New Tag!
            </p>
        </field>
    </record>

    <menuitem id="menu_guest_tag"
              name="Tags"
              action="action_guest_tag"
              parent="menu_configuration"
              sequence="0"/>
</odoo>
```

menu.xml
```xml
<menuitem id = "menu_configuration"
             name = "Guest Tag"
             parent = "menu_hotel_root"
             sequence = "10"/>
```

__manifest__.py
```python
'data': [
        'views/guest_tag_view.xml',
    ],
```

models\__init__.py
```python
from . import guest_tag
```
ir.model.access.csv
```csv
access.guest.tag,access_guest_tag,hotel_B.model_guest_tag,base.group_user,1,1,1,1
```
