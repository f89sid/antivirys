import os

print("Привет это антивирус OMEGA он создан для того чтобы защищать твой комп")
print("----------------------------------------------------------------------")


#print(/ydal   "Удаление файлов с не понятным расширением")
#print(/prosmotr   "Просмотр кода")


#/prosmotr указать директорию где находится файл с не понятным кодом
a = input('Введите директорию где находится файл с вирусом:')  
f = open(a ,'r')
print('В данном файле содержится :'  + f.read())
f.close()


#/del удаление только одного файла 
d = input('Введите где находится файл:')
if d == 'нет':
	raise SystemExit
else:
	os.remove(d)
	print("Поздравляем всё успешно удалилось")


#/ydal со всеми расширениями 
#dir_name = input("Введите директорию:")
#test = os.listdir(dir_name)
#print(test)

#for item in test:
	#if item.endswitch(".txt"):
		#os.remove(os.path.join(dir_name,item))