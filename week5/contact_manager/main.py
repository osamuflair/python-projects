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
    return contact_list

@app.post('/contacts/')
def create_contact(contact: Contact):
    item = contact_list[-1]
    num = item["id"] + 1
    new_contact = contact.model_dump()
    new_contact["id"] = num
    contact_list.append(new_contact)
    return({"message": "successful created", "contact": contact_list})