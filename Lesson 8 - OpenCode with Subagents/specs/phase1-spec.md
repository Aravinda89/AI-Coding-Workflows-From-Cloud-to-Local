# Phase 1 Spec — Home Page

## Task List

### Task 1: Create app.py with FastAPI application instance
- Create `app.py` with FastAPI app instance
- Import necessary modules (FastAPI, Request, Jinja2Templates, Path)

### Task 2: Create templates/ directory
- Create `templates/` directory

### Task 3: Create templates/base.html
- HTML5 doctype and `<html lang="en">`
- `<head>` with charset, viewport meta, Bootstrap 5 CSS CDN link
- `<link>` favicon pointing to `https://www.python.org/static/favicon.ico`
- Title block (default: "AgentClinic")
- Simple navbar with "AgentClinic" brand and links to Home (`/`) and Complaints (`/complaints`)
- `{% block content %}` for page-specific content
- Bootstrap 5 JS bundle CDN at bottom of `<body>`

### Task 4: Create templates/home.html
- Extends `base.html`
- Hero/jumbotron section with tagline: *"Come in. Sit down. Tell us about your human."*
- Brief welcoming paragraph about the clinic

### Task 5: Add `/` route in app.py
- Add GET `/` route returning the home template

### Task 6: Add main block in app.py
- Add `if __name__ == "__main__"` block to run with `uvicorn.run("app:app", reload=True)`

### Task 7: Write smoke test in tests/test_app.py
- Import `TestClient` from `starlette.testclient`
- Test `GET /` returns status 200
- Test response body contains the tagline text