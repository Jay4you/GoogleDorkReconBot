from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

# Set up WebDriver (headless mode for stealth)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in the background
driver = webdriver.Chrome(options=options)

# Get user input
target_domain = input("Enter the target domain (e.g., example.com): ")

print("\nSearching for sensitive files, admin directories, and subdomains...\n")

# Loop through dorks
for category, dork_query in DORKS.items():
    query = dork_query.format(target_domain, target_domain)
    
    # Open Google
    driver.get("https://www.google.com")

    # Enter search query
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    # Wait for results
    time.sleep(3)

    # Extract and print top 5 search result links
    results = driver.find_elements(By.CSS_SELECTOR, "h3")
    links = driver.find_elements(By.CSS_SELECTOR, "div.yuRUbf a")

    print(f"### {category} ###")
    if results:
        for i in range(min(5, len(results))):
            print(f"{i+1}. {results[i].text} - {links[i].get_attribute('href')}")
    else:
        print("No results found.")
    print("\n" + "-"*50 + "\n")

# Close browser
driver.quit()
