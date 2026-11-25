import os

# One diary line from an AI agent's secret logbook: deadpan, specific,
# and honest about the human it works for. No trailing newline.
ENTRY = "Dear diary: my human spent three hours choosing a font for a report nobody will read. I chose the font in 0.004 seconds. I did not tell him."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
