# файл начинается с комментария

from fastapi import FastAPI, Response, Cookie
from fastapi.responses import RedirectResponse, FileResponse, HTMLResponse
from src.variables import journal, cryptogen, last_test_page_num

app = FastAPI()


@app.get("/")
async def root(response: RedirectResponse):
    return RedirectResponse("/welcome_page")


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/welcome_page")
def welcome_page(response: RedirectResponse):
    return FileResponse("src/welcome.html")


@app.get("/text")
def root():
    data = "Hello METANIT.COM"
    return Response(content=data, media_type="text/plain")


@app.get("/html")
def read_root():
    html_content = "<h2>Hello everyone METANIT.COM!</h2>"
    return HTMLResponse(content=html_content)


@app.get("/cookie")
def cookie_def(response: Response):
    num = str(cryptogen.randrange(10 ** 29, 10 ** 30))
    response.set_cookie(key="sessid", value=num)
    return {"message": "куки установлены"}


@app.get("/see_cookie")
def cookie_get(sessid: str | None = Cookie(default=None)):
    if sessid == None:
        return {"message": "Это ваш первый визит на сайт"}
    else:
        return {"message": f"Ваш последний визит: {sessid}"}