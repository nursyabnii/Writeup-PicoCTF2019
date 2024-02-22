# 1_wanna_b3_a_r0ck5tar
### AUTHOR: ALEX BUSHKIN
### Challenge Points: 350

## Category
General Skills

## Challenge Description
I wrote you another [song](lyrics.txt). Put the flag in the picoCTF{} flag format
## Solution
Continuing from the mus1c challenge, we encounter another Rockstar language file. However, this time, when we compile it using the [online compiler](https://codewithrockstar.com/online), the compiler requires us to provide an input. To determine the required input, we need to decode the logic of the Rockstar language. Referring to [the documentation](https://codewithrockstar.com/docs) is quite helpful in understanding the code. Let's analyze the code:
```
Rocknroll is right              
Silence is wrong                
A guitar is a six-string        
Tommy's been down               
Music is a billboard-burning razzmatazz!
Listen to the music             
If the music is a guitar                  
Say "Keep on rocking!" 
```
In this part of the code, we're setting up some variables. In Rockstar, the word `is` is used for assigning values. In this language, integers are represented by words, where each word's length corresponds to a digit. For instance, `a six-string` translates to `136`, as 'a' has 1 character, 'six' has 3 characters, and so forth. Words with 10 characters are equivalent to 0s. The keyword `Listen` is used for taking input, and `if` functions similar to other programming languages. So, if we were to convert this segment of code into C++, it would look like:
```cpp
boolean rocknroll = true;
boolean silence = false;
int a_guitar = 136;
int tommy = 4;
int music = 1970;
int the_music;
cin >> the_music;
if (the_music == a_guitar) {
    cout << "Keep on rocking!";
}
```
We move on to the next segment:
```
Listen to the rhythm
If the rhythm without Music is nothing
```
Here we get another input. `without` is subtract and `nothing` is zero. So effectively, this segment in C++ would be:
```cpp
int rhythm;
cin >> rhythm;
if (rhythm - music == 0) {
    ...
}
```
Since we initialized music to 1970 earlier, that is our input. After inputting that, we get our output. Convert it into ASCII and we get our flag.
## Flag
`picoCTF{BONJOVI}`