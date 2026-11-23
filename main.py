from pathlib import Path

OUTPUT = Path("/output/entry.txt")

def main():
    text = """Pondlight

Recorded live right at the edge of the pond after midnight. Three of them, no amps, no second takes. Bass sitting low in the water, brushes barely touching the snare, saxophone only coming in when the crickets actually stop. You can hear the reeds. You can hear them waiting on each other. This is just what it sounds like when nobody’s asking them to be anything else."""
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text.strip() + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
