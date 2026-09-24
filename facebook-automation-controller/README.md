# Facebook Automation Controller

A modular controller/orchestrator for user-owned account workflows.

## Architecture

- Global rounds: iterate through all configured accounts for N rounds.
- Account order: App 1 -> App 2 -> ... -> App N.
- Feature toggles: enable/disable modules per account.
- Per-feature limits: each module receives its configured N limit.
- Modules are adapters behind a common interface.
- Credentials, cookies, tokens, and sessions are never stored in source control.

## Project status

This ZIP contains the orchestration/configuration skeleton. Platform-specific actions are intentionally left behind module interfaces and must comply with the platform's terms and applicable APIs.
