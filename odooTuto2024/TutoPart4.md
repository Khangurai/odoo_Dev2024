# Understanding Rec Name

note ကျန်

---

# How To Add Notebook And Pages

note ကျန်

---

# How To Define HTML Field

add appointment.py
`room = fields.Html(string='Room')`

```xml
<notebook>
	<page string="Room" name="Room">
	<field name="room" placeholder="Enter your room"/>
	</page>
	<page string="Services" name="Services">
	</page>
</notebook>
```

---

# Remove Create, Edit, Delete and Duplicate Options From Views

ကိုယ်ပေးမလုပ်ချင်တဲ့ model ,form တွေကို zero ပေးရင် permission ပိတ်တာနဲ့တူတူပဲ့
`<form></form>` `<tree></tree>`

> create="0" delete="0" edit="0"

```xml
<form create="0" delete="0" edit="0">
</form>
<tree create="0" delete="0" edit="0">
</tree>
```

---

# Working Of Priority Widget

star widget ထည့်နည်း

add code to appointment.py

```xml
priority = fields.Selection([
        ('0', 'Very Low'),
        ('1', 'Low'),
        ('2', 'Normal'),
        ('3', 'High')], string='Priority')
```

add xml format to view

```xml
<form>
	<sheet>
		<div class="oe_title">
			<h2>
				<field name="priority" widget="priority" class="mr-3"/>
			</h2>
		</div>
```

---

# How To Add Buttons

## Show Confirmation Message On Button Click

# How To Add Help Messages For Fields And Buttons

# How To Fix Compute Method Failed To Assign Value Error

# Rainbow Effect

# Badge Widget And Decorations

# How To Give Color For Tree View Records

# Widget List Activity In Odoo

# Dynamic Tree View

# Many2one Avatar And Many2One Avatar User Widget

add field in appointment.py not working

# odoo module auto update command

go to pycharm \edit configuration\ type `-c conf/odoo.conf -u hotel_B`

# Create Module Using Scaffold Command In Odoo

in terminal

```
D:\odoo_dev\odoo_version\venu\Scripts\python.exe .\odoo-bin scaffold hotel_B_inheritence D:\odoo_dev\odoo_version\15\custom_module
```

to create module with command

```
D:\odoo_dev\odoo_version\venu\Scripts\python.exe .\odoo-bin scaffold hotel_test D:\odoo_dev\odoo_version\15\custom_module
```

---

# How To Create Sequence And Generate Sequential Value For Record

`data\sequence_dat.xml`

```xml
<?xml version = "1.0" encoding = "utf-8" ?>
<odoo>
    <record id="seq_hotel_guest" model="ir.sequence">
            <field name="name">Hotel Guest</field>
            <field name="code">hotel.guest</field>
            <field name="prefix">HT</field>
            <field name="padding">5</field>
            <field name="company_id" eval="False"/>
        </record>
</odoo>
```

`guest.py`

```python
@api.model
    def create(self, vals):
        vals['ref']=self.env['ir.sequence'].next_by_code('hotel.guest')
        return super(HotelGuest, self).create(vals)
```

`__manifest__.py`

```python
'data/sequence_data.xml'
```

---

# How To Override Write Method In Odoo

```python
def write(self, vals):
        if not self.ref and not vals.get('ref'):
            vals['ref']=self.env['ir.sequence'].next_by_code('hotel.guest')
        return super(HotelGuest, self).write(vals)
```

---

# Default Get Function In Odoo

> cancel_appointment.py

```python
@api.model
        def default_get(self, fields):
            res = super(CancelAppointmentWizard, self).default_get(fields)
            res['cancellation_date'] = datetime.date.today()
            return res
```

---

# Name Get Functiong

`guest.py`

```python
def name_get(self):
        return [(record.id, "[%s] %s" % (record.ref, record.name)) for record in self]
```

you will see result in appointment guest field

![logo](https://github.com/Khangurai/odoo15/blob/master/odoo_Tuto2024/assests/3.png)

---

# Menu And SubMenu Without Specifying Parent

> menu_nested format

create menu [check](https://github.com/Khangurai/odoo15/blob/master/odoo_Tuto2024/how_to_create_menu_and_submenu.md)
so easy check out [youtube](https://www.youtube.com/watch?v=bKHDHMP9usg&list=PLqRRLx0cl0hoZM788LH5M8q7KhiXPyuVU&index=84)

---

# Target Inline In Odoo || Inline Actions In Odoo || Target In Odoo Actions || Odoo Window Action

---

# Active Id In Odoo

appointment form ထဲက cancel button ကို wizard pop up ပေါ်အောင်ချိတ်နည်း

```xml
<button name = "%(hotel_B.action_cancel_appointment)d" string = "Cancel"
                type = "action" states = "confirm,done"/>
```

appointment form ထဲက sequence  ကို wizard appointment_id ပေါ်အောင်ချိတ်နည်း
`appointment.py`

```python
def name_get(self):
    result = []
    for record in self:
        name = record.sequence or '[No Sequence]'
        result.append((record.id, name))
    return result
```

`cancel_appointment.py`

```python
@api.model
def default_get(self, fields):
    res = super(CancelAppointmentWizard, self).default_get(fields)
    res['cancellation_date'] = datetime.date.today()
    res['appointment_id'] = self.env.context.get('active_id')
    return res
```

add res appointment_id

`appointment_view.xml`
add context

```xml
<button name = "%(hotel_B.action_cancel_appointment)d" string = "Cancel"
                    context="{'default_appointment_id':'active_id'}
<!--                context="{'default_reason':'Test'}"-->
                type = "action" states = "confirm,done"/>
```

# Hide Field Based On Context In Odoo

`appointment.py`

```xml
<button name = "%(hotel_B.action_cancel_appointment)d" string = "Cancel"
            context="{'default_reason':'Test', 'hide_appointment': 1 }"
            type = "action" states = "confirm,done"/>
```

`cancel_appointment.py`

```xml
<field name="appointment_id" invisible="context.get('hide_appointment')"/>
```

# How To Raise Validation Error In Odoo

`cancel_appointment.py add condition`

```python
def action_cancel(self):
    for rec in self:
        if rec.appointment_id:
            rec.appointment_id.state = 'cancel'  # Ensure that you are updating the correct model
            rec.state = 'cancel'
        else:
            raise UserError("No appointment selected.")
    if self.appointment_id.booking_date == fields.Date.today():
        raise ValidationError(_('Sorry, cancellation is not allowed on the same day of booking date'))
```

# Apply Domain For Fields In Odoo

[options]
; This is the password that allows database operations:
admin_passwd = Akk@712001
db_maxconn = 64
db_host = localhost
db_port = 5432
db_user = odoo
db_password = odoo
xmlrpc_port = 8072
limit_memory_hard = 0
addons_path = D:\odoo_dev\odoo_version\15\odoo\addons,D:\odoo_dev\odoo_version\15\custom_module


