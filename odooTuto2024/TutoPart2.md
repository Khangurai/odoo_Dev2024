# To create form view

add this code in guest_view.xml
```xml
<record id="view_hotel_guest_form" model="ir.ui.view">
            <field name="model">hotel.guest.form</field>
            <field name="model">hotel.guest</field>
            <field name="arch" type="xml">
                <form>
                    <group>
                        <field name = "name"/>
                        <field name = "age"/>
                        <field name = "gender"/>
                    </group>
                </form>
            </field>
     </record>
```
>in `<form>` tag you can easily create the format of form

**to view form `Settings\views`**

> [!TIP]
>if you create sheet view fom just create `<sheet>` tag between `<form>` and `<group>` tag

![ViewForm](https://github.com/Khangurai/odoo_Tuto2024/blob/main/assests/2.png)

>**to devide the form group like this** 

**add code in this section between `<group>` tag** 

```xml
<form>
    <sheet>
        <group>
            <group>
                <field name = "name"/>
                <field name = "age"/>
            </group>
            <group>
                <field name = "gender"/>
            </group>
        </group>
    </sheet>
</form>
```


------------

# How to define a Tree view

view form/list/tree တွေပြောင်းမယ်ဆိုရင် windows action ရဲ့  xml ထဲမှာ ပဲ့ပြောင်းရုံပဲ့ view type ပြောင်းရုံပဲ့

add befor the form view 
i think this view type is order by window action 
so you see the first one is tree view `(primary view)`
and then you add the record u'll see  `(form view)`
```xml
<record id="view_hotel_guest_tree" model="ir.ui.view">
            <field name="model">hotel.guest.tree</field>
            <field name="model">hotel.guest</field>
            <field name="arch" type="xml">
                <tree>
                    <field name = "name" string="Guest Name"/>
                    <field name = "age"/>
                    <field name = "gender"/>
                </tree>
            </field>
     </record>
```

------------

# How To Define Search View In Odoo

add serarch tag in guest_view.xml

```xml
<record id="view_hotel_guest_search" model="ir.ui.view">
            <field name="model">hotel.guest.search</field>
            <field name="model">hotel.guest</field>
            <field name="arch" type="xml">
                <search>
                    <field name = "name" string="Guest Name" filter_domain="['|',('name','ilike',self),('age','ilike',self),('code','ilike',self)]"/>
                    <field name = "code"/>
                    <field name = "age"/>
                    <field name = "gender"/>
                </search>
            </field>
    </record>
```

- search view က search bar မှာ ရှာလို့ရအောင် လုပ်ပေးတယ်
- ရှာစေချင်တဲ့ attribute တွေကို search tag ထဲမှာ ထည့်ပေးရုံပဲ့

if you want to search multiple search attribute 
just add **`filter domain`**  code like this 

```xml
<field name = "name" string="Guest Name" filter_domain="['|',('name','ilike',self),('age','ilike',self),('code','ilike',self)]"/>
```
if you not clear check this [youtube](https://www.youtube.com/watch?v=zPJrnQ8YUms&list=PLqRRLx0cl0hoZM788LH5M8q7KhiXPyuVU&index=13)
# How To Add Filters

add code in `search<>` tag 
```xml
<filter name = "filter_male" string="Male" domain="[('gender','=','male')]"/>
<filter name = "filter_female" string="Female" domain="[('gender','=','female')]"/>
```
> ဒီလို ထည့်လိုက်မယ်ဆိုရင် male or female select မှတ်ပြီးရှာလို့ရတယ်

**Add Speatator**
```xml
<filter name = "filter_male" string="Male" domain="[('gender','=','male')]"/>
<separator/>
<filter name = "filter_female" string="Female" domain="[('gender','=','female')]"/>
```
`<separator/>` ပါရင်  record မှာ male ရော female ရော ပါတာကို ရှာတာမျိုးဖြစ်တယ်
> [!NOTE]
> sample code like this `<filter name = "filter_kids" string="Kids" domain="[('age','&lt;=','5')]"/>`

## How To Add Group By Options
code:
```xml
<group expand="0" string="Group By">
                        <filter name="group_by_gender" string="Gender" context="{'group_by':'gender'}"/>
                        <filter name="group_by_age" string="Adult" domain="[('age','&lt;=','5')]" context="{'group_by':'age'}"/>
                    </group>
```
groupအလိုက်ပြတာ မိုက်တော့မိုက်တယ်

# How To Add Archive and Unarchive Options

> [!CAUTION]
>tutorial is unavailable in this chapter
 to study [youtube](https://www.youtube.com/watch?v=wNRONFlI3xo&list=PLqRRLx0cl0hoZM788LH5M8q7KhiXPyuVU&index=15)


------------
# How To Apply Domain For Menu In Odoo
> [!CAUTION]
>tutorial is unavailable in this chapter
 to study [youtube](https://www.youtube.com/watch?v=AqlXJVUYshs&list=PLqRRLx0cl0hoZM788LH5M8q7KhiXPyuVU&index=16)

------------



# How To Set Default Value Using Context In Odoo
> [!CAUTION]
>tutorial is unavailable in this chapter
 to study [youtube](https://www.youtube.com/watch?v=AqlXJVUYshs&list=PLqRRLx0cl0hoZM788LH5M8q7KhiXPyuVU&index=17)








