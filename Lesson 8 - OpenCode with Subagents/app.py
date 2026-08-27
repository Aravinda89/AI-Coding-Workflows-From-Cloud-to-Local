from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from pathlib import Path
from models import complaints, Complaint

app = FastAPI()

templates = Jinja2Templates(directory=Path(__file__).parent / "templates")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request, "home.html")


@app.get("/complaints")
async def get_complaints(request: Request):
    return templates.TemplateResponse(request, "complaints.html", {"complaints": complaints})


@app.post("/complaints")
async def post_complaint(agent_name: str = Form(...), text: str = Form(...)):
    complaints.append(Complaint(agent_name=agent_name, text=text))
    return RedirectResponse(url="/complaints", status_code=303)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", reload=True)