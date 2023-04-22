from typing import List
from dataclasses import dataclass

@dataclass
class Article:
    source: dict
    author: str
    title: str
    description: str
    url: str
    urlToImage: str
    publishedAt: str
    content: str

@dataclass
class News:
    status: str
    totalResults: int
    articles: List[Article]
