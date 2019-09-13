# Writeup 2 - OSINT

Name: *Yuting Zhong*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *Yuting Zhong*

## Assignment Writeup

### Part 1 (45 pts)

1. Real Name: Eric J. Norman(or Eric Norman)
2. Company Name: *Wattsamp Energy* Website: http://wattsamp.net/
3. Personal Info:
    - Address: 1300 Adabel Dr, El Paso, TX 79835, US
    - Phone:+1 2026562837
    - Email: ejnorman84@gmail.com
        + I got his contact information and address from using the tool whois on kali
        ```root@kali:~# whois wattsamp.net```
    - Instagram Username: ejnorman84
    - Reddit UserName: ejnorman84
        + On instantusername.com, search ejnorman84,
        and it shows that the username has been taken on Instagram
        and reddit and some of other websites.
        I checked each website and find that the user on instagram followed
        UMD, so it is definitely the target. The user on reddit commented on
        ChesterEnergyDC "It surprises me that Texas isn't on this list!".
        The instagram post shows he is a Texas football fan and he works in
        an energy company, so I think this is his reddit account.
4. IP Addresses:
    - IP: 157.230.179.99
    location:  DigitalOcean, LLC 101 Ave of the Americas 10th Floor New York NY 10013 US
        + I got the IP from https://dnsdumpster.com by giving the domain name.
        I got server location from https://dnsdumpster.com by giving the IP address.  
5. Hidden Directory/Files  

    I Got this by using DirBuster
        /
        /assets/
        /views/
        /vendor/
        /vendor/bootstrap/
        /vendor/jquery/
        /vendor/bootstrap/css/
        /vendor/bootstrap/js/

        /index.html
        /views/about.html
        /views/admin.html
        /views/signin.css
        /vendor/jquery/jquery.min.js
        /vendor/jquery/jquery.min.map
        /vendor/jquery/jquery.js
        /vendor/jquery/jquery.slim.min.js
        /vendor/jquery/jquery.slim.js
        /vendor/jquery/jquery.slim.min.map
        /vendor/bootstrap/css/bootstrap-grid.css
        /vendor/bootstrap/css/bootstrap-grid.min.css
        /vendor/bootstrap/css/bootstrap-grid.css.map
        /vendor/bootstrap/js/bootstrap.bundle.min.js
        /vendor/bootstrap/css/bootstrap-reboot.css
        /vendor/bootstrap/css/bootstrap-grid.min.css.map
        /vendor/bootstrap/js/bootstrap.bundle.js.map
        /vendor/bootstrap/css/bootstrap-reboot.css.map
        /vendor/bootstrap/css/bootstrap-reboot.min.css
        /vendor/bootstrap/js/bootstrap.bundle.js
        /vendor/bootstrap/css/bootstrap-reboot.min.css.map
        /vendor/bootstrap/js/bootstrap.min.js
        /vendor/bootstrap/js/bootstrap.js
        /vendor/bootstrap/js/bootstrap.js.map
        /vendor/bootstrap/js/bootstrap.min.js.map
        /vendor/bootstrap/css/bootstrap.css
        /vendor/bootstrap/css/bootstrap.min.css
        /vendor/bootstrap/css/bootstrap.css.map
        /vendor/bootstrap/css/bootstrap.min.css.map
        /vendor/bootstrap/js/bootstrap.bundle.min.js.map

6. Open Ports:  
Discovered by using nmap
```root@kali:~# nmap -v -A -p 1-5000 157.230.179.99```
|ports|service|system                                                       |
|---  |---    |---                                                          |
|  22 |  ssh  | OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)|
|  80 | http  |  Apache httpd 2.4.29 ((Ubuntu))                             |
|1337 | waste |                                                             |  

  ![Alt][port_scan_result]

7. The system that hosting the site is Apache httpd 2.4.29 (Ubuntu). The same approach as above.
    The result from nmap shows that the system that doing http service is Apache httpd 2.4.29 (Ubuntu)

8.  
  ```CMSC389R-{n0_indexing_pls}```  
  ```CMSC389R-{html_h@x0r_lulz}```  
  ```CMSC389R-{Do_you-N0T_See_this}```  
  ```CMSC389R-{LOOKING_CLOSELY_PAYS}```   
  ```CMSC389R-{!enough_nrg_4_a_str0ng_Pa$$wrd}```




### Part 2 (75 pts)  
Based on the result of nmap scan, I believe the target port is 1337.
I tried ```nc 157.230.179.99 1337```, and then captcha appears. To get rid of this captcha is easy, just use regular expression to extract out the first number, second number, operator then calculate the result and send it back to the server. To brute force the password, I need to iterate through the dictionary. The first time I tried is using one loop and it turns out really inefficient. That is because each iteration, I have to answer the captcha and it is time consuming. Therefore, I modified my script to a multi thread brute force program. And it works! After waiting for 2 hours, I got the password:```hello1```   
![Alt][getpassword]  

GetShell  

![Alt][getshell]  

Cd to home and I find the flag, here it is  
```CMSC389R-{!enough_nrg_4_a_str0ng_Pa$$wrd}```

[port_scan_result]: /screen_shots/port_scan_result.png
[getpassword]: /screen_shots/getpassword.png
[getshell]: /screen_shots/getshell.png
