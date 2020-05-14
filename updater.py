import requests
import re

f = open(".version.txt")
vernow = f.read()
f.close()

def update():
	info = requests.get('https://github.com/Werryx/Console')
	output = "".join(re.findall(r"</h(.*?)ml>", info.text))

	f = open("main.py", "w")
	f.write(output)
	f.close()

	print("Файл обновлён до версии v." + vernow + " успешно")

iv = requests.get('https://github.com/Werryx/Console/blob/master/.version.txt')
ver = "".join(re.findall(r"<td id=\"LC1\" class=\"blob-code blob-code-inner js-file-line\">(.*?)</td>", iv.text))

print(str(ver))

if(vernow != ver):
	update()
