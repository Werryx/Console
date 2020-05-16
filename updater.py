# <updater_version>FIRST RELEASE</updater_version>
updater_version = "FIRST RELEASE"
print("Поиск обновлений...")

import requests
import re

f = open(".version.txt")
vernow = f.read()
f.close()

iv = requests.get('https://github.com/Werryx/Console/blob/master/.version.txt')
ver = "".join(re.findall(r"<td id=\"LC1\" class=\"blob-code blob-code-inner js-file-line\">(.*?)</td>", iv.text))

def update():
	# Обновление файла .data
	info = requests.get('https://github.com/Werryx/Console/blob/master/.data')
	output = "".join(re.findall(r"<td id=\"LC1\" class=\"blob-code blob-code-inner js-file-line\">(.*?)</td>", info.text)).replace("\j", "\n").replace("&gt;", ">").replace("&quot;", "\"")
	f = open(".data", "w")
	f.write(output)
	f.close()

	# Обновление файла .version.txt
	f = open(".version.txt", "w")
	f.write(ver)
	f.close()
	vernow = ver

	# Обновление файла main.py
	info2 = requests.get('https://github.com/Werryx/Console/blob/master/main.py.txt')
	output2 = "".join(re.findall(r"<td id=\"LC1\" class=\"blob-code blob-code-inner js-file-line\">(.*?)</td>", info2.text)).replace("\j", "\n").replace("\k", "\t").replace("&quot;", "\"")
	f = open("main.py", "w")
	f.write(output2)
	f.close()

	print("Файл обновлён до версии v." + vernow + " успешно")

if(vernow != ver):
	update()
else:
	print("Вы используете последнюю версию")
