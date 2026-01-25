import requests

res = requests.post("https://wings.msn.to/tmp/post.php", data={"name": "佐々木新之助"})
print(res.text)
