#!/usr/bin/env Python
# coding=utf-8

import tornado.web
import tornado.escape
import methods.readdb as mrd
from base import BaseHandler

class UserRegisterHandler(BaseHandler):
    def get(self):
        self.render("register.html")

    def post(self):
        # get information from cookie and DB
        self.check_xsrf_cookie()
        username = self.get_argument("username")
        password = self.get_argument("password")
        emailaddress = self.get_argument("mailaddress")
        user_register = mrd.select_table(table="users",column="*",condition="username",value=username)

        # check permission
        if user_register:
            self.redirect('/')
        else:
        	mrd.insert_user(table="users", value1=username, value2=password, value3=emailaddress)
        	self.set_current_user(username)
        	self.write(username)