# Test request
import requests

# request
# request(method,url,**kwargs):basic method;
    # **kwargs:
        # data
        # json
        # headers hd={'user-agent':'Chrome/10'} r=request.request('POST','http://wwww.baidu.com',headers=he)
        # cookies
        # auth
        # files fs={'file':open('data.xls',''rb)} r=requests.request('POST','http://wwww.baidu.com',,files=fs)
        # timeout
        # proxies pxs={'http':'http://user：pass@10.10.10.1:1234' 'https':'https://10.10.10.1:4321'} r=requests.request('GET',
# 'http://wwww.baidu.com',proxies=pxs)
        # allow_redirects
        # stream
        # verify
        # cert




# get(url,params=None,**kwargs): a method of submitting request
# post(url,data=None,json=None,**kwargs): a method of submitting request
# head(url,**kwargs): acquire head information
# put(url,data=None,**kwargs): a method of submitting put request
# patch(url,data=None,**kwargs): submit part of modification
# delete(url,**kwargs): submit delete request


# Response object
#r.status_code  status code
#r.text content of page to url
#r.encoding encoding of header default:ISO-8859-1
#r.apparent_encoding encoding of content
#r.content two binary except string

# General frame to crawl website
def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status() # judge connection status, HTTPError
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "ERROR"

if __name__ == "__main__":
    url = "http://www.baidu.com"
    print(getHTMLText(url))
    r = requests.head("http://www.baidu.com")
    print(r.headers)



 


