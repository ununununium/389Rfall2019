# Writeup 2 - Pentesting

Name: *Yuting Zhong*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *Yuting Zhong*

## Assignment Writeup

### Part 1 (45 pts)

  -  Flag: ```CMSC389R-{p1ng_as_a_$erv1c3}```
  -  Input: ```;cat home/flag.txt```
  -  Thought Process: After ```nc wattsamp.net 1337```, server promt to enter your IP address. Here is my chance to test if the server is vulnerable to command injection. The following characters```|  ; & $ > < ` \ ! ``` might cause this happened. So, I put ```;ls```, luckily the whole file system showed up. I saw there is ```home``` directory, so I go ahead tried ```;ls home```. and I find a ```flag.txt``` in that home directory. Finally, I used ```;cat home/flag.txt``` to get the Flag.
  - Suggestion: Command injection is the vulnerability that allows users to run system command on server from user end(the application).  According to the article [OS command injection][1], the most effective way of preventing from command injection is never call OS command from the user end(application layer). If for some reason you have to do that or it is too late to update your software, you should implement strong validation on users' inputs. This article [OS command injection][1] also provides several useful validations:
    -  Validating against a whitelist of permitted values.
    -  Validating that the input is a number.
    -  Validating that the input contains only alphanumeric characters, no other syntax or whitespace.

    Another solution is to sanitize users' inputs, avoid them from inputing the following characters: ```|  ; & $ > < ` \ ! ``` But remember this solution is not as strong as the two I mentioned above.


### Part 2 (55 pts)  

  -  Thought process:  

    -  Interactive Shell:  
      To implement an interactive shell, I should have an infinite loop that do command injection. The way I do it is just put ''';''' in front of each command user provides. After implementing these, my shell is already powerful enough to achieve almost every one line commands. However, this shell does not allow users to save the current working directory. For example, there is a flag exist in ```home/flag.txt```, me shell could help me reading this flag by using one line command ```cat home/flag.txt``` but if I want to seperate the command to two ```cd home``` ```cat flg.txt``` my shell will not work because this shell did save the current working directory. To accomplish this functionality, I should have a variable ```curr_dir``` to save the current working directory whenever users use ```cd``` command. And call ```cd curr_dir``` each time before user call on their command. Above all is how my interactive shell works.  
    -  Pull:  
      To implement pull, I should first use shell injection command to read the file ```;cat <remote_path>```. Then use python file IO functionality to write the returned string to ```<local_path>```  
    -  Help:  
      List all commands ```shell``` ```pull``` ```help``` ```quit``` and print detail description of each commands  
    -  Quit:  
      Break the loop to end the program.



[1]:https://portswigger.net/web-security/os-command-injection
