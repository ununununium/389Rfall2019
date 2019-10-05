# Writeup 2 - Pentesting

Name: *Yuting Zhong*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *Yuting Zhong*

## Assignment Writeup

### Part 1 (45 pts)

  -  Flag: ```CMSC389R-{p1ng_as_a_$erv1c3}```
  -  Input: ```$ ;cat home/flag.txt```
  -  Thought Process: After ```$ nc wattsamp.net 1337```, server promt to enter your IP address. Here is my chance to test if the server is vulnerable to command injection. So, I put ```$ ;ls```, luckily the whole file system showed up. I saw there is ```home``` directory, so I go ahead tried ```;ls home```. and I find a ```flag.txt``` in that home directory. Finally, I used ```$ ;cat home/flag.txt``` to get the Flag.
  - Suggestion: Command injection is the vulnerability that allows users to run system command on server from user end(the application).  According to the article [OS command injection][1], the most effective way of preventing from command injection is never call OS command from the user end(application layer). If for some reason you have to do that or it is too late to update your software, you should implement strong validation on users' inputs. This article [OS command injection][1] also provides several useful validations:
    -  Validating against a whitelist of permitted values.
    -  Validating that the input is a number.
    -  Validating that the input contains only alphanumeric characters, no other syntax or whitespace.

  Another solution is to sanitize users' inputs, avoid them from inputing the following characters: ```|  ; & $ > < ` \ ! ``` But remember this solution is not as strong as the two I mentioned above.


### Part 2 (55 pts)

[1]:https://portswigger.net/web-security/os-command-injection
