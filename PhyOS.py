confg = ["0", "1", "11", "111", "1111", "11111"]
version = 2.03

#Updater
import requests
def update():
	try:
		upd=requests.get('https://raw.githubusercontent.com/MaksPV/PhysicalOS/master/last_version.txt')
		if float(upd.text) > version:
			print("Найдено обновление\n" + upd.text + "\nОбновить?\n1 - Да, 2 - Нет")
			update_menu = input()
			if update_menu == confg[1]:
				upd_phyos=requests.get('https://raw.githubusercontent.com/MaksPV/PhysicalOS/master/PhyOS.py')
				f = open("PhyOS.py", "wb")
				f.write(upd_phyos.content)
				f.close()
		elif float(upd.text) == version: print("Установлена последняя версия, вы прекрасны")
		elif float(upd.text) < version: print("Не хочешь попать в команду PhysicalOS?")
		else: print("Ошибка, файл обновлений не найден")
#	print(send.text)
#file = open('bdseo.html','w') #создаем файл для записи результатов
#file.write(send.text) #записываем результат
#file.close() #закрываем файл
#Updater
	except BaseException:
		print("Нет интернета, попробуйте позже")

#Клавиатура
def keyboard_chose(text,a1,a2,a3,a4,b1,b2,b3,b4,c1,c2,c3,c4,d1,d2,d3,d4,e1,e2,e3,e4,f1,f2,f3,f4,g1,g2,g3,g4,h1,h2,h3,h4):
	while True:
		print(text)
		print("1 - следующая страница, 2 - "+a1+", 3 - "+a2+", 4 - "+a3+", 5 - "+a4+", 0 - выход")
		keyboard_sub_menu = input("\nkeyboard@: ")
		if keyboard_sub_menu == confg[0]: break
		if keyboard_sub_menu == confg[2]:
			if a1 == "Пробел":
				text += " "
			else:
				text += a1
		if keyboard_sub_menu == confg[3]:
			if a2 == "Удаление последнего символа":
				text = text[:-1]
			else:
				text += a2
		if keyboard_sub_menu == confg[4]:
			if a3 == "Перенос строки":
				text += "\n"
			else:
				text += a3
		if keyboard_sub_menu == confg[5]: text += a4
		if keyboard_sub_menu == confg[1]:
			print("1 - следующая страница, 2 - "+b1+", 3 - "+b2+", 4 - "+b3+", 5 - "+b4+", 0 - выход")
			keyboard_sub_menu = input("\nkeyboard@: ")
			if keyboard_sub_menu == confg[0]: break
			if keyboard_sub_menu == confg[2]: text += b1
			if keyboard_sub_menu == confg[3]: text += b2
			if keyboard_sub_menu == confg[4]: text += b3
			if keyboard_sub_menu == confg[5]: text += b4
			if keyboard_sub_menu == confg[1]:
				print("1 - следующая страница, 2 - "+c1+", 3 - "+c2+", 4 - "+c3+", 5 - "+c4+", 0 - выход")
				keyboard_sub_menu = input("\nkeyboard@: ")
				if keyboard_sub_menu == confg[0]: break
				if keyboard_sub_menu == confg[2]: text += c1
				if keyboard_sub_menu == confg[3]: text += c2
				if keyboard_sub_menu == confg[4]: text += c3
				if keyboard_sub_menu == confg[5]: text += c4
				if keyboard_sub_menu == confg[1]:
					print("1 - следующая страница, 2 - "+d1+" 3 - "+d2+", 4 - "+d3+", 5 - "+d4+", 0 - выход")
					keyboard_sub_menu = input("\nkeyboard@: ")
					if keyboard_sub_menu == confg[0]: break
					if keyboard_sub_menu == confg[2]: text += d1
					if keyboard_sub_menu == confg[3]: text += d2
					if keyboard_sub_menu == confg[4]: text += d3
					if keyboard_sub_menu == confg[5]: text += d4
					if keyboard_sub_menu == confg[1]:
						print("1 - следующая страница, 2 - "+e1+", 3 - "+e2+", 4 - "+e3+", 5 - "+e4+", 0 - выход")
						keyboard_sub_menu = input("\nkeyboard@: ")
						if keyboard_sub_menu == confg[0]: break
						if keyboard_sub_menu == confg[2]: text += e1
						if keyboard_sub_menu == confg[3]: text += e2
						if keyboard_sub_menu == confg[4]: text += e3
						if keyboard_sub_menu == confg[5]: text += e4
						if keyboard_sub_menu == confg[1]:
							print("1 - следующая страница, 2 - "+f1+", 3 - "+f2+", 4 - "+f3+", 5 - "+f4+", 0 - выход")
							keyboard_sub_menu = input("\nkeyboard@: ")
							if keyboard_sub_menu == confg[0]: break
							if keyboard_sub_menu == confg[2]: text += f1
							if keyboard_sub_menu == confg[3]: text += f2
							if keyboard_sub_menu == confg[4]: text += f3
							if keyboard_sub_menu == confg[5]: text += f4
							if keyboard_sub_menu == confg[1]:
								print("1 - следующая страница, 2 - "+g1+", 3 - "+g2+", 4 - "+g3+", 5 - "+g4+", 0 - выход")
								keyboard_sub_menu = input("\nkeyboard@: ")
								if keyboard_sub_menu == confg[0]: break
								if keyboard_sub_menu == confg[2]: text += g1
								if keyboard_sub_menu == confg[3]: text += g2
								if keyboard_sub_menu == confg[4]: text += g3
								if keyboard_sub_menu == confg[5]: text += g4
								if keyboard_sub_menu == confg[1]:
									print("1 - следующая страница, 2 - "+h1+", 3 - "+h2+", 4 - "+h3+", 5 - "+h4+", 0 - выход")
									keyboard_sub_menu = input("\nkeyboard@: ")
									if keyboard_sub_menu == confg[0]: break
									if keyboard_sub_menu == confg[2]: text += h1
									if keyboard_sub_menu == confg[3]: text += h2
									if keyboard_sub_menu == confg[4]: text += h3
									if keyboard_sub_menu == confg[5]: text += h4
	return text
	
	
