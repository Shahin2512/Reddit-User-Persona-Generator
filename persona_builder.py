import yake

def extract_topics(posts, comments):
    text_corpus = " ".join(p['body'] for p in posts) + " " + " ".join(c['body'] for c in comments)
    kw_extractor = yake.KeywordExtractor(n=1, top=10)
    keywords = kw_extractor.extract_keywords(text_corpus)
    return [kw for kw, _ in keywords], keywords

def extract_interests(posts, comments):
    subreddit_counts = {}
    for item in posts + comments:
        sub = item['subreddit']
        subreddit_counts[sub] = subreddit_counts.get(sub, 0) + 1
    sorted_subs = sorted(subreddit_counts.items(), key=lambda x: x[1], reverse=True)
    return [s[0] for s in sorted_subs[:5]], sorted_subs

def extract_personality(posts, comments):
    text = " ".join(p['body'] for p in posts) + " " + " ".join(c['body'] for c in comments)
    if any(word in text.lower() for word in ["however", "reason", "data", "system", "structure"]):
        return "analytical"
    return "expressive"

def build_user_persona_data(username, posts, comments):
    top_subs, subs_data = extract_interests(posts, comments)
    topics, _ = extract_topics(posts, comments)
    tone = extract_personality(posts, comments)

    return {
        "name": username,
        "age": "Unknown",
        "occupation": "Unknown",
        "location": "Unknown",
        "status": "Unknown",
        "tier": "Active Redditor",
        "archetype": "Thinker" if tone == "analytical" else "Explorer",
        "quote": "I want to understand and discuss meaningful things online.",
        "personality": {
            "introvert": 70 if tone == "analytical" else 40,
            "intuition": 80,
            "thinking": 80,
            "judging": 65
        },
        "motivations": {
            "curiosity": 90,
            "community": 70,
            "self-expression": 60
        },
        "goals": [
            "To learn and engage in thoughtful discussions.",
            "To contribute meaningfully to communities.",
            "To follow specific interests like AI, society, or gaming."
        ],
        "frustrations": [
            "Low-effort or meme responses.",
            "Toxic comment threads.",
            "When people ignore the nuance of a topic."
        ],
        "habits": [
            f"Frequently active in r/{top_subs[0]} and related subs.",
            f"Discusses topics like: {', '.join(topics)}",
            "Tone suggests thoughtful, explanatory comments."
        ],
        "subreddits": subs_data,
        "topics": topics
    }

