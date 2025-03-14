from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
import requests

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="http://localhost:8080/realms/myrealm/protocol/openid-connect/token")

@app.get("/user")
async def get_user(token: str = Depends(oauth2_scheme)):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get("http://localhost:8080/realms/myrealm/protocol/openid-connect/userinfo", headers=headers)
    return response.json()
