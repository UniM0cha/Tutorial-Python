import requests
from bs4 import BeautifulSoup
req = requests.get(
    'https://ncov.kdca.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun=')
html = req.text
soup = BeautifulSoup(html, "html.parser")
print(soup)
