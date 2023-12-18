import urllib.request
import urllib.parse

def creat_request(page):
    url='https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
    data = {
        'start':page*20,
        'limit':20,
    }
    data = urllib.parse.urlencode(data)
    url+=data
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
    }
    request = urllib.request.Request(url=url,headers=headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(content,page):
    with open('douban_'+str(page)+'.json','w',encoding='utf-8') as fp:
        fp.write(content)


#程序入口
if __name__=='__main__':
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入结束的页码'))
    for page in range(start_page-1,end_page):
#      请求对象的定制
        request=creat_request(page)
#       获取响应的数据
        content = get_content(request)
#       下载获取到的数据
        down_load(content, page)






