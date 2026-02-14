
---

# 🚀 GearUp Lite Booster

**GearUp Lite Booster** is a lightweight Windows optimization tool built with Python and Tkinter. It provides quick system performance tweaks designed to improve gaming and general PC responsiveness.

This application focuses on RAM optimization, DNS flushing, process priority management, and basic network tuning — all through a simple graphical interface.

---

## 🛠 Features

### 🧠 RAM Optimization

* Lowers priority of background processes
* Helps free up system resources
* Keeps essential processes like `explorer.exe` and `python.exe` untouched

### 🌐 DNS Flush

* Clears the Windows DNS cache
* Can resolve connection and browsing issues
* Uses the Windows `ipconfig /flushdns` command

### 🎮 Set Game High Priority

* Allows you to enter a game `.exe` name
* Sets the selected process to **HIGH priority**
* May improve in-game performance and responsiveness

⚠ Requires Administrator privileges.

### 📡 Network Optimization

Applies TCP optimization settings using `netsh`:

* Enables RSS (Receive Side Scaling)
* Enables Chimney Offload
* Sets TCP autotuning level to normal

---

## 🖥 Built With

* Python
* Tkinter (GUI)
* psutil (Process management)
* Windows system commands (`netsh`, `ipconfig`)

---

## 📦 Requirements

* Windows OS
* Python 3.x
* Required Python package:

```bash
pip install psutil
```

---

## ▶ How to Run

1. Install dependencies:

```bash
pip install psutil
```

2. Run the script:

```bash
python your_script_name.py
```

3. (Recommended) Run as Administrator for full functionality.

---

## ⚠ Important Notes

* This tool is designed for Windows only.
* Some features require Administrator privileges.
* Improper use of priority settings may affect system stability.
* Always save your work before optimizing.

---

## 🎯 Purpose

GearUp Lite Booster is intended as a lightweight, easy-to-use optimization helper for gamers and users who want quick access to performance tweaks without navigating deep system settings.
