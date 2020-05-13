#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os

import jinja2
import webapp2

from pages.presentations import presentations
from pages.blog import blog
from pages.experiments import experiments

JINJA_ENVIRONMENT = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'template')),
        autoescape=True,
        extensions=['jinja2.ext.autoescape'])


class MainHandler(webapp2.RequestHandler):
    def get(self):
        variables = {
            "cv": "https://drive.google.com/file/d/18I-HMqul82L3MEKdDjd-xxw4AiK3GRWZ"
        }
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(variables))


class Experiments(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('details.html')
        self.response.write(template.render(experiments))


class Blog(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('details.html')
        self.response.write(template.render(blog))


class Presentations(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('details.html')
        self.response.write(template.render(presentations))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/blog', Blog),
    ('/presentations', Presentations),
    ('/experiments', Experiments)
], debug=True)
