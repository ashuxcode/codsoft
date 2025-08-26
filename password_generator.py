# Password Generator - CodSoft Internship (Task 3)
# Author: Ashutosh Bind

import secrets
import string
import random

def ask_yes_no(prompt: str) -> bool:
    while True:
        ans = input(prompt + " (y/n): ").strip().lower()
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        print("Please enter y or n.")

def get_length() -> int:
    while True:
        raw = input("Enter password length (8–128 recommended): ").strip()
        if not raw.isdigit():
            print("Length must be a number.")
            continue
        n = int(raw)
        if n <= 0:
            print("Length must be positive.")
        else:
            return n

def build_charset(include_lower, include_upper, include_digits, include_symbols, avoid_similar):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{};:,.?/|~"

    # characters that are easily confused: 0/O, 1/l/I, etc.
    similar = set("0O1lI|S5B8G6Z2Q9")

    pools = []
    if include_lower:
        pools.append(lower)
    if include_upper:
        pools.append(upper)
    if include_digits:
        pools.append(digits)
    if include_symbols:
        pools.append(symbols)

    if not pools:
        raise ValueError("You must enable at least one character type.")

    # merged charset
    charset = "".join(pools)

    if avoid_similar:
        charset = "".join(ch for ch in charset if ch not in similar)
        # also scrub each pool so our "at least one per pool" rule uses the same filtered set
        pools = ["".join(ch for ch in p if ch not in similar) for p in pools]
        # Ensure no pool became empty after filtering
        for p in pools:
            if not p:
                raise ValueError("Filtering similar characters removed a selected category. Disable 'avoid similar' or change categories.")

    return charset, pools

def generate_password(length: int, pools: list[str], charset: str) -> str:
    if length < len(pools):
        # ensure space for at least one from each chosen pool
        raise ValueError(f"Length must be at least {len(pools)} for the selected options.")

    # 1) Guarantee at least one char from each selected pool
    password_chars = [secrets.choice(pool) for pool in pools]

    # 2) Fill the rest from the full charset
    remaining = length - len(password_chars)
    password_chars += [secrets.choice(charset) for _ in range(remaining)]

    # 3) Shuffle for unpredictability (use SystemRandom)
    random.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)

def main():
    print("======================================")
    print("         PASSWORD GENERATOR")
    print("======================================")

    length = get_length()
    include_lower = ask_yes_no("Include lowercase letters (a-z)?")
    include_upper = ask_yes_no("Include uppercase letters (A-Z)?")
    include_digits = ask_yes_no("Include digits (0-9)?")
    include_symbols = ask_yes_no("Include symbols (!,@,#,...) ?")
    avoid_similar = ask_yes_no("Avoid similar-looking characters (0/O, 1/l/I, etc.)?")

    try:
        charset, pools = build_charset(include_lower, include_upper, include_digits, include_symbols, avoid_similar)
        pwd = generate_password(length, pools, charset)
        print("\nYour generated password:")
        print("--------------------------------------")
        print(pwd)
        print("--------------------------------------")
        print("Tip: Store it in a password manager.")
    except ValueError as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
