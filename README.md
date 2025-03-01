# Google Dorking Recon Bot

- Overview

Google Dorking Recon Bot automates reconnaissance using Google Dorks to find:
✅ Exposed directories and sensitive files

✅ Admin panels and login pages

✅ WordPress configuration files

✅ Subdomains using Google search queries

This tool helps penetration testers and bug bounty hunters quickly discover security risks.

---

- Features

Automated Google Dorking – Finds sensitive files, admin pages, and subdomains

Headless Mode – Runs without opening a browser for efficiency

Dynamic Search – User provides a domain, and the bot finds related security risks

Customizable Dork Queries – Expand the bot with new search queries

---

- Installation

1. Clone the Repository

   		git clone https://github.com/Jay4you/GoogleDorkReconBot.git

  		cd GoogleDorkReconBot

3. Create a virtual enviroment and Install Dependencies:
python3 -m venv myenv
   
    	source myenv/bin/activate  # On Linux/macOS
     
    	myenv\Scripts\activate     # On Windows
   
    	pip install -r requirements.txt

5. Check Your Google Chrome Version:
   
        google-chrome --version # On Linux/macOS
        chrome --version # On Windows
        # You'll see something like: Google Chrome 120.0.6099.110

   	If not available, download :
		On Kali Linux / Debian-based Systems

		wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
		sudo apt install ./google-chrome-stable_current_amd64.deb

7. Download the matching ChromeDriver and version for your operating system from [here](https://chromedriver.chromium.org/downloads/)

8. Extract & Place in Project Folder

    Windows:
      Extract the chromedriver.exe and move it to the GoogleDorkReconBot folder.
   
    Linux/macOS:
   
      	mv chromedriver GoogleDorkReconBot/
      	chmod +x GoogleDorkReconBot/chromedriver  # Make it executable

---

- Usage

Run the bot and enter a target domain:

	python dork_recon.py

Example input:

Enter the target domain (e.g., example.com): netflix.com

Example output:

	Admin Panels
	1. Netflix Admin Login - https://netflix.com/admin
	2. Secure Dashboard - https://secure.netflix.com/admin
	
	WordPress Config
	No results found.
	
	Subdomains
	1. support.netflix.com
	2. api.netflix.com

---

- To-Do List

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
