# Веб-приложение для выполнения ВКР бакалавра
# папка с источниками - src
# Этапы выполнения работы в веб-приложении:
# просмотр картинок
# прохождение опроса
# сбор данных местоположения курсора мыши при выполнении задания выбора

from fastapi import FastAPI, Form, Body, Cookie, Path
from fastapi.responses import Response, FileResponse, HTMLResponse, PlainTextResponse
from fastapi.responses import RedirectResponse, JSONResponse
from starlette import status
from datetime import datetime
from src.variables import journal, cryptogen, last_test_page_num
import json
import os


app = FastAPI()


# добавление cookie новому пользователю
# переход на первую страницу - welcome страница
@app.get("/", response_class=RedirectResponse)
def root(response: RedirectResponse) -> RedirectResponse:
    # 30-значное значение для нового пользователя
    num = str(cryptogen.randrange(10 ** 29, 10 ** 30))

    # добавление в журнал записи о посещении первой (welcome страница) и
    # второй (опрос) страницы и сохранение в файл-журнал
    journal[num] = 2
    with open("res/journal.json", "w", encoding="utf-8") as write_file:
        json.dump(journal, write_file, indent=4)

    # установка куки для нового участника
    response = RedirectResponse(url="/welcome_page")
    response.set_cookie(key="sessid", value=num)

    return response


# главная страница - welcome страница
# первая страница
@app.get("/welcome_page")
def welcome_page(response: RedirectResponse):
    return FileResponse("src/welcome.html")


# вторая страница - опрос
@app.get("/questionnaire")
def questionnaire(response: RedirectResponse):
    return FileResponse("src/form.html")


# страница благодарности
@app.get("/gratitude")
def gratitude():
    return FileResponse("src/gratitude.html")


# страница с эмоциональным изображением
# значение n определяется из пути запроса
@app.get("/image/{n}", response_class=HTMLResponse)
def image_page(n: int = Path()):
    # журнал посещения не обновляется
    return FileResponse("src/emotional_image_{}.html".format(n))


# страница с опросом после страницы с эмоциональным изображением
@app.get("/emotional_poll", response_class=HTMLResponse)
def emotional_poll():
    # журнал посещения не обновляется
    return FileResponse("src/emotional_poll.html")


# страница тестирования
# открывается n-ая страница тестирования
# значение n определяется из пути запроса
@app.get("/test/{n}", response_class=HTMLResponse)
def test(n: int = Path(), sessid=Cookie()):
    # обновление данных журнала посещения
    journal[sessid] += 1
    with open("res/journal.json", "w", encoding="utf-8") as write_file:
        json.dump(journal, write_file, indent=4)

    return FileResponse("src/test_{}.html".format(n))


# обработка нажатия кнопки Продолжить на первой странице
@app.post("/welcome_page_next_button")
def welcome_page_next_button():
    return RedirectResponse("/questionnaire", status_code=status.HTTP_302_FOUND)


# обработка данных формы основного опроса
# после опроса переход на первое эмоциональное изображение
@app.post("/postdata")
def postdata(username: str = Form(default="Undefined", min_length=2, max_length=20),
             gender: int = Form(default=1),
             userage: int = Form(default=18, ge=1, lt=111),
             country=Form(default=""),
             depression=Form(default=""),
             sessid=Cookie()):

    # создание директории для участника в папе res
    # и сохранение полученных данных
    path = "res/{}".format(sessid)
    if not os.path.isdir(path):
        os.mkdir(path)

    form = {"username":username,
            "gender":gender,
            "userage":userage,
            "country":country,
            "depression":depression}
    with open("{}/{}_form.json".format(path, sessid), "w", encoding="utf-8") as write_file:
        json.dump(form, write_file, indent=4, ensure_ascii=False)

    return RedirectResponse("/image/1", status_code=status.HTTP_302_FOUND)


# обработка нажатия кнопки Продолжить на страницах с эмоциональными изображениями
@app.post("/image/to_emotional_poll")
def to_emotional_poll():
    return RedirectResponse("/emotional_poll", status_code=status.HTTP_302_FOUND)


# обработка данных опроса на эмоции
# после опроса переход на тестовое задание
@app.post("/to_test")
def to_test(answer=Form(default=""),
             sessid=Cookie()):
    path = "res/{}".format(sessid)

    form = {}
    with open("{}/{}_form.json".format(path, sessid), "r", encoding="utf-8") as read_file:
        form = json.load(read_file)

    # тест 1 - это третья по счёту страница, посещенная пользователем
    test_num = int((journal[sessid]+1)/3)
    form["test_{}".format(test_num)] = answer

    with open("{}/{}_form.json".format(path, sessid), "w", encoding="utf-8") as write_file:
        json.dump(form, write_file, indent=4, ensure_ascii=False)

    # тест 1 - это третья по счёту страница, посещенная пользователем
    next_page_num = journal[sessid] - 1
    return RedirectResponse("/test/{}".format(next_page_num), status_code=status.HTTP_302_FOUND)


# обработка нажатия кнопки Продолжить на страницах теста
@app.post("/test/nextpage")
def nextpage(sessid=Cookie()):
    # тест 1 - это третья по счёту страница, посещенная пользователем
    next_page_num = journal[sessid] - 1
    if next_page_num <= last_test_page_num:
        # если участник посетил 3 страницы с тестом после предыдущего изображения
        # (т.е. mod(next_page_num, 3)=1 ) - направить на страницу с изображением
        if next_page_num % 3 == 1:
            return RedirectResponse("/image/{}".format(next_page_num//3+1), status_code=status.HTTP_302_FOUND)
        return RedirectResponse("/test/{}".format(next_page_num), status_code=status.HTTP_302_FOUND)
    # если все тесты пройдены, отправляем на страницу благодарности
    else:
        return RedirectResponse("/gratitude", status_code=status.HTTP_302_FOUND)


# обработка положения курсора на страницах теста
@app.post("/mouseposition")
def mouseposition(data=Body(), sessid=Cookie()):
    x = data["x"]
    y = data["y"]

    # тест 1 - это третья по счёту страница, посещенная пользователем
    file_name = "res/{}/{}_test{}.txt".format(sessid, sessid, journal[sessid]-2)

    # извлекаем последнюю строку файла
    last_line = ""
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            file_lines = f.readlines()
            if len(file_lines) > 0:
                last_line = file_lines[-1]
    except:
        pass

    # если в строке записано left или right - не запоминаем положение
    # достигнуто нажатие кнопки Левая или Правая
    if last_line != "left\n" and last_line != "right\n":
        # запись в файл
        with open(file_name, "a+", encoding="utf-8") as f:
            f.write(f"{x}, {y}, {datetime.now()} \n")

    return {"message": f"{x}, {y}"}


# обработка нажатия кнопки Левая или Правая на страницах теста
@app.post("/leftOrRightBut")
def leftOrRightBut(data=Body(), sessid=Cookie()):
    mes = data["message"]

    # тест 1 - это третья по счёту страница, посещенная пользователем
    file_name = "res/{}/{}_test{}.txt".format(sessid, sessid, journal[sessid] - 2)

    # запись в файл пользователя
    # после записи значения mes (left/right) в файл с координатоми курсора пользователя
    # сохранение дальнейших координат будет остановлено (реализация остановки записи в mouseposition)
    f = open(file_name, 'a+', encoding="utf-8")
    f.write(f"{mes}\n")
    f.close()
    return {"message": f"{mes}"}
