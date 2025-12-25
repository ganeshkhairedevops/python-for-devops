import requests
import json

def fetch_posts():
    url = "https://jsonplaceholder.typicode.com/posts" # API endpoint for fetching posts
    response = requests.get(url) # Fetch the data
    data = response.json() # Parse the JSON response
    data = response.json()   # Parse JSON response

    posts = []

    for post in data[:12]:    # Take only first 12 posts
        posts.append({
            "id": post["id"],
            "title": post["title"],
            "userId": post["userId"]
        })

    return posts
def save_to_file(posts): 
    with open("output.json", "w") as file: # Open file in write mode
        json.dump(posts, file, indent=4) 


def main():
    posts = fetch_posts()

    print("Fetched Posts:\n")
    for post in posts:
        print(f"ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"User ID: {post['userId']}")
        print("-" * 30)

    save_to_file(posts)
    print("\nData saved to output.json") 


main()
