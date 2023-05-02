from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
import pandas as pd
import json
import requests
import ndjson

cookies = {
    'FOODY.AUTH': 'EBAEBEE165959E81A0736398585AB7DD9E0009C06B2688305C9B9CCA64C46C285C4417BEF0A49898A3391B85E9174119D2AC84E48831B0D093DB3E1714D114C668F893AD2807F206D5456DEE8D5E68E55D25F9B44528C5B5BDCD0FD32A02D00C587C4D77AFCAB28048085E790DDA866831B181C2A3C11A4A9510D77BDB7867496AE292FE0C40D14BD4BB60464110C2A5D88E25A84BF8C2CDE6F1F08A969563F5F19DFE83FE46BE79FF6EA198FA74F73D69F6ABB578814A1A297C9F44941B53239575CADD2C27529B863E12099A2EF2DCA8D0A2D2EE2B88340C95196FE1A57B11A5711DC709D7967EDB87C4328EC87DD5F85F9005CDE3DF8DA73D2C1F35C82648',
    '__utmt_UA-33292184-1': '1',
    '__utma': '257500956.2075570300.1676786881.1679910529.1680325195.9',
    '_ga': 'GA1.2.2075570300.1676786881',
    '__ondemand_sessionid': 'blgctyu442iktyyv2sedi0l2',
    'fbsr_395614663835338': 'S-jVDBaZ1tgkVuXnE9a96PyHYb1xwia6RgkGhE-aztU.eyJ1c2VyX2lkIjoiMTI4NjI4NzY2ODM5MjY3MSIsImNvZGUiOiJBUUJjVGtwM3ZKaWVIRDl5UlhFOUp6Uk5jeWhJRzJHQ3NFNmhJdjJiOVNmb1JSeG10NDlfNFgtc01pdG5mUTR6VTZ6ZGZENHB3elhWZ1lVWnpEMGgyY2NmVXpQX3JqOUQ4bG0zMjJreEJnTEkteVBhSzhMdkJDMDZxTGt6V2hEZmItS2hJYlVnbWM1ZUtQVDBEdEJKNXNwVUlSVHVpZmdRZHhHZFVQcHdFUWFWTngzQXJLMEd0M2FCYXRXMEE3NkxQbmMtRWNOTk5VWEpVWkhiQXBiTTc5LUM5VGZmXzZYV28xUmJPRDUtVkUwaDNhYWFTd0JTeWR3RGtEV1VaYjBmQVpRZ1otZGFiajZaOEpON2laTFlKd3hWXzlBMlVpR0tfNXYzVl82SEk4OTlJOG1fVmxwTGlhMjlUc1M3Y0h1UWUxSGtON1MyQVZROV9BeENqLTZwc2JZLSIsIm9hdXRoX3Rva2VuIjoiRUFBRm56emVCZnNvQkFDVEpKbjY2T3VDQ0dxQjJBMFFmNkZ3WkFoY1ZIVFFHeDJLNWJiaEVSSXJkVW1sQkVaQnE3RWpaQjBSZjlSbXBkbHlqQWVxWkJhRlRkb3dpTHZnd3BOd05OZGRMbUhPRFlGRE9jQ0g1YkNFb3F4SUlkNXBzSlBDbHlSMkFEQzB4Y0NZMURiTnJiNzJONEZnZmFVNXM2UkVoN3JHNVdWanFQYzh0aFpCZXdEaFhlOGhmbENPc1pEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2ODAzMjk3NDd9',
    '__utmz': '257500956.1679539841.4.4.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    'fd.verify.password.22062698': '01/04/2023',
    'gcat': 'food',
    'fd.keys': '#kfc',
    '__utmc': '257500956',
    'FOODY.AUTH.UDID': 'ffdba1ee-64be-44c7-ab27-67bec195dbfd',
    'fbm_395614663835338': 'base_domain=.foody.vn',
    '_gid': 'GA1.2.429558754.1680325192',
    'bc-jcb': '1',
    'AWSALBCORS': '5amnsgdi2ioDR7zZuZkkeZ+lM2KvUxqOloElcVFqFM7TUCAem1yI+MFK3Xyr8nw9IqRFhb1n8sAZI7LjjYzbIftFl5gcHPrb8EgIyjs7ja2/8r99F4l1RC1x83zz',
    'floc': '217',
    '__utmb': '257500956.28.9.1680329833798',
    'fbsr_395614663835338': 'bh7XHHJjt8WfbbhLysBKLXAsq-SKMh85F6XnWrBQGcU.eyJ1c2VyX2lkIjoiMTI4NjI4NzY2ODM5MjY3MSIsImNvZGUiOiJBUUFkdFdJekxuc0tSVV84Y1REdVlSVWJORVNjYkNsRE9RZlg3Q2kyRUxxZEJpUzBqWjlLeTlad0txa19lTFJCQXdHSWN2cmtWRjdTbUlmcjR1STlyc182ODhoUmRFY0VHd242ZmE2ZEd2Q1FxNS1HeWhXSWdVZDFzY1BNbW1IZDFWdFJZbGc0OUEzMlRFQnlHNmlCTlJWZlFwTTZGMnVXY2hHblVQT1NKTExSQ01kYzJVRXJrTnFnR3VEQmZMS2JEdFRTRDhUcmhacWF0a3U2cEJBc0YxZzc1OURfSXNyTjM5ckliNnVhelQ5TEFIZWVwZUVqdGJhUVljeF9DZjRpOVYzUEo3Q1h3ZUpIblRubUdZcFpwdDBHTkYyNWdHTk1Ca0Z0LXRpbUp0YTVFVVpOWjI5X01PWG02a29WdmlNWGJGNWh5NUZPeTVuX0pJV0ZUbmFjVlNNZiIsIm9hdXRoX3Rva2VuIjoiRUFBRm56emVCZnNvQkFDVEpKbjY2T3VDQ0dxQjJBMFFmNkZ3WkFoY1ZIVFFHeDJLNWJiaEVSSXJkVW1sQkVaQnE3RWpaQjBSZjlSbXBkbHlqQWVxWkJhRlRkb3dpTHZnd3BOd05OZGRMbUhPRFlGRE9jQ0g1YkNFb3F4SUlkNXBzSlBDbHlSMkFEQzB4Y0NZMURiTnJiNzJONEZnZmFVNXM2UkVoN3JHNVdWanFQYzh0aFpCZXdEaFhlOGhmbENPc1pEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2ODAzMjg3NjR9',
    'fd.res.view.217': '42888,595,77729,112526,1145123,88420,5714,46914',
    'flg': 'vn'
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    'Connection': 'keep-alive',
    'Host': 'www.foody.vn',
    'Referer': 'https://www.foody.vn/ho-chi-minh/dia-diem',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'X-Foody-User-Token': 'null',
    'X-Requested-With': 'XMLHttpRequest'
}

