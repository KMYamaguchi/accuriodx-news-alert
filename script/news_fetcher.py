import requests
import yaml

def fetch_news():
    with open("config/config.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    query = " OR ".join(
        config["keywords"]["INNOVATION_KEYWORDS"]
        + config["keywords"]["PROMOTION_KEYWORDS"]
        + config["keywords"]["ACCURIO_KEYWORDS"]
    )

    url = f"https://newsapi.org/v2/everything?q={query}&language=ja&pageSize=100&apiKey={config['news_api_key']}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json().get("articles", [])
    else:
        print("ニュース取得失敗:", response.status_code)
        return []
