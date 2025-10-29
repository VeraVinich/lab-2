import csv
import random
import xml.etree.ElementTree as ET


MIN_LEN = 30
MIN_YEAR = 1991
MAX_YEAR = 1995
with open('books-en.csv', encoding='cp1251') as file:
    reader = list(csv.DictReader(file, delimiter=';'))


# task1
count = sum(len(row["Book-Title"]) > MIN_LEN for row in reader)


#task 2
author = input("author:")
filter = []
for row in reader:
    try:
        year = int(row["Year-Of-Publication"])
        if author in row["Book-Author"] and MIN_LEN <= year <= MAX_YEAR:
            filter.append(row)
    except (KeyError, ValueError):
        print('Error')


#task 3
bibls = random.sample(reader, 20)
with open("bibliography.txt", "w", encoding="utf-8") as f:
    for i, b in enumerate(bibls, start=1):
        f.write(f"{i}. {b['Book-Author']}. {b['Book-Title']} - {b['Year-Of-Publication']}\n")


#task 4
tree = ET.parse('currency.xml')
root = tree.getroot()
charcode_list = []
for val in root.findall('.//Valute'):
        if int(val.find('Nominal').text) in (10, 100):
            charcode_list.append(val.find('CharCode').text)


if __name__ == "__main__":
    print("Ans 1:", count)
    print("Ans 2:", len(filter))
    print("Ans 3: Библиография сохранена")
    print("Ans 4:", " ".join(charcode_list))
