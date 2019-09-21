# Operational Security and Social Engineering

## Assignment details

This assignment has two parts. It is due by 9/20 at 11:59 PM.

**There will be a late penalty of 5% off per day late!**

### Part 1

You have been hired by a penetration testing firm and have been asked to collect some specific information about the Wattsamp employee from HW2, Eric Norman. Some of the information you're looking for seems to be unavailable or unlikely to be found through OSINT:

- What's his mother's maiden name?
- What browser does she primarily use?
- What city was she born in?
- What's her ATM pin number?
- What was the name of her first pet?

Write up a pretext that you would use to social engineer this information out of Eric Norman. What approach would you take and how would you present yourself to elicit this information under the radar? Use the slides and what we covered in lecture to come up with a plan to obtain this information.

# Part1 answer  
Based on his reddit post and his instgram post, I know his interest is football. I will send him a fishing email with title "SIGN UP TO GET A SIGNATRUE FROM YOUR FAVORITE STAR" which lead to my fishing website. The website will ask him to select his favorite football super star and after he sign up he will get a signature from that star. At the process of signing up, he will need to answer some security questions:
- What's his mother's maiden name?  
- What browser does she primarily use?
- What city was she born in?
- What's her ATM pin number?
- What was the name of her first pet?  

The website will remind him :  
 - You have to answer these questions to proceed you sign up process. These question will be helpful when you forget your password and trying to reset your password.(ensure he will answer these question)  
 - The home delivery man of your gift signature will also ask you these question to verify your identity.(ensure he give the right answer and make him believe the signature thing is real)


### Part 2

Eric Norman has recently discovered that Watsam's web server has been broken into by the crafty CMSC389R ethical hackers. After reading your published report, he has reached out to you to seek guidance in how he can repair some of the vulnerabilities that you have discovered.
Choose 3 specific vulnerabilities from homework 2 that you have identified (ie. exposed ports, weak passwords, etc.) and write a brief summary of some suggestions you can provide Eric for the Wattsamp web server and admin server. Be as thorough as possible in your answer, use specific examples and citing online research into security techniques that could be applied to the servers (ie. firewall, IDS/IPS, password managers, etc.).

# Part 2 Answer  
- Choose a stronger password
  - Your password is too weak, a weak password will definitely be cracked by hackers' sec-lists. For your case, your password is cracked by my brute force script in 2 hours. Try to come up with a strong password which consists random numbers,combination of capitalized and non-capitalized, and special characters,try to make the length of your password as long as possible. Or you could try some password generator tools https://my.norton.com/extspa/passwordmanager?path=pwd-gen to generate a strong passoword.

- Close unused ports
  - You have your port 1337 open and waste which allow hackers get your shell. Often use nmap to scan your server to see if there is any waste ports and check back on your server if that port is unused, if that is close it.https://www.acunetix.com/blog/articles/close-unused-open-ports/ This websites teaches your how to identify which ports are unused and how to close them.

- Use 2 Factor Authentication on your server
  - Two factor authentication is better than password for identify user's identity. After your entering your password, the server will ask you two do one more thing(a push confirmation, email or text you a verification code) to login. In your case, hackers just need to crack your password the they could do anything on your server, if you implement 2FA on your server, hackers will not able to hack your sever even if they got the password. Here is an article teaches you how to implement 2FA. https://dzone.com/articles/enabling-two-factor-authentication-for-your-web-ap


### Format

The submission should be answered in bullet form or full, grammatical sentences. It should also be stored in `assignments/3_OPSEC_SE/writeup/README.md`. Push it to your GitHub repository by the deadline.

### Scoring

Part 1 is worth 40 points, part 2 is worth 60 points. The rubric with our expectations can be found on the ELMS assignment posting.

Good luck!
