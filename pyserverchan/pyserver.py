# Author: GanjinZero
# Description: Server-chan for python.
# P.S. You should go to http://sc.ftqq.com/ to get an url.


import requests
import base64

def check_is_web(string):
    check_list = ['www', 'com', 'net']
    for checker in check_list:
        if string.find(checker) != -1:
            return True
    return False

class ServerChan(object):
    def __init__(self, url):
        self.url = url

    def output_to_weixin(self, title, content=''):
        requests.get(self.url, params={'text':title, 'desp':content})
        return

    def output_to_weixin_picture(self, picture, title='Picture'):
        # picture: A network address or a local address
        # may only support png
        # local picture cannot be sent now
        if check_is_web(picture):
            content = '![' + title + '](' + picture + ')'
        else:
            with open(picture, 'rb') as pic:
                base64pic = base64.b64encode(pic.read())
                content = '![' + title + '](data:image/png;base64,' + str(base64pic) + ')'
        requests.get(self.url, params={'text':title, 'desp':content})
        return

    def output_to_weixin_markdown(self, markdown_file, title='MarkdownFile'):
        # markdwon_file: A local address
        with open(markdown_file, 'r', encoding='utf-8') as md:
            content = md.read()
        requests.get(self.url, params={'text':title, 'desp':content})
        return