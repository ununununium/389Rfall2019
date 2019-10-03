# Writeup 2 - Pentesting

Name: *Yuting Zhong*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *Yuting Zhong*

## Assignment Writeup

### Part 1 (45 pts)

  -  Flag: ```CMSC389R-{p1ng_as_a_$erv1c3}```
  -  Input: ```$ ;cat home/flag.txt```
  -  Thought Process: After ```$ nc wattsamp.net 1337```, server promt to enter your ip address. Here is my chance to test if the server is vulnerable to command injection. So, I put ```$ ;ls```, luckily the whole file system showed up. I saw there is ```home``` directory, so I go ahead tried ```|ls home```. and I find a ```flag.txt``` in that home directory. Finally, I used ```$ ;cat home/flag.txt``` to get the Flag.
  - Suggestion: You should sanitize users' input, avoid them from using the following characters: ```|  ; & $ > < ` \ ! ```

### Part 2 (55 pts)

*Please use this space to detail your approach and solutions for part 2. Don't forget to upload your completed source code to this /writeup directory as well!*
