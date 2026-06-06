import os,csv,json, requests,initial 
OUTPUT_FOLDER = r"C:\Users\Mohan lal\Documents\Python_experiment\Day-3 API requests"

def print_summary(total_posts, most_active_user, max_posts):
    print(f"Total posts fetched: {total_posts}")
    print(f"User with most posts: userId {most_active_user} with {max_posts} posts")

def create_csv(OUTPUT_FOLDER, post_count, total_posts):
    most_active_user = max(post_count, key=post_count.get)
    max_posts = post_count[most_active_user]
    
    with open(os.path.join(OUTPUT_FOLDER,"user_post_summary.csv"),"w",newline="") as f:
        writer = csv.DictWriter(f,fieldnames=["user_id","total_posts"])
        writer.writeheader()
        for user_id, count in post_count.items():
            writer.writerow({"user_id":user_id, "total_posts": count})
    print_summary(total_posts, most_active_user, max_posts)

def fetch_posts(OUTPUT_FOLDER):
    total_posts = 0
    post_count = {}
    page = 1
    while True:
        response = requests.get("https://jsonplaceholder.typicode.com/posts", params={"_page": page, "_limit": 10})
        response.raise_for_status()
        
        posts = response.json()
        if not posts:
            break
        # print(type(posts))
        for post in posts:
            post_count[post["userId"]] = post_count.get(post["userId"],0) + 1
        
        total_posts += len(posts)
        page += 1
    create_csv(OUTPUT_FOLDER, post_count,total_posts)

def main():
    # print("fetching posts...")
    os.makedirs(OUTPUT_FOLDER,exist_ok=True)
    fetch_posts(OUTPUT_FOLDER)
    
if __name__ == "__main__":
    # print(__name__)
    main()
