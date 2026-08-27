from pathlib import Path
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from models import complaints, Complaint

BASE_DIR = Path(__file__).resolve().parent
app = FastAPI()
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request, "home.html")

@app.get("/complaints")
async def complaints_list(request: Request):
    return templates.TemplateResponse(request, "complaints.html", {"complaints": complaints})

@app.post("/complaints")
async def create_complaint(agent_name: str = Form(...), text: str = Form(...)):
    complaint = Complaint(agent_name=agent_name, text=text)
    complaints.append(complaint)
    return RedirectResponse(url="/complaints", status_code=303)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", reload=True)
