import tkinter as tk
import requests
from tkinter import messagebox

def send_message():
    message = message_entry.get()
    if not message:
        messagebox.showwarning("Warning", "請輸入訊息")
        return

    # LINE Notify API 的 URL
    url = 'https://notify-api.line.me/api/notify'
    token = '68xcbXACa6nF44QmJd4jCiauAre26HwXurBuA4DqYTV'  # 在這裡使用您提供的實際 token
    headers = {
        'Authorization': f'Bearer {token}'
    }
    params = {
        'message': message
    }

    response = requests.post(url, headers=headers, params=params)
    
    if response.status_code == 200:
        messagebox.showinfo("Success", "訊息發送成功")
    else:
        messagebox.showerror("Error", f"訊息發送失敗\n狀態碼: {response.status_code}")

# 建立主窗口
root = tk.Tk()
root.title("LINE Notify 發送訊息")

# 設置窗口大小
root.geometry("400x200")

# 建立並配置 UI 元素
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

message_label = tk.Label(frame, text="請輸入訊息:")
message_label.pack(padx=5, pady=5)

message_entry = tk.Entry(frame, width=50)
message_entry.pack(padx=5, pady=5)

send_button = tk.Button(frame, text="送出", command=send_message)
send_button.pack(padx=5, pady=20)

# 啟動主循環
root.mainloop()
