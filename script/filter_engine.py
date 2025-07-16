import yaml

def calculate_relevance(article, keywords):
    score = 0
    text = (article.get("title", "") + " " + article.get("description", "")).lower()
    for category in keywords.values():
        for kw in category:
            if kw.lower() in text:
                score += 1
    return min(score, 5)
