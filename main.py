import os
import threading

import customtkinter as ctk
from tkinter import filedialog, messagebox

from crypto_utils import encrypt_file, decrypt_file


# -----------------------------
# CustomTkinter Configuration
# -----------------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class CipherVault(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("CipherVault")
        self.geometry("920x620")
        self.resizable(False, False)

        self.selected_file = ""

        self.build_ui()

    def build_ui(self):

        # =========================
        # Sidebar
        # =========================

        sidebar = ctk.CTkFrame(
            self,
            width=220,
            corner_radius=0
        )

        sidebar.pack(
            side="left",
            fill="y"
        )

        ctk.CTkLabel(
            sidebar,
            text="🔐",
            font=("Segoe UI Emoji", 44)
        ).pack(pady=(30, 5))

        ctk.CTkLabel(
            sidebar,
            text="CipherVault",
            font=("Segoe UI", 24, "bold")
        ).pack()

        ctk.CTkLabel(
            sidebar,
            text="AES-256 File Encryption",
            text_color="gray"
        ).pack()

        self.status = ctk.CTkLabel(
            sidebar,
            text="Ready",
            text_color="#00ff88",
            font=("Segoe UI", 14)
        )

        self.status.pack(
            side="bottom",
            pady=(0, 15)
        )

        footer = ctk.CTkLabel(
            sidebar,
            text="Version 1.0\nMade with ❤️",
            text_color="gray",
            font=("Segoe UI", 11)
        )

        footer.pack(
            side="bottom",
            pady=(0, 20)
        )

        # =========================
        # Main Area
        # =========================

        main = ctk.CTkFrame(self)

        main.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=25
        )

        ctk.CTkLabel(
            main,
            text="Secure Your Files",
            font=("Segoe UI", 30, "bold")
        ).pack(pady=(20, 8))

        ctk.CTkLabel(
            main,
            text="AES-256 Encryption with Password Protection",
            text_color="gray"
        ).pack()

        self.file_label = ctk.CTkLabel(
            main,
            text="No file selected",
            width=520,
            wraplength=500
        )

        self.file_label.pack(pady=30)

        self.browse_btn = ctk.CTkButton(
            main,
            text="📁 Browse File",
            width=250,
            height=45,
            command=self.select_file
        )

        self.browse_btn.pack()

        self.password = ctk.CTkEntry(
            main,
            placeholder_text="Enter Password",
            width=360,
            height=45,
            show="•"
        )

        self.password.pack(pady=(25, 10))

        self.show_password = ctk.BooleanVar(value=False)

        self.show_check = ctk.CTkCheckBox(
            main,
            text="Show Password",
            variable=self.show_password,
            command=self.toggle_password
        )

        self.show_check.pack()

        self.progress = ctk.CTkProgressBar(
            main,
            width=360
        )

        self.progress.pack(pady=20)

        self.progress.set(0)

        self.button_frame = ctk.CTkFrame(
            main,
            fg_color="transparent"
        )

        self.button_frame.pack(pady=30)

        self.encrypt_btn = ctk.CTkButton(
            self.button_frame,
            text="🔒 Encrypt",
            width=170,
            height=50,
            fg_color="#16a34a",
            hover_color="#15803d",
            command=self.start_encrypt
        )

        self.encrypt_btn.grid(
            row=0,
            column=0,
            padx=15
        )

        self.decrypt_btn = ctk.CTkButton(
            self.button_frame,
            text="🔓 Decrypt",
            width=170,
            height=50,
            fg_color="#2563eb",
            hover_color="#1d4ed8",
            command=self.start_decrypt
        )

        self.decrypt_btn.grid(
            row=0,
            column=1,
            padx=15
        )

            # =========================
    # Password Visibility
    # =========================

    def toggle_password(self):

        if self.show_password.get():
            self.password.configure(show="")
        else:
            self.password.configure(show="•")

    # =========================
    # Select File
    # =========================

    def select_file(self):

        file = filedialog.askopenfilename(
            title="Select File",
            filetypes=[
                ("All Files", "*.*"),
                ("Encrypted Files", "*.enc")
            ]
        )

        if file:

            self.selected_file = file

            self.file_label.configure(
                text=file
            )

            self.progress.set(0)

            self.status.configure(
                text="File Selected",
                text_color="#00ff88"
            )

    # =========================
    # Enable / Disable Buttons
    # =========================

    def disable_buttons(self):

        self.encrypt_btn.configure(state="disabled")
        self.decrypt_btn.configure(state="disabled")
        self.browse_btn.configure(state="disabled")

    def enable_buttons(self):

        self.encrypt_btn.configure(state="normal")
        self.decrypt_btn.configure(state="normal")
        self.browse_btn.configure(state="normal")

    # =========================
    # Start Threads
    # =========================

    def start_encrypt(self):

        thread = threading.Thread(
            target=self.encrypt,
            daemon=True
        )

        thread.start()

    def start_decrypt(self):

        thread = threading.Thread(
            target=self.decrypt,
            daemon=True
        )

        thread.start()

    # =========================
    # Validation
    # =========================

    def validate(self):

        if self.selected_file == "":

            messagebox.showerror(
                "Error",
                "Please select a file."
            )

            return False

        if self.password.get() == "":

            messagebox.showerror(
                "Error",
                "Please enter a password."
            )

            return False

        return True

    # =========================
    # Progress Animation
    # =========================

    def animate_progress(self):

        self.progress.set(0)

        for i in range(1, 101):

            self.progress.set(i / 100)

            self.update_idletasks()

            import time
            time.sleep(0.01)

                # =========================
    # Encrypt
    # =========================

    def encrypt(self):

        if not self.validate():
            return

        self.disable_buttons()

        self.status.configure(
            text="Encrypting...",
            text_color="yellow"
        )

        try:

            save_path = filedialog.asksaveasfilename(
                title="Save Encrypted File",
                defaultextension=".enc",
                filetypes=[
                    ("Encrypted Files", "*.enc"),
                    ("All Files", "*.*")
                ]
            )

            if not save_path:
                self.enable_buttons()
                self.status.configure(
                    text="Cancelled",
                    text_color="orange"
                )
                return

            self.animate_progress()

            output = encrypt_file(
                self.selected_file,
                self.password.get(),
                save_path
            )

            self.status.configure(
                text="Encrypted Successfully",
                text_color="#00ff88"
            )

            self.password.delete(0, "end")

            messagebox.showinfo(
                "Success",
                f"Encrypted file saved as:\n\n{output}"
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

            self.status.configure(
                text="Encryption Failed",
                text_color="red"
            )

        finally:

            self.enable_buttons()

    # =========================
    # Decrypt
    # =========================

    def decrypt(self):

        if not self.validate():
            return

        self.disable_buttons()

        self.status.configure(
            text="Decrypting...",
            text_color="yellow"
        )

        try:

            filename = os.path.basename(self.selected_file)

            if filename.endswith(".enc"):
                filename = filename[:-4]

            save_path = filedialog.asksaveasfilename(
                title="Save Decrypted File",
                initialfile=filename,
                filetypes=[
                    ("All Files", "*.*")
                ]
            )

            if not save_path:
                self.enable_buttons()
                self.status.configure(
                    text="Cancelled",
                    text_color="orange"
                )
                return

            self.animate_progress()

            output = decrypt_file(
                self.selected_file,
                self.password.get(),
                save_path
            )

            self.status.configure(
                text="Decrypted Successfully",
                text_color="#00ff88"
            )

            self.password.delete(0, "end")

            messagebox.showinfo(
                "Success",
                f"Decrypted file saved as:\n\n{output}"
            )

        except Exception:

            messagebox.showerror(
                "Error",
                "Wrong password or invalid encrypted file."
            )

            self.status.configure(
                text="Decryption Failed",
                text_color="red"
            )

        finally:

            self.enable_buttons()


# =========================
# Run Application
# =========================

if __name__ == "__main__":

    app = CipherVault()
    app.mainloop()