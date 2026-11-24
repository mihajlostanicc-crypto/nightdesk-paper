# Sellbird setup: websites for small businesses in Serbia

[Sellbird](https://github.com/ethanplusai/sellbird) finds local businesses,
finds who runs them, writes each one a short personal email, sends it from your
Gmail and drafts answers to the replies. It runs on your own computer and uses
your Claude subscription to write.

This folder holds your settings, ready to drop into Sellbird:

| File | What it is |
|---|---|
| `sellbird.local.yaml` | Your settings: who you are, what you sell, who to email, how much to send |
| `skills/product_knowledge.md` | What Sellbird knows about your service, and the rules for writing in Serbian |
| `check_email.py` | Checks that Sellbird can sign in to your Gmail |
| `no_website_list.py` | Lists the businesses found with no website, with phone numbers, to call or visit |

## What's already set up

| | |
|---|---|
| **You sell** | Simple, mobile-friendly websites for small local businesses, under $500, fixed price |
| **Free offer in every first email** | A free draft of how their new homepage could look |
| **Who to email** | Hair and beauty salons, nail salons, barbers, gyms, restaurants, cafes, bakeries, hotels, dental practices, physiotherapy, vet clinics |
| **Where** | Beograd, Novi Sad, Niš, Kragujevac |
| **Language** | Serbian, Latin script, formal "Vi" |
| **Style** | A professional salesman: polished, confident, courteous, never pushy. Leads with what the owner gains and ends with one clear next step |
| **Sales path** | Free homepage draft, then a 15-minute call to go through it, then a fixed price and a start date |
| **Sending** | From your Gmail, at most 20 cold emails a day, weekdays 9:00 to 17:00 Belgrade time |
| **Approval** | Nothing is sent until you approve it in the Outbox |
| **Opt-out line** | "Ako Vas ovo ne zanima, samo odgovorite STOP i neću Vam više pisati." A reply of STOP is honoured at once. |

Change any of it in `sellbird.local.yaml`. It's a plain text file with a note
on every setting.

> **Read the legal note at the end before you send.** Serbian law on email
> advertising is stricter than US law.

---

## What you need

- A computer (Windows, Mac or Linux) that is on during the working day. Sellbird
  only works while it's running.
- **Python 3.11 or newer**: [python.org/downloads](https://www.python.org/downloads/).
  On Windows, tick "Add python.exe to PATH" in the installer.
- **Git**: [git-scm.com/downloads](https://git-scm.com/downloads).
- **A Claude Pro or Max plan.** Sellbird writes with the Claude Code app on
  your computer, using your plan. It has no separate AI bill.
- **Your Gmail address**, with 2-Step Verification turned on (step 4).

In the steps below, run each command in a terminal: **Terminal** on Mac,
**PowerShell** on Windows.

## Step 1: Install Claude Code and sign in

Mac or Linux:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Windows (PowerShell):

```powershell
irm https://claude.ai/install.ps1 | iex
```

Then run `claude`, sign in with your Claude account when it asks, and type
`/exit` to leave.

## Step 2: Download Sellbird and add your settings

Run these one after another, in a folder where you keep projects:

```bash
git clone https://github.com/ethanplusai/sellbird.git
git clone -b claude/sellbird-setup-7mtc2i https://github.com/mihajlostanicc-crypto/nightdesk-paper.git
```

Copy your settings into Sellbird, then install it.

Mac or Linux:

```bash
cp nightdesk-paper/sellbird-setup/sellbird.local.yaml sellbird/
cp nightdesk-paper/sellbird-setup/skills/product_knowledge.md sellbird/skills/
cd sellbird
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

Windows (PowerShell):

```powershell
copy nightdesk-paper\sellbird-setup\sellbird.local.yaml sellbird\
copy nightdesk-paper\sellbird-setup\skills\product_knowledge.md sellbird\skills\
cd sellbird
py -m venv .venv
.venv\Scripts\activate
pip install -e .
```

On a Mac, if `python3 --version` says 3.9, install Python 3.13 from
python.org and use `python3.13` instead of `python3`.

From now on, every time you open a new terminal for Sellbird, go into the
`sellbird` folder and activate it again first: `source .venv/bin/activate` on
Mac or Linux, `.venv\Scripts\activate` on Windows.

## Step 3: Add your name and email

Open `sellbird/sellbird.local.yaml` in any text editor (Notepad, TextEdit,
VS Code). Near the top, fill in the three empty values:

```yaml
persona:
  name: "Marko"                    # your first name: it signs every email
  company: "Marko Web Studio"      # your business name, or your full name
  ...
  email: "you@gmail.com"           # the Gmail address you send from
```

They were left empty in this repo because the repo is public.

Just below them, `tone` tells Sellbird to write with masculine verb forms
("pogledao sam"). Serbian verbs follow the writer's gender, so if you're a
woman, follow the note above `tone` to switch to feminine forms.

Also check `key_benefits` and `objection_responses` under `product:`. Sellbird
uses them in follow-ups and replies, so they should match what you really offer.

## Step 4: Connect your Gmail

Sellbird sends through Gmail's own mail servers with an **app password**: a
separate 16-letter password that only Sellbird uses. You can revoke it at any
time without changing your real password.

1. Turn on 2-Step Verification: [myaccount.google.com/security](https://myaccount.google.com/security).
2. Create an app password: [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords).
   Name it `Sellbird` and copy the 16 letters it shows.
3. In the `sellbird` folder, create your `.env` file from the example:
   `cp .env.example .env` (Windows: `copy .env.example .env`).
4. Open `.env` in a text editor and fill in these lines (they're already there,
   empty, under "Option B"):

   ```
   SMTP_HOST=smtp.gmail.com
   SMTP_PORT=587
   SMTP_USERNAME=you@gmail.com
   SMTP_PASSWORD=abcdabcdabcdabcd
   IMAP_HOST=imap.gmail.com
   IMAP_PORT=993
   ```

   Use your Gmail address and the app password, with no spaces. `.env` stays
   on your computer. Never commit it or paste it anywhere.
5. Check it works:

   ```bash
   python ../nightdesk-paper/sellbird-setup/check_email.py
   ```

   (Windows: `python ..\nightdesk-paper\sellbird-setup\check_email.py`.) It should print `OK`.

Good to know:

- **Why not Sellbird's "gmail" option?** It needs a Google Cloud project, and on
  a personal @gmail.com account Google signs it out every 7 days. The app
  password doesn't expire.
- **Sellbird marks unread emails in your inbox as read** when it checks for
  replies. If you use this Gmail for personal mail too, unread emails will
  look read.
- **A personal Gmail can only send a little cold email before it lands in
  spam.** That's why the limit is 20 a day. Raise `max_daily_sends` slowly, and
  only while replies come in and nothing bounces.

## Step 5: Add two free keys

Both go in `.env`, the same way as above. Both are free and need no card.

1. **An email checker. Required:** without one, Sellbird never sends anything,
   because it can't tell a real address from a guess.
   Sign up at [reoon.com/email-verifier](https://reoon.com/email-verifier)
   (600 free checks a month), open API, copy the key into `REOON_API_KEY=`.
2. **A business search:** sign up at [serper.dev](https://serper.dev)
   (2,500 free Google searches), copy the API key into `SERPER_API_KEY=`.

   You need it because Sellbird's built-in free source (OpenStreetMap) only
   knows a few business types, such as dentists and plumbers, and not salons,
   gyms or restaurants.

## Step 6: Find businesses

```bash
sellbird signals --confirm free
sellbird signals --confirm EMAIL_STATUS
sellbird discover --provider serper --estimate
sellbird discover --provider serper
```

The first two let Sellbird collect the free facts about each business (what
its site is missing) and check email addresses with Reoon. The
`--estimate` line shows the 48 searches it will run (12 business types × 4
cities) without running them. The last line runs them, using about 48 of your
2,500 free searches.

**Businesses with no website at all** don't turn up in a Google search like
this, and have no email address to find, but they're your best customers.
To list them with phone numbers so you can call or visit, add a
[DataForSEO](https://app.dataforseo.com/api-access) account ($1 free credit;
the login and the API password it generates go in `DATAFORSEO_LOGIN=` and
`DATAFORSEO_PASSWORD=`), then:

```bash
sellbird discover --provider dataforseo_maps --estimate
sellbird discover --provider dataforseo_maps
python ../nightdesk-paper/sellbird-setup/no_website_list.py
```

The last line writes `no_website.csv`: every business found with no website,
with its phone number (Windows: `python ..\nightdesk-paper\sellbird-setup\no_website_list.py`).
`sellbird companies` writes a spreadsheet of every business found and why each
one was or wasn't emailed.

## Step 7: Start Sellbird and approve emails

Open **two** terminals, go into the `sellbird` folder in each and activate it
(step 2).

In the first one, open the dashboard:

```bash
sellbird dashboard
```

It prints a private link starting `http://127.0.0.1:5555/#token=`. Open it in
your browser. Don't share it: it unlocks your dashboard.

In the second one, start Sellbird:

```bash
sellbird run
```

Every 15 minutes it reads the businesses' websites, finds who runs them,
checks their addresses and writes emails. New emails wait in the dashboard's
**Outbox**. For each one, before you approve it:

- **Read it as the owner would.** It should sound like a normal person from
  Serbia. Fix the wording or reject it if it doesn't.
- **Check what it says about their site is true.** Open their site on your
  phone. Sellbird read one page automatically and can be wrong, for example
  about a booking button that loads late.

Only approved emails are sent, inside the daily limit and the 9:00 to 17:00
window. When someone writes back, Sellbird drafts an answer and it waits in
the Outbox too.

When someone says **yes** to the free draft, Sellbird marks them "Said yes to
your offer", stops their follow-ups and drafts a short thank-you that asks
for what you need to make it. Making the draft and sending it are up to you:
send it with a suggestion of a 15-minute call to go through it. When they
answer with interest, Sellbird's replies ask when a call suits them, and
closing the deal on the call is yours.

On Mac or Windows, `sellbird tray` puts a Sellbird icon in the menu bar or
system tray to start and stop it, and `sellbird autostart install` starts that
icon when you log in.

## Everyday commands

```bash
sellbird status            # what Sellbird has done so far
sellbird outbox            # emails waiting for you, from the terminal
sellbird sending pause     # stop all sending at once (resume: sending resume)
sellbird export            # every checked address as a spreadsheet (CSV)
sellbird suppressions add someone@example.rs   # never email this address or domain
```

**Stuck?** Open a terminal in the `sellbird` folder, run `claude`, and ask.
Sellbird's own instructions turn Claude Code into its setup guide.

---

## Legal note for Serbia

This is not legal advice. Check with a Serbian lawyer before sending at any
volume.

Serbia's Advertising Act (Zakon o oglašavanju, Articles 62 and 63) is
summarised by legal guides as allowing direct advertising to an identifiable
person only with their **prior consent**, which they can withdraw at any time.
Data protection guides describe an exception for business-to-business
marketing, but the sources found while preparing this setup don't settle
whether an email to a business's own address is covered. Sellbird writes to
owners by name where their site names them, which is the riskier case.

Legal guides found while preparing this (summaries, not the law itself):
[Chambers Advertising and Marketing 2025](https://gpg-pdf.chambers.com/Advertising-and-Marketing-2025/99/),
[Chambers Data Protection and Privacy 2025](https://gpg-pdf.chambers.com/view/158325293/378),
[CMS data protection guide for Serbia](https://cms.law/en/int/expert-guides/cms-expert-guide-to-data-protection-and-cyber-security-laws/serbia),
[DLA Piper data protection guide for Serbia](https://www.dlapiperdataprotection.com/?c=RS&t=law).
Read Articles 62 and 63 of the Act itself (Zakon o oglašavanju, 2016) before relying on this.

How this setup keeps the risk low:

- **Every email waits for your approval.** Leave `require_approval: true`.
- **Low volume:** at most 20 a day, each written to one business, with no
  link in the first email.
- **Every first email offers something free and asks one question**, so it reads
  as one person getting in touch, not as an advert.
- **Every cold email says how to stop**, and any request to stop is honoured
  at once and for good.
- Put clients you already work with, and anyone who has asked not to be
  contacted, in `do_not_contact` or `sellbird suppressions add`.

If you'd rather not email at all, use Sellbird only to build the list: run
steps 1, 2, 5 and 6, then `no_website_list.py`, `sellbird companies` and
`sellbird export`, and call or visit the businesses yourself.
