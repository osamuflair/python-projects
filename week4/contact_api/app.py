from flask import Flask, jsonify, request

app = Flask(__name__)


contact_list = [{"name": "Osamu", "email": "osamu@gmail.com", "phone": "08012345678"},{"name": "Flair", "email": "flair@gmail.com", "phone": "08012330678"},]
#used a list of dictionaries as database


@app.route('/contacts')#no need to specify the method, method is GET by default
def get_contacts():
    """a function that returns the data from the database"""
    return jsonify(contact_list) #jsonify converts the list of dictionaries into JSON

@app.route('/contacts', methods=['POST'])
def add_contact():
    """a function that appends data to the database"""
    data = request.get_json() #it first gets the data from the user
    contact_list.append(data) #then appends it to the database
    return jsonify({"message": "successful", "contact": data})

@app.route('/contacts/<name>', methods=['PUT'])
def update_contacts(name):
    """a function that updates existing data in a database"""
    data = request.get_json()
    for item in contact_list:#finding the data in the database, and updates it when found
        if item["name"] == name:
            item.update({'name' : data['name'], 'email' : data['email'], 'phone' : data['phone']})
            return jsonify({"message": "successful", "contact": data})
    return('NOT FOUND')
    

@app.route('/contacts/<name>', methods=['DELETE'])
def delete_contacts(name):
    """a function that deletes a specific data from a database"""
    for item in contact_list:
        if item["name"] == name:
            contact_list.remove(item)
            return jsonify({"message": "successful deleted", "contact": item})
    return('NOT FOUND')
    
if __name__ == '__main__':
    app.run(debug=True)

