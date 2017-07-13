# python 3.x
import time
import urllib.request
import json
import pymysql.cursors
from datetime import datetime
urltoday = time.strftime("%Y%m%d")
urlreq = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&date=" + urltoday + "&json"
content = urllib.request.urlopen(urlreq).read().decode('utf-8')
parsed_string = json.loads(content)
connection = pymysql.connect(host='192.168.0.1', user='  ', password='  ', db='currency_cource', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
SQLdate = datetime.strptime(parsed_string[0]['exchangedate'], "%d.%m.%Y").strftime("%Y-%m-%d")
SQLcc = parsed_string[0]['cc']
SQLrate = str(parsed_string[0]['rate'])
SQLQuery = "INSERT INTO cc (exchangedate,cc,rate) VALUES('" + SQLdate + "','" + SQLcc + "','" + SQLrate + "');"
try:
    with connection.cursor() as cursor:
        cursor.execute(SQLQuery)
    connection.commit()
finally:
    connection.close()
