# Writeup 6 - Binaries I

Name: *Yuting Zhong*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *0101*

## Assignment Writeup

### Part 1 (50 pts)

```CMSC389R-{di5a55_0r_d13}```

### Part 2 (50 pts)

First, I use the command ```./crackme``` I got permission denied. I realize I need to change the permission of ```crackme``` file. After I use the command ```chmod 777 crackme```, I could excute the ```crackme``` file. I used the command ```./crackme``` to excute ```crackme``` ,I got a message ```Did you even try disassembling?``` Then I opened ```Binary ninja``` and loaded the binary into it. I saw there are five functions on the symbols column: ```update_flag``` ```check1``` ```check2``` ```check3``` ```main```. I read the ```main``` function assembly code. From the frame of this code, I could see that main will call ```check1``` then ```check2``` then ```check3```, It will also print some string after each checking progress, and it will print something after pass ```check3```, that must be the flag. Then I read ```check1``` assembly code, I saw it push a string ```"Oh God"``` to ```strcmp```'s argument. I tried ```./crackme "Oh God"``` and I successfully passed check1, and it printed a message ```I wish you cared more about the environment```. I continued to see the assembly code of ```check2```. I saw it pushed a string ```FOOBAR``` to ```getenv```'s argument, that means it is getting the value of ```FOOBAR``` environment variable. Then it compared the value of ```FOOBAR``` to the string ```seye ym ``` in reverse order. So I should have an environment varibel called ```FOOBAR``` and set its value to ```" my eyes"```. the way I did this is using the command ```export FOOBAR = " my eyes"```. After setting up the environment variable, I execute the ```crackme``` file and I got a message ```open sesame```.  I go ahead analyzed the assembly code for ```check3```. ```check3``` pushed the string ```"sesame"``` to the argument and called open so I guess it is opening a file called ```"seasame"```.  Then it compares its content character by character to some hex value. I checked those hex value on ASCII table by using ```man ascii``` and get the characters 0x20:```space``` 0x74:```t``` 0x68:```h``` 0x65:```e``` 0x79:```y``` 0x62:```b``` 0x75:```u``` 0x72:```r``` 0x6e:```n```.
I created a file ```sesame``` under the same directory and wrote the string " they burn" into it. Run crackme again, I got the flag ```CMSC389R-{di5a55_0r_d13}```
