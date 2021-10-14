# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import json
import logging
import re

from lxml import etree
import odoo as odoo1
import werkzeug
import werkzeug.contrib.sessions
import werkzeug.datastructures
import werkzeug.exceptions
import werkzeug.local
import werkzeug.routing
import werkzeug.wrappers
import werkzeug.wsgi
from odoo import api, models, _
from odoo.exceptions import AccessError, RedirectWarning, UserError
from odoo.tools import ustr
import shutil
import os


class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'
    

    def restrict_clear_session(self):
        path = odoo1.tools.config.session_dir
        shutil.rmtree(path)
        os.mkdir(path,mode = 0o777)
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }