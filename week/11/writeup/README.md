# Writeup 1 - Web I

Name: *Yuting Zhong*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *Yuting Zhong*


## Assignment details
This assignment has two parts. It is due by 11/27/19 at 11:59PM.

**There will be late penalty of 5% per day late!**

### Part 1 (40 Pts)
Each url of the vuln goods are end with `?id=` so I think I could try sql injection on them. 
I tried `id = 0'` but it did not work.
Then I tried `http://142.93.136.81:5000/item?id=0'||'1'='1` and it worked.
Flag:`CMSC389R-{y0u_ar3_th3_SQ1_ninj@}`
### Part 2 (60 Pts)

 1. This is a xss attack so I need to find a place where I could insert my malicious code. After reading the source code, I know that the server will perform query by using user's raw input from the text entry, So the text entry is the right place to insert code. The code I insert is `<script>alert();</script>` and it successfully rendered in my browser. Level 1 passed.

 2. Hint #3 tells me to use img onerror attribute. So I tried `<img a = '' onerror = alert()>` and alert window appeared. Level 2 passed. 

 3. Similar to level 2. I find it handles user's at the end of the url. So instead of putting numbers here, I put my code `<img a = '' onerror = alert()>` here and the alert window appeared. Level 3 passed.

 4. After reading the source code, I saw the way they use user's input is `<img src="/static/loading.gif" onload="startTimer('{{ timer }}');" />` So I just need a to use `');` to close the `onload` function and add my alert function after the semicolon. They already provide the tail `');" />` to end my alert function so I just need to pass in `alert('`. Overall, the input should be `');alert('`. Level 4 passed.

 5. Hint3 tells me to make the link excute javascript code. So I tried to assign `javascript:alert()` to next and I clicked on Next>> button, it worked. Level 5 passed.

 6. After read the functions I know it will load something from a url. Hint 4 suggests me to use api from google. So I tried `https://xss-game.appspot.com/level6/frame#//google.com/jsapi?callback=alert` and it worked. Level 6 passed.

