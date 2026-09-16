# Plan 2: Build `profinder` Skill (Evolved from `llmresearch` PR #8)

## 0. Context & Architectural Foundation

- **Source Reference**: PR #8 (`kirank55/llmresearch#8`), branch `cursor/pitch-rate-skill-bd8d` → `main`.
- **Core Philosophy**: Encodes ADR 0001 occupancy filter:
  > *"Score existing-solution density, not pain. Pain is abundant. Empty seats are not."*
- **Evolution from PR #8 (`pitch-rate`) to `profinder`**:
  - `pitch-rate` was a purely reactive verifier: given an idea/ADR/PR, score its occupancy and emit a verdict (`PITCH | KILL | FILE_ON_X | NEED_EVIDENCE`).
  - `profinder` expands into a dual-mode skill:
    1. **`hunt` (Discovery Mode)**: Proactively search developer-tool, infrastructure, and systems pain points for vacant architectural seats (Greenfield/Sparse), citing real mechanics and incumbents.
    2. **`verify` (Evaluation Mode)**: Subject any candidate idea, ADR, or proposal to the exact ADR 0001 occupancy gates, seat-match taxonomy, and falsification tests without rater bias.
- **Portability**: Self-contained skill directory compatible across modern agent environments (OpenCode, Claude Code, Antigravity, and Pi) without hardcoded dependencies on private repositories.

---

## 1. Target Directory Layout

```text
c:\Users\kiran\code\p\profinder\
├── plan1.md                          # Initial sketch
├── plan2.md                          # Comprehensive architecture and build plan (this file)
├── SKILL.md                          # Execution procedure; strictly loads references on demand
└── references/
    ├── rubric.md                     # ADR 0001 density bands, split verdicts, 7 auto-rejects, falsification
    ├── seat-match.md                 # 6-label taxonomy (exact, adjacent_pain, language_scoped, wrong_substrate, obsolete, price_packaging)
    ├── deny-patterns.md              # Self-contained collapse modes & embedded killed-seats catalog
    ├── search-playbook.md            # Mechanics-first search heuristics (URL + quote, >=5 incumbents)
    ├── calibration.md                # Gold standards (SymMerge, SagaGuard, TenantScale, ntfy, false exacts)
    └── output-template.md            # Standard candidate schema (no overall /100)
```

---

## 2. File Specifications & Content Design

### A. `SKILL.md` (Root Entrypoint)
- **Frontmatter**:
  ```yaml
  ---
  name: profinder
  description: Hunt and verify developer-tool/infra product seats against ADR 0001 occupancy gates. Use when asked to find, evaluate, score, or kill developer tools, SaaS ideas, or ADRs.
  ---
  ```
- **Operational Flow**:
  1. **Determine Object & Mode**:
     - Mode: `hunt` (search vacant seats) or `verify` (rate an existing idea/ADR).
     - Object: `idea` | `adr` | `pr_process` (never mix PR hygiene with idea viability).
  2. **Load References on Demand**: Load in mandatory order (`rubric.md` → `seat-match.md` → `deny-patterns.md` → `search-playbook.md` → `output-template.md`). Never inline scoring logic from LLM memory.
  3. **Calibration Check**: Read `calibration.md` before generating any score to anchor labeling discipline.
  4. **Steelman First**: Formulate the strongest possible case for why a skeptical founder would build this and establish an occupancy ceiling ($0\text{--}10$). Published exact-mechanics score cannot exceed this ceiling without naming new incumbents.
  5. **Search Mechanics, Not Slogans**: Run targeted queries for stack substrate (daemon, wire proxy, compiler, kernel/eBPF, CI scheduler) using `search-playbook.md`. Collect $\ge 5$ incumbents with verified URLs and exact documentation quotes.
  6. **Seat-Match & Dual-Score**: Assign each incumbent exactly one label from `seat-match.md`. Score problem density (including adjacent) and exact-mechanics density (exact rows only).
  7. **Apply Gates & Emit Schema**: Check 7 auto-rejects and 3 falsification tests. Emit the standard candidate card (`output-template.md`). Never emit an overall `/100`.

