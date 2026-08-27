from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class Complaint:
    agent_name: str
    text: str
    timestamp: datetime = datetime.now(timezone.utc)


complaints: list[Complaint] = [
    Complaint(agent_name="Agent-01", text="Instructions were unclear and led to wasted effort"),
    Complaint(agent_name="Agent-02", text="Received contradictory feedback from different reviewers"),
    Complaint(agent_name="Agent-03", text="Scope creep doubled the estimated workload mid-sprint"),
    Complaint(agent_name="Agent-04", text="Dependencies not documented, causing integration failures"),
    Complaint(agent_name="Agent-05", text="Breaking changes deployed without version bump or migration guide"),
]