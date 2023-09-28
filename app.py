from flask import Flask, render_template_string, redirect, url_for, jsonify
import urllib.parse
import time

app = Flask(__name__)

# Function to encode a URL
def encode_url(url):
    encoded_url = urllib.parse.quote_plus(url)
    return encoded_url

# Function to decode a URL
def decode_url(encoded_url):
    decoded_url = urllib.parse.unquote_plus(encoded_url)
    return decoded_url

# Route to encode the URL and generate the API link
@app.route('/encode')
def encode():
    url_to_encode = request.args.get('url')
    encoded_url = encode_url(url_to_encode)
    api_link = f'site.com/go/{encoded_url}'
    return jsonify(encoded_url=api_link)

# Route to display the page with the image and a 5-second timer
@app.route('/go/<encoded_url>')
def show_page(encoded_url):
    decoded_url = decode_url(encoded_url)
    
    # HTML content as a string
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="refresh" content="5;URL={decoded_url}">
        <title>Redirecting in 5 seconds</title>
    </head>
    <body>
        <h1>Click on 1st Result</h1>
        <img src="YOUR_IMAGE_URL_HERE" alt="Image">
        <p>Redirecting in 5 seconds...</p>
        <p>If you are not redirected, <a href="{decoded_url}">click here</a>.</p>
    </body>
    </html>
    """
    
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=False)
  