# https://www.foody.vn/ho-chi-minh/dia-diem?ds=Restaurant&vt=row&st=1&page=2&provinceId=217&categoryId=&append=true
params = {
    'ds': 'Restaurant',
    'vt': 'row',
    'st': 1,
    'page': 1,
    'provinceId': 217,
    'ategoryId': '',
    'append': 'true'
}

categories = []
urls = []
list_cat_id = []
for i in range(1, 6):
        params['page'] = i
        response = requests.get('https://www.foody.vn/ho-chi-minh/dia-diem?', headers=headers, params=params, cookies=cookies)
        if response.status_code == 200:
                print('request success!!!')
                
                for record in response.json().get('searchItems'):
                        url = 'https://www.foody.vn' + record.get('DetailUrl')
                        id = record.get('Cuisines')[0]['Id']
                        if id not in list_cat_id:
                                list_cat_id.append(id)
                                cat = dict()
                                cat['_id'] = str(id)
                                cat['_type'] = 'category'
                                cat['name'] = record.get('Cuisines')[0]['Name']
                                cat['image'] = {
                                        '_type': 'image',
                                        "_sanityAsset": f"image@{record.get('MobilePicturePath')}"
                                }
                                categories.append(cat)
                                
                        urls.append(url)

json_cats = json.dumps(categories,indent = 4)
with open("json\\categories.json", "w") as outfile:
    outfile.write(json_cats)
    
