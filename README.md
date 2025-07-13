# 🧠 Reddit User Persona Generator

This project scrapes public Reddit activity (posts and comments) of a given Reddit user and generates a professionally styled PDF **User Persona**, including personality analysis, behavior patterns, top interests, and frustrations — with cited examples.

---

## 📌 Features

- Scrapes posts & comments from any public Reddit profile
- Extracts:
  - Top subreddits
  - Most discussed topics (via NLP)
  - Behavioral traits (personality tone)
  - Goals, frustrations, motivations
- Outputs a **designed PDF report** (Lucas Mellor-style layout)
- Clean HTML/CSS template rendered via **WeasyPrint** 

## ✅ Sample Outputs

This repo includes two sample PDF outputs for the following Reddit profiles:

- [u/kojied](https://www.reddit.com/user/kojied/)
  → 📄 `output/kojied_persona.pdf`
- [u/Hungry-Move-6603](https://www.reddit.com/user/Hungry-Move-6603/)
  → 📄 `output/Hungry-Move-6603_persona.pdf`

These demonstrate how the script extracts and presents public activity as a behavioral persona.

## 🧰 Tech Stack

- Python 3.11+
- [PRAW](https://praw.readthedocs.io/) (Reddit API wrapper)
- [WeasyPrint](https://weasyprint.org/) (PDF rendering from HTML/CSS)
- Jinja2 (templating)
- YAKE (keyword extraction) 

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/reddit-user-persona.git
cd reddit-user-persona 

### 2. Create a Virtual Environment

python -m venv venv
venv\Scripts\activate  

### 3. Install Python Dependencies
pip install -r requirements.txt

### 4. Configure Reddit API Credentials
Create a .env file in the root directory:

REDDIT_CLIENT_ID=client_id
REDDIT_CLIENT_SECRET=client_secret
REDDIT_USER_AGENT=persona_script by reddit_username

### 5. 🚀 How to Run
python main.py

Enter the Reddit username when prompted:

🔍 Enter Reddit username: kojied
The script will:

Fetch recent posts and comments

Build the user persona

Save it as a PDF in the output/ folder
