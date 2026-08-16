# Caesar Cipher Encryption & Decryption

A simple Python script that encrypts and decrypts text using the **Caesar Cipher** technique — shifting each character by a user-defined number of positions based on its ASCII value.

## How It Works

The script shifts characters through the alphabet, digits, and punctuation:

- **Uppercase letters (A–Z):** shifted forward by `shift`, wrapping around from `Z` back to `A`
- **Lowercase letters (a–z):** shifted forward by `shift`, wrapping around from `z` back to `a`
- **Digits (0–9):** shifted forward by `shift`, wrapping around from `9` back to `0`
- **Punctuation:** shifted by ASCII value (no wraparound)
- **Everything else** (e.g. spaces): left unchanged

Decryption simply reverses the shift to recover the original text.

## Requirements

- Python 3.x
- No external libraries required (uses only the built-in `string` module)

## Usage

Run the script from your terminal:

```bash
python encryption.py
```

You'll be prompted to enter:
1. The text you want to encrypt
2. A shift value (integer)

The script will print both the encrypted and decrypted versions of your text.

## Sample Output

```
Enter text : Fmec674(-.
Enter shift value : 5
Encrypted Text :  Krjh129-23
Decrypted Text :  Fmec674(-.

Enter text : hello Everyone :)
Enter shift value : 3
Encrypted Text :  khoor Hyhubrqh =;
Decrypted Text :  hello Everyone :)
```

## Example

```python
text = "Hello, World!"
shift = 3
# Encrypted -> "Khoor, Zruog$"
# Decrypted -> "Hello, World!"
```

## Notes / Limitations

- Punctuation shifting is based on raw ASCII values, so some shifted punctuation characters may not stay within the standard punctuation range (as seen in the sample output above, e.g. `:)` → `=;`).
- Large shift values will still work correctly since Python's `chr()`/`ord()` and the wraparound logic handle them, but very large shifts on punctuation can produce non-printable or unexpected characters since there's no wraparound for that category.

## License

Feel free to use, modify, and distribute this project for learning purposes.
