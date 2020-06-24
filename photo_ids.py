import requests,traceback
import json

your_token=""#токен акка
idgroup="-193776981"#айди группы
album_id="271756227"#айди албома в группе
count="30"
h=requests.get("https://api.vk.com/method/photos.get?access_token=%s" % your_token+"&v=5.92&owner_id="+idgroup+"&album_id="+album_id+"&count="+count+"&offset=0").json()["response"]["items"][0]["id"]

for x in range(int(count)+1):
	x+=1
	try:
		a=open("фотки.txt","at")
		a.write("photo"+idgroup+"_"+str(int(h)+x)+"\n")
		a.close()
		print("photo"+idgroup+"_"+str(int(h)+x))
	except:
		pass
