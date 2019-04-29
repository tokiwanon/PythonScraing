#urllibによるWebページ取得
from urllib.request import urlopen

f = urlopen('https://gihyo.jp/dp')
f = urlopen('https://sample.scraping-book.com/dp')

type(f)
f.read()
f.status
f.getheader('Content-Type')
