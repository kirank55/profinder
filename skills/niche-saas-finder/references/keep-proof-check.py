#!/usr/bin/env python3
"""keep-proof-check.py — mechanical keep-gate for niche-saas-finder cards.

Usage: python3 keep-proof-check.py card1.yaml [card2.yaml ...]

Only cards claiming `as_company` Sparse/Greenfield are gated. Anything
else (Occupied/Saturated/drop/file) reports SKIP: the validator gates
keeps, it never blocks honest drops.

A claimed keep FAILs unless every check below holds against the card
as written. A failing check is `keep_gate: fail`, not an invitation
to relabel rows until it passes.

Exit 0 iff no claimed keep FAILs.
"""

import sys
from urllib.parse import urlparse

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required (pip install pyyaml)", file=sys.stderr)
    sys.exit(2)

SEARCH_CLASSES = ("sor_primitive", "dropin_addon", "commercial_sku",
                  "tracker_leftover")
KEEP_BANDS = ("sparse", "greenfield")
HOST_HINTS = ("help.", "support.", "marketplace.", "docs.")


def band_of(verdict):
    return (verdict or "").strip().split()[0].lower() if verdict else ""


def is_keep(card):
    return band_of((card.get("verdicts") or {}).get("as_company")) in KEEP_BANDS


def host_like(url):
    netloc = urlparse(url or "").netloc.lower()
    return any(h in netloc for h in HOST_HINTS)


def check(card):
    """Return list of failure strings; empty means the keep holds."""
    fails = []
    v = card.get("verdicts") or {}

    if (card.get("keep_gate") or "").strip().lower() != "pass":
        fails.append("keep_gate is not 'pass' on a Sparse/Greenfield claim")

    sc = card.get("search_classes") or {}
    missing = [k for k in SEARCH_CLASSES if not sc.get(k)]
    if missing:
        fails.append(f"G2: search_classes missing keys: {missing}")

    inc = card.get("incumbents") or []
    if len(inc) < 5 and not card.get("could_not_find_5"):
        fails.append(f"G2: {len(inc)} incumbent rows (<5, no could_not_find_5 + why)")
    urls = [str(r.get("url") or "") for r in inc]
    if len(set(urls)) < 4 and len(inc) >= 5:
        fails.append(f"G2: only {len(set(urls))} distinct urls (<4)")

    uncovered = [k for k in SEARCH_CLASSES
                 if not any((r.get("found_via") or "") == k for r in inc)]
    no_via = [r.get("name", "?") for r in inc if not r.get("found_via")]
    if no_via:
        fails.append(f"G2: rows without found_via: {no_via}")
    if uncovered:
        fails.append(f"G2: search classes with zero rows: {uncovered}")

    need_ev = [r.get("name", "?") for r in inc
               if str(r.get("quote") or "").startswith("NEED_EVIDENCE")]
    if need_ev:
        fails.append(f"G1: NEED_EVIDENCE rows on a keep: {need_ev}")

    file_on = str(card.get("file_on") or "none").strip().lower()
    if file_on == "none" and any(host_like(u) for u in urls):
        fails.append("G3: SoR-help/marketplace incumbent with file_on: none")

    rejects = card.get("auto_rejects_fired") or []
    if rejects:
        fails.append(f"auto-reject(s) fired on a keep: {rejects}")

    fals = card.get("falsification") or {}
    for key in ("1_vacant_process", "2_not_a_wrapper", "3_mechanical_gap"):
        if str(fals.get(key) or "").strip().lower() != "pass":
            fails.append(f"falsification {key} is not pass")

    dens = card.get("density_scores") or {}
    steel = card.get("steelman") or {}
    try:
        exact = float(dens.get("exact_mechanics_density", 0))
        ceiling = float(steel.get("occupancy_ceiling", 0))
        if exact > ceiling:
            fails.append(f"G9: exact_mechanics_density {exact} exceeds "
                         f"steelman ceiling {ceiling}")
    except (TypeError, ValueError):
        fails.append("G9: density/ceiling not numeric")

    proof = card.get("keep_proof") or {}
    hit = proof.get("search_class_hit") or {}
    if not proof:
        fails.append("keep_proof block missing")
    else:
        if [k for k in SEARCH_CLASSES if not hit.get(k)]:
            fails.append("keep_proof.search_class_hit must name a row per class")
        if proof.get("need_evidence_rows", 1) != 0:
            fails.append("keep_proof.need_evidence_rows must be 0")
        if str(proof.get("distinct_urls", 0)) != str(len(set(urls))):
            fails.append("keep_proof.distinct_urls must match card urls")
        wpa = str(proof.get("write_path_attempt") or "").strip()
        if not wpa:
            fails.append("keep_proof.write_path_attempt missing")
        elif wpa == "NEED_EVIDENCE":
            fails.append("keep_proof.write_path_attempt unproven (AR7 fires)")

    return fails


def main(paths):
    failed = skipped = held = 0
    for path in paths:
        try:
            with open(path) as fh:
                card = yaml.safe_load(fh) or {}
        except Exception as exc:  # noqa: BLE001 — report, don't crash the run
            print(f"FAIL {path}: unreadable ({exc})")
            failed += 1
            continue
        name = card.get("candidate_seat", path)
        if not is_keep(card):
            print(f"SKIP {name}: not an as_company keep")
            skipped += 1
            continue
        fails = check(card)
        if fails:
            print(f"FAIL {name}:")
            for f in fails:
                print(f"  - {f}")
            failed += 1
        else:
            print(f"HOLD {name}: keep proof complete")
            held += 1
    print(f"\n{held} hold / {failed} fail / {skipped} skip across {len(paths)} cards")
    return 1 if failed else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1:]))
