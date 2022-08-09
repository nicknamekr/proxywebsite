from proxy_requests import ProxyRequests
import os

url = os.getenv('url')
r = ProxyRequests(url)
r.get()
print('접속 완료')
