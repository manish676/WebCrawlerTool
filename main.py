import scanner
import time

welcome_message = r"""
 __        __   _                            _         
 \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___   
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  
   \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | 
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  

         Welcome to the Web Crawler Tool! 🕸️
       Scan websites and retrieve all linked URLs 🌐
"""

print(welcome_message)
time.sleep(1)

user_input_url = input("🌐 Please enter the target URL to scan: ")
valu_scanner = scanner.Scanner(user_input_url)
corrected_url = valu_scanner.target_url

print("\n🔍 Starting the crawling process... Please wait.\n")

# Start the crawling and scanning process
valu_scanner.crawl(corrected_url)

print("\n✅ Crawling completed! All discovered links have been displayed. Happy crawling! 🚀")
