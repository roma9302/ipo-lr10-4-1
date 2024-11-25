import requests   #Запросы в интернет
from bs4 import BeautifulSoup 
import json # работа с json 


list_quotes = []  #Лист для хранения цитат
list_author = [] #Лист для хранения авторов цитат
writer_list = [] #Общий лист цитаты + авторы


file_json = "data.json"  #Переменная для файла json
file_index="index.html" #Создаваемая программой страница
url = 'https://quotes.toscrape.com/' #Сайт для парсинга информации


response = requests.get(url) #Получаем html страницы 
soup = BeautifulSoup(response.text, 'lxml') #парсим информацию
quotes = soup.find_all('span', class_='text') #Собираем все цитаты через тег span/text
authors = soup.find_all('small', class_='author') #Собираем всех авторов через тег small/author


for quote in quotes:       #добавление цитат в ранее созданный список
    list_quotes.append(quote.text)  
for atr in authors:  #добавление авторо в ранее созданный список
    list_author.append(atr.text)  


for i in range(len(list_quotes)):  #вывод номер + цитата + автор  
    print(f"{i + 1}. Quote: {list_quotes[i]}; Author: {list_author[i]};") # 1. Quote: “The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”; Author: Albert Einstein;
    
with open(file_json, "w+", encoding='utf-8') as file:  #Запись в json файл
    for i in range(len(list_quotes)):   
        writer = {'Quote': list_quotes[i], 'Author': list_author[i]}
        writer_list.append(writer)
    json.dump(writer_list, file, indent=5, ensure_ascii=False)




with open(file_index, "w+" , encoding='utf-8') as file:  #создание файла index.html
    file.write("<html><head><title>Quotes</title></head><body>\n")  #титульник старницы
    file.write('<h1><p align="center" > <a href="https://quotes.toscrape.com/">Великие цитаты</h1></a></p>\n') #Текст над таблицей с гиперссылкой на оригинальный источник
    file.write('<body bgcolor="FFCC99">\n') #цвет фона
    file.write('<table cellspacing="2"  bordercolor="purple"  BGCOLOR= #0ABAB5 border="1" align="center" ') #Атрибуты таблицы цвет границ\заливка таблицы\толщина границ\выравнивание по центру
    file.write("<table>\n") #создание таблицы
    file.write("<tr>\n")
    file.write(" <td>Цитата</td>\n<td>Автор</td>\n<td>Номер</td>\n</tr>\n") #заголовки старницы

    with open(file_json, "r", encoding='utf-8') as input:
        data_writer =  json.load(input) #переменная считывающая информацию с файла json 
        for i in range(len(data_writer)): #цикл для записи информации в таблицу
            file.write(f"<tr>\n<td>{data_writer[i]['Quote']}</td>\n<td>{data_writer[i]['Author']}</td>\n<td>{i+1}</td>\n")
    file.write("</table>\n") #закрывающий тег таблицы
    file.write("</body></html>") #закрывающий тег страницы




