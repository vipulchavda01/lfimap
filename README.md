# LFIMAP

**LFIMAP (Local File Inclusion Mapper)** is a simple Python-based tool to **detect Local File Inclusion (LFI) vulnerabilities** in websites.  
It automatically tests multiple payloads, directory traversal levels (up to 20), and common sensitive files on both Linux and Windows systems.

---

## Features
- Scans **single URL** or **multiple targets** (from a wordlist)
- Tests **20 levels of directory traversal**
- Checks for **common Linux & Windows sensitive files**
- Detects LFI by looking for specific patterns (like `/etc/passwd`, `win.ini`, etc.)
- Uses **Random User-Agents** for each request to avoid detection and blocking
- Color-coded output for **easy identification of vulnerable targets**

---

## Installation
```bash
git clone https://github.com/yourusername/lfimap.git
cd lfimap
pip install -r requirements.txt
