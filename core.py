#!/usr/bin/env python
#coding: utf8
import webapp2
from webapp2_extras import jinja2, sessions, auth, security
import pprint
import sys

def jinja2_factory(app):
    "True ninja method for attaching additional globals/filters to jinja"

    j = jinja2.Jinja2(app)
    
    j.environment.globals.update({
        'uri_for': webapp2.uri_for,
        'hasattr': hasattr,
    })
    return j

class mdict(dict):
    def getlist(self, key):
        return self[key] if type(self[key]) == list else [self[key]]

    def __repr__(self):
        return type(self).__name__ + '(' + dict.__repr__(self) + ')'


class BaseHandler(webapp2.RequestHandler):
    "Handler Base for all requests"


    # Jinja2 setup
    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(factory=jinja2_factory, app=self.app)
    
    def render_response(self, _template, **context):
        ctx = {}
        ctx.update(context)
        rv = self.jinja2.render_template(_template, **ctx)
        self.response.write(rv)

    def log(self, context):
        pprint.pprint(vars(context))

    def write(self, context):
        self.response.write(context)

    def die(self, context):
        self.response.write(context)
        sys.exit(context)


