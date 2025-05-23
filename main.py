from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

SUMMONER_NAME = "FENERBAHÇE-S1KER"
REGION = "euw"

@app.get("/rank")
def get_rank():
    url = f"https://www.op.gg/summoners/{REGION}/{SUMMONER_NAME}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    rank_div = soup.find("div", class_="TierRank")
    if rank_div:
        return {"rank": rank_div.text.strip()}
    return {"rank": "Derece bulunamadı."}
