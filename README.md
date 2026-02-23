# 🚀 ReconPy v1.0
### High-Speed Multi-threaded Port Scanner ⚡

**ReconPy** is a fast and lightweight port scanner written in Python. It utilizes **multi-threading** to scan hundreds of ports in seconds, providing a clean and colored terminal output for easy reconnaissance.

---

## ✨ Features
- ⚡ **Fast Scanning:** Multi-threading makes it significantly faster than sequential scanners.
- 🎨 **Colored Output:** Green for `OPEN` ports and Red for `CLOSED` ports (Optional).
- 📂 **Save Results:** Automatically logs findings to a `.txt` file without messy ANSI color codes.
- 🛠️ **Full Control:** Scan a range of ports, specific ports, or show all results.
- ⏱️ **Execution Time:** Provides a precise report on how long the scan took.

---

## 🚀 Usage Examples

### 1️⃣ Default Scan (First 1000 ports)
```bash
python reconpy.py 192.168.1.1

```

### 2️⃣ Scan Specific Range & Save Results

```bash
python reconpy.py 127.0.0.1 -n 500 -o scan_results.txt

```


### 3️⃣ Scan Specific Ports Only (e.g., HTTP & HTTPS)


```bash
python reconpy.py 192.168.1.3 -p 80 443 8080
```


### 4️⃣ Show All Results (Open & Closed)


```bash
python reconpy.py 192.168.1.1 -n 100 -a
```



### 🛠️ Requirements
###### Python 3.13.3
No external libraries required.

Built-in Modules: socket, threading, argparse, time.

### 👨‍💻 Developer
  
##### Fikri Mohamed

🌐 Website: https://fikri.42web.io/profile

--- 
⚠️ Disclaimer
This tool is for educational and authorized security testing purposes only. Do NOT scan networks or systems without explicit permission. The developer is not responsible for any misuse.
