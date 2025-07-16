import requests
import yaml
import json
from bs4 import BeautifulSoup

def summarize(text, max_length=300):
    if not text:
        return "要約情報なし"
    soup = BeautifulSoup(text, "html.parser")
    plain = soup.get_text()
    return plain[:max_length] + "..." if len(plain) > max_length else plain

def format_message(articles):
    message = {
        "title": "今日のおすすめニュースTOP5",
        "text": ""
    }
    sorted_articles = sorted(articles, key=lambda x: x["relevance"], reverse=True)[:5]
    for i, article in enumerate(sorted_articles, 1):
        message["text"] += f"**{i}. {article['title']}**\\n"
        message["text"] += f"AccurioDX関連度：{'★' * article['relevance']}{'☆' * (5 - article['relevance'])}\\n"
        message["text"] += f"{article['summary']}\\n"
        message["text"] += f"関連リンク\\n\\n"
    return message

def post_to_teams(message):
    with open("config/config.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    headers = {"Content-Type": "application/json"}
    payload = {
        "title": message["title"],
        "text": message["text"]
    }
    response = requests.post(config["teams_webhook_url"], headers=headers, data=json.dumps(payload))
    return response.status_code == 200
