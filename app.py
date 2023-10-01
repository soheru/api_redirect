from flask import Flask, render_template, request, jsonify
import base64

app = Flask(__name__)

# Function to encode a URL
def encode_url(url):
    encoded_url = base64.b64encode(url.encode('utf-8')).decode('utf-8')
    return encoded_url

# Function to decode a URL
def decode_url(encoded_url):
    decoded_url = base64.b64decode(encoded_url.encode('utf-8')).decode('utf-8')
    return decoded_url


@app.route('/encode')
def encode():
    url_to_encode = request.args.get('url')
    encoded_url = encode_url(url_to_encode)
    api_link = f'https://redirect.sohailkhan.in/go/{encoded_url}'
    return jsonify(encoded_url=api_link)    

# Route to display the page with the image and a 5-second timer
@app.route('/go/<encoded_url>')
def show_page(encoded_url):
    decoded_url = decode_url(encoded_url)
    return render_template('redirect.html', decoded_url=decoded_url)

if __name__ == '__main__':
    app.run(debug=True)
