import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests

req = requests.get(
    "https://ncov.kdca.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun=")
html = req.text
soup = BeautifulSoup(html, "html.parser")

# result = soup.find_all("th", scope="row")
# print(result)
# result = soup.select(
#     "#content > div > div.data_table.midd.mgt24 > table > tbody > tr:nth-child(2) > th")
# result = soup.select(
#     "#content > div > div.data_table.midd.mgt24 > table > tbody")
# result = soup.select(
#     "tbody > tr:nth-child(2) > th")

city = soup.find_all("th", scope="row")
x_data = []
for i in range(1, len(city)):
    x_data.append(city[i].text)

data = soup.find_all("td", headers="status_level l_type1")
y_data = []
for i in range(1, len(data)):
    y_data.append(int(data[i].text.replace(",", "")))
print(y_data)

plt.bar(range(18), y_data, label="발생자수")
plt.xticks(range(18), x_data)
plt.show()
