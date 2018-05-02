import requests
import os

def getHTMLText(url,path):
    try:
        r=requests.get(url)
        r.raise_for_status()
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("Successful")
    except:
        return "ERRORs"

if __name__ == "__main__":
    url = "http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg"
    root = "//home//dreamingson//Pictures//Crawl//"
    path = root + url.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            getHTMLText(url,path)
        else:
            print("Existed")
    except:
        print("FAILED")