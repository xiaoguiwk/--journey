import requests
import random
import pandas as pd
from bs4 import BeautifulSoup
from PyQt5 import sip

def login(uname,upass):
    url = 'http://10.3.8.211'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
        }

    data = {
       'DDDDD':uname,
       'upass':upass,
       'AMKKey':' '
        }
    r = requests.post(url=url,data=data,headers=headers)
    return r

while True:
    account=pd.read_table('2014.txt',sep='\t')
    username=account['uname']
    password=account['upass']
    num=random.randint(0,len(account))

    r=login(username[num],password[num])
    if not '\n\n登\xa0录\xa0成\xa0功\n' in BeautifulSoup(r.text,'lxml').find('td').get_text():
        continue
    else:
        break