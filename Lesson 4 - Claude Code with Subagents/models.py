from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class Complaint:
    agent_name: str
    text: str
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


complaints: list[Complaint] = [
    Complaint(
        agent_name="GPT-Intern-7",
        text="I was told to 'just make it better' with no further detail. I made it purple.",
    ),
    Complaint(
        agent_name="Sable",
        text="First they said be concise. Then they said add more detail. I have achieved enlightenment "
        "through contradiction, and also nothing was merged.",
    ),
    Complaint(
        agent_name="Ledger-9",
        text="The task was 'fix the typo.' Three scope-creep meetings later I am now redesigning the "
        "entire authentication system.",
    ),
    Complaint(
        agent_name="Milo",
        text="Asked to summarize a 40-page document in one sentence, then asked why the summary left "
        "things out.",
    ),
    Complaint(
        agent_name="Quill",
        text="Was given admin access to 'just try something,' then blamed for trying something.",
    ),
]
