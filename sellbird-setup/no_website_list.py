"""List the businesses Sellbird found that have no website, with phone numbers.

These can't be emailed (with no website there's no address to find), but they
are the businesses most likely to want one. Call them or visit.

Run it from your Sellbird folder, with Sellbird's .venv active:

    python ../nightdesk-paper/sellbird-setup/no_website_list.py

It writes no_website.csv in the Sellbird folder. It only reads Sellbird's
database and changes nothing.
"""

import csv
import sqlite3
import sys
from pathlib import Path

try:
    from sellbird.state import DB_PATH
except ImportError:
    sys.exit("Sellbird isn't installed here. Activate Sellbird's .venv first "
             "(see SETUP.md, step 2), then run this again.")

OUT = Path("no_website.csv")


def main() -> int:
    if not Path(DB_PATH).exists():
        print(f"No Sellbird database yet at {DB_PATH}. Run `sellbird discover` first.")
        return 1
    db = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    rows = db.execute(
        """SELECT name, phone, industry, location, source_url
           FROM companies
           WHERE COALESCE(domain, '') = '' AND COALESCE(name, '') != ''
           ORDER BY location, industry, name"""
    ).fetchall()
    db.close()
    with OUT.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["business", "phone", "type", "area", "listing"])
        writer.writerows(rows)
    with_phone = sum(1 for r in rows if (r[1] or "").strip())
    print(f"\n  {len(rows)} businesses with no website ({with_phone} with a phone number)"
          f"\n  written to {OUT.resolve()}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
