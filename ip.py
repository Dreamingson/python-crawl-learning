import requests

def getIPAddress(url,ip):
    try:
        r = requests.get(url+ip)
        r.raise_for_status()
        return r.text[-500:]
    except:
        return "ERRORs"

if __name__ == "__main__":
    url = "http://m.ip138.com/ip.asp?ip="
    ip = "202.204.80.112"
    print(getIPAddress(url,ip))
