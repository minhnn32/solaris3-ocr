# Solaris-3 OCR
An OCR system for Wuthering Waves Solaris-3 language.

## Dataset
Synthetic dataset generated using Solaris-3 font from NathLWX.
Here is a link to his thread: [Reddit](https://www.reddit.com/r/WutheringWaves/comments/1fj6vgk/the_font_files_for_wuwas_fictional_scriptalphabet/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)

The text used to generate this synthetic dataset are from Wikipedia.

## How to train the Tesseract model

### Install Solaris-3 font
Navigate to folder `./font`.
The installed font is called `Jiting` for some reasons.

### Generate Synthetic data
Run:
```bash
python split_training_text.py
python clean_error_null_box.py
```

### Train the model
Run:
```bash
sh train.sh
```

### Test the model
Checkout the notebook `pytesseract.ipynb`.