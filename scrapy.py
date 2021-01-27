import requests
from lxml import etree

headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3823.400 QQBrowser/10.7.4307.400'
    }
homepage_url='https://manhua.fzdm.com/39//'
#检索出每一章节的名字
homepage_text=requests.get(url=homepage_url,headers=headers).text
#print(homepage_text)
tree=etree.HTML(homepage_text)
#获取href与标题
title_list=tree.xpath('//div[@class="pure-g"]/div/li/a/text()')
href_list=tree.xpath('//div[@class="pure-g"]/div/li/a/@href')
print(title_list,href_list)

section_first_url_list=[]
for href in href_list:
    sec_url=homepage_url+href
    #print(sec_url)
    section_first_url_list.append(sec_url)
print(section_first_url_list)

def spiderfunc():                                                     #这个函数用于解析每一张页面的图片数据
    response=requests.get(url=whole_url,headers=headers).text
    tree=etree.HTML(response)
    pic_url=tree.xpath("//div[@id='mh']/div/div/a[@href='index_1.html']/@src")
    return pic_url       
  
def checkfunc():
    response=requests.get(url=whole_url,headers=headers).text
    tree=etree.HTML(response)
    check_class=tree.xpath("//div[@id='mh']/div/div[@class='navigation']/a[7]/@class")
    return check_class
  
def tryfeunc(check_class):
    if check_class=='pure-button button-success':
        pass
    else:
        break
        
whole_url_list=[]
for url in section_first_url_list:
    for i in range(0,60):
        whole_url=url+"index_{}.html".format(i)
        checkfunc()
        if check==True:
            whole_url_list.append(whole_url)
        else:
            break
                
# print(whole_url_list)

for whole_url in whole_url_list:
    spiderfunc()
