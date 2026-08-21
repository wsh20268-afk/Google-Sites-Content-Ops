"""UI module for Google Sites Content Ops Pro v2.0."""


def run_app():
    try:
        import tkinter as tk
        root = tk.Tk()
        root.title("Google Sites Content Ops Pro v2.0")
        root.geometry("900x600")
        label = tk.Label(root, text="Google Sites Content Ops Pro v2.0\n新版开发中", font=("Microsoft YaHei", 18))
        label.pack(expand=True)
        root.mainloop()
    except Exception as e:
        print("启动失败:", e)
