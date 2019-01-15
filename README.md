# pyserverchan
Server-chan for python.

# Install
```Python
pip install pyserverchan
```

# Getting started
You should go to [Server-Chan](http://sc.ftqq.com/3.version) get a SCKEY and bind WeChat. Your URL will be like 'https://sc.ftqq.com/[SCKEY].send '. You can use following functions to send text, picture, markdown files.
```Python
from pyserverchan import pyserver
svc = pyserver.ServerChan(user_URL)
svc.output_to_weixin("ATestMessage.")
svc.output_to_weixin_picture("http://sc.ftqq.com/static/image/bottom_logo.png")
svc.output_to_weixin_markdown("J:/pyserverchan/README.md")
```