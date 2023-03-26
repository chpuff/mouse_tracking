# файл начинается с комментария

from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse, FileResponse, HTMLResponse

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