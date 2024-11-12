import os

for i in range(10000):
    with open(f'tesstrain/data/Solaris-3-ground-truth/eng_{i}.box', 'rb') as input_file:
        if not input_file.readlines():
            os.remove('tesstrain/data/Solaris-3-ground-truth/eng_6132.box')
            os.remove('tesstrain/data/Solaris-3-ground-truth/eng_6132.tif')
            os.remove('tesstrain/data/Solaris-3-ground-truth/train_text_6132.gt.txt')
            print(f"Removed files ./tesstrain/data/Solaris-3-ground-truth/eng_{i}*")