driver = webdriver.Chrome('chromedriver.exe')
dishes = []
for url in urls: # each item is a dictionary
        driver.get(url)
        sleep(random.randint(5,10))
        titles = driver.find_elements(By.CSS_SELECTOR, ".delivery-dishes-item-right [href]")
        titles = [x.text for x in titles]
        prices = driver.find_elements(By.CSS_SELECTOR, ".price")
        prices = [x.text for x in prices]
        prices = [int(x.replace(',','').replace('đ','')) for x in prices]
        images = driver.find_elements(By.CSS_SELECTOR, ".delivery-dishes-item-left [src]")
        images = [x.get_attribute('src') for x in images]
        i = 1
        for x, y, z in zip(titles,prices,images):
                dish = dict()
                dish['_id'] = url.split('/')[4] + '-' + str(i)
                dish['_type'] = 'dish'
                dish['name'] = x
                dish['price'] = y
                dish['short_description'] = url.split('/')[4].replace('-',' ')
                dish['image'] = {
                    '_type': 'image',
                    '_sanityAsset': f"image@{z}"
                }
                dishes.append(dish)
                i = i + 1
driver.close()

json_dishes = json.dumps(dishes,indent = 4)
with open("json\\dishes.json", "w") as outfile:
    outfile.write(json_dishes)
    
def parse_res(record):
    d = dict()
    d['_id'] = str(record.get('Id'))
    d['name'] = record.get('Name')
    d['short_description'] = record.get('UrlRewriteName')
    d['image'] = {
        "_type": "image",
        "_sanityAsset": 'image@' + record.get('MobilePicturePath')
    }
    d['lat'] = record.get('Latitude')
    d['long'] = record.get('Longitude')
    d['_type'] = 'restaurant'
    d['address'] = record.get('Address')
    d['rating'] = record.get('AvgRating')
    d['type'] = dict()
    d['type']['_type'] = 'reference'
    d['type']['_ref'] = str(record.get('Cuisines')[0]['Id'])
    d['dishes'] = []
    d['hasbooking'] = record.get('HasBooking')
    d['hasdelivery'] = record.get('HasDelivery')
    d['url'] = 'https://foody.vn' + record.get('DetailUrl')
    return d

json_file = open('json\\dishes.json')
data = json.load(json_file)

restaurant = []
for i in range(1, 6):
    params['page'] = i
    response = requests.get('https://www.foody.vn/ho-chi-minh/dia-diem?', headers=headers, params=params, cookies=cookies)
    if response.status_code == 200:
        print('request success!!!')
        for record in response.json().get('searchItems'):
            obj = parse_res(record)
            if ((obj['hasbooking'] == True) & (obj['hasdelivery'] == True)):
                obj.pop('hasbooking', None)
                obj.pop('hasdelivery', None)
                for row in data:
                    id = row['_id']
                    if (obj['url'].split('/')[4] == id[0:id.rfind('-')]):
                        dish = {
                            '_type': 'reference',
                            '_ref': id
                        }
                        obj['dishes'].append(dish)
                obj.pop('url', None)
                restaurant.append(obj)

jsonRestaurant = []
for row in restaurant:
    row['lat'] = float(row['lat'])
    row['long'] = float(row['long'])
    row['rating'] = float(row['rating'])/2
    jsonRestaurant.append(row)

with open("json\\restaurant_id.json", 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonRestaurant, indent=4)
        jsonf.write(jsonString)
        

# json_list = ['categories', 'dishes', 'restaurant_id']

# for file in json_list:
#     json_file = open(f"json\\{file}.json")
#     data = json.load(json_file)
#     with open(f"ndjson\\{file}.ndjson", 'w', encoding='utf-8') as outfile:
#         output = ndjson.dumps(data)
#         outfile.write(output)