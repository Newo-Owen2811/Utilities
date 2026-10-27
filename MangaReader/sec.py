from pathlib import Path
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

library_path = Path(__file__).parent / "manga_library"

# ==========================================
# PART 1: THE LAUNCHER MENU WINDOW
# ==========================================
def open_launcher():
    menu_root = tk.Tk()
    menu_root.title("Select Chapter")
    menu_root.geometry("400x300")
    menu_root.configure(bg="#1e1e1e")

    volumes = sorted([f.name for f in library_path.iterdir() if f.is_dir()])
    selected_volume = tk.StringVar(menu_root)
    selected_volume.set(volumes[0] if volumes else "")

    selected_chapter = tk.StringVar(menu_root)

    def update_chapters(event):
        vol = selected_volume.get()
        vol_path = library_path / vol
        chapters = sorted([f.name for f in vol_path.iterdir() if f.is_dir()])
        chapter_combo['values'] = chapters
        if chapters:
            chapter_combo.set(chapters[0])

    tk.Label(menu_root, text="Select Volume:", bg="#1e1e1e", fg="#FFFFFF", font=("Arial", 12)).pack(pady=10)
    volume_combo = ttk.Combobox(menu_root, textvariable=selected_volume, values=volumes, state="readonly", font=("Arial", 12))
    volume_combo.pack(pady=5)
    volume_combo.bind("<<ComboboxSelected>>", update_chapters)

    tk.Label(menu_root, text="Select Chapter:", bg="#1e1e1e", fg="#FFFFFF", font=("Arial", 12)).pack(pady=10)
    chapter_combo = ttk.Combobox(menu_root, textvariable=selected_chapter, state="readonly", font=("Arial", 12))
    chapter_combo.pack(pady=5)

    if volumes:
        update_chapters(None)

    def on_start():
        chosen_vol = selected_volume.get()
        chosen_chap = selected_chapter.get()
        
        # Close the menu window
        menu_root.destroy()
        
        # Launch the reader with the user's choices!
        launch_manga_reader(chosen_vol, chosen_chap)

    start_btn = tk.Button(menu_root, text="Start Reading", font=("Arial", 12), bg="#333333", fg="#FFFFFF", command=on_start)
    start_btn.pack(pady=20)

    menu_root.mainloop()


# ==========================================
# PART 2: YOUR MANGA READER WINDOW
# ==========================================
def launch_manga_reader(vol, chap):
    root = tk.Tk()
    root.title("Manga Reader")
    root.geometry("1600x1000")
    root.configure(bg="#1e1e1e")

    # Use the volume and chapter passed from the menu!
    img_path = library_path / vol / chap
    image_files = sorted(img_path.glob("*.jpg"))

    if not image_files:
        raise FileNotFoundError(f"No JPG files found in {img_path}")

    current_index = 0

    main_frame = tk.Frame(root, bg="#1e1e1e")
    main_frame.pack(expand=True)  

    left_label = tk.Label(main_frame, bg="#1e1e1e", bd=0, highlightthickness=0)
    left_label.pack(side="left")

    right_label = tk.Label(main_frame, bg="#1e1e1e", bd=0, highlightthickness=0)
    right_label.pack(side="left")

    counter_label = tk.Label(root, text="", bg="#1e1e1e", fg="#FFFFFF", font=("Arial", 12))
    counter_label.pack(side="bottom", pady=10)

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


# Start the whole program by opening the menu first!
if __name__ == "__main__":
    open_launcher()