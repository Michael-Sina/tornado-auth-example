#!/usr/bin/env Python
# coding=utf-8

import sys    
reload(sys)
sys.setdefaultencoding("utf-8")

from handlers.main import MainHandler, PageNotFoundHandler
from handlers.user import UserLoginHandler, UserLogoutHandler
from handlers.register import UserRegisterHandler

url = [
    (r'/', MainHandler),
    (r'/login', UserLoginHandler),
    (r'/register', UserRegisterHandler),
    (r'/logout', UserLogoutHandler),
    (r'.*', PageNotFoundHandler),
]
