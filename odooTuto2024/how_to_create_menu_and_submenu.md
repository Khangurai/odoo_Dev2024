# How to create menu and submenu

1.create models python file
`playground.py`
```python
from odoo import models, fields

class PlaygroundItem(models.Model):
    _name = 'playground.item'
    _description = 'Playground Item'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')

```
2.create views xml file
`playground_view.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<odoo>

    <!-- Define the action for the submenu -->
    <record id="playground_item_action" model="ir.actions.act_window">
        <field name="name">Playground Items</field>
        <field name="res_model">playground.item</field>
        <field name="view_mode">tree,form</field>
        <field name="target">current</field>
    </record>

    <!-- Define the tree view for the model -->
    <record id="view_playground_item_tree" model="ir.ui.view">
        <field name="name">playground.item.tree</field>
        <field name="model">playground.item</field>
        <field name="arch" type="xml">
            <tree>
                <field name="name"/>
                <field name="description"/>
            </tree>
        </field>
    </record>

    <!-- Define the form view for the model -->
    <record id="view_playground_item_form" model="ir.ui.view">
        <field name="name">playground.item.form</field>
        <field name="model">playground.item</field>
        <field name="arch" type="xml">
            <form>
                <sheet>
                    <group>
                        <field name="name"/>
                        <field name="description"/>
                    </group>
                </sheet>
            </form>
        </field>
    </record>

    <menuitem id="playground_main_menu" name="Playground" sequence="10" parent="menu_hotel_root">
        <menuitem id="playground_submenu" name="Items" sequence="10" action="playground_item_action"/>
    </menuitem><!--nested format-->

</odoo>

```
3.models `__init__.py`
`from . import playground`

4.add xml path in manifest.py
`'views/playground_view.xml'`

5.access right
```
access.playground.item.wizard,access_playground_item_wizard,hotel_B.model_playground_item,base.group_user,1,1,1,1
```