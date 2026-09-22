# Login Security Practice

## What This Code Does
This code allows a user to enter their credentials up to three times. After each attempt, the code checks whether the credentials are correct or incorrect. If the credentials are correct, access is granted and the program ends. If the credentials are incorrect, the user is prompted to try again. After three failed attempts, the account is locked.

## How the Code Works
- `attempt = 0` keeps track of login attempts.
- `while attempt < 3` allows up to three attempts.
- `if` checks whether the password is correct.
- `break` ends the loop after successful login.
- `attempt += 1` increases the attempt counter.
