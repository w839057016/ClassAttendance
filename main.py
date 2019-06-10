# -*- coding: utf-8 -*-
# filename: main.py
import web
from handle import Handle
import menu
urls = (
    '/wx', 'Handle',
)


if __name__ == '__main__':
    app = web.application(urls, globals())
    menu.default_menu()
    app.run()