# Project 1: Website Launcher

### What it is
A one-command "digital workspace" starter. It opens all the websites you use every day in your default browser: the first one in a new window, the rest as tabs in that window.

### Why it's useful
- **Start your day faster**: one command instead of typing five URLs every morning.
- **Different workspaces**: make copies like `study.py`, `work.py`, or `gaming.py`, each with its own list of sites.
- **Run at login**: add it to your startup applications and your tabs are ready when you log in.
- **Learning**: a short example of Python's built-in `webbrowser` module, lists, and loops.

### How it works
1. `websites` is a list of URLs at the top of `launcher.py`.
2. The script loops over the list with `enumerate`:
   - the first URL uses `webbrowser.open_new()` (asks the browser for a new window),
   - the rest use `webbrowser.open_new_tab()`.
3. `time.sleep(0.5)` waits half a second between sites so the browser can open each tab cleanly.

Whether you actually get a *new window* depends on your browser and whether it's already open. Some browsers always open a tab instead.

### Requirements
Python 3 only. `webbrowser` and `time` are built in. You need a desktop session with a default browser (this won't open anything over SSH).

### How to run it
```bash
cd "Website Launcher"        # quotes needed because of the space in the folder name
python3 launcher.py
```

### Customize your sites
Edit the list in `launcher.py`. Each entry needs the full address, including `https://`:
```python
websites = [
    "https://github.com",
    "https://mail.google.com",
    "https://calendar.google.com",
]
```

### Run it on login (Ubuntu)
Open **Startup Applications** → **Add** and use this command:
```
python3 "/full/path/to/Website Launcher/launcher.py"
```
