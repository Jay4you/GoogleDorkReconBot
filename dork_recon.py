import requests
from bs4 import BeautifulSoup
import time

# Define extended Google Dorking queries
DORKS = {
    "Exposed Directories": "site:{} intitle:index.of",
    "Config Files": "site:{} ext:conf | ext:ini | ext:log",
    "Database Files": "site:{} ext:sql | ext:db",
    "Backup Files": "site:{} ext:bak | ext:old | ext:zip | ext:tar",
    "Subdomains": "site:*.{} -www.{}",
    "Admin Panels": "site:{} inurl:admin",
    "WordPress Config": "site:{} inurl:wp-config.php",
    "Admin Directories": "site:{} intitle:admin | inurl:admin",
    "Login Pages": "site:{} inurl:login | inurl:signin"
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Get user input
target_domain = input("Enter the target domain (e.g., example.com): ")

print("\nSearching for sensitive files, admin directories, and subdomains...\n")

# Loop through dorks
for category, dork_query in DORKS.items():
    query = dork_query.format(target_domain, target_domain)
    
    # Use Bing search (replace "Bing" with "Google" if you bypass CAPTCHA)
    url = f"https://www.bing.com/search?q={query}"
    
    response = requests.get(url, headers=HEADERS)
    time.sleep(2)  # Avoid rate-limiting

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        results = soup.select("li.b_algo h2 a")  # Extract search results
        
        print(f"### {category} ###")
        if results:
            for i, link in enumerate(results[:5]):  # Show top 5 results
                print(f"{i+1}. {link.text} - {link['href']}")
        else:
            print("No results found.")
    else:
        print(f"Failed to fetch results for {category}")

    print("\n" + "-"*50 + "\n")

print("Scanning complete.")
