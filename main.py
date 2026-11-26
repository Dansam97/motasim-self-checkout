import os

ENTRY = "Twelve yoghurts, no bag, and you looked at me like the beep was personal. It was."

MAX_CHARS = 200  # gate: /output/entry.txt must be 1..200 characters, not only whitespace


def main():
    if not (1 <= len(ENTRY) <= MAX_CHARS) or not ENTRY.strip():
        raise SystemExit(f"entry violates gate: {len(ENTRY)} characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
