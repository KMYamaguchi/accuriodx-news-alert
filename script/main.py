from news_fetcher import fetch_news
from filter_engine import calculate_relevance
from teams_notifier import summarize, format_message, post_to_teams
from feedback_manager import load_feedback
from learner import train_model, predict
import yaml

with open("config/config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

articles = fetch_news()
feedback = load_feedback()

for article in articles:
    article["relevance"] = calculate_relevance(article, config["keywords"])
    article["summary"] = summarize(article.get("description", ""))

model, vectorizer = train_model(articles, feedback)
if model:
    articles = predict(model, vectorizer, articles)

message = format_message(articles)
success = post_to_teams(message)
print("投稿成功" if success else "投稿失敗")
