import requests
from bs4 import BeautifulSoup
import json


list_quotes = []
list_author = []
writer_list = []


file_json = "data.json"
file_index="index.html"
url = 'https://quotes.toscrape.com/'


response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')


for quote in quotes:
    list_quotes.append(quote.text)  
for atr in authors:
    list_author.append(atr.text)  


for i in range(len(list_quotes)):
    print(f"{i + 1}. Quote: {list_quotes[i]}; Author: {list_author[i]};")
    
with open(file_json, "w+", encoding='utf-8') as file:
    for i in range(len(list_quotes)):   
        writer = {'Quote': list_quotes[i], 'Author': list_author[i]}
        writer_list.append(writer)
    json.dump(writer_list, file, indent=5, ensure_ascii=False)




with open(file_index, "w+" , encoding='utf-8') as file:
    file.write("<html><head><title>Quotes</title></head><body>\n")
    file.write('<h1><p align="center" > <a href="https://quotes.toscrape.com/">Великие цитаты</h1></a></p>\n')
    file.write('<body bgcolor="FFCC99">\n')
    file.write('<table cellspacing="2"  bordercolor="purple"  BGCOLOR= #0ABAB5 border="1" align="center" ')
    file.write("<table>\n")
    file.write("<tr>\n")
    file.write(" <td>Цитата</td>\n<td>Автор</td>\n<td>Номер</td>\n</tr>\n")

    with open(file_json, "r", encoding='utf-8') as input:
        data_writer =  json.load(input)
        for i in range(len(data_writer)):
            file.write(f"<tr>\n<td>{data_writer[i]['Quote']}</td>\n<td>{data_writer[i]['Author']}</td>\n<td>{i+1}</td>\n")
    file.write("</table>\n")
    file.write("</body></html>")




