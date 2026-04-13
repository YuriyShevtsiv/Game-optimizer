import psutil
import subprocess
import tkinter as tk
from tkinter import messagebox

# -------- RAM CLEANER --------
def clear_ram():
    for proc in psutil.process_iter():
        try:
            if proc.name().lower() not in ["explorer.exe", "python.exe"]:
                proc.nice(psutil.IDLE_PRIORITY_CLASS)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    messagebox.showinfo("Boost", "RAM Optimized!")

# -------- DNS FLUSH --------
def flush_dns():
    try:
        subprocess.run("ipconfig /flushdns", shell=True, check=True)
        messagebox.showinfo("Network", "DNS Flushed!")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to flush DNS. Run as Administrator.")

# -------- SET HIGH PRIORITY --------
def set_high_priority():
    try:
        game_name = entry.get()
        for proc in psutil.process_iter():
            try:
                if game_name.lower() in proc.name().lower():
                    proc.nice(psutil.HIGH_PRIORITY_CLASS)
                    messagebox.showinfo("Priority", f"{game_name} set to HIGH priority!")
                    return
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        messagebox.showwarning("Error", "Game not found.")
    except psutil.AccessDenied:
        messagebox.showerror("Error", "Run as Administrator.")

# -------- TCP OPTIMIZATION --------
def optimize_network():
    try:
        subprocess.run("netsh int tcp set global autotuninglevel=normal", shell=True, check=True)
        subprocess.run("netsh int tcp set global rss=enabled", shell=True, check=True)
        subprocess.run("netsh int tcp set global chimney=enabled", shell=True, check=True)
        messagebox.showinfo("Network", "Network Optimized!")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to optimize network. Run as Administrator.")

# -------- GUI --------
app = tk.Tk()
app.title("GearUp Lite Booster")
app.geometry("400x350")
app.resizable(False, False)

title = tk.Label(app, text="GearUp Lite", font=("Arial", 18, "bold"))
title.pack(pady=10)

boost_btn = tk.Button(app, text="Optimize RAM", width=25, command=clear_ram)
boost_btn.pack(pady=5)

dns_btn = tk.Button(app, text="Flush DNS", width=25, command=flush_dns)
dns_btn.pack(pady=5)

network_btn = tk.Button(app, text="Optimize Network", width=25, command=optimize_network)
network_btn.pack(pady=5)

entry = tk.Entry(app, width=25)
entry.pack(pady=10)
entry.insert(0, "Enter game .exe name")

priority_btn = tk.Button(app, text="Set Game High Priority", width=25, command=set_high_priority)
priority_btn.pack(pady=5)

app.mainloop()
