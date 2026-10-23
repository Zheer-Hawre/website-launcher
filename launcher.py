import webbrowser
import time

# 1. Define the list of websites you want to open
# Change these to your favorite websites (include the https:// part)

websites = [
    "https://github.com",
    "https://gmail.com",
    "https://youtube.com",
    "https://labex.io/learn/linux",
    "https://chatgpt.com/"
]
print("Launching your digital workspace...")

# 2. Loop through the list and open each one
for index, url in enumerate(websites):
    if index == 0:
        # Open the first website in a brand new browser window
        webbrowser.open_new(url)
    else:
        # Open the rest of the websites in new tabs within that same window
        webbrowser.open_new_tab(url)

    # A tiny 0.5-second pause gives Ubuntu a moment to process each tab cleanly
    time.sleep(0.5)

print("All sites launched! Have a productive session.")

