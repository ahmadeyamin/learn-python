import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.44',
    'Content-type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest'
}
config = {
    '_method': 'POST',
    '_csrfToken': None
}

all_accounts = [
    {
        'mobile': '*********',
        'password': '***********',
    },
    {
        'mobile': '**********',
        'password': '***********',
    },
    {
        'mobile': '**********',
        'password': '***********',
    },
    

]

while True:

    for info in all_accounts:
        
        with requests.Session() as session:

            web = session.get('https://eselfcare.banglalink.net/?redirect=%2Fecare', headers=headers)
            ss = BeautifulSoup(web.content, 'html.parser')

            config['mobile'] = info['mobile']
            config['password'] = info['password']
            config['_csrfToken'] = ss.find('input',attrs={'name':'_csrfToken'})['value']

            login = session.post('https://eselfcare.banglalink.net/home/index',headers=headers,data=config)
            next_d = session.get('https://eselfcare.banglalink.net/ecare',headers=headers)

            check = BeautifulSoup(next_d.text,'html.parser')
            if (check.select(".author-mobile h4")[0].get_text() == info['mobile']):
                print('Login Successfull')
            else:
                print('Login Failed')

    time.sleep((60*1)*5)
    print('End Sleep')