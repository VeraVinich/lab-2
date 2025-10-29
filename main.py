import csv
import random
import xml.etree.ElementTree as ET


with open('books-en.csv', encoding='cp1251') as file:
    reader = list(csv.DictReader(file, delimiter=';'))


# task1
count = sum(len(row["Book-Title"]) > 30 for row in reader)


#task 2
author = input("author:")
filter = []
for row in reader:
    try:
        year = int(row["Year-Of-Publication"])
        if author in row["Book-Author"] and 1991 <= year <= 1995:
            filter.append(row)
    except:
        pass


#task 3
bibls = random.sample(reader, 20)
with open("bibliography.txt", "w", encoding="utf-8") as f:
    for i, b in enumerate(bibls, start=1):
        f.write(f"{i}. {b['Book-Author']}. {b['Book-Title']} - {b['Year-Of-Publication']}\n")


#task 4
tree = ET.parse('currency.xml')
root = tree.getroot()


if __name__ == "__main__":
    print("ans1:", count)
    print('ans2:', len(filter))
    print("Библиография сохранена")
    for val in root.findall('.//Valute'):
        if int(val.find('Nominal').text) in (10, 100):

            print(val.find('CharCode').text)
