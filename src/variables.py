from random import SystemRandom
import json

# актуальные данные посещения веб-приложения
journal = {}
with open("res/journal.json", "r") as read_file:
    journal = json.load(read_file)

# переменная для генерации криптостойких ключей
cryptogen = SystemRandom()

# всего 30 тестовых страниц
last_test_page_num = 30
