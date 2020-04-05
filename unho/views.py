from bs4 import BeautifulSoup as bs
import requests
html = requests.get("http://school.cbe.go.kr/unho-h/M0104020201/")
html_text = html.text
bs_html = bs(html_text, "html.parser")

result = {}

result['title'] = bs_html.title.get_text()
result['content'] = bs_html.body.div.get_text()

