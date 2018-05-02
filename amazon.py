import requests

def getHTMLText(url):
    try:
        kv = {'user-agent': 'Moziila/5.0'}
        r = requests.get(url, timeout=30, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.request.headers)
        return r.text[1000:2000]
    except:
        return "ERRORs"

if __name__== "__main__":
    url="https://www.amazon.cn/gp/product/B01M8L5Z3Y"
    print(getHTMLText(url))