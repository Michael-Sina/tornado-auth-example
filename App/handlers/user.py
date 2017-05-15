#!/usr/bin/env Python
# coding=utf-8

import tornado.web
import tornado.escape
import methods.readdb as mrd
from base import BaseHandler

class UserLoginHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        username = self.get_argument("user")
        username = tornado.escape.json_decode(self.current_user)
        user_infos = mrd.select_table(table="users",column="*",condition="username",value=username)
        self.render("user.html", users = user_infos)

class UserLogoutHandler(BaseHandler):
	def get(self):
		self.clear_current_user()
		self.redirect(self.get_argument("next", "/"))


