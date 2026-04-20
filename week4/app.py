from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'INDEX'


contact_list = [{"name": "Osamu", "email": "osamu@gmail.com", "phone": "08012345678"},{"name": "Flair", "email": "flair@gmail.com", "phone": "08012330678"},]

@app.route('/contacts')
def get_contacts():
    return jsonify(contact_list)

if __name__ == '__main__':
    app.run(debug=True)

