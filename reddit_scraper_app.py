import streamlit as st
import praw

# Streamlit App Title
st.title("Reddit HFY Stories Scraper")

# Step 1: Set up Reddit API credentials
reddit = praw.Reddit(
    client_id="TyArbdXtwLsUq7sNU1QhcQ",  # Replace with your client ID
    client_secret="9fk9HQR9LsLta5e9pbexKpIRVCCE4A",  # Replace with your client secret
    user_agent="Reddit Scraper (by u/Hasanaries07)"  # Replace with your Reddit username
)

# Input Fields
limit = st.number_input("Enter Number of Stories to Fetch (1-50):", min_value=1, max_value=50, value=5)

# Step 2: Fetch HFY Stories
if st.button("Fetch Stories"):
    try:
        subreddit = reddit.subreddit("HFY")  # Access the Humanity F*** Yeah subreddit
        stories = subreddit.hot(limit=limit + 2)  # Fetch extra to account for skipped posts

        count = 0
        for story in stories:
            # Skip pinned posts or specific titles
            if story.stickied or story.title in ["Content Theft", "Looking for Story Thread #262"]:
                continue

            # Display the story
            st.subheader(story.title)  # Show the story title
            st.write(f"**Text:** {story.selftext[:200]}...")  # Show the first 200 characters of the story
            st.write(f"[Read More]({story.url})")  # Add a link to the full story
            st.write(f"**Upvotes:** {story.score}, **Comments:** {story.num_comments}")
            st.write("-" * 50)

            count += 1
            if count >= limit:  # Stop when we've displayed the desired number of stories
                break
    except Exception as e:
        st.error(f"An error occurred: {e}")
