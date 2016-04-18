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
import os,webapp2,jinja2
from google.appengine.ext import db
from google.appengine.api import images

template_dir = os.path.join(os.path.dirname(__file__), 'bootstrap')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)

class Handler(webapp2.RequestHandler):
    def write (self,*a,**kw):
        self.response.out.write(*a,**kw)
    def render_str(self, template, **params):
        t= jinja_env.get_template(template)
        return t.render(params)
    def render(self, template,**kw):
        self.write(self.render_str(template,**kw))

class MainPage(Handler):
    def render_main(self):  #,title="",post="",error="",creator="",new=True)
        #posts=db.GqlQuery("SELECT * FROM Post ORDER BY created DESC")

        self.render("index.html")#,user=user,events=events,articles=articles)
    def get(self):
        #self.write("hello")
        #q=self.request.get("q")
        self.render_main()
    def post(self):
        #title=self.request.get("title")
            #p=Post(title=title,creator=creator,post=post)
            #p.put()
            #theid=p.key().id()
            #app.router.add(('/blogs'+theid, redirect))
            #self.redirect("/blog/%d" %theid)
            #self.redirect('/r')
        pass

app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)