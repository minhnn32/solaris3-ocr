import os
import random
import pathlib
import subprocess
import datasets

random.seed(0)

lines = []
# load text dataset (Huggingface): rahular/simple-wikipedia
dataset = datasets.load_dataset('rahular/simple-wikipedia')
for data in dataset['train']:
    lines.append(data['text'])


training_text_file = 'langdata/eng.training_text'

# lines = []

# with open(training_text_file, 'r') as input_file:
#     for line in input_file.readlines():
#         lines.append(line.strip())

output_directory = 'tesstrain/data/Solaris-3-ground-truth'

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

random.shuffle(lines)

count = 10000

lines = lines[:count]

line_count = 0
for line in lines:
    # only use alphabet
    line = ''.join([c.lower() for c in line if c.isalpha() or c.isspace()])
    training_text_file_name = pathlib.Path(training_text_file).stem
    line_training_text = os.path.join(output_directory, f'{training_text_file_name}_{line_count}.gt.txt')
    with open(line_training_text, 'w') as output_file:
        output_file.writelines([line])

    file_base_name = f'eng_{line_count}'

    subprocess.run([
        'text2image',
        # '--fonts_dir=font',
        '--font=Jiting',
        f'--text={line_training_text}',
        f'--outputbase={output_directory}/{file_base_name}',
        '--max_pages=1',
        '--strip_unrenderable_words',
        '--leading=12',
        '--xsize=4800',
        '--ysize=560',
        '--char_spacing=0.0',
        '--exposure=0',
        '--unicharset_file=langdata/eng.unicharset'
    ])
    
    # make sure we have all 3 files: (tiff, box and gt.txt)
    tiff_file = f'{output_directory}/{file_base_name}.tif'
    box_file = f'{output_directory}/{file_base_name}.box'
    gt_file = f'{output_directory}/{file_base_name}.gt.txt'
    if not os.path.exists(tiff_file) or not os.path.exists(box_file) or not os.path.exists(gt_file):
        print(f"Error: {file_base_name} is missing one of the files")
        # remove the files
        if os.path.exists(tiff_file):
            os.remove(tiff_file)
        if os.path.exists(box_file):
            os.remove(box_file)
        if os.path.exists(gt_file):
            os.remove(gt_file)
    else:
        with open(box_file, 'rb') as input_file:
            box_content = input_file.readlines()
        with open(gt_file, 'r') as input_file:
            gt_content = input_file.readlines()
        if not box_content or not gt_content:
            os.remove(tiff_file)
            os.remove(box_file)
            os.remove(gt_file)
            print(f"Removed files {file_base_name}")
        else:
            print(f"Created {file_base_name}")

    line_count += 1