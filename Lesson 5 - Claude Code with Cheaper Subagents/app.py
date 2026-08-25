from fastapi import FastAPI, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
import uvicorn
from models import Complaint, complaints

app = FastAPI(title="AgentClinic")

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request, "home.html")


@app.get("/complaints")
async def view_complaints(request: Request):
    return templates.TemplateResponse(request, "complaints.html", {"complaints": complaints})


@app.post("/complaints")
async def create_complaint(agent_name: str = Form(...), text: str = Form(...)):
    new_complaint = Complaint(agent_name=agent_name, text=text)
    complaints.append(new_complaint)
    return RedirectResponse(url="/complaints", status_code=303)


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)
