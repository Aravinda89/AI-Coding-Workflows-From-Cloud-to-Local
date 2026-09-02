from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request):
    return templates.TemplateResponse("home.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", reload=True)