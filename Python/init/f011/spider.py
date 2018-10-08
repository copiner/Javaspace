import urllib.request
import os

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User_Agent','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()

    return html


def get_page(url):
    html = url_open(url).decode('utf-8')

    a = html.find('current-comment-page') + 23
    b = html.find(']', a)
    print(html[a:b])


def find_imgs(url):
    html = url_open(url).decode('utf-8')

def save_imgs(folder, img_addrs):
    pass

def load_mm(folder='ooxx', pages=10):
    os.mkdir(folder)
    os.chdir(folder)

    url = 'http://jandan.net/ooxx/'
    page_num = int(get_page(url))

    for i in range(pages):
        page_num -= i
        page_url = url + 'page-'+str(page_num)+'#comments'
        img_addrs = find_imgs(page_url)
        save_imgs(folder, img_addrs)


if __name__ == '__main__':
    load_mm()
