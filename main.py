from capmonster_python.turnstile import TurnstileTask
from fake_useragent import UserAgent
from web3.auto import w3
import random
import string
import json as js
import time
import random, string
import requests
import names

capmonster = 1
ref_code = 'N9MemUokiOfTrSTdCgcq'
test_proxy_url = 'http://wtfismyip.com/text'

def cap_get_token():
    captcha_key = 'eac19636562d91ede821335029ce2eef'
    if '\n' in captcha_key:
        captcha_key = captcha_key[:-1]
    capmonster = TurnstileTask(captcha_key)
    task_id = capmonster.create_task("https://form.waitlistpanda.com/go/4C0JLtlQcH3sBqb0wCbx?ref=UDKXyeixLhYG2lQDxtNm",
                                     "0x4AAAAAAABCOgX4x6RvmA0a")
    result = capmonster.join_task_result(task_id)
    return result['token']

headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ru,en-US;q=0.9,en;q=0.8',
    'authorization': 'Bearer',
    'content-length': '575',
    'content-type': 'application/json',
    'origin': 'https://form.waitlistpanda.com',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'user-agent': UserAgent().random
    }

def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string

def generate_random_number():
    rand_num = random.randint(1000, 9999)
    stringg = str(rand_num)
    return stringg

def work():
    while True:
        lines_proxe = open('proxies.txt').read().splitlines()
        proxy = random.choice(lines_proxe)
        lines_emails = open('emails.txt').read().splitlines()
        emails = random.choice(lines_emails)
        sess = requests.Session()
        sess.proxies = {
            'http': proxy,
            'https': proxy
    }
        sess.headers = headers
        account = w3.eth.account.create()
        address = account.address
        url = 'https://audience-consumer-api.zootools.co/v3/lists/4C0JLtlQcH3sBqb0wCbx/members'
        test_proxy_url = 'http://wtfismyip.com/text'
        try:
            r = sess.post(url=test_proxy_url)
        except:
            print(f'invalid proxy - {proxy}')
            continue
        json = {
            'captchaToken': cap_get_token(),
            'cryptoAddress': address,
            'e41be8h2g372f': generate_random_string(15) + '#' + generate_random_number(),
            'email': emails,
            'referral': ref_code
        }
        try:
            r = sess.post(url=url, headers=headers, json=json)
        except Exception as ex:
            print(ex)
            continue
        if r.status_code < 400:
            jres = js.loads(r.text)
            if jres['nextStep'] == 'confirmation':
                print(f'SUCCESS : {proxy} : {emails}\n')
        else:
            print('ip limit')
            time.sleep(1)
            continue




while True:
    work()
