import requests
import lxml.html

#映画.comのURLを指定して、HTMLソースを得る
r = requests.get("https://eiga.com/ranking/")
html = r.text

#HTMLをHtmlElementオブジェクトにする
root = lxml.html.fromstring(html)

print("映画ランキング第1位")

#Xpathを指定して、映画タイトルをスクレイピング
rank1_title = root.xpath("//*[@id='document_2575126293']/main/div/div/section[1]/table/tbody/tr[1]/td[2]/div/h2/a")

print(rank1_title[0].text)

#CSSセレクターで指定して、公開日をスクレイピング
rank1_day = root.cssselect("#document_2575126293 > main > div > div > section:nth-child(4) > table > tbody > tr:nth-child(1) > td.img > small")

print(rank1_day[0].text)

#2位, 3位も同様にコードを書きます

print('----------------------------')
print("映画ランキング第2位")

rank2_title = root.xpath("//*[@id='document_2575126293']/main/div/div/section[1]/table/tbody/tr[2]/td[2]/div/h2/a")

print(rank2_title[0].text)

rank2_day = root.cssselect("#document_2575126293 > main > div > div > section:nth-child(4) > table > tbody > tr:nth-child(2) > td.img > small")

print(rank2_day[0].text)

print('----------------------------')
print("映画ランキング第3位")

rank3_title = root.xpath("//*[@id='document_2575126293']/main/div/div/section[1]/table/tbody/tr[3]/td[2]/div/h2/a")

print(rank3_title[0].text)

rank3_day = root.cssselect("#document_2575126293 > main > div > div > section:nth-child(4) > table > tbody > tr:nth-child(3) > td.img > small")

print(rank3_day[0].text)