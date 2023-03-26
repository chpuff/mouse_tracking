# файл начинается с комментария

from fastapi import FastAPI, Form, Body, Cookie, Path
from fastapi.responses import Response, FileResponse, HTMLResponse, PlainTextResponse
from fastapi.responses import RedirectResponse, JSONResponse
from starlette import status
from datetime import datetime
from src.variables import journal, cryptogen, last_test_page_num
import json
import os

app = FastAPI()


@app.get("/")
async def root(response: RedirectResponse):
    return RedirectResponse("/welcome_page")


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


# обработка нажатия кнопки Продолжить на первой странице
@app.post("/welcome_page_next_button")
def welcome_page_next_button():
    return RedirectResponse("/questionnaire", status_code=status.HTTP_302_FOUND)





# @app.get("/cookie")
# def cookie_def(response: Response):
#     num = str(cryptogen.randrange(10 ** 29, 10 ** 30))
#     response.set_cookie(key="sessid", value=num)
#     return {"message": "куки установлены"}
#
#
# @app.get("/see_cookie")
# def cookie_get(sessid: str | None = Cookie(default=None)):
#     if sessid == None:
#         return {"message": "Это ваш первый визит на сайт"}
#     else:
#         return {"message": f"Ваш последний визит: {sessid}"}