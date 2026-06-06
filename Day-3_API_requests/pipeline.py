import os,csv, requests
OUTPUT_FOLDER = r"C:\Users\Mohan lal\Documents\Python_experiment\Day-3 API requests"

def print_summary(success, failed):
    print(f"Total successful: {success}")
    print(f"Total failed: {failed}")

def create_csv(output_folder, data):
    if not data:
        return
    with open(os.path.join(output_folder, "fetched_posts.csv"), "w", newline="") as f:
        writer = csv.DictWriter(f,fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def fetch_data(endpoint):
    try:
        response = requests.get(endpoint)
        response.raise_for_status()
        endpoint_result = response.json()
        flattened_data = []
        for item in endpoint_result:
            flat_item = {k: v for k, v in item.items() if isinstance(v, (str, int, float))}
            flattened_data.append(flat_item)
        total_records = len(flattened_data)
        create_csv(OUTPUT_FOLDER, flattened_data)
        print(f"✅ {endpoint} — {total_records} records saved")
        return True
    except requests.exceptions.HTTPError as e:
        print(f"❌ {endpoint} — Failed: {e}")
        return False
    except requests.exceptions.ConnectionError as e:
        print(f"❌ {endpoint} — Connection error: {e}")
        return False


def main():
    endpoints = [
    "https://jsonplaceholder.typicode.com/users",
    "https://jsonplaceholder.typicode.com/posts",
    "https://jsonplaceholder.typicode.com/invalid",  # ← this will fail 404
    ]
    success = 0
    for endpoint in endpoints:
        if fetch_data(endpoint):
            success += 1
    print_summary(success, len(endpoints) - success)
        

if __name__ == "__main__":  
    main()  
    
    
    