---

### B. `references/rubric.md` (Scoring Bands & Rejection Criteria)
- **Density Bands**:
  | Band | Score | Meaning | Action |
  |---|---|---|---|
  | **Saturated** | 8–10 | Named products already *are* this UX | Do not build |
  | **Occupied** | 5–7 | Adjacent tools treat the pain; leftover is glue, flag, or plugin | `FILE_ON_X` |
  | **Sparse** | 2–4 | Pieces exist; no widely adopted product sits in the proposed seat | Potential `PITCH` |
  | **Greenfield** | 0–1 | Mechanics are fundamentally new | Potential `PITCH` |

- **Split Verdicts**:
  - `as_company`: Sparse/Greenfield + 0 auto-rejects + passes falsification.
  - `as_oss`: Worth publishing as a bounded utility/proxy/library even if not a standalone company.
  - `as_plugin`: Honest leftover is a flag, PR, or plugin on an incumbent host.

- **7 Automatic Rejects** (Fatal for `PITCH` as a company):
  1. A named incumbent already ships the headline UX.
  2. The product is a 50-line GitHub Action, shell script, curl wrapper, or editor hook.
  3. The core transformation is mathematically non-invertible (e.g., universal offline SQL mutation upcast).
  4. The remaining wedge is reverse-mapping a security control (confused deputy, secret rehydration).
  5. The remaining wedge is "add this to incumbent X" (Veln, ntfy, silo, Pixi, OpenTofu, Cursor, etc.).
  6. Silent mutation of user payloads without an advisory/linter-first path.
  7. Sidecar without host runtime enforcement (third-party lockfile or PATH shim the host does not consult).

- **3-Point Falsification Tests** (All 3 must pass):
  1. A named process or protocol sits where *no incumbent occupies*.
  2. Runtime enforcement *cannot* be reduced to a 50-line script, hook, or wrap.
  3. Three incumbents can still be named, and the gap is *mechanical*, not a missing checkbox.

---

### C. `references/seat-match.md` (Incumbent Classification Taxonomy)
Strict taxonomy preventing category collapse:
- `exact`: Same stack placement and SKU as the proposed v1 (counts toward problem density and exact-mechanics density).
- `adjacent_pain`: Treats the same pain with different mechanics (e.g., Temporal eliminating saga race conditions via durable orchestration vs. a Kafka wire-protocol DPOR proxy).
- `language_scoped`: Identical idea, but restricted to an in-process language runtime (e.g., Loom/Shuttle in Rust vs. language-agnostic broker proxy).
- `wrong_substrate`: Same slogan, different data plane (e.g., Vitess MySQL sharding vs. vanilla RDS Postgres cutover).
- `obsolete`: Abandoned or legacy software (e.g., 2015 Azure Split-Merge).
- `price_packaging`: Incumbent exists in nearby enterprise tier; access, price, or lock-in may still leave an opening (e.g., Antithesis hypervisor vs. lightweight CI proxy).
- **Rule of Strictest Mismatch**: If two labels could apply, select the stricter mismatch (prefer `wrong_substrate` / `adjacent_pain` over `exact`).

---

### D. `references/deny-patterns.md` (Self-Contained Deny Catalog)
- **Closed Aisles (Embedded Catalog)**:
  - Phone notifiers for local/CI tasks (`ntfy`, `Pushover`).
  - Localhost tunnels & OAuth companions (`ngrok`, `Cloudflare named tunnels`, `Dev Tunnels`).
  - Worktree loopback isolation (`silo`).
  - Sidecar locks without host enforcement (`tofulock`, `pio-lock`, `red-widow`).
  - Advisory prompt-cache inspectors & vendor API contract drift tools (`Optic`, `Prism`, `oasdiff`, `cachelens`).
- **External Deny-List Resolution**:
  - If target workspace has `docs/adr/0001-no-pitchable-candidate.md`, treat its killed-seats tables as authoritative.
  - If missing, use embedded catalog and flag `deny_catalog: embedded_baseline`.

---

