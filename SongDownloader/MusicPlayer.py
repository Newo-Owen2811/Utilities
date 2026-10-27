from pathlib import Path
import pygame
pygame.init()
pygame.mixer.init()

def check(p):
  lana = input(p)
  while not lana.isdigit() or int(lana) == 0 or int(lana) > len(song_files):
    print(f"Enter a Valid Number (1-{len(song_files)})")
    lana = input()
  print("Playing song of the choice...")
  return int(lana)

def music(song):
  pygame.mixer.music.load(f"{song}")
  pygame.mixer.music.play(loops=-1)

def next(n):
  return 1 if n == len(song_files) else n + 1

def prev(n):
  return len(song_files) if n == 1 else n - 1

base_dir = Path(__file__).resolve().parent
folder_path = base_dir / "downloads"

song_files = {}
song_names = {}

if folder_path.exists() and folder_path.is_dir():
    print(f"Scanning folder: {folder_path.name}\n")
    mp3_files = sorted(list(folder_path.glob("*.[mM][pP]3")))

    if mp3_files:
        for i, file_path in enumerate(mp3_files, start=1):
            song_files[i] = file_path
            song_names[i] = file_path.stem
    else:
        print("No MP3 files found in this folder.")
else:
    print(f"Could not find the folder at: {folder_path}")

prompt = ["Choose The Song:"]
for index, name in song_names.items():
    prompt.append(f"{index}. {name}")
prompt.append("Selection: ")

prompt_text = "\n".join(prompt)

choice = check(prompt_text)
music(song_files[choice])
print(f"-> Now Playing: {song_names[choice]}")

print("--- Terminal Music Controls ---")
print("   [p] Pause")
print("   [u] Unpause")
print("   [n] Next")
print("   [b] Back")
print("   [q] Quit")
print("-" * 31)

while True:
  command = input("Enter command: ").strip().lower()

  if command == "p":
    pygame.mixer.music.pause()
    print("-> Music Paused")

  elif command == "u":
    pygame.mixer.music.unpause()
    print("-> Music Resumed")

  elif command == "n":
    choice = next(choice)
    music(song_files[choice])
    print(f"-> Moving to song number: {choice} ({song_names[choice]})")

  elif command == "b":
    choice = prev(choice)
    music(song_files[choice])
    print(f"Moving to song number: {choice} ({song_names[choice]})")

  elif command == "q":
    pygame.mixer.music.stop()
    print("-> Exiting player...")
    break

  else:
    print("Invalid command. Use p, u, n, b, or q.")