#!/usr/bin/env python
#coding: utf8
import webapp2
from webapp2_extras import jinja2, sessions, auth, security
import core
import json
import os
from pprint import pprint
config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': '',
}
config['webapp2_extras.auth'] = {
}

debug = True
class IndexHandler(core.BaseHandler):
    "Lista as campanhas"
    def get(self):
    	fdata = open('data.json')
    	data = json.load(fdata)
    	fdata.close()
		
        self.render_response("index.html",data=data)



app = webapp2.WSGIApplication([
    webapp2.Route(r'/', handler=IndexHandler, name='home'),
], debug=True, config=config)