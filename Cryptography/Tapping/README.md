# Tapping
### AUTHOR: DANNY 
### Challenge Points: 200

## Category
Cryptography

## Challenge Description
Theres tapping coming in from the wires. What's it saying `nc jupiter.challenges.picoctf.org 9422`.
## Hints
1. What kind of encoding uses dashes and dots?
2. The flag is in the format PICOCTF{}
## Solution
I am connect to the service and get the following output:
```console
root@kali:/Cryptography/Tapping# nc jupiter.challenges.picoctf.org 9422
.--. .. -.-. --- -.-. - ..-. { -- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. ..--- -.... ---.. ...-- ---.. ..--- ....- -.... .---- ----- }
```
This enables us to infer that the encryption method used is one of the widely recognized codes: Morse code. If you're skilled in Morse code, you can attempt to decipher it independently. Alternatively, you can utilize an online tool like [unit-conversion.info](http://www.unit-conversion.info/texttools/morse-code/) to assist you.
## Flag
`picoctf{m0rs3c0d31sfun2683824610}`