import requests
import json

query = input("what type of news are you intersted in : ")
url=f"https://newsapi.org/v2/everything?q={query}&from=2025-02-28&sortBy=publishedAt&apiKey=f0bbeb1daa894534bd3d572fb00398d6"
r=requests.get(url)
news=json.loads(r.text)
# print(news, type(news))

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("----------------------------------------------")