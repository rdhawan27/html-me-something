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
import random
def Lucky_message():
    List_Lucky_message=["You will strike gold","Going down will bring luck","Work hard",
    "Keep learning and you shall find your reward"]
    random_number=random.randint(0,2)
    Lucky_Message= List_Lucky_message[random_number]
    return  Lucky_Message
class MainHandler(webapp2.RequestHandler):
    def get(self):
        Header= "<H1> Fortune Cookie </H1>"
        random_number= str(random.randint(1,100))
        Lucky_number="<H3><p> Your lucky number is:<p></H1>" + "<strong>" +random_number +"</strong>"

        Lucky_phrase= "<H3><p> Your Fortune today is: <p></H1>"+ "<strong>"+Lucky_message()+"</strong>"

        Refresh_button= "<p><a href='.'><button> Refresh Button for Cookie</button> </a></p>"
        Content= Header + Lucky_number + Lucky_phrase + Refresh_button


        self.response.write(Content)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
