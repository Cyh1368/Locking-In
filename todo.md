# Project TODOs — Locking-In (from JoeIdea.md)

## Milestones

- M1 — Spec & tasks (this file)
- M2 — Prototype demo (mocked data + UI overlay)
- M3 — Rule engine + logging
- M4 — Usability test & metrics

## Tasks (priority order)

1. Project setup
- 1.1 Create repo structure: `src/`, `demo/`, `docs/`.
- 1.2 Add README and development instructions.
- Acceptance: repo can run demo locally.

2. Mock data & integrations
- 2.1 Implement mocked Calendar, Tasks, and Inbox count services.
- 2.2 Provide configurable scenarios (e.g., "no unread", "urgent message", "focus meeting").
- Acceptance: demo can toggle scenarios via config file or UI.

3. Decision rule engine (core logic)
- 3.1 Implement configurable heuristics (recency threshold N, priority contacts, calendar importance).
- 3.2 Add a lightweight scoring function for app-open events.
- 3.3 Expose overrides and cooldowns.
- Acceptance: given a scenario, engine outputs action (`allow`, `nudge`, `soft-block`) and rationale.

4. Messaging & UX overlay
- 4.1 Build a minimal overlay UI with message, reason, and actions: `Proceed`, `Snooze`, `Block (10m)`, `Override`.
- 4.2 Ensure accessible labels and keyboard support.
- Acceptance: overlay displays appropriate message and actions for each scenario.

5. Logging & developer/debug view
- 5.1 Record decision events, timestamps, and inputs used for decisions.
- 5.2 Build a debug UI showing the decision log and rule evaluation breakdown.
- Acceptance: developer view shows full decision trace for any event.

6. Privacy & permissions
- 6.1 Implement local-first storage for usage logs and settings.
- 6.2 Add consent flow and clear explanation of data usage.
- Acceptance: demo runs without external network calls by default.

7. Testing & metrics
- 7.1 Scripted scenarios to measure app-switch reductions and session times.
- 7.2 Simple user survey for qualitative satisfaction.
- Acceptance: collect example metrics from scripted runs.

8. Documentation & demo script
- 8.1 Write a short demo script showing 3 scenarios.
- 8.2 Add README instructions for running the demo and toggling mocks.
- Acceptance: an external reviewer can follow README and run demo.

9. Optional follow-ups
- 9.1 Add simple ML model for personalization (deferred).
- 9.2 Multi-device syncing design notes.

## Short-term next actions (this week)
- Create `src/` and `demo/` skeletons and README.
- Implement basic mocked services and a single overlay scenario.
- Add a short demo script with 2 scenarios.

---
Generated from `JoeIdea.md` to break the spec into implementation tasks.
