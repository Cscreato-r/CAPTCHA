CAPTCHA Verification System

A simple CAPTCHA generation and verification program implemented in
Python using the captcha library. The program generates a random CAPTCHA
image, saves it locally, displays it to the user, and verifies the
entered text.

This project demonstrates the basic principle of CAPTCHA systems used to
distinguish humans from automated bots, similar to mechanisms used in
authentication systems, login forms, and online security frameworks.

------------------------------------------------------------------------

FEATURES

-   Random CAPTCHA generation
-   Image-based CAPTCHA using the captcha library
-   Removal of visually confusing characters (0, O, 1, I)
-   Automatic image saving
-   CAPTCHA verification with 3 attempts
-   Simple command-line interface

------------------------------------------------------------------------

TECHNOLOGIES USED

-   Python 3
-   captcha library
-   Standard Python libraries:
    -   random
    -   string
    -   os

------------------------------------------------------------------------

INSTALLATION

1.  Clone the repository

git clone https://github.com/yourusername/captcha-generator.git cd
captcha-generator

2.  Install dependencies

pip install captcha

------------------------------------------------------------------------

HOW THE PROGRAM WORKS

1.  The program generates a random 6-character CAPTCHA string.
2.  Confusing characters such as 0, O, 1, and I are removed from the
    character pool.
3.  The CAPTCHA text is rendered as an image using ImageCaptcha.
4.  The generated image is saved as: captcha.png
5.  The image is automatically opened for the user.
6.  The user must type the CAPTCHA correctly.
7.  The user gets 3 attempts before access is denied.

------------------------------------------------------------------------

EXAMPLE OUTPUT

======================================== CAPTCHA Verification System
========================================

Attempt 1/3 CAPTCHA saved as: captcha.png Enter CAPTCHA: AB3DFK

CAPTCHA Passed

If incorrect:

Attempt 2/3 Incorrect CAPTCHA

If all attempts fail:

Access Denied Correct CAPTCHA was: X7KPLD

------------------------------------------------------------------------

PROJECT STRUCTURE

captcha-project │ ├── captcha_generator.py ├── captcha.png └──
README.txt

------------------------------------------------------------------------

CODE CONFIGURATION

WIDTH = 280 HEIGHT = 110 CAPTCHA_LENGTH = 6 OUTPUT_FILE = “captcha.png”

These parameters control the CAPTCHA image size, text length, and output
file name.

------------------------------------------------------------------------

SECURITY NOTE

This project is intended for educational purposes and demonstrates the
basic architecture of CAPTCHA systems. Production-grade CAPTCHA systems
typically include additional security mechanisms such as:

-   Image distortion
-   Noise injection
-   Machine learning resistance
-   Server-side validation
-   Time-based expiry

------------------------------------------------------------------------

POSSIBLE IMPROVEMENTS

-   Add noise and distortion
-   Implement a web-based CAPTCHA using Flask or Django
-   Generate multiple CAPTCHA styles
-   Add CAPTCHA expiration timer
-   Log failed attempts
-   Integrate with authentication systems

------------------------------------------------------------------------

LICENSE

This project is open-source and available for educational and academic
use.
