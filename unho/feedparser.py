import feedparser

url = "http://school.cbe.go.kr/unho-h/M0104020201/"

feed = feedparser.parse(url)

print(feed)