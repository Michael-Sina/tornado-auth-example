#!/usr/bin/env Python
# coding=utf-8

import tornado.web
import methods.readdb as mrd
from base import BaseHandler

class MainHandler(BaseHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        # get information from cookie and DB
        self.check_xsrf_cookie()
        username = self.get_argument("username")
        password = self.get_argument("password")
        user_infos = mrd.select_table(table="users",column="*",condition="username",value=username)

        # check permission
        if user_infos:
            db_pwd = user_infos[0][2]
            if db_pwd == password:
               self.set_current_user(username) 
               self.write(username)
            else:
               return self.finish('password is wrong!')
        else:
            return self.finish('username is wrong!')


class PageNotFoundHandler(BaseHandler): 
    def get(self):                            
        self.render("404.html")


