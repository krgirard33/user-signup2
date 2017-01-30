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
import webapp2

def build_page():
    page_header = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Signup Form</title>
            <style type="text/css"> 
                .error {color: red;}
            </style>
        </head>
    <body>
        <h1>
                <a href="/">Signup Form</a>
        </h1>  """

    # html boilerplate for the bottom of every page
    page_footer = """
        </body>
    </html> """

    # html signin form 
    form_signup = """
        <form method="post">
            <table>
                <tr>
                    <td><label for="username">Username</label></td>
                    <td>
                        <input name="username" type="text" value="" required>
                        <span class="error"></span>
                    </td>
                </tr>
                <tr>
                    <td><label for="password">Password</label></td>
                    <td>
                        <input name="password" type="password" required>
                        <span class="error"></span>
                    </td>
                </tr>
                <tr>
                    <td><label for="verify">Verify Password</label></td>
                    <td>
                        <input name="verify" type="password" required>
                        <span class="error"></span>
                    </td>
                </tr>
                <tr>
                    <td><label for="email">Email (optional)</label></td>
                    <td>
                        <input name="email" type="email" value="">
                        <span class="error"></span>
                    </td>
                </tr>
            </table>
            <input type="submit">
        </form> """
    return page_header + form_signup + page_footer 

def build_welcome():
    page_header = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Welcome Page</title>
            <style type="text/css"> 
                .error {color: red;}
            </style>
        </head>
        <body>
            <h1>
                Welcome, {{username}}!                
            </h1> 
        </body>
    </html> """
    return page_header + page_footer

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(build_page())


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/', build_welcome)
], debug=True)
