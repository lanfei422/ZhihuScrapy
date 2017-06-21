import sys
import re
import urllib2
import urllib
import requests
import cookielib

## 这段代码是用于解决中文报错的问题
reload(sys)
sys.setdefaultencoding("utf8")

loginurl = 'http://www.renren.com/PLogin.do'
logindomain = 'renren.com'  