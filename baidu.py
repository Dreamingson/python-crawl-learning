import requests

def getHTMLText(url, keyword):
    try:
        r = requests.get(url,params=kv,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.request.url)
        return len(r.text)
    except:
        return "ERRORs"

if __name__ == "__main__":
    url = "http://www.baidu.com/s"
    kv = {'wd':'Python'}
    print(getHTMLText(url,kv))