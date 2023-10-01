from flask import Flask, request, redirect
import base64

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    redirect("https://t.me/AkenoHimejimaHBot")

@app.route('/paste/', methods=['POST'])
def paste():
    content = request.form['content']
    encoded_url = base64.b64encode(content.encode('utf-8')).decode('utf-8')
    return encoded_url

@app.route('/view/<encoded_url>', methods=['GET'])
def view(encoded_url):
    content = base64.b64decode(encoded_url.encode('utf-8')).decode('utf-8')
    return redirect(content)

if __name__ == '__main__':
    app.run(debug=True)
