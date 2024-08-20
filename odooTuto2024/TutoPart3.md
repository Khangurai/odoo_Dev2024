# How To Add Chatter To Form View

go to __manifest__.py
- add `'depends': ['mail'],`

go to guest_view.py
- add
```xml
<form>
	<sheet>
	</sheet>
	 <!--chatter-->
	<div class="oe_chatter">
		<field name="message_follower_ids" group="base.group_user"/>
		<field name="activity_ids"/>
		<field name="message_ids"/>
	</div>
</form>
```

go to guest.py
add
```python
_inherit = ["mail.thread",'mail.activity.mixin']
```

------------

# How To Enable Tracking For Fields

not working for me

------------


# How To Add Search Panel
go to guest_view.xml
add 
```xml
<search>
  <searchpanel>
  	<field name="gender" icon="fa-users" select="multi" enable_counters="1"/>
  </searchpanel>
</search>

```
in the `<search>` tag


------------

# How To Add Many2one Field

resource ပြန်စုရဦးမယ်

# How To Add Date And Datetime Fields

add  appointment.py
```python
appointment_time = fields.Datetime(string='Appointment Time')
booking_date = fields.Datetime(string='Booking Date')
```

add appointment_view.xml
```xml
<tree>
		<field name="guest_id"/>
		<field name="appointment_time"/>
		<field name="booking_date"/>
</tree>
```
add appointment_view.xml in form tag
```xml
<group>
		<field name="guest_id"/>
		<field name="appointment_time"/>
		<field name="booking_date"/>
</group>
```

To view time with  am pm
- go to settings\translation\languages
- add time format `%p`

------------


# How To Set Default Values For Fields

just add appointment.py(Models file)

```python
appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now)
```
this is time default values `default=fields.Datetime.now`

if you can add `default='male'`

------------

# How To Add Related Fields

- **field ပြင်ချင်ရင် models မှာသွားပြင် **
- **ပြီးတော့ xml view မှာ သွားပြောင်း**

in appointment.py

```python
gender = fields.Selection(related='guest_id.gender', readonly=False)
```

add `related`

`readonly=False` >>>> ***To edit***

------------
# How To Create Computed Field for datetime to age converter

in guest.py add class

```python
def _compute_age(self):
	for rec in self:
		today = date.today()
		if rec.date_of_birth:
			dob = fields.Date.from_string(rec.date_of_birth)  # Convert to datetime.date
			age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
			rec.age = age
			else:
				rec.age = 0
```

add `compute='_compute_age'`
```
age = fields.Integer(string='Age', compute='_compute_age', tracking=True)
```
and you can change  in guest_view.xml form view to view the field tab

if you want to directly answer to calculate age without save button 

`@api.depends('date_of_birth')`

------------

# How To Define Onchange Functions

in appointment.py add...
```python
@api.onchange('guest_id')
    def onchange_guest_id(self):
        if self.guest_id:
            self.ref = self.guest_id.ref
```

`ref` means field name so instead the name as you want to

`Onchange Functions` means you can link the data from primary model to another models

# How to rename field from view ....
in postgres type qurery
```query
delete from select_model;
```
select_model = `hotel_appointment`

and change run configuration on pycharm
`-c conf/odoo.conf -u hotel_B`

restart the server 

and now u'll see the results


------------















