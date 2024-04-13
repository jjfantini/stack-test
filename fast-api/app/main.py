from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client, Client
from pydantic import BaseModel
import json
import requests
import os


url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

if url is None:
    raise Exception('SUPABASE_URL not defined in environment variables')

if key is None:
    raise Exception('SUPABASE_KEY not defined in environment variables')

headers = {
    "apiKey": key,
    "Content-Type": "application/json",
}

supabase: Client = create_client(url, key)
app = FastAPI()


# cors setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get("/")
def read_root():
    return {"Hello": "rehab"}


class RegisterInput(BaseModel):
    email: str
    password: str


@app.post('/register')
def register(data: RegisterInput):
    body = json.dumps({
        "email": data.email,
        "password": data.password
    })

    endpoint = url + '/auth/v1/signup'
    resp = requests.request('POST', endpoint, headers=headers, data=body)
    return resp.json()


class LoginInput(BaseModel):
    email: str
    password: str


@app.post('/login')
def login(data: LoginInput, response: Response):
    body = json.dumps({
        "email": data.email,
        "password": data.password
    })

    endpoint = url + '/auth/v1/token?grant_type=password'
    resp = requests.request('POST', endpoint, headers=headers, data=body)

    if resp.status_code != 200:
        err = resp.json()
        raise HTTPException(status_code=401, detail=err["error_description"])

    respObj = resp.json()
    token = respObj["access_token"]
    response.set_cookie(key="token", value=token)
    return resp.json()


@app.get('/user')
def getUser(request: Request):
    token = request.headers.get('authorization')
    endpoint = url + '/auth/v1/user'
    print(token)
    if token is None:
        raise HTTPException(status_code=400, detail="Unauthorized")

    authorizedHeader = {
        **headers,
        "Authorization": token
    }

    resp = requests.request('GET', endpoint, headers=authorizedHeader)
    return resp.json()
