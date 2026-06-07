import csv,requests,time,os
OUTPUT_FOLDER = r"C:\Users\Mohan lal\Documents\Python_experiment\Day-4_Exception_Handling"


class DataFetchError(Exception):
    pass

def create_csv(output_folder, filename, data):
    # normalize to list
    rows = data if isinstance(data, list) else [data]
    with open(os.path.join(output_folder, f"{filename}.csv"), "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

def failed_url_csv(output_folder, url, error_reason):
    filepath = os.path.join(output_folder, "failed_urls.csv")
    file_exists = os.path.exists(filepath) # Check if file already exists RETURN True/False
    with open(filepath, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["endpoint_url", "error_reasons"])
        if not file_exists:       # ✅ only write header first time
            writer.writeheader()
        writer.writerow({"endpoint_url": url, "error_reasons": error_reason})

def fetch_data(url,max_retries=3):
    for attempt in range(1, max_retries + 1):
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if not data:
                print(f"⚠️ {os.path.basename(url)} - Empty Response")
                failed_url_csv(OUTPUT_FOLDER, url, "Empty data")
                return None
            if isinstance(data, list):
            # multiple records — flatten each one
                flat_data = [
                    {k: v for k, v in item.items() if isinstance(v, (str, int, float, bool))}
                    for item in data
                ]
            else:
            # single record — flatten directly
                flat_data = {k: v for k, v in data.items() if isinstance(v, (str, int, float, bool))}
            return flat_data
        except requests.exceptions.RequestException as e:
            wait = 2 ** attempt
            time.sleep(wait)
    failed_url_csv(OUTPUT_FOLDER, url, "All retries failed")
    raise DataFetchError(f"All retries failed for {url}")

def main():
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts?userId=999",  # returns empty
        "https://jsonplaceholder.typicode.com/invalid",    # 404
        "https://not-a-real-url-xyz.com/data",             # connection error
        ]
    empty = 0
    success = 0
    failed = 0
    for url in urls:
        try:
            data = fetch_data(url)
            if data is None:
                empty += 1
            else:
                create_csv(OUTPUT_FOLDER, os.path.basename(url), data)
                success += 1
        except DataFetchError:
            failed += 1
    
    print(f"Successful fetches: {success}")
    print(f"Empty responses: {empty}")
    print(f"Failed fetches: {failed}")

if __name__ == "__main__":
    main()