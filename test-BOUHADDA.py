import requests
import json


auth_token='ZDdmNDVmYzU1NWZkMDkwMDc4YjBjMzYyZDk2MDI3NGVlNmFmNTJkZDU5MzBhYWRiZGZmNzAxOGM1NDkzNDYxYQ'
hed = {'Authorization': 'Bearer ' + auth_token}
data = {'app' : 'aaaaa'}

url = 'https://web.mention.com/api/accounts/661072_53ca2jsh01c88c4wwkc0wockckk0w4440o4o0w8wkkgco4o888/alerts/1214654/mentions'
response = requests.get(url, json=data, headers=hed)

print(response)
print(response.text)




fichier = open("MentionChallenge/Resulat.txt","w")
fichier.write(response.text)
fichier.close()





