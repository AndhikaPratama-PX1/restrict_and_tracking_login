# -*- coding: utf-8 -*-
{
    'name': 'Restrict And Tracking User Login',
    'category': 'Technical', 
    'author': 'Apra IT Solutions', 
    'version': '1.0',
    'license': 'LGPL-3',
    'summary': """
        Use this module if you want to user cannot login with multi device, if user login with multi device so previosly login automatically logout from system. And this module can tracking or get location and ip from user login. This module have feature to force logout user too. 
    """, 
    'depends': ['base','base_setup'],
    'data': [ 
       'security/ir.model.access.csv',
       'views/users_views.xml',
       'views/res_config_setting_views.xml',

    ],   
    'images': [
        'static/description/restrict_and_tracking_login.png',
    ],

    'maintainer': 'Apra IT Solutions',
    'price': 35.00,
    'currency': 'USD',
}
