# GitHub + Git, start to finish

I can't create the GitHub account for you — it needs your own email and password, same as any account —
but here's the whole path from zero to a live portfolio repo. It's about 20 minutes the first time,
5 minutes every time after.

## 1. Create your GitHub account (2 min)

1. Go to [github.com](https://github.com) → **Sign up**.
2. Use a professional-looking username — recruiters will see it. `monicaaspiras` or `nica-aspiras` reads
   better than something cutesy. You can't easily change it later without breaking links, so pick it once.
3. Verify your email.

## 2. Install git on your Mac (2 min)

Open **Terminal** and run:

```
git --version
```

If it's not installed, macOS will prompt you to install the Xcode Command Line Tools — click install and
wait a couple minutes. Re-run `git --version` to confirm.

## 3. Tell git who you are (one-time, 1 min)

```
git config --global user.name "Monica Aspiras"
git config --global user.email "the-email-you-used-for-github@example.com"
```

## 4. Create the repo on GitHub (2 min)

1. On github.com, click the **+** in the top right → **New repository**.
2. Name it something specific, not generic: `airline-delay-sql-analysis`, not `project1`.
3. Add a short description (you can paste the first line of the README's business question).
4. Leave it **Public** — the whole point is recruiters can see it.
5. Do **not** check "Add a README" — you already have one, and it'll conflict.
6. Click **Create repository**. Leave the page open — it shows you the exact commands for step 5.

## 5. Push this project folder up (5 min, first time)

In Terminal, `cd` into the project folder, then:

```
git init
git add .
git commit -m "Initial commit: project scaffold and README"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/airline-delay-sql-analysis.git
git push -u origin main
```

The first push will ask you to sign in — it'll open a browser window to authenticate. Follow that prompt
once and you won't see it again on this machine.

## 6. The 4 commands you'll use for every update after this

This is genuinely the whole loop. You will use these four commands for the rest of your data career:

```
git add .                      # stage your changes
git commit -m "what you did"   # save a checkpoint with a message
git push                       # send it to GitHub
git status                     # anytime, to see what's changed / staged
```

Write a real commit message every time — `"added join query for carrier delay by airport"`, not
`"update"`. Interviewers occasionally click into commit history; it's a small signal, but it's the kind
of small signal that adds up.

## What to say about this if it comes up in an interview

"I version-controlled the project with git and pushed it to GitHub" is a real, legitimate thing to say —
plenty of candidates at your level haven't done even this much. You don't need to oversell it, but don't
undersell it either.
