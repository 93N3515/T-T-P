import os
import datetime
import threading

def cookieParser(path):
    savefilename = f"tokens {str(datetime.date.today()) + ' ' + str(datetime.datetime.now().hour) + '.' + str(datetime.datetime.now().minute) + '.' + str(datetime.datetime.now().second)}"
    os.mkdir(savefilename)
    print("Загрузка логов")
    tokens = []
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

    main_logs_path = cookieParser(input("Вставьте путь до папки с логами"))

menu()