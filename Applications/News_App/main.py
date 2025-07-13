import requests
key = "acb38e9d56ca4de5be8916d059d7d3db"
about = input("What topic news you want? ")
url = f"https://newsapi.org/v2/everything?q={about}&from=2025-06-13&sortBy=publishedAt&apiKey={key}"

r = requests.get(url)
data = r.json()

list = data["articles"]

for index,l in enumerate(list):
    
    print(f"{index}:- {l["title"]}")
    print(l["url"])
    print("\n***************************\n")
