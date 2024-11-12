import os

for i in range(10000):
    try:
        with open(f'tesstrain/data/Solaris-3-ground-truth/eng_{i}.box', 'rb') as input_file:
            box_content = input_file.readlines()
        with open (f'tesstrain/data/Solaris-3-ground-truth/eng_{i}.gt.txt', 'r') as input_file:
            gt_content = input_file.readlines()
        if not box_content or not gt_content:
            os.remove(f'tesstrain/data/Solaris-3-ground-truth/eng_{i}.box')
            os.remove(f'tesstrain/data/Solaris-3-ground-truth/eng_{i}.tif')
            os.remove(f'tesstrain/data/Solaris-3-ground-truth/eng_{i}.gt.txt')
            print(f"Removed files ./tesstrain/data/Solaris-3-ground-truth/eng_{i}*")
    except FileNotFoundError:
        try:
            os.remove(f'tesstrain/data/Solaris-3-ground-truth/eng_{i}.box')
            os.remove(f'tesstrain/data/Solaris-3-ground-truth/eng_{i}.tif')
            os.remove(f'tesstrain/data/Solaris-3-ground-truth/eng_{i}.gt.txt')
            print(f"Removed files ./tesstrain/data/Solaris-3-ground-truth/eng_{i}*")
        except FileNotFoundError:
            pass
        