from fastapi import FastAPI
from pydantic import BaseModel

class Contact(BaseModel):
    name: str
    email: str
    phone: str

app = FastAPI()

contact_list = [{'id':1, 'name':'Osamu', 'phone':'07089646092', 'email':'osamu1000@gmail.com'}, {'id':2, 'name':'Flair', 'phone':'08183029383', 'email':'flair2000@gmail.com'}]

@app.get('/contacts')
def get_contact():
    """gets all contact from the database(contact_list)"""
    return contact_list

@app.post('/contacts/')
def create_contact(contact: Contact):
    """creates a new contact"""
    item = contact_list[-1]
    num = item["id"] + 1
    new_contact = contact.model_dump()#convert to a dictionary
    new_contact["id"] = num
    contact_list.append(new_contact)
    return({"message": "successful created", "contact": contact_list})

@app.get('/contacts/{id}')
def get_contact_by_id(id: int):
    """gets a specific contact from the database(contact_list) by its id"""
    for items in contact_list:
        if items["id"] == id:
            return items
    return "NOT FOUND"


@app.put('/contacts/{id}')
def update_contact(id:int, contact: Contact):
    """updates an existing contact"""
    for items in contact_list:
        if items["id"] == id:
            new_contact = contact.model_dump()#convert to a dictionary
            items.update(new_contact)
            return({"message": "successful updated", "contact": contact_list})
    return "NOT FOUND"
