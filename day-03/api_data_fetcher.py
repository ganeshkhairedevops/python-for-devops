import requests 
import json #For handling JSON data


def fetch_posts():
    url = "https://jsonplaceholder.typicode.com/posts" #Fetch posts from JSONPlaceholder API
    try:# Improved error handling
        response = requests.get(url, timeout=5) # Added timeout for better error handling
        response.raise_for_status()   # Handles 4xx / 5xx errors
        return response.json()

    except requests.exceptions.RequestException as error:# Catch all request-related exceptions
        print("Error while calling API:", error)
        return []

# Process the fetched posts
def process_posts(posts):
    """
    Extract meaningful data from API response
    """
    processed_data = []
    # Limit to first 50 posts for brevity
    for post in posts[:50]:
        processed_data.append({
            "id": post.get("id"),
            "title": post.get("title"),
            "user_id": post.get("userId")
        })

    return processed_data 

# Save processed data to a JSON file
def save_to_json(data, filename="output.json"):
    """
    Save processed data to a JSON file
    """
    try:# Improved file handling with exception management
        with open(filename, "w") as file: # Open file in write mode
            json.dump(data, file, indent=4)
        print(f"\nData successfully saved to {filename}")

    except IOError as error:
        print("File write error:", error)

# Main function to orchestrate fetching, processing, and saving data
def main():
    posts = fetch_posts()

    if not posts:
        print("No data fetched. Exiting safely.")
        return

    processed_posts = process_posts(posts)

    print("\nFetched Posts:\n")
    for post in processed_posts:
        print(f"ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"User ID: {post['user_id']}")
        print("-" * 30)

    save_to_json(processed_posts)


if __name__ == "__main__":
    main()
