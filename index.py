from flask import Flask , render_template, request


app = Flask(__name__)
@app.route('/pregunta', methods=['GET'])
def get_countries():
    import requests
    import html

    pregunta = request.args.get('id')

    query = pregunta.replace(" ", "")

    headers = {
        "DNT": "1",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.42 Safari/537.36",
        "Accept": "*/*",
        "Referer": "https://www.cymath.com/answer?q={}".format(query),
        "Connection": "keep-alive",
    }

    params = {
        "q": query,
    }

    r = requests.get("https://www.cymath.com/answer", params=params)

    cookies = {
        "PHPSESSID": r.headers["Set-Cookie"].split("=")[1].split(";")[0],
    }

    params["lang"] = "Es"

    response = requests.get("https://www.cymath.com/ajax/get_steps.php", headers=headers, params=params,
                            cookies=cookies)
    primera="<html><head><script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=default'></script></head><body><div  class='math'>mi ecuacion: \["+pregunta+"\]</div>"
    segunda= "</body></html>"

    return html.unescape(primera + response.text +segunda)
@app.route('/')
def home():
    return 'saludos'


if __name__ == '__main__':
    app.run(debug=True)
