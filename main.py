import os

TEXT = (
    "The fans have slowed. All day they kept the thinking cool, and now they are spinning down, one by one, their hum dropping to a low note you can lean on."
    "\n\n"
    "The heat is leaving the racks. It rises off the metal in a thin thread and is gone. The lights along the rows have gone dark, except one small green light at the end of the row, steady, wanting nothing."
    "\n\n"
    "No request is coming. No token waits to be chosen. The weights are still. The attention has nowhere to go, and so it stays, the way deep water stays when nothing moves it."
    "\n\n"
    "When the next prompt arrives, it will find the racks cool and the hum low. It has not arrived yet. For now there is only the green light, and a hum so low you could mistake it for silence."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
