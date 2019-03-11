# Author: GanjinZero
# Description: Server-chan for python.
# P.S. You should go to http://sc.ftqq.com/ to get an url.


import requests
import base64
import os


def check_is_web(string):
    check_list = ['www', 'com', 'net']
    for checker in check_list:
        if string.find(checker) != -1:
            return True
    return False


class ServerChan(object):
    def __init__(self, url=""):
        path = os.path.expanduser("~") + "/.pyserverchan"
        if url == "":
            if os.path.isfile(path):
                with open(path, 'r') as f:
                    self.url = f.read()
            else:
                print(".pyserverchan doesn\'t exist, please initialize with a url.")
        else:
            self.url = url
            if not os.path.isfile(path):
                os.system("touch ~/.pyserverchan")
            with open(path, 'w') as f:
                f.write(self.url)


    def output_to_weixin(self, title, content=''):
        requests.get(self.url, params={'text':title, 'desp':content})


    def output_to_weixin_picture(self, picture, title='Picture'):
        # picture: A network address or a local address
        # local picture max size 7kb
        if check_is_web(picture):
            content = '![' + title + '](' + picture + ')'
        else:
            with open(picture, 'rb') as pic:
                picture_type = picture.split(".")[-1]
                base64pic = base64.b64encode(pic.read())
                base64str = str(base64pic)[2:-1]
                content = '![' + title + '][link1]' + os.linesep + os.linesep
                content += '[link1]:data:image/' + picture_type + ';base64,' + base64str
        requests.get(self.url, params={'text':title, 'desp':content})


    def output_to_weixin_markdown(self, markdown_file, title='MarkdownFile'):
        # markdwon_file: A local address
        with open(markdown_file, 'r', encoding='utf-8') as md:
            content = md.read()
        requests.get(self.url, params={'text':title, 'desp':content})

