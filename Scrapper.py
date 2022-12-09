import os
import datetime
import threading
import zipfile
from zipfile import ZipFile
import rarfile

def cookieParser(path,work):
    savefilename = f"tokens {str(datetime.date.today()) + ' ' + str(datetime.datetime.now().hour) + '.' + str(datetime.datetime.now().minute) + '.' + str(datetime.datetime.now().second)}"
    os.mkdir(savefilename)
    result = open(f'{savefilename}\\result.txt', 'w+', encoding="UTF-8")
    result_p = open(f'{savefilename}\\result_path.txt', 'w+', encoding="UTF-8")
    print("Загрузка логов")
    tokens = 0
    token_list = []
    if work == "1":
        for root, dirs, filename in os.walk(path):
            for file in filename:
                filep = root + "\\" + file
                try:
                    fileo = open(root + "\\" + file, 'r', encoding='latin-1')
                except:
                    print(f"произошла ошибка{fileo}")
                    pass
                for line in fileo.readlines():
                    if line.find("	/	") >= 1:
                        cc_split = line.split("	")
                        if cc_split[0] == ("tiktok.com") or cc_split[0] == (".tiktok.com") or cc_split[0] == (
                        ".www.tiktok.com") or cc_split[0] == ("www.tiktok.com"):
                            print(line)
                            if str(cc_split[5]) == ('sessionid_ss') or str(cc_split[5]) == ('sessionid'):
                                tt_c = line.split("	")[6]
                                token = tt_c + "_-#-_" + filep
                                if tt_c not in token_list:
                                    token_list.append(tt_c)
                                    result.write(token.split("_-#-_")[0])
                                    result_p.write(token.split("_-#-_")[1])
                                    tokens += 1

    else:
            for file in os.listdir(path):
                if os.path.isdir(path+"\\"+file) != True:
                    if zipfile.is_zipfile(path+"\\"+file):
                        try:
                            with ZipFile(path+"\\"+file) as myzip:
                                for i in ZipFile.infolist(myzip):
                                        if i.filename.find(".txt") >= 1:
                                                for line in myzip.open(i).readlines():
                                                    line = line.decode(errors="replace")
                                                    if line.find("	/	") >= 1:
                                                        line = line.split("	")
                                                        if line[0] == ("tiktok.com") or line[0] == (".tiktok.com") or line[0] == (
                                                                ".www.tiktok.com") or line[0] == ("www.tiktok.com"):
                                                            if str(line[5]) == ('sessionid_ss') or str(line[5]) == ('sessionid'):
                                                                if line[6] not in token_list:
                                                                    token_list.append(line[6])
                                                                    result.write(token.split("_-#-_")[0])
                                                                    result_p.write(token.split("_-#-_")[1])
                                                                    tokens += 1
                        except RuntimeError:
                            print(f"\t{file}\t Имеется пароль")

                    elif rarfile.is_rarfile(path+"\\"+file):
                            with rarfile.RarFile(path + "\\" + file) as myrar:
                                if rarfile.PasswordRequired(myrar) != True:
                                    for i in rarfile.RarFile.infolist(myrar):
                                        if i.filename.find(".txt") >= 1:
                                                for line in myrar.open(i).readlines():
                                                    line = line.decode(errors="replace")
                                                    if line.find("	/	") >= 1:
                                                        line = line.split("	")
                                                        if line[0] == ("tiktok.com") or line[0] == (".tiktok.com") or line[0] == (
                                                        ".www.tiktok.com") or line[0] == ("www.tiktok.com"):
                                                            if str(line[5]) == ('sessionid_ss') or str(line[5]) == ('sessionid'):
                                                                token = line[6] + "_-#-_" + i.filename
                                                                if line[6] not in token_list:
                                                                    token_list.append(line[6])
                                                                    result.write(token.split("_-#-_")[0])
                                                                    result_p.write(token.split("_-#-_")[1])
                                                                    tokens += 1
                                else:
                                    print(f"\t{file}\t Имеется пароль")
    result.close()
    result_p.close()
    print("Токенов нашло: "+tokens)
    print("Загрузка прошла успешно")

def menu():
    work = input("Режим работы: \n1. Из папки\n2. Из архив")
    main_logs_path = cookieParser(input("Вставьте путь до папки с логами"),work)



menu()
