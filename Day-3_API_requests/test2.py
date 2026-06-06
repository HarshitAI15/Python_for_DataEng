import os,csv,json, requests
# from urllib import response

output_folder = r"C:\Users\Mohan lal\Documents\Python_experiment\Day-3 API requests"
os.makedirs(output_folder,exist_ok=True)

all_posts = []
post_count = {}
for user_id in [1,2,3]:
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts" , params={"userId": user_id})
    response.raise_for_status()
    
    post= response.json()
    all_posts.extend(post)
    post_count[user_id] = len(post)
    
flattened = []
for post in all_posts:
    flat = {
        "user_id": post.get("userId", "N/A"),
        "post_id": post.get("id", "N/A"),
        "title": post.get("title", "N/A")
    }
    flattened.append(flat)
with open(os.path.join(output_folder,"combined_posts.csv"),"w",newline="") as f:
    writer = csv.DictWriter(f,fieldnames=["post_id","user_id","title"])
    writer.writeheader()
    writer.writerows(flattened)

for user_id, count in post_count.items():
    print(f"User {user_id}: {count} posts")
print("Grand Total:", len(all_posts), " posts")