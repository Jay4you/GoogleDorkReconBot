# Google Dorking Recon Bot

Overview

Google Dorking Recon Bot automates reconnaissance using Google Dorks to find:
✅ Exposed directories and sensitive files
✅ Admin panels and login pages
✅ WordPress configuration files
✅ Subdomains using Google search queries

This tool helps penetration testers and bug bounty hunters quickly discover security risks.

---

Features

Automated Google Dorking – Finds sensitive files, admin pages, and subdomains

Headless Mode – Runs without opening a browser for efficiency

Dynamic Search – User provides a domain, and the bot finds related security risks

Customizable Dork Queries – Expand the bot with new search queries

---

Installation

1. Clone the Repository

git clone https://github.com/Jay4you/GoogleDorkReconBot.git
cd GoogleDorkReconBot

2. Install Dependencies

pip install -r requirements.txt

3. Download ChromeDriver

1. Check your Google Chrome version


2. Download the matching ChromeDriver from here


3. Place it in the project folder

---

Usage

Run the bot and enter a target domain:

python dork_recon.py

Example input:

Enter the target domain (e.g., example.com): netflix.com

Example output:

### Admin Panels ###
1. Netflix Admin Login - https://netflix.com/admin
2. Secure Dashboard - https://secure.netflix.com/admin

### WordPress Config ###
No results found.

### Subdomains ###
1. support.netflix.com
2. api.netflix.com

---

To-Do List

✅ Initial bot implementation
⬜ Save results to a file (results.txt or JSON)
⬜ Add proxy support to prevent Google blocks
⬜ Integrate with Nmap/Nuclei for deeper scanning
⬜ Dockerize for easy deployment

---

Legal Disclaimer

⚠️ This tool is for educational and ethical security research purposes only. Do not use it on unauthorized systems. The developer is not responsible for any misuse.

---

Contributions

Pull requests and feature suggestions are welcome! 🚀
