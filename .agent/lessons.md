# Lessons Learned

## 2026-03-24

- **Never remove data without explicit consent.** When user says a list count is wrong, ask which item to remove — don't guess. (User was angry when I silently dropped a team member.)

- **Use "tôi" not "em" in Vietnamese writing.** User considers "em" weak and submissive. Always use assertive, confident tone in all Vietnamese academic text.

- **Always deep research before drafting academic content.** Don't write opinion/analysis based on surface-level knowledge. Spawn a research agent first, get real facts and scholarly sources, then draft. The user called out a generic draft that wasn't grounded in verified knowledge.

- **Use gcloud auth on this machine for Google APIs.** Don't waste time extracting OAuth tokens from browser sessions — `gcloud auth print-access-token` is right there.
