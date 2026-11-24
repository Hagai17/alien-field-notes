"""Write one alien tourist's review of Earth to /output/entry.txt.

The line is a single line of at most 200 characters: a review of planet
Earth left by an alien tourist, written like a real travel review --
verdict, amenities, complaints and all.
"""

import os

LINE = (
    "Checked in for two days, stayed for the eclipses. Pros: breathable "
    "air, dramatic tides, cheese. Cons: the apex species pays rent to "
    "live on its own planet. Overall 8/10, would abduct again."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
