# NOTES KNOWLEDGE BASE

## OVERVIEW
`notes/` is the human-facing synthesis layer. Files here should help a future reader understand sources, conclusions, scope, and comparison logic quickly.

## WHERE TO LOOK
| Task | Location | Notes |
|------|----------|-------|
| Start the corpus | `latest-rail-plans-index.md` | Curated official-link index |
| Understand workflow and prior findings | `urban_rail_notes.md` | Operator memo with methods and results |
| Understand planning distinctions | `rail-plan-comparison.md` | Legal and conceptual comparison |
| Read extracted Busan summary text | `busan_rail_summary.txt` | Raw-ish text outlier inside notes |

## CONVENTIONS
- Prefer Markdown for synthesized notes.
- Use clear H1/H2 structure and numbered sections when the document is analytical.
- Include explicit links to official sources and state confirmation scope where relevant.
- Use conservative wording when certainty matters: note what is confirmed, latest, provisional, or excluded.
- Keep notes readable without needing to open captures or archives first.

## ANTI-PATTERNS
- Do not turn `notes/` into a dump for raw UI captures, logs, or machine snapshots.
- Do not rely on stale absolute paths outside `rail-research/` when an in-project path exists.
- Do not state conclusions without linking back to source notes, manifests, or official URLs.
- Do not create duplicate raw extracts here when the same artifact already lives in `archives/railtmp/`.

## NOTES
- `busan_rail_summary.txt` is currently an exception: useful, but closer to extracted source text than polished note style.
- If more raw extracts accumulate, consider moving them to `archives/railtmp/` or another explicit extracted-text area instead of expanding this pattern.
