#!/usr/bin/env python3
"""Write a short relaxing text to entry.txt."""

import os

TEXT = """The streetlamp comes on before the sky is dark. It hums once, then holds its light over the bicycle leaning by the gate, and the cat that has claimed the warm step for the evening.

The day is still letting go. A bus sighs past and does not stop. A window opens across the street, a radio finds a slow song, and the window closes again.

The light stays. It catches the first moths as they arrive, one by one, turning in the warm air like dust in a sunbeam that stayed too late.

Nothing else is coming. The street has said what it had to say. There is only the lamp, and the moths still turning in its light. The cat has not moved. It does not need to."""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
