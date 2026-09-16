# Deny patterns

Short catalog of collapse modes. Not a substitute for a full killed-seats table.

If `docs/adr/0001-no-pitchable-candidate.md` exists, **read it**. Its killed-seats tables are authoritative. Do not rediscover those seats as Sparse or Greenfield.

If that file is missing, say so: `deny_catalog: incomplete`. Still apply the patterns below.

## Collapse modes (automatic `FILE_ON_X` or `KILL`)

1. **File it on the incumbent.** Named product already *is* the headline UX (silo for loopback isolation; ntfy `--wait-cmd` for silent local jobs).
2. **Add the missing ecosystem to Veln** (or Pixi, OpenTofu, ntfy, cachelens, Electric, Cursor, …). Cross-ecosystem absence is not a company.
3. **Sidecar without host runtime enforcement.** Third-party lockfile, PATH wrap, or controller the platform does not consult (`tofulock`, `pio-lock`, `red-widow`). Real engineering, not a company.

## Recurring occupied aisles

Treat as closed unless a **mechanical** gap appears that the write-up missed:

- ntfy-class phone notifiers for local/CI jobs
- localhost tunnel / OAuth companion (ngrok, Cloudflare named tunnels, Dev Tunnels, Zedra)
- worktree loopback isolation (**silo**)
- advisory prompt-cache inspectors (vendor diagnostics, cachelens)
- vendor API contract drift (Optic, Prism, Speedscale, oasdiff)
- universal offline SQL mutation upcast (non-invertible; reject)
- PTY secret reverse-map (confused deputy; reject)
- agent sandbox / FS / secrets / MCP wraps the host already ships
- package-manager-shaped lock/integrity seats the platform absorbed (`actions.lock`, native Helm/dbt/mise locks)

## Priors are not a rubric

Files under `docs/ratings/` (including an ADR 0002 SymMerge rating) are **priors**:

- Use them to avoid rediscovering a seat you already scored.
- Do **not** copy their verdict onto a new idea because “it bundles occupied tools too.”
- Re-search **this** idea’s seat. Name **this** idea’s incumbents. Seat-match those rows.

A previous kill is a deny-list entry, not a scoring template.

## Confirm unused before scoring

If the idea’s one-line seat matches a killed row, stop: `FILE_ON_X` or `KILL` with a pointer to that row. Do not spend the session redesigning v1 pricing.
