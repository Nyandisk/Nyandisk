import requests

response = requests.get("https://static.wikia.nocookie.net/meme/images/d/db/Rick-astley.png")

with open("dwnld.png","wb") as f:
  f.write(response.content)
  f.close()
  
print("Done")
