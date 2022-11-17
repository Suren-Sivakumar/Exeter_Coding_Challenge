import csv
import shutil
import pandas as pd
import psutil
import time

word_list_txt_file = open('find_words.txt','r')
txtreader2 = word_list_txt_file.readlines()

open ('t8.shakespeare.txt','r')
shutil.copyfile('t8.shakespeare.txt','t8.shakespeare.translated.txt')

dict_csv = open("./french_dictionary.csv",'rt')
csvreader = csv.reader(dict_csv)

upd = 0
for a in csvreader:
    df = pd.read_csv("frequency.csv")
    for j in txtreader2:
        if (j.rstrip() == a[0]):
            df.loc[upd, 'English word'] = a[0]
            df.loc[upd, 'French word'] = a[1]
            with open('t8.shakespeare.translated.txt', 'r') as file:
                data = file.read()
                count = data.count(a[0])
                data = data.replace(a[0], a[1])
            with open('t8.shakespeare.translated.txt', 'w') as file:
                file.write(data)
            df.loc[upd, 'Frequency'] = count
            df.to_csv("frequency.csv", index=False)
            
    upd = upd+1

t1 = 0
t1 = int(time.process_time())
t2= int(t1/60)
t3= int(t1%60)
t= "Time to process: " + str(t2) + " minutes " + str(t3) + " seconds"
m = "Memory used: " + str(int(psutil.Process().memory_info().rss / (1024 * 1024))) + " MB"

txt = t + "\n" + m
with open('performance.txt', 'w') as file:
    file.write(txt)