# Mr-Worldwide
### AUTHOR: DANNY
### Points: 200

## Category
Cryptography

## Challenge Description
A musician left us a [message](message.txt). What's it mean?

## Hints
(None)
## Solution
This challenge may be considered one of the more unusual ones, but it remains entertaining. We're provided with a text file containing what appears to be coordinates. Plugging these coordinates into Google Maps in the format of (longitude, latitude) yields major cities corresponding to each coordinate. These cities are listed in the same sequence as they appear in the text file:
```
Kyoto, Japan				
Odessa, Ukraina				
Dayton, United States			
Istanbul, Turkey			
Abu Dhabi, United Arab Emirates		
Kuala Lumpur, Malaysia			
_					
Addis Ababa, Ethiophia			
Loja, Ecuador				
Amsterdam, Netherlands			
Sleepy Hollow, United States		
Kodiak, United States			
Alexandria, Egypt		
```
When we take the first character from each of these cities, we get another city: KODIAK_ALASKA, which is our flag.
## Flag
`picoCTF{KODIAK_ALASKA}`