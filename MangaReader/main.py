from pathlib import Path
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

library_path = Path(__file__).parent / "manga_library"

def open_launcher():
    menu_root = tk.Tk()
    menu_root.title("Select Volume")
    menu_root.geometry("400x220")
    menu_root.configure(bg="#1e1e1e")

    
    volumes = sorted([f.name for f in library_path.iterdir() if f.is_dir()])
    selected_volume = tk.StringVar(menu_root)
    selected_volume.set(volumes[0] if volumes else "")

    
    tk.Label(menu_root, text="Select Volume:", bg="#1e1e1e", fg="#FFFFFF", font=("Arial", 12)).pack(pady=15)
    volume_combo = ttk.Combobox(menu_root, textvariable=selected_volume, values=volumes, state="readonly", font=("Arial", 12))
    volume_combo.pack(pady=5)

    def on_start():
        chosen_vol = selected_volume.get()
        
        
        menu_root.destroy()
        
    
        launch_manga_reader(chosen_vol)

    start_btn = tk.Button(menu_root, text="Start Reading", font=("Arial", 12), bg="#333333", fg="#FFFFFF", command=on_start)
    start_btn.pack(pady=20)

    menu_root.mainloop()


def launch_manga_reader(vol):
    root = tk.Tk()
    root.title("Manga Reader")
    root.geometry("1600x1000")
    root.configure(bg="#1e1e1e")

    img_path = library_path / vol
    image_files = sorted(img_path.glob("*.jpg"))

    if not image_files:
        raise FileNotFoundError(f"No JPG files found in {img_path}")

    current_index = 0

  # 1. Your original manga frame, untouched and perfectly centered
    main_frame = tk.Frame(root, bg="#1e1e1e")
    main_frame.pack(expand=True)  

    left_label = tk.Label(main_frame, bg="#1e1e1e", bd=0, highlightthickness=0)
    left_label.pack(side="left")

    right_label = tk.Label(main_frame, bg="#1e1e1e", bd=0, highlightthickness=0)
    right_label.pack(side="left")

    # 2. Minimal counter floating in the upper-right corner without shifting your layout
    counter_label = tk.Label(root, text="", bg="#1e1e1e", fg="#FFFFFF", font=("Arial", 12, "bold"))
    counter_label.place(relx=0.98, rely=0.02, anchor="ne")

    def load_page(path, max_size):
        with Image.open(path) as source:
            page = source.copy()
        page.thumbnail(max_size)
        return ImageTk.PhotoImage(page)

    def show_image():
        page_width = max(1, (root.winfo_width() - 40) // 2)
        page_height = max(1, root.winfo_height() - 40)
        max_size = (page_width, page_height)

        photo = load_page(image_files[current_index], max_size)
        left_label.config(image=photo)
        left_label.image = photo

        if current_index + 1 < len(image_files):
            right_photo = load_page(image_files[current_index + 1], max_size)
            right_label.config(image=right_photo)
            right_label.image = right_photo
            display_page = current_index + 2  
        else:
            right_label.config(image="")
            right_label.image = None
            display_page = current_index + 1
        counter_label.config(text=f"{display_page}/{len(image_files)} pages")

    root.update_idletasks()
    show_image()
    root.bind("<Configure>", lambda event: show_image() if event.widget is root else None)

    def next_page():
        nonlocal current_index
        if current_index < len(image_files) - 1:
            current_index = current_index + 2
            show_image()

    def prev_page():
        nonlocal current_index
        if current_index > 0:
            current_index = current_index - 2
            show_image()

    root.bind("<Left>", lambda event: next_page())
    root.bind("<Right>", lambda event: prev_page())

    root.mainloop()


# Start the program
if __name__ == "__main__":
    open_launcher()