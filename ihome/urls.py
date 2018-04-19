# coding=utf-8
import os

from handlers import Passport, VerifyCode
from tornado.web import StaticFileHandler

handlers = [

    (r"/api/piccode", VerifyCode.PicCodeHandler),
    (r"/(.*)", StaticFileHandler,
     dict(path=os.path.join(os.path.dirname(__file__), "html"), default_filename="index.html")),
    (r"/", Passport.IndexHandler),
]