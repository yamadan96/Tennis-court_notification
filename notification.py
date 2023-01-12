from bs4 import BeautifulSoup
import requests

# 国府台テニスコート
url = "http://reserve.city.ichikawa.lg.jp/(S(osluhzmxrmspkg45nwvrjjvq))/Wg_ShisetsubetsuAkiJoukyou.aspx"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

# スキャンセルが発生した予約枠の日時を取得する
date = soup.find('span', class_='date')

# スキャンセルが発生した予約枠のコート番号を取得する
court_number = soup.find('span', class_='court-number')

# スキャンセルが発生した予約枠の施設名を取得する
facility = soup.find('span', class_='facility-name')

print(date.text, court_number.text, facility.text)
