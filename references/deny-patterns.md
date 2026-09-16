# Deny patterns

Ported collapse modes from `vendor/pitch-rate/references/deny-patterns.md`. Not a substitute for a full killed-seats table. Do not condense ADR 0001 tables into this file as the working catalog (prior-kill-as-rubric).

## ADR pointer

If `docs/adr/0001-no-pitchable-candidate.md` exists in the target workspace, its killed-seats tables are authoritative (`deny_catalog: local_adr_0001`). Confirm the candidate's one-line seat against those rows before scoring; a match stops the run with a pointer to that row.

If that file is missing, use the embedded baseline below (`deny_catalog: embedded_baseline`).

`deny_catalog: incomplete` only if the vendor deny file, ADR 0001, *and* this fallback are all missing. That is not the happy path.

## Collapse modes (ported from vendor)

1. **File it on the incumbent.** Named product already *is* the headline UX (silo for loopback isolation; ntfy `--wait-cmd` for silent local jobs).
2. **Add the missing ecosystem to Veln** (or Pixi, OpenTofu, ntfy, cachelens, Electric, Cursor, ...). Cross-ecosystem absence is not a company.
3. **Sidecar without host runtime enforcement.** Third-party lockfile, PATH wrap, or controller the platform does not consult (`tofulock`, `pio-lock`, `red-widow`). Real engineering, not a company.

## Embedded fallback (use only when ADR 0001 is absent)

Treat as closed unless a **mechanical** gap appears that the write-up missed:

- Phone notifiers for local/CI tasks (ntfy, Pushover)
- Localhost tunnels and OAuth companions (ngrok, Cloudflare named tunnels, Dev Tunnels)
- Worktree loopback isolation (silo)
- Sidecar locks without host enforcement

Fuller ported aisles from the vendor file (same rule -- closed unless a mechanical gap appears): advisory prompt-cache inspectors, vendor API contract drift seats, universal offline SQL mutation upcast (non-invertible; reject), PTY secret reverse-map (confused deputy; reject), agent sandbox / FS / secrets / MCP wraps the host already ships, package-manager-shaped lock/integrity seats the platform absorbed.

## Priors are not a rubric

A previous kill is a deny-list entry, not a scoring template. Do not use closed-aisle leftovers as generation seeds. Re-search **this** seat. Name **this** seat's incumbents. Seat-match those rows.
