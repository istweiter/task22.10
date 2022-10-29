import csv
modelList = [
    "LADA",
    "Mercedes-benz",
    "Land Cruiser",
    "BMW",
    "Lexus",
    "Tesla",
    "Volvo",
    "Hunday"
]
priceList = [
    800349,
    4382300,
    3928700,
    3145200,
    5099900,
    2961500,
    2351100,
    2300000
]
# создать словарь из списков
def createDict(a, b):
    dict = {}
    for i in range(len(a)):
        dict[a[i]] = b[i]
    return dict
# создать CSV файл из словаря
def createCSV(path, dict):
    writer = csv.writer(open(path, 'w', newline=''))
    for i in range(len(dict)):
        keys = list(dict.keys())
        values = list(dict.values())
        writer.writerow([keys[i], values[i]])
# показать кол-во букв в тексте
def getCharacters(path, symbol):
    counter = 0
    with open(path, 'r', encoding='utf-8') as file:
        for i in file.read():
            if i == symbol:
                counter += 1
    f.close()
    return counter
# вывод в консоль словаря
print(createDict(modelList, priceList))
# вывод в консоль файла CSV
createCSV('ff.csv', createDict(modelList, priceList))
with open('ff.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# Вывод в консоль количества букв 'о' в txt файле
print(getCharacters('Новость.txt', 'о'))
