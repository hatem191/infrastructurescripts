# Python-Based API for Threat Intelligence

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/threats', methods=['GET'])
def get_threats():
    threats = {"malware": ["Trojan", "Ransomware"], "phishing_sites": ["phishingsite.com", "malicious.com"]}
    return jsonify(threats)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
