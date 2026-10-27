import pygame
from pathlib import Path
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
    script_dir = Path(__file__).parent
    song_path = script_dir / "MP3" / f"{song}.mp3"
    pygame.mixer.music.load(str(song_path))
    pygame.mixer.music.play(loops=-1)

def next(n):
  return 1 if n == len(song_files) else n + 1


def prev(n):
  return len(song_files) if n == 1 else n - 1

def pause():
    pygame.mixer.music.pause()
    print("-> Music Paused")

def unpause():
   pygame.mixer.music.unpause()
   print("-> Music Resumed")
   


song_files = {
    1: "cin",
    2: "first",
    3: "butterfly",
    4: "love",
    5: "boys",
    6: "salva",
    7: "heaven",
    8: "summer",
    9: "Brooklyn_Baby",
    10: "ultra",
    11: "west",
    12: "young",
    13: "margaret",
}

song_names = {
    1: "Cinnamon Girl",
    2: "First Light",
    3: "Happiness is a butterfly",
    4: "Love song",
    5: "Music To Watch Boys To",
    6: "Salvatore",
    7: "Say Yes To Heaven",
    8: "Summertime Sadness",
    9: "Brooklyn Baby",
    10: "Ultraviolence",
    11: "West Coast",
    12: "Young And Beautiful",
    13: "Margaret",
}

prompt_text = """Choose The Song:
1. Cinnamon Girl
2. First Light
3. Happiness is a butterfly
4. Love song
5. Music To Watch Boys To
6. Salvatore
7. Say Yes To Heaven
8. Summertime Sadness
9. Brooklyn Baby
10. Ultraviolence
11. West Coast
12. Young And Beautiful
13. Margaret
Selection: """


if __name__ == "__main__":
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
      pause()

    elif command == "u":
      unpause()
      
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