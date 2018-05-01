import requests

def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status() # judge connection status, HTTPError
        r.encoding = r.apparent_encoding
        return r.text[:100]
    except:
        return "ERROR"

if __name__ == "__main__":
    url = "http://www.jd.com"
    print(getHTMLText(url))