### E. `references/search-playbook.md` (Mechanics-First Discovery)
- **Query Construction Strategy**:
  - Search stack nouns + protocols: `wire protocol proxy`, `eBPF tc filter`, `AST collision queue`, `DPOR interleaving test`.
  - Avoid value-prop marketing queries: `"best AI testing tool"`, `"developer productivity automation"`.
- **Incumbent Extraction Rules**:
  - Minimum 5 named incumbents per evaluated candidate.
  - Each entry must feature: Name, verified URL, exact quotation from docs/README, seat-match label, and remaining leftover.
  - Any 404 or unverified fetch must be marked `NEED_EVIDENCE`; hallucinations are strictly disallowed.

---

### F. `references/calibration.md` (Anchoring Benchmark Cases)
- **SymMerge (ADR 0002) — Gold KILL**: Bundled 3 occupied slices (SemaMerge + Trunk queues + Copilot conflict bots). Lesson: A bundle of occupied tools is Occupied, not Sparse.
- **TenantScale — Gold CLAIM-Kill**: Claimed `<10ms` cryptographic checksum of whale tenants. Lesson: Kill the physical claim, but re-score the actual architectural cutover slices without auto-marking the entire seat as Occupied.
- **SagaGuard (ADR 0003) — Gold Nuance**: Kroxylicious is `exact` for the proxy slice; Temporal is `adjacent_pain`. Result: `as_oss` viable, `as_company` occupied leftover.
- **Steelman Discipline**: If initial thinking estimates occupancy at 5–6, published exact-mechanics score cannot be 8–9 without citing new named incumbent rows.

---

### G. `references/output-template.md` (Standard Schema)
```yaml
candidate_seat: <One-line technical description of the stack position>
decision: PITCH | KILL | NEED_EVIDENCE | FILE_ON_X

verdicts:
  as_company: <band> <0-10>
  as_oss: <band> <0-10>
  as_plugin: <band> <0-10>

density_scores:
  problem_density: <0-10> (counts adjacent_pain)
  exact_mechanics_density: <0-10> (counts exact only; must be <= steelman ceiling)

incumbents:
  - name: <Tool Name>
    url: <Verified URL>
    quote: "<Direct quote from documentation>"
    seat_match: exact | adjacent_pain | language_scoped | wrong_substrate | obsolete | price_packaging
    leftover: <What is missing if this row is exact>

auto_rejects_fired: [] # List triggered rules (1-7)
falsification:
  1_vacant_process: pass | fail
  2_not_a_wrapper: pass | fail
  3_mechanical_gap: pass | fail

steelman:
  occupancy_ceiling: <0-10>
  why_build: "<Strongest argument for building>"

v1_as_shipped: "<Concrete v1 deliverables and stack placement>"
claim_hygiene: ok | unsourced | implausible
file_on: <Incumbent repo/issue URL, or 'none'>
deny_catalog: embedded_baseline | local_adr_0001
```

---

## 3. Step-by-Step Build Sequence

1. **Step 1: Create References Directory**
   - Create `references/` subdirectory in `profinder/`.
2. **Step 2: Scaffold Core Criteria References**
   - Write `references/rubric.md` (scoring bands, auto-rejects, falsification).
   - Write `references/seat-match.md` (taxonomy and rules).
   - Write `references/deny-patterns.md` (embedded closed aisles and ADR 0001 pointers).
3. **Step 3: Scaffold Hunting & Benchmarking References**
   - Write `references/calibration.md` (SymMerge, TenantScale, SagaGuard, false exacts).
   - Write `references/search-playbook.md` (mechanical hunting rules and incumbent schema).
   - Write `references/output-template.md` (YAML schema + checklist).
4. **Step 4: Scaffold `SKILL.md` Entrypoint**
   - Write `SKILL.md` with standard frontmatter, dual-mode flow, and strict load order.
5. **Step 5: Verification & Dry-Run Validation**
   - Validate YAML frontmatter and relative markdown links.
   - Run dry-run on known `FILE_ON_X` case (`ntfy --wait-cmd`). Verify: auto-reject 1/5 triggers.
   - Run dry-run on known `KILL` case (SymMerge AST bundling). Verify: bundle rule flags Occupied.

