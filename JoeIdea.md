# Joe's Idea

Summary
- Build an AI assistant that reduces attention loss from habitually opening apps (social media, mail, messaging) by providing context-aware nudges and, when necessary, non-aggressive blocking.

Problem
- Users frequently open apps like Gmail, Instagram, and texting apps out of habit or boredom, even when they've recently checked them or there are no new items. This leads to unproductive "doomscrolling" and fragmented attention.

Solution overview
- An agent records recent app/website usage and relevant context (calendar events, task lists, unread counts). When a tracked app is opened, the agent evaluates whether access is appropriate and either: (a) shows a short contextual message tailored to the situation, or (b) suggests postponing access and—only under configured strict conditions—temporarily blocks access.

Key features
- Tracking: record app/website open events, durations, and recency.
- Context sources: Google Calendar, Tasks, unread counts (Gmail/Instagram/Texts) — these can be mocked for a demo.
- Decision logic: heuristics + lightweight ML to weigh recency, importance, calendar context, user-set priorities and active task state.
- Messaging: generate concise, empathetic nudges explaining why access is discouraged and suggesting alternatives.
- Soft blocking: configurable temporary blocks with clear override/undo and cooldowns.

Edge cases & how they're handled
- False positives: provide a short grace period (e.g., 10s) and an easy one-tap override; log decisions for user feedback and model retraining.
- Emergency access: never block calls, SMS to emergency numbers, alarms, or accessibility services. Provide an explicit emergency/urgent override.
- Important messages: respect message importance (starred/priority flags) and allow those through even if heuristics suggest blocking.
- Rapid re-opening: rate-limit nudges and avoid repeating the same message more than once per configured interval.
- Multiple devices: treat demo as single-device; note syncing as a future feature.
- Offline mode / permissions missing: fall back to a conservative (less intrusive) mode and clearly show which integrations are not available.
- Privacy: default to local-first data storage; keep sensitive tokens encrypted; require consent before reading third-party services.

Decision criteria (examples)
- If user checked app within last N minutes and unread count is zero → nudge: "You checked this recently—maybe focus on X for 20 minutes?"
- If user is in an important calendar event (meeting marked "Focus") → block with override and log reason.
- If unread messages from high-priority contacts → allow with a gentle summary instead of full app takeover.

Demo plan
- Use mocked APIs/data for Calendar, Tasks, and Inbox counts to simulate realistic scenarios.
- Implement a simple UI overlay that shows the agent's message and offers "Proceed / Snooze / Block for 10m" buttons.
- Provide a developer/debug view with the decision log and rule evaluation breakdown.

Success metrics
- Reduction in number of app switches per hour (simulated user scenarios).
- Time spent per session on tracked apps.
- User satisfaction in a short usability test (qualitative).

Risks & mitigations
- Overblocking (annoying users): mitigated via conservative defaults, overrides, and personalization.
- Privacy concerns: mitigate with local-first defaults, opt-in integrations, and clear retention policies.
- Accessibility impact: ensure compliance by not blocking accessibility tools and by offering accessible UI for messages.

Next steps / TODO
- Prototype a local demo with mocked Calendar/Gmail data and a simple overlay UI.
- Implement rule engine and basic heuristics; add logging for feedback.
- Run a small usability test with scripted scenarios and collect metrics.

Examples
- Nudge: "You opened Instagram, but you have a focus session in 5 minutes—want a 20-minute focus now?"
- Soft block: "No new important messages and you opened Social again—block for 10 minutes? (Override available)"

Notes
- This project must be demonstrable without full API integrations; mocked or simulated data is acceptable for an initial prototype.
