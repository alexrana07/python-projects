# Password Manager

A simple password manager made with Python. It saves your passwords in a file in locked (encrypted) form, and shows them again when you ask.

## Files in this folder

- `password_manager.py` - the main program. Run this file.
- `key.key` - the secret key used to lock and unlock the passwords.
- `passwords.txt` - where the saved passwords are stored. They are encrypted, so you can't read them by opening the file.

## What you need

- Python 3
- The `cryptography` library

Install the library with:

```
pip install cryptography
```

## How to use

1. Open `password_manager.py` and find this line:

   ```python
   # write_key()
   ```

2. Remove the `#` and run the program once. This creates the `key.key` file.
3. Put the `#` back so the key is not made again.
4. Run the program:

   ```
   python password_manager.py
   ```

5. Type one of these:
   - `add` - save a new account name and password
   - `view` - show all saved passwords
   - `q` - quit the program

## Important things to remember

- **Do not delete or change `key.key`.** If you lose it, you can never unlock your saved passwords.
- **Do not run `write_key()` again.** It makes a new key and the old passwords will stop working.
- **Do not share `key.key`.** Anyone who has this file and `passwords.txt` can read your passwords.
- Use `add` before `view`. If `passwords.txt` doesn't exist yet, `view` will give an error.

## How it works

- `write_key()` makes a random key and saves it in `key.key`.
- `load_key()` reads the key from the file when the program starts.
- `add()` locks the password with the key and saves it as `name|lockedpassword`.
- `view()` reads each line, splits the name and password, unlocks the password, and prints it.

## Note

This is a beginner project made for learning. For real passwords, use a trusted password manager like Bitwarden or KeePassXC.