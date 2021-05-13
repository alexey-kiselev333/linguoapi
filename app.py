from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html',translation=res['Translation']['Translation'])



if __name__ == '__main__':
    app.run()

URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = 'ZGQzNzUyZjctOGNiMC00ZjMxLWI0OTMtZGM0NjdiOGI0NjVlOjUxNWM2MzI4MDY1ZjQxOTE4NWFkMDgxZDMzMjhlYzEz'

headers_auth = {'Authorization': 'Basic ' + KEY}
auth = requests.post(URL_AUTH, headers=headers_auth)
if auth.status_code == 200:
    token = auth.text
    count=1
    while count==1:
        count=count-1
        word = input('Введите слово для перевода: ')
        if word:
            headers_translate = {
                'Authorization': 'Bearer ' + token
            }
            params = {
                'text': word,
                'srcLang': 1033,
                'dstLang': 1049
            }
            r = requests.get(URL_TRANSLATE, headers=headers_translate, params=params)
            res = r.json()
            try:
                print(res['Translation']['Translation'])
            except:
                print('Не найдено варианта для перевода')
else:
    print('Error!')

