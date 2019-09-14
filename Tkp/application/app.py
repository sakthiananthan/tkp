import requests
from flask import Flask, render_template ,request,session

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('hompage.html')

@app.route('/redirect', methods=['POST'])
def redirect():
    return render_template('site_under_construction.html')