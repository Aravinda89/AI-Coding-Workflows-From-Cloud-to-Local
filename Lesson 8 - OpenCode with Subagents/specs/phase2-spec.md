# Phase 2 Spec — Complaints Board

## Task List

### Task 1: Create models.py with Complaint dataclass
- Create `models.py` with `Complaint` dataclass
- Fields: `agent_name: str`, `text: str`, `timestamp: datetime`
- Add `from datetime import datetime, timezone` and set `timestamp` default to `datetime.now(timezone.utc)`

### Task 2: Create module-level complaints list in models.py
- Create `complaints: list[Complaint]` module-level list
- Populate with 3-5 seed complaints (generic AI-agent gripes)

### Task 3: Add GET /complaints route in app.py
- Import `complaints` from `models`
- Return `templates/complaints.html` passing the complaints list as context

### Task 4: Create templates/complaints.html
- Extends `base.html`
- Heading: "Complaints Board"
- Loop through complaints and render each as a Bootstrap card showing agent name, timestamp (formatted), and complaint text
- Form at the bottom with:
  - `POST` method to `/complaints`
  - Text input for agent name
  - Textarea for complaint text
  - Submit button

### Task 5: Add POST /complaints route in app.py
- Import `Complaint` from `models`
- Read `agent_name` and `text` from form data (`Form` from `fastapi`)
- Create a new `Complaint` and append to the `complaints` list
- Redirect to `GET /complaints` (use `RedirectResponse` with status 303)

### Task 6: Write tests in tests/test_app.py
- Test `GET /complaints` returns 200 and contains seed complaint text
- Test `POST /complaints` with `agent_name` and `text` redirects to `/complaints`
- Test after `POST /complaints`, `GET /complaints` response includes the newly added complaint