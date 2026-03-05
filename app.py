"""
CAPTCHA Generator — using captcha library
"""

import random
import string
import os
from captcha.image import ImageCaptcha

WIDTH = 280
HEIGHT = 110
CAPTCHA_LENGTH = 6
OUTPUT_FILE = "captcha.png"

POOL = (string.ascii_uppercase + string.digits)\
        .replace("0","").replace("O","")\
        .replace("1","").replace("I","")


def random_captcha_text(length=CAPTCHA_LENGTH):
    return "".join(random.choice(POOL) for _ in range(length))


def generate_captcha():

    text = random_captcha_text()

    image = ImageCaptcha(
        width=WIDTH,
        height=HEIGHT,
        font_sizes=[42,46,50]
    )

    image.write(text, OUTPUT_FILE)

    return text


def main():

    print("="*40)
    print("CAPTCHA Verification System")
    print("="*40)

    attempts = 3

    for i in range(1, attempts+1):

        print(f"\nAttempt {i}/{attempts}")

        secret = generate_captcha()

        print("CAPTCHA saved as:", OUTPUT_FILE)

        # macOS command to open image
        os.system(f"open {OUTPUT_FILE}")

        user = input("Enter CAPTCHA: ").strip().upper()

        if user == secret:
            print("\nCAPTCHA Passed")
            return

        else:
            print("❌ Incorrect CAPTCHA")

    print("\nAccess Denied")
    print("Correct CAPTCHA was:", secret)


if __name__ == "__main__":
    main()