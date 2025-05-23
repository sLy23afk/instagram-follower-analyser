# instagram-follower-analyser
# 📸 Instagram Follower Analyzer

> I got bored and made this... so here's a Python script that tells you who unfollowed you, who you're following but they’re not following you back, and your fans (people who follow you but you don't follow back). It works locally — no API, no login, just vibes.

---

## 💡 What This Does

- 📥 Takes Instagram’s `followers.json` and `following.json` export files
- 🔍 Analyzes:
  - Who **you follow** but **don’t follow you back**
  - Who **follows you**, but **you don't follow back** (aka *your fans*)
  - People who have **unfollowed you recently**
- 📊 Displays a clean summary in the terminal (with a table!)
- 🧾 Exports a detailed `.csv` file for your records

---

## 🧠 Why I Made This

> Just bored. Wanted to mess with some JSON and practice Python.

---

## 🛠️ Tech Used

- Python 🐍 (of course)
- `tabulate` – for the clean terminal table
- `csv` – for exporting results
- Basic Python libraries (`json`, `os`, etc.)

---

## ⚙️ Setup & How to Run

### 1. Download your Instagram data:
> Go to **Instagram Settings → Your Activity → Download Your Information**, and request a copy in **JSON** format.

From the downloaded folder:
- Grab `followers_1.json`
- Grab `following.json`
- Grab `recently_unfollowed_profiles.json`

Place all the three files into the same folder
