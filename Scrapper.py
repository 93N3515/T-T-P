import os
import datetime
import threading
import zipfile
from zipfile import ZipFile
import rarfile

def cookieParser(path,work):
    savefilename = f"tokens {str(datetime.date.today()) + ' ' + str(datetime.datetime.now().hour) + '.' + str(datetime.datetime.now().minute) + '.' + str(datetime.datetime.now().second)}"
    os.mkdir(savefilename)
    print("Загрузка логов")
    tokens = []

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
                            if str(cc_split[5]) == ('sessionid_ss') or str(cc_split[5]) == ('sessionid'):
                                tokens.append(line.split("	")[6].strip() + "_-#-_" + filep)

    else:
        for file in os.listdir(path):
            if os.path.isdir(path+"\\"+file) != True:
                if zipfile.is_zipfile(path+"\\"+file):
                    with ZipFile(path+"\\"+file) as myzip:
                        for i in ZipFile.infolist(myzip):
                                if i.filename.find(".txt") >= 1:
                                    try:
                                        for line in myzip.open(i).readlines():
                                            line = line.decode()
                                            if line.find("	/	") >= 1:
                                                line = line.split("	")
                                                if line[0] == ("tiktok.com") or line[0] == (".tiktok.com") or line[0] == (
                                                        ".www.tiktok.com") or line[0] == ("www.tiktok.com"):
                                                    if str(line[5]) == ('sessionid_ss') or str(line[5]) == ('sessionid'):
                                                        tokens.append(
                                                            line[6].strip() + "_-#-_" + myzip.filename + str(i.filename))
                                    except UnicodeDecodeError:
                                        print("unicode error")

                elif rarfile.is_rarfile(path+"\\"+file):
                    with rarfile.RarFile(path + "\\" + file) as myrar:
                        for i in rarfile.RarFile.infolist(myrar):
                            if i.filename.find(".txt") >= 1:
                                try:
                                    for line in myrar.open(i).readlines():
                                        line = line.decode()
                                        if line.find("	/	") >= 1:
                                            line = line.split("	")
                                            if line[0] == ("tiktok.com") or line[0] == (".tiktok.com") or line[0] == (
                                            ".www.tiktok.com") or line[0] == ("www.tiktok.com"):
                                                if str(line[5]) == ('sessionid_ss') or str(line[5]) == ('sessionid'):
                                                    tokens.append(line[6].strip() + "_-#-_" + myrar.filename + str(i.filename))
                                except UnicodeDecodeError:
                                    print("unicode error")


    tokens = list(set(tokens))
    print(len(tokens))
    result = open(f'{savefilename}\\result.txt', 'w+', encoding="UTF-8")
    result_p = open(f'{savefilename}\\result_path.txt', 'w+', encoding="UTF-8")
    for token_i in tokens:
        try:
            token = token_i.split("_-#-_")[0]
            filep = token_i.split("_-#-_")[1]
            result.write(f"{token}\n")
            result_p.write(f"{token}\n{filep}\n\n")
        except:
            pass
    result.close
    result_p.close()
    print("Загрузка прошла успешно")

def menu():
    work = input("Режим работы: \n1. Из папки\n2. Из архив")
    main_logs_path = cookieParser(input("Вставьте путь до папки с логами"),work)



menu()
