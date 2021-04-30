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
soup = BeautifulSoup(response.text, 'html.parser')

response2 = requests.get(f'http://kart.nexon.com/Garage/Record?strRiderID={nickname}')
soup2 = BeautifulSoup(response2.text, 'html.parser')

name = str(soup.find_all('span', {'id':'RiderName'})[0])
name = re.sub(r'<[^>]+>', '', name, 0).strip()

print("\n라이더명 - "+name+f'(http://kart.nexon.com/Garage/Record?strRiderID={name})')

try:
    map1 = str(soup.find('div', {'id':'RecordTime'}).img['alt'])

    maprank = str(soup.find('div', {'id': 'RecordTime'}).find_all('span', {'class': 'TimeRank'})[0])
    maprank = re.sub('<.+?>', '', maprank, 0).strip()

    map2 = str(soup.find('div', {'id': 'RecordTime'}).find_next('span', {'class': 'TimeLicense'}))
    map2 = re.sub('<.+?>', '', map2, 0).strip()
    mapkart = str(soup.find('div', {'id': 'RecordTime'}).find_all('span', {'class': 'TimeKart'})[0])
    mapkart = re.sub('<.+?>', '', mapkart, 0).strip()

    maptime1 = str(soup.find('div', {'id': 'RecordTime'}).find_all('span', {'class': 'TimeRecordNum'})[0])
    maptime1 = re.sub('<.+?>', '', maptime1, 0).strip()
    maptime2 = str(soup.find('div', {'id': 'RecordTime'}).find_all('span', {'class': 'TimeRecordNum'})[1])
    maptime2 = re.sub('<.+?>', '', maptime2, 0).strip()
    maptime3 = str(soup.find('div', {'id': 'RecordTime'}).find_all('span', {'class': 'TimeRecordNum'})[2])
    maptime3 = re.sub('<.+?>', '', maptime3, 0).strip()
    maptime4 = str(soup.find('div', {'id': 'RecordTime'}).find_all('span', {'class': 'TimeRecordNum'})[3])
    maptime4 = re.sub('<.+?>', '', maptime4, 0).strip()
    maptime5 = str(soup.find('div', {'id': 'RecordTime'}).find_all('span', {'class': 'TimeRecordNum'})[4])
    maptime5 = re.sub('<.+?>', '', maptime5, 0).strip()
    maptime6 = str(soup.find('div', {'id': 'RecordTime'}).find_all('span', {'class': 'TimeRecordNum'})[5])
    maptime6 = re.sub('<.+?>', '', maptime6, 0).strip()
    mapimg = str(soup.find('div', {'id':'RecordTime'}).img['src'])

    print("랭킹타임어택 - "+map1+f"({mapimg})")
    print(f"속도/카트 - {map2}/{mapkart}")
    print(f"순위/기록 - {maprank}/{maptime1}{maptime2}:{maptime3}{maptime4}:{maptime5}{maptime6}")
except IndexError:
    mapnone = str(soup.find('div', {'id': 'RecordTime'}).find_all('span', {'class': 'TimeNone'})[0])
    mapnone = re.sub('<.+?>', '', mapnone, 0).strip()
     
    mapimg2 = str(soup.find('div', {'id': 'RecordTime'}).img['src'])
    
    print("랭킹타임어택 - "+mapnone+f"({mapimg2})")

try:
    gpn1 = str(soup2.find_all('td', {'class':'CntGpL1'})[0])
    gpn1 = re.sub('<.+?>', '', gpn1, 0).strip()
    gps1 = str(soup2.find_all('td', {'class':'CntGpL2'})[0])
    gps1 = re.sub('<.+?>', '', gps1, 0).strip()
    gpr1 = str(soup2.find_all('td', {'class':'CntGpL3'})[0])
    gpr1 = re.sub('<.+?>', '', gpr1, 0).strip()

    print("그랑프리 - "+gpn1)
    print("점수 - "+gps1)
    print("랭킹 - "+gpr1)
except IndexError:
    gper = str(soup2.find_all('td', {'colspan':'3'})[0])
    gper = re.sub('<.+?>', '', gper, 0).strip()
    
    print(gper) 


try:
    gpn2 = str(soup2.find_all('td', {'class':'CntGpL1'})[1])
    gpn2 = re.sub('<.+?>', '', gpn2, 0).strip()
    gps2 = str(soup2.find_all('td', {'class':'CntGpL2'})[1])
    gps2 = re.sub('<.+?>', '', gps2, 0).strip()
    gpr2 = str(soup2.find_all('td', {'class':'CntGpL3'})[1])
    gpr2 = re.sub('<.+?>', '', gpr2, 0).strip()
        
    print("그랑프리 - "+gpn2)
    print("점수 - "+gps2)
    print("랭킹 - "+gpr2)
except IndexError:
    pass

try:
    gpn3 = str(soup2.find_all('td', {'class':'CntGpL1'})[2])
    gpn3 = re.sub('<.+?>', '', gpn3, 0).strip()
    gps3 = str(soup2.find_all('td', {'class':'CntGpL2'})[2])
    gps3 = re.sub('<.+?>', '', gps3, 0).strip()
    gpr3 = str(soup2.find_all('td', {'class':'CntGpL3'})[2])
    gpr3 = re.sub('<.+?>', '', gpr3, 0).strip()
        
    print("그랑프리 - "+gpn3)
    print("점수 - "+gps3)
    print("랭킹 - "+gpr3)
except IndexError:
    pass