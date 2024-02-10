# The Numbers
### AUTHOR: DANNY
### Challenge Points: 50

## Category
Cryptography

## Challenge Description
The [numbers](the_numbers.png)... what do they mean?
## Hints
The flag is in the format PICOCTF{}
## Solution
When we open this file manually and examine the image, we observe a series of numerical sequences. It becomes evident that these numbers range from 1 to 26. By manually correlating each number with its corresponding uppercase letter in the alphabet, we obtain our flag. Alternatively, we can utilize a simple script like [this](the_numbers.py) to derive the flag.
## Flag
`PICOCTF{THENUMBERSMASON}`