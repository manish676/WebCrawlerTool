import scanner
import time

# Cool ASCII Art for Welcome Screen
welcome_message = r"""
 __        __   _                            _         
 \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___   
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  
   \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | 
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  
                                                       
         Welcome to the Web Crawler Tool! 🕸️
       Scan websites and retrieve all linked URLs 🌐
"""

# Print the welcome message with a short delay for effect
print(welcome_message)
time.sleep(1)

# Ask the user for the target URL
target_url = input("🌐 Please enter the target URL to scan: ")

# Initialize the scanner with the provided URL
valu_scanner = scanner.Scanner(target_url)

print("\n🔍 Starting the crawling process... Please wait.\n")

# Start the crawling and scanning process
valu_scanner.crawl(target_url)

print("\n✅ Crawling completed! All discovered links have been displayed. Happy crawling! 🚀")
