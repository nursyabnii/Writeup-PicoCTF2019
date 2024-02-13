# So Meta
### AUTHOR: KEVIN COOPER/DANNY
### Challenge Points: 150

## Category
Forensics

## Challenge Description
Find the flag in this [picture](pico_img.png). You can also find the file in /problems/so-meta_0_7c0b2ae7a38b024c6b1c68cf50970a88.
## Hints
1. What does meta mean in the context of files?
2. Ever heard of metadata?
## Solution
The title and clue suggest examining the metadata of this file. There are various methods to achieve this, but I opted for `exiftool`, which provides comprehensive details about a file. The command utilized in the shell was `exiftool pico_img.png`. The flag is discernible within the file's artist information.

<br>

![Screenshot](screenshot.JPG)
## Flag
`picoCTF{s0_m3ta_eb36bf44}`