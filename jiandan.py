import requests,urllib.request
from bs4 import BeautifulSoup

url= 'http://jandan.net/pic/page-2176'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
source_code =requests.get(url,headers =header)
plain_text =source_code.text

soup =BeautifulSoup(plain_text,'lxml')

download_links=[]
folder_path='c://a3/'
for pic_tag in soup.find_all('img'):
    pic_link=pic_tag.get('src')
    download_links.append(pic_link)

for item in download_links:
    urllib.request.urlretrieve(item,folder_path + item[-10:])
    print('down')



