'''
$ sudo pip3 install fastapi
$ pip install uvicorn[standard]
$ uvicorn main:app --reload
'''
from typing import Optional

from fastapi import FastAPI

import requests

import json

import uvicorn

app = FastAPI()

file='https://raw.githubusercontent.com/OvierI/OpenAlexGroupclon/main/data/advisor.json'

#JSON SCHEME
#[{"student_id": str,
# "Evaluation 1":{"value": int,
#                 "%": int,
#                 "Description": str
#                 }, 
# ...
# }
#]

@app.get("/")
def read_item(student_id: str = ""):
    '''
    http://clustercien.udea.edu.co:8000/?student_id=1113674432
    '''
    #Real time JSON file
    r=requests.get(file)
    db=r.json()
    new_db=[ d for d in db if str(d.get('publication_year'))==student_id  ]
    f=open('data/filtered.json','w')
    json.dump(new_db,f)
    f.close()
    #with open(file) as json_file:
    #   db=json.load(json_file)

    if not student_id:
        return db
    else:
        return new_db
