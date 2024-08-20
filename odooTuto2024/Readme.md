# To create module

```
custom modules/
└── hotel_management/
    ├── __manifest.py__
    └── __init.py__
```
> add json format in manifest

```python
{
    'name':'Hotel Management'
}
```

> turn on active developer mode

> update app list

------------


# To creat a icon of module 
```
custom modules/
├── hotel_management
└── static/
    ├── description/
    │   └── icon.png
    ├── __manifest.py__
    └── __init.py__
```
> then upgrade the module


------------


# To create a database Model
```sh
custom modules/
└── hotel_management/
    ├── models/
    │   ├── guests.py
    │   └── __init.py__
    ├── static/
    │   └── description/
    │       └── icon.png
    ├── __manifest.py__
    └── __init.py__
```
>guests.py

```python
from odoo import api, models,fields

class HotelGuests(models.Model):
    _name = 'hotel.guests'
    _description = 'Hotel Guests'

    ref = fields.Char(string='Ref')
    name = fields.Char(string='Name')
    dob = fields.Datetime(string='Date of Birth')
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male','Male'), ('female','Female')], string='Gender')
    active = fields.Boolean(string='Active', default = True)
```
>models/init py

```
from . import guests
```

>main init file

```
from . import models
```
- to check in settings\technical\database\models
- to check in models in database
- open terminal

```
psql -U postgres -d demo_db
```
- username - postgres
- database - demo_db
- you can aslo check in pgadmin4
- select database `demo_db` and type query 

```
psql -U postgres -d demo_db
```

>and type query

```
select * from hotel_guests
```

------------


# To create menu
```
custom modules/
└── hotel_management/
    ├── views/
    │   └── menu.xml
    ├── models/
    │   ├── guests.py
    │   └── __init.py__
    ├── static/
    │   └── description/
    │       └── icon.png
    ├── __manifest.py__
    └── __init.py__
```    
in xml file 
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <menuitem id="menu_hotel_root"
             name="Hotel"
             sequence="0"/>

</odoo>
```
add path to manifest file
```python
'data':[  
    'views/menu.xml',  
],
```

ဒီအထိကမပေါ်သေးဘူး  menu မှာ 

`menu`မှာပေါ်ချင်ရင်settings\techinal\user interface\menu items မှာပြင်ပေးမှ ရမယ်

check this [youtube](https://www.youtube.com/watch?v=jdsP7RQ-8Hs&list=PLqRRLx0cl0hoZM788LH5M8q7KhiXPyuVU&index=7) how to create sub menu


>[!NOTE]
>တစ်ခုနဲ့တစ်ခုကို link ချိတ်ပေးရမယ်
>
>တစ်ခုခုပေါ်အောင်action တစ်ခုထည့်ပေး

![logo](https://github.com/Khangurai/odoo_Tuto2024/blob/main/assests/1.png)

------------


# To create window action 

```
custom modules/
└── hotel_management/
    ├── views/
    │   ├── menu.xml
    │   └── guests_view.xml
    ├── models/
    │   ├── guests.py
    │   └── __init.py__
    ├── static/
    │   └── description/
    │       └── icon.png
    ├── __manifest.py__
    └── __init.py__
```
add file in guests_view.xml
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <record id="action_hotel_guests" model="ir.actions.act_window">
            <field name="name">Guests</field>
            <field name="type">ir.actions.act_window</field>
            <field name="res_model">hotel.guests</field>
            <field name="view_mode">tree,form</field>
            <field name="context">{}</field>
            <field name="help" type="html">
                <p class="o_view_nocontent_smiling_face">
                    Create a new product
                </p>
            </field>
        </record>
</odoo>
```
add path to manifest file
```python
'data':[  
    'views/guests_view.xml',  
],
```
to check window action in settings\window action

------------


# To link windows action and Menu items

add security csv
```python
'data': [
        'security/ir.model.access.csv',
]
```
add action in menu.xml
```
<menuitem id="menu_guests"
              name="Guests"
              action="action_hotel_guests"
              parent="menu_guests_master"
              sequence="0"/>
```
# How to Access Right

> [!WARNING]
>error for me so I copied from another

------------

# To set icon for menu
```
hotel_B/
├── models/
│   ├── __init__.py
│   └── guest.py
├── static/
│   └── description/
│       └── hotel.png
│       └── icon.png
├── security/
│   └── ir.model.access.csv
├── views/
│   ├── guest_view.xml
│   └── menu.xml
├── __init__.py
└── __manifest__.py
```

first download web_responsive 15
and add custom modlues folder 


in menu.xml
```xml
<?xml version = "1.0" encoding = "utf-8" ?>
<odoo>

   <menuitem id = "menu_hotel_root"
             name = "Hotel"
             web_icon = "hotel_B,static/description/hotel.png"
             sequence = "0"/>

   <menuitem id = "menu_guest_master"
             name = "Guest Details"
             parent = "menu_hotel_root"
             sequence = "0"/>
</odoo>
```

