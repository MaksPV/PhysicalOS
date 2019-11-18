import requests

try:
	upd=requests.get('https://raw.githubusercontent.com/MaksPV/PhysicalOS/master/last_version.txt')
	print("Последняя версия:\n" + upd.text[0:6] + "\nИзменения:\n" + upd.text[7:] +"\nУстановить?\n1 - Да, 2 - Нет")
	update_menu = input("installer@: ")
	if update_menu == "1":
		upd_phyos=requests.get('https://raw.githubusercontent.com/MaksPV/PhysicalOS/master/PhyOS.py')
		f = open("PhyOS.py", "wb")
		f.write(upd_phyos.content)
		f.close()
		print("Установлено")
	elif update_menu == "2" or "11": print("Досвидания")
	else: print("Что-то пошло не так")
except BaseException:
	print("Нет интернета, попробуйте позже")