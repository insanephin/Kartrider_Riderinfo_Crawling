import requests, re
from bs4 import BeautifulSoup

i=input("라이더명을 입력해주세요 : ")

hdr = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50X2lkIjoiMTY5NTA1ODUyNSIsImF1dGhfaWQiOiIyIiwidG9rZW5fdHlwZSI6IkFjY2Vzc1Rva2VuIiwic2VydmljZV9pZCI6IjQzMDAxMTM5MyIsIlgtQXBwLVJhdGUtTGltaXQiOiIyMDAwMDoxMCIsIm5iZiI6MTU4OTc1NjI3NCwiZXhwIjoxNjUyODI4Mjc0LCJpYXQiOjE1ODk3NTYyNzR9.PtHODk_744Qb2kQbgRWfC5hDraV8MCzwtBS22t495fs",
}
url = 'https://api.nexon.co.kr/kart/v1.0/users/nickname/' + i
req = requests.get(url, headers=hdr)
result = req.json()
try:
    nickname = result['name']
except KeyError:
    print("존재하지 않는 라이더명입니다.")
    exit

response = requests.get(f'http://kart.nexon.com/Garage/Main?strRiderID={nickname}')
response2 = requests.get(f'http://kart.nexon.com/Garage/Item?strRiderID={nickname}')
response3 = requests.get(f'http://kart.nexon.com/Garage/Emblem?strRiderID={nickname}')

soup = BeautifulSoup(response.text, 'html.parser')
soup2 = BeautifulSoup(response2.text, 'html.parser')
soup3 = BeautifulSoup(response3.text, 'html.parser')

name = str(soup.find_all('span', {'id':'RiderName'})[0])
name = re.sub(r'<[^>]+>', '', name, 0).strip()

totalit = str(soup2.find('div', {'id':'CntItemDet'}).find_all('span')[0])
totalit = re.sub('<.+?>', '', totalit, 0).strip()

ch = str(soup2.select('dd')[2])
ch = re.sub('<.+?>', '', ch, 0).strip()
kart = str(soup2.select('dd')[3])
kart = re.sub('<.+?>', '', kart, 0).strip()
wear = str(soup2.select('dd')[4])
wear = re.sub('<.+?>', '', wear, 0).strip()
chi = str(soup2.select('dd')[5])
chi = re.sub('<.+?>', '', chi, 0).strip()
ex = str(soup2.select('dd')[6])
ex = re.sub('<.+?>', '', ex, 0).strip()
em = str(soup3.select('b')[2])
em = re.sub('<.+?>', '', em, 0).strip()

mainitem1 = str(soup2.find_all('span', {'class':'TxtItem'})[0])
mainitem1 = re.sub('<.+?>', '', mainitem1, 0).strip()
mainitem2 = str(soup2.find_all('span', {'class':'TxtItem'})[1])
mainitem2 = re.sub('<.+?>', '', mainitem2, 0).strip()
mainitem3 = str(soup2.find_all('span', {'class':'TxtItem'})[2])
mainitem3 = re.sub('<.+?>', '', mainitem3, 0).strip()

mainimg = str(soup.find('span', {'class': 'ImgItem'}).img['src'])

print("\n라이더명 - "+name+f'(http://kart.nexon.com/Garage/Item?strRiderID={name})')
print("총 아이템개수 - "+totalit)
print("캐릭터 - "+ch)
print("카트바디 - "+kart)
print("착용아이템 - "+wear)
print("치장아이템 - "+chi)
print("기타아이템 - "+ex)
print("엠블럼 - "+em)
print(f"메인아이템 - {mainitem1}/{mainitem2}/{mainitem3}")
print("메인아이템이미지(1번)"+mainimg)