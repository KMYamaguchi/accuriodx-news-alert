from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def train_model(articles, feedback):
    texts = []
    labels = []
    for article in articles:
        url = article.get("url")
        if url in feedback:
            text = article.get("title", "") + " " + article.get("description", "")
            texts.append(text)
            labels.append(1 if feedback[url] == "like" else 0)

    if not texts:
        return None, None

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)
    model = LogisticRegression()
    model.fit(X, labels)
    return model, vectorizer

def predict(model, vectorizer, articles):
    if not model:
        return articles
    texts = [a.get("title", "") + " " + a.get("description", "") for a in articles]
    X = vectorizer.transform(texts)
    preds = model.predict(X)
    return [a for a, p in zip(articles, preds) if p == 1]
