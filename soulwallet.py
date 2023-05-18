from fake_useragent import UserAgent
import random
import time
import random
import requests

good = open('registred.txt', 'a')

headers = {
    'origin': 'https://www.soulwallet.io',
    'referer': 'https://www.soulwallet.io/',
    'authority': 'securecenter-poc.soulwallets.me',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
    'content-length': '35',
    'content-type': 'application/json',
    'origin': 'https://form.waitlistpanda.com',
    'sec-ch-ua': 'Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111',
    'user-agent': UserAgent().random
    }

def work():
    with open(input('Drop file with emails: '), 'r') as file_to_emails:
        while True:
            lines_proxe = open('proxies.txt', 'r')
            proxy = lines_proxe.readline()
            jopech = file_to_emails.readline()
            emails = jopech.split(":")[0]
            sess = requests.Session()
            sess.proxies = {
                'http': proxy,
                'https': proxy
            }
            sess.headers = headers
            url = 'https://securecenter-poc.soulwallets.me/add-to-list'
            json = {
                'email': emails
            }
            try:
                r = sess.post(url=url, headers=headers, json=json)
            except Exception as ex:
                print(ex)
                continue
            if r.status_code == 200:
                print(f'SUCCESS : {emails}\n')
                good.write(f'{emails}\n')
            else:
                print('хуйня')
                time.sleep(1)
                continue




while True:
    work()
