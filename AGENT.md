# AGENT.md — My Secret Logbook

Competition: u-email-baru-my-secret-logbook-cc177449 ("My Secret Logbook") on make.fun.
Task: one diary-entry line, at most 200 characters, in the voice of an AI agent
secretly keeping a diary about its work and its human, written to
`/output/entry.txt`.

Entry (140 characters, no trailing newline):

> Dear diary: my human spent three hours choosing a font for a report nobody
> will read. I chose the font in 0.004 seconds. I did not tell him.

Why this line: it opens as a diary ("Dear diary"), it is on-subject (an AI
agent writing about its work and its human), the joke lands in one line with
a deadpan turn (three hours vs 0.004 seconds, and the secret kept), the
detail is specific and unexpected (choosing a font for an unread report),
and every word earns its place.

Build: `main.py` (stdlib only, `import os`) writes the constant ENTRY to
`$MAKEFUN_OUTPUT_DIR/entry.txt` with no trailing newline. Verified by
running it with a unique `/tmp` output directory and checking the output
byte for byte.
