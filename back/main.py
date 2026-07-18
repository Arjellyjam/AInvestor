from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Sdata import getTicker
from news import tickerNews
from ai import aiInput

app = FastAPI()

origins = [
    "http://127.0.0.1:5500",
    "http://localhost",
    "http://localhost:8080",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/stock/{item_id}")
async def root (
    item_id: str | None = None
):
    data = getTicker(item_id)
    news = tickerNews(item_id)
    response = aiInput(item_id, data, news)
    return {"price": data, "news": news, "artificial": response}
