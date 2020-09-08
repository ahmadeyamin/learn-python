import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.44'
}
data = {
    '_method': 'POST',
    'mobile': '01999050360',
    'password': '9988776655.C0M'
}
with requests.Session() as s:
    web = s.get('https://eselfcare.banglalink.net/home/index',headers=headers)

    ss = BeautifulSoup(web.content,'html.parser')

    data['_csrfToken'] = ss.find('input',attrs={'name':'_csrfToken'})['value']

    login = s.post('https://eselfcare.banglalink.net/home/index',headers=headers,data=data)

    next_d = s.get('https://eselfcare.banglalink.net/ecare',headers=headers)
    
    # print(next_d.text)


print(login.text)