import tkinter as tk
from scanner.url_checker import check_url
from utils.logger import print_logs


class RedirectLogger:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, message):
        self.text_widget.insert(tk.END, message)
        self.text_widget.see(tk.END)

    def flush(self):
        pass


def start_gui():
    root = tk.Tk()
    root.title("🔍 Anti-Phishing Scanner")
    root.geometry("500x500")
    root.resizable(False, False)

    tk.Label(root, text="🔍 Enter website URL to check", font=("Arial", 14)).pack(pady=10)
    url_entry = tk.Entry(root, width=50, font=("Arial", 12))
    url_entry.pack(pady=5)
    result_label = tk.Label(root, text="", font=("Arial", 12), fg="black")
    result_label.pack(pady=10)

    # Output label
    tk.Label(root, text="Logs and Output", font=("Arial", 12, "bold")).pack(pady=5)
    log_text = tk.Text(root, height=10, width=60, font=("Arial", 10))
    log_text.pack(pady=10)

    import sys
    sys.stdout = RedirectLogger(log_text)

    def scan_url():
        url = url_entry.get().strip()
        if not url:
            return
        result_label.config(text="🔄 Scanning...", fg="blue")
        root.update_idletasks()
        phishing_score, status = check_url(url)
        result_label.config(text=f"📊 Website Status: {status}",
                            fg="green" if phishing_score < 40 else "orange" if phishing_score < 70 else "red")

    tk.Button(root, text="🔍 Scan", command=scan_url, font=("Arial", 12), bg="blue", fg="white").pack(pady=5)
    tk.Button(root, text="📜 Show Logs", command=print_logs, font=("Arial", 12), bg="gray", fg="white").pack(pady=5)
    tk.Button(root, text="❌ Exit", command=root.quit, font=("Arial", 12), bg="red", fg="white").pack(pady=5)
    root.mainloop()
