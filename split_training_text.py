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


# training_text_file = 'langdata/eng.training_text'

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
    line_training_text = os.path.join(output_directory, f'train_text_{line_count}.gt.txt')
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
        '--ysize=2400',
        '--char_spacing=0.0',
        '--exposure=0'
    ])

    line_count += 1