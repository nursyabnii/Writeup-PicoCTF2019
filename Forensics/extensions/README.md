# extensions
### AUTHOR: SANJAY C/DANNY
### Challenge Points: 150

## Category
Forensics

## Challenge Description
This is a really weird text file [TXT](flag.txt)? Can you find the flag?
## Hints
1. How do operating systems know what kind of file it is? (It's not just the ending!
2. Make sure to submit the flag as picoCTF{XXXXX}
## Solution
We're presented with a text file containing bytes, suggesting it's not a conventional plain-text .txt file. Upon opening the file, the presence of the term `PNG` becomes immediately apparent. By changing the file extension to .png, it transforms into an image revealing the flag.
## Flag
`picoCTF{now_you_know_about_extensions}`