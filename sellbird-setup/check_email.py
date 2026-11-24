"""Check that Sellbird can sign in to your Gmail to send and read replies.

Run it from your Sellbird folder, with Sellbird's .venv active:

    python ../nightdesk-paper/sellbird-setup/check_email.py

It signs in over SMTP (sending) and IMAP (reading replies) with the values in
Sellbird's .env, then signs out. It sends nothing and changes nothing.
"""

import asyncio
import sys

try:
    from sellbird.config import load_config, load_env
    from sellbird.integrations.smtp_mail import SmtpImapProvider
except ImportError:
    sys.exit("Sellbird isn't installed here. Activate Sellbird's .venv first "
             "(see SETUP.md, step 2), then run this again.")


def main() -> int:
    config = load_config()
    if config.channels.email.provider != "smtp":
        print("sellbird.local.yaml doesn't use provider: smtp, so this check "
              "doesn't apply. Did you copy it into your Sellbird folder?")
        return 1
    ok, detail = asyncio.run(SmtpImapProvider(config, load_env()).test_connection())
    if ok:
        print(f"\n  OK: Sellbird can send from and read your Gmail. ({detail})\n")
        return 0
    print(f"\n  Not connected: {detail}\n")
    print("  Check SMTP_USERNAME is your full Gmail address and SMTP_PASSWORD is\n"
          "  the 16-letter app password with no spaces (SETUP.md, step 4).\n")
    return 1


if __name__ == "__main__":
    sys.exit(main())
