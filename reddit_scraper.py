import praw
import os
from dotenv import load_dotenv

load_dotenv()

def get_reddit_instance():
    return praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT")
    )

def scrape_user_data(username):
    reddit = get_reddit_instance()
    user = reddit.redditor(username)
    posts, comments = [], []

    try:
        for submission in user.submissions.new(limit=50):
            posts.append({
                "title": submission.title,
                "body": submission.selftext,
                "subreddit": str(submission.subreddit),
                "permalink": f"https://www.reddit.com{submission.permalink}"
            })
    except Exception as e:
        print(f"Error fetching posts: {e}")

    try:
        for comment in user.comments.new(limit=50):
            comments.append({
                "body": comment.body,
                "subreddit": str(comment.subreddit),
                "permalink": f"https://www.reddit.com{comment.permalink}"
            })
    except Exception as e:
        print(f"Error fetching comments: {e}")
    
    return posts, comments
