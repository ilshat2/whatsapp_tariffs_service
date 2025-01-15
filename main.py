from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import httpx
from config import Config

app = FastAPI()


@app.get("/tariffs")
async def get_tariffs(currency: str = "RUB", crm: str = "lk"):
    url = f"{Config.API_URL}?currency={currency}&crm={crm}"
    headers = {
        "X-Whatsapp-Token": Config.API_TOKEN
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)

    if response.status_code == 200:
        return JSONResponse(content=response.json())
    else:
        raise HTTPException(status_code=response.status_code, detail="Error fetching tariffs")
