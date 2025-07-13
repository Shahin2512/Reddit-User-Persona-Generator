from reddit_scraper import scrape_user_data
from persona_builder import build_user_persona_data
from generate_pdf import render_pdf
import os

if __name__ == "__main__":
    username = input("🔍 Enter Reddit username (not full URL): ").strip()
    posts, comments = scrape_user_data(username)
    
    if not posts and not comments:
        print("❌ No data found.")
    else:
        persona = build_user_persona_data(username, posts, comments)
        os.makedirs("output", exist_ok=True)
        render_pdf(persona, f"output/{username}_persona.pdf")
