{
    "name" : "Sales Order View",
    "version" : "1.0",
    "category" : "Generic Modules Control",
    'depends' : ['account','base','base_setup','product','sale','sale_order_dates'],
    'description': """
Functions:
==================================================
* Add menu items under Sales to show more details of Sales Orders in list view.
    """,
    
    "data" : ["sale_order_tree.xml"],
    "installable": True,
    "active": True
}
