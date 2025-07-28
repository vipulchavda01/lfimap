# LFIMAP

**LFIMAP (Local File Inclusion Mapper)** is a simple Python-based tool to **detect Local File Inclusion (LFI) vulnerabilities** in websites.  
It automatically tests multiple payloads, directory traversal levels (up to 20), and common sensitive files on both Linux and Windows systems.

---
<img width="944" height="599" alt="lfimap" src="https://github.com/user-attachments/assets/86cbdaa7-de5c-479a-8fca-9ff4ea39260f" />

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
git clone https://github.com/vipulchavda01/lfimap.git
cd lfimap.py
