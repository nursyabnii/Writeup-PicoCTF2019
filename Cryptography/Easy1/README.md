# Easy1
### AUTHOR: ALEX FULTON/DANNY
### Challenge Points: 100

## Category
Cryptography

## Challenge Description
The one time pad can be cryptographically secure, but not when you know the key. Can you solve this? We've given you the encrypted flag, key, and a table to help `UFJKXQZQUNB` with the key of `SOLVECRYPTO`. Can you use this [table](table.txt) to solve it?.
## Hints
1. Submit your answer in our competition's flag format. For example, if you answer was 'hello', you would submit 'picoCTF{HELLO}' as the flag.
2. Please use all caps for the message.
## Solution
The presence of a key and a double-entry table immediately suggests one of the frequently used encryption techniques: the Vigenère cipher. Although there are manual methods to decrypt messages using the table provided in the text file, it's far simpler to utilize an online tool like [DCODE](https://cryptii.com/pipes/vigenere-cipher).
## Flag
`picoCTF{CRYPTOISFUN}`