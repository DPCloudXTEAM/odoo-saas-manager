# -*- coding: utf-8 -*-
##############################################################################
#
#    Saas Manager
#    Copyright (C) 2013 Sistemas ADHOC
#    No email
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{   'active': False,
    'author': u'Sistemas ADHOC',
    'category': u'base.module_category_knowledge_management',
    'demo_xml': [],
    'depends': ['saas_manager','stock',],
    'description': u"""
SaaS Manager Modifications
========================== 
Requires:
--------- 
* Requiere instalar sudo oerpenv pip install openerp-client-lib
""",
    'init_xml': [],
    'installable': True,
    'license': 'AGPL-3',
    'name': u'Saas Manager Modifications',
    'test': [
            'test/cannot_create_admin_user.yml',
            'test/instance_name_cannot_have_special_characters.yml'
            ],
    'data': [   
                'data/product.uom.csv',
                'data/res_partner_image_data.xml',
                # 'data/product_product_data.xml',
                'data/product.product.csv',
                'view/product_view.xml',
                'view/instance_view.xml',
                'view/instance_additional_view.xml',
                'workflow/instance_workflow.xml',
                  ],
    'version': u'1.1',
    'website': ''}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
