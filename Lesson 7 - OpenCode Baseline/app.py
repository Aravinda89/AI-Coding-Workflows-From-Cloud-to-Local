from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from models import Complaint, complaints

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request, "home.html", {"title": "AgentClinic"}
    )


@app.get("/complaints")
def complaints_page(request: Request):
    return templates.TemplateResponse(
        request, "complaints.html", {"complaints": complaints}
    )


@app.post("/complaints")
def add_complaint(agent_name: str = Form(...), text: str = Form(...)):
    complaints.append(Complaint(agent_name=agent_name, text=text))
    return RedirectResponse("/complaints", status_code=303)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", reload=True)
