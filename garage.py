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
    print("존재하지 않는 닉네임입니다.")
    exit

response = requests.get(f'http://kart.nexon.com/Garage/Main?strRiderID={nickname}')
soup = BeautifulSoup(response.text, 'html.parser')

response2 = requests.get(f'http://kart.nexon.com/Garage/Record?strRiderID={nickname}')
soup2 = BeautifulSoup(response2.text, 'html.parser')

name = str(soup.find_all('span', {'id':'RiderName'})[0])
name = re.sub(r'<[^>]+>', '', name, 0).strip()

guild = str(soup.find_all('span', {'id':'GuildName'})[0])
guild = re.sub('<.+?>', '', guild, 0).strip()

vicpst = str(soup2.find_all('span', {'class':'RecordOra'})[0])
vicpst = re.sub('<.+?>', '', vicpst, 0).strip()

vicpstsp = str(soup2.find_all('span', {'class':'RecordSky'})[0])
vicpstsp = re.sub('<.+?>', '', vicpstsp, 0).strip()

vicpstit = str(soup2.find_all('span', {'class':'RecordSky'})[2])
vicpstit = re.sub('<.+?>', '', vicpstit, 0).strip()

stkart = str(soup2.find_all('dd')[2])
stkart = re.sub('<.+?>', '', stkart, 0).strip()
tlrun = str(soup2.find_all('dd')[3])
tlrun = re.sub('<.+?>', '', tlrun, 0).strip()
laslog = str(soup2.find_all('dd')[5])
laslog = re.sub('<.+?>', '', laslog, 0).strip()

gloveimg = str(soup.find('div', {'id': 'GloveImg'}).img['src'])
riderimg = str(soup.find('span', {'id': 'RiderImg'}).img['src'])

print("\n라이더명 - "+name+f'(http://kart.nexon.com/Garage/Main?strRiderID={name})')
print("클럽명 - "+guild)
print(f"TMI 바로가기 - https://tmi.nexon.com/kart/user?nick={name}")
print("라이더생성일 - "+stkart)
print("총 주행시간 - "+tlrun)
print("마지막 접속일 - "+laslog)
print("종합승률 - "+vicpst)
print("스피드전승률 - "+vicpstsp)
print("아이템전승률 - "+vicpstit)
print("레벨이미지(글러브) - "+gloveimg)
print("라이더이미지 - "+riderimg)