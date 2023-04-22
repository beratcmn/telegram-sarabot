from dataclasses import dataclass
from classes.news import News, Article
import requests


@dataclass
class RequestHandler:
    NEWS_API: str = ""

    def getNews(self):
        url = (f'https://newsapi.org/v2/top-headlines?country=tr&apiKey={ self.NEWS_API }&category=general&pageSize=10')

        response = requests.get(url)
        # print(response.json())
        news = News(**response.json())
        news.articles = [Article(**article) for article in news.articles]

        return news
    

if __name__ == "__main__":
    from dotenv import load_dotenv
    import os
    load_dotenv()

    request_handler = RequestHandler(NEWS_API=os.getenv("NEWS_API_KEY"))
    news = request_handler.getNews()

    for article in news.articles:
        print(article.title)
    