def keyboard(text):
	while True:
		print("\n" + text + "\n")
		print("1 - Русский язык, 2 - Английский язык, 3 - цифры и знаки, 4 - Операции над текстом, 0 - Подтвердить")
		keyboard_menu = input('\nkeyboard@: ')
		# о а е и н !с т р л !в п у к !м д я ь !ы з б г! ш ч й ж !ю х щ ц !ф э ъ ё!
		if keyboard_menu == confg[0]: break
		if keyboard_menu == confg[1]: text = keyboard_chose(text, "о", "а", "е", "и", "н", "с", "т", "р", "л", "в", "п", "у", "к", "м", "д", "я", "ь", "ы", "з", "б", "г", "ш", "ч", "й", "ж", "ю", "х", "щ", "ц", "ф", "э", "ъ")
		if keyboard_menu == confg[2]: text = keyboard_chose(text, "e", "a", "o", "i", "d", "h", "n", "r", "s", "t", "u", "y", "c", "f", "g", "l", "m", "w", "b", "k", "p", "q", "x", "z", "v", "j", "", "", "", "", "", "")
#e, a, o, i,\ d, h, n, r, \s, t, u, y, \c, f, g, l, \m, w, b, k, \p, q, x, z\v,j.
		
		if keyboard_menu == confg[3]: text = keyboard_chose(text, "Пробел", ".", ",", "!", "?", "-", ":", ";", "1", "2", "3", "4", "5", "6", "7", "8", "9", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
		
		if keyboard_menu == confg[4]: text = keyboard_chose(text, "Пробел", "Удаление последнего символа", "Перенос строки", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
		
	return text
#Клавиатура

#Калькулятор
import fractions
import math

calc_confg = [9.80666, 0.5]

calc_a = 0
calc_b = 0
calc_mode = "+"
calc_sum = 0

def calc_screen():
	print("\n" + str(calc_a) + " " + calc_mode + " " + str(calc_b) + " = " + str(calc_sum))

def calc_int(a, x):
	while True:
		print("\n" + a + " = " + str(x) + "\n1 - +, 2 - -; 3 - /, 4 - *, 5 - следующая страница, 0 - выход")
		calc_int_menu = input("calc@: ")
		
		# Сложение
		while calc_int_menu == confg[1]:
			print("\n" + a + " = " + str(x) + "\n1 - +1, 2 - +5; 3 - +10, 4 - +50, 5 - +100, 0 - выход")
			calc_int_sub_menu = input("calc@: ")
			if calc_int_sub_menu == confg[1]: x += 1
			if calc_int_sub_menu == confg[2]: x += 5
			if calc_int_sub_menu == confg[3]: x += 10
			if calc_int_sub_menu == confg[4]: x += 50
			if calc_int_sub_menu == confg[5]: x += 100
			if calc_int_sub_menu == confg[0]: break
			
		#вычитание
		while calc_int_menu == confg[2]:
			print("\n" + a + " = " + str(x) + "\n1 - -1, 2 - -5; 3 - -10, 4 - -50, 5 - -100, 0 - выход")
			calc_int_sub_menu = input("calc@: ")
			if calc_int_sub_menu == confg[1]: x -= 1
			if calc_int_sub_menu == confg[2]: x -= 5
			if calc_int_sub_menu == confg[3]: x -= 10
			if calc_int_sub_menu == confg[4]: x -= 50
			if calc_int_sub_menu == confg[5]: x -= 100
			if calc_int_sub_menu == confg[0]: break
		
		#деление
		while calc_int_menu == confg[3]:
			print("\n" + a + " = " + str(x) + "\n1 - /10, 2 - /100; 3 - /1000, 0 - выход")
			calc_int_sub_menu = input("calc@: ")
			if calc_int_sub_menu == confg[1]: x /= 10
			if calc_int_sub_menu == confg[2]: x /= 100
			if calc_int_sub_menu == confg[3]: x /= 1000
			if calc_int_sub_menu == confg[0]: break
			
			#умножение
		while calc_int_menu == confg[4]:
			print("\n" + a + " = " + str(x) + "\n1 - *-1, 2 - *10; 3 - *100, 4 - *0, 0 - выход")
			calc_int_sub_menu = input("calc@: ")
			if calc_int_sub_menu == confg[1]: x *= -1
			if calc_int_sub_menu == confg[2]: x *= 10
			if calc_int_sub_menu == confg[3]: x *= 100
			if calc_int_sub_menu == confg[4]: x *= 0
			if calc_int_sub_menu == confg[0]: break
			
		if calc_int_menu == confg[5]:
			print("\n" + a + " = " + str(x) + "\n1 - пи, 2 - е; 3 - гравитационная постоянная")
			calc_int_sub_menu = input("calc@: ")
			if calc_int_sub_menu == confg[1]: x = 3.1415926
			if calc_int_sub_menu == confg[2]: x = 2.718281
			if calc_int_sub_menu == confg[3]: x = 6.67e-11
		
		if calc_int_menu == confg[0]: break
	return x
	
def calc_chose():
	print("1 - +, 2 - -, 3 - *, 4 - /, 5 - следующая страница")
	calc_chose_menu = input("calc@: ")
	if calc_chose_menu == confg[1]: calc_mode = "+"
	if calc_chose_menu == confg[2]: calc_mode = "-"
	if calc_chose_menu == confg[3]: calc_mode = "*"
	if calc_chose_menu == confg[4]: calc_mode = "/"
	if calc_chose_menu == confg[5]:
		print("1 - степень, 2 - корень, 3 - синус, 4 - косинус, 5 - следующая страница")
		calc_chose_menu = input("calc@: ")
		if calc_chose_menu == confg[1]: calc_mode = "ст"
		if calc_chose_menu == confg[2]: calc_mode = "кк"
		if calc_chose_menu == confg[3]: calc_mode = "sin"
		if calc_chose_menu == confg[4]: calc_mode = "cos"
		if calc_chose_menu == confg[5]:
			print("1 - логарифм, 2 - факториал, 3 - тангенс")
			calc_chose_menu = input("calc@: ")
			if calc_chose_menu == confg[1]: calc_mode = "log"
			if calc_chose_menu == confg[2]: calc_mode = "fac"
			if calc_chose_menu == confg[3]: calc_mode = "tan"
	return calc_mode
	
def calc_func_chose():
	print("1 - конвертация, 2 - падение, 3 - площадь многоугольника")
	calc_func_chose_menu = input("\ncalc@: ")
	if calc_func_chose_menu == confg[1]:
		print("1 - (a) м/с -> км/ч, 2 - (b) км/ч -> м/с")
		calc_func_chose_sub_menu = input("\ncalc@: ")
		if calc_func_chose_sub_menu == confg[1]: calc_mode = "м/с -> км/ч"
		if calc_func_chose_sub_menu == confg[2]: calc_mode = "км/ч -> м/с"
	if calc_func_chose_menu == confg[2]:
		print("\ng = " + str(calc_confg[0]) + "\nВы можете его изменить в пункте переноса результата\n\n1 - (fall1) Расстояние, пройденное телом за время падения (a), зная конечную скорость (b)\n2 - (fall2) Расстояние, пройденное телом за время падения(a), зная ускорение свободного падения\n3 - (fall3) Скорость тела, в конце падения, зная ускорение свободного падения и время(a)\n4 - (fall4) Скорость тела, в конце падения, зная ускорение свободного падения и высоту (a)")
		calc_func_chose_sub_menu = input("\ncalc@: ")
		if calc_func_chose_sub_menu == confg[1]: calc_mode = "fall1"
		if calc_func_chose_sub_menu == confg[2]: calc_mode = "fall2"
		if calc_func_chose_sub_menu == confg[3]: calc_mode = "fall3"
		if calc_func_chose_sub_menu == confg[4]: calc_mode = "fall4"
	if calc_func_chose_menu == confg[3]:
		print("Размер стороны клетки "+ str(calc_confg[1]) + " см площадь " + str(calc_confg[1] ** 2) + " см²\nРазмер клетки вы можете изменить в пункте переноса переменных\n\nПлощадь многоугольника на клетчатой бумаге по соприкосновения периметром пересечения клеток (a) и внутиенним точкам (b)")
		calc_mode = "sq"
	return calc_mode
#Калькулятор

#Brainfuck
import os

bf_code = ""
bf_adrs = ""

if not os.path.isdir("programs"):
   os.makedirs("programs")

def bf_block(code):
    opened = []
    blocks = {}
    for i in range(len(code)):
        if code[i] == '[':
            opened.append(i)
        elif code[i] == ']':
            blocks[i] = opened[-1]
            blocks[opened.pop()] = i
    return blocks

def bf_parse(code):
    return ''.join(c for c in code if c in '><+-.,[]')

def bf_run(code):
    code = bf_parse(code)
    x = i = 0
    bf = {0: 0}
    blocks = bf_block(code)
    l = len(code)
    while i < l:
        sym = code[i]
        if sym == '>':
            x += 1
            bf.setdefault(x, 0)
        elif sym == '<':
            x -= 1
        elif sym == '+':
            bf[x] += 1
        elif sym == '-':
            bf[x] -= 1
        elif sym == '.':
            print(chr(bf[x]), end='')
        elif sym == ',':
            bf[x] = int(input('Input: '))
        elif sym == '[':
            if not bf[x]: i = blocks[i]
        elif sym == ']':
            if bf[x]: i = blocks[i]
        i += 1

def bf_edit(code):
	while True:
		print(code + "\n\n1 - Следующая страница, 2 - +, 3 - -, 4 - >, 5 - <, 0 - выход")
		bf_edit_menu = input("\nbf@: ")
		if bf_edit_menu == confg[2]: code += "+"
		if bf_edit_menu == confg[3]: code += "-"
		if bf_edit_menu == confg[4]: code += ">"
		if bf_edit_menu == confg[5]: code += "<"
		if bf_edit_menu == confg[0]: break
		while bf_edit_menu == confg[1]:
			print(code + "\n\n1 - . 2 - , 3 - [, 4 - ], 5 - убрать последний символ, 0 - прошлая страница")
			bf_edit_sub_menu = input("\nbf@: ")
			if bf_edit_sub_menu == confg[1]: code += "."
			if bf_edit_sub_menu == confg[2]: code += ","
			if bf_edit_sub_menu == confg[3]: code += "["
			if bf_edit_sub_menu == confg[4]: code += "]"
			if bf_edit_sub_menu == confg[5]: code = code[:-1]
			if bf_edit_sub_menu == confg[0]: bf_edit_menu = "0"
	return code
#Brainfuck

#Читалка
read_text = ""
read_adrs = ""
if not os.path.isdir("files"):
   os.makedirs("files")
#Читалка

#------------------------------------------#
print("PhysicalOS")

update()

print("\nВведите 1 для помощи")
while True:
	menu = input("\n@: ")
	if menu == confg[1]:
		print("Build 17.11.19\n\n1 - меню помощи\n2 - калькулятор\n3 - Brainfuck IDE\n4 - Читалка")
	elif menu == confg[2]:
		#калькулятор
		
		print("\nКалькулятор\n")
		while True:
			if calc_mode == "+": calc_sum = calc_a + calc_b
			if calc_mode == "-": calc_sum = calc_a - calc_b
			if calc_mode == "*": calc_sum = calc_a * calc_b
			if calc_mode == "/":
				if calc_b == 0: calc_b = 1
				calc_sum = calc_a / calc_b
			if calc_mode == "ст": calc_sum = calc_a ** calc_b
			if calc_mode == "кк":
				if calc_b == 0: calc_b = 1
				calc_sum = calc_a ** fractions.Fraction(1, calc_b)
			if calc_mode == "sin": calc_sum = math.sin(calc_a)
			if calc_mode == "cos": calc_sum = math.cos(calc_a)
			if calc_mode == "log": calc_sum = math.log(calc_a, calc_b)
			if calc_mode == "fac": calc_sum = math.factorial(calc_a)
			if calc_mode == "tan": calc_sum = math.tan(calc_a)
			if calc_mode == "м/с -> км/ч": calc_sum = calc_a * 3.6
			if calc_mode == "км/ч -> м/с": calc_sum = calc_a / 3.6
			if calc_mode == "fall1": calc_sum = (calc_b * calc_a) / 2
			if calc_mode == "fall2": calc_sum = (calc_confg[0] * (calc_a ** 2)) / 2
			if calc_mode == "fall3": calc_sum = calc_confg[0] * calc_a
			if calc_mode == "fall4": calc_sum = (2 * calc_confg[0] * calc_a) ** 0.5
			if calc_mode == "sq": calc_sum = (calc_confg[1] ** 2) * (calc_b+(calc_a/2)-1)
			
			calc_screen()
			calc_menu = input("\ncalc@: ")
			if calc_menu == confg[0]: break
			elif calc_menu == confg[1]: calc_a = calc_int("a", calc_a)
			elif calc_menu == confg[2]: calc_b = calc_int("b", calc_b)
			elif calc_menu == confg[3]: calc_mode = calc_chose()
			elif calc_menu == confg[4]: calc_mode = calc_func_chose()
			elif calc_menu == confg[5]:
				print("Введите, в какую переменную вы хотите внести результат\n1 = a; 2 = b; 3 = как ускорение свободного падения; 4 = как сторону клетки")
				calc_menu = input("\ncalc@: ")
				if calc_menu == confg[1]: calc_a = calc_sum
				if calc_menu == confg[2]: calc_b = calc_sum
				if calc_menu == confg[3]: calc_confg[0] = calc_sum
				if calc_menu == confg[4]: calc_confg[1] = calc_sum	
		#Калькулятор
	#Brainfuck
	elif menu == confg[3]:
		print("Brainfuck IDE\n")
		while True:
			print(bf_code + "\n\n1 - Редактировать, 2 - Выполнить, 3 - Сохранить, 4 - Загрузить")
			bf_menu = input("\nbf@: ")
			if bf_menu == confg[0]: break
			elif bf_menu == confg[1]: bf_code = bf_edit(bf_code)
			elif bf_menu == confg[2]: bf_run(bf_code)
			elif bf_menu == confg[3]:
				print("Введите название программы: ")
				bf_adrs = keyboard(bf_adrs)
#				bf_adrs = "programs/" + bf_adrs + ".bf"
				f = open("programs/" + bf_adrs + ".bf", "w")
				f.write(bf_code)
				f.close()
#				bf_adrs = ""
			elif bf_menu == confg[4]:
				print("Все программы " + str(os.listdir("programs/")) + "\nВведите название программы: ")
				bf_adrs = keyboard(bf_adrs)
#				bf_adrs = "programs/" + bf_adrs + ".bf"
				if os.path.isfile("programs/" + bf_adrs + ".bf") == 1:
					f = open("programs/" + bf_adrs + ".bf", "r")
					bf_code = f.read()
					f.close()
#					bf_adrs = ""
	elif menu == confg[4]:
		print("Чтение текстов\n")
		while True:
			print("\n" + read_text + "\n")
			print("1 - Редактировать, 2 - Загрузить, 3 - Сохранить, 0 - Выход")
			read_menu = input("\nread@: ")
			if read_menu == confg[0]: break
			if read_menu == confg[1]: read_text = keyboard(read_text)
			if read_menu == confg[2]:
				print("Все файлы " + str(os.listdir("files/")) + "\nВведите название файла (с расширением): ")
				read_adrs = keyboard(read_adrs)
				if os.path.isfile("files/" + read_adrs) == 1:
					f = open("files/"+read_adrs, "r")
					read_text = f.read()
					f.close()
			if read_menu == confg[3]:
				print("Все файлы " + str(os.listdir("files/")) + "\nВведите название файла (с расширением): ")
				read_adrs = keyboard(read_adrs)
				f = open("files/" + read_adrs, "w")
				f.write(read_text)
				f.close()
				
	else:
		print("Введите 1 для помощи")
