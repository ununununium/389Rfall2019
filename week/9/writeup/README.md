# Writeup 9 - Forensics II

Name: *Yuting Zhong*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *Yuting Zhong*


## Assignment details

### Part 1 (45 Pts)
1. Warmup: what IP address has been attacked?
  -  ```142.93.136.81``` 
2. What kind of assessment tool(s) were the attackers using against the victim machine? List the name(s) of the tool(s) as well.
  - The hacker was bruteforce ports on the server so he/she might used Nmap.
3. What are the hackers' IP addresses, and where are they connecting from?
 - ```159.203.113.181```  They are connecting from 101 Ave of the Americas 10th Floor, New York, 10013, US
4. What port are they using to steal files on the server?
 - server:21, hacker:55914
5. Which file did they steal? What kind of file is it? Do you recognize the file?
 - find_me.jpeg. It is a JPEG file. Yes I do recognize the file.
6. Which file did the attackers leave behind on the server?
 - `greetz.fpff`
7. What is a countermeasure to prevent this kind of intrusion from happening again? Note: disabling the vulnerable service is *not* an option.
 - Limit the ip request faliure times.
 - Use whitelist, only the authorized IPs on the whitelist could access the server.

### Part 2 (55 Pts)

After looking at a file that you discovered in #6 above, we were unable to identify its file type or any program that can open it. Fortunately, our friends at UMDCSEC were able to dig up a file specification sheet for this file type! Can you write a parser for us and tell us what the file contains?

Here is file's spec sheet [here](fpff-spec.md). Once you write the parser, report back with what you've found!

Perform the following tasks:

1. Develop the parser, using both the
[specification](fpff-spec.md) and
`greetz.fpff` for reference. [stub.py](stub.py) contains the beginnings of a Python parser, if
you'd like to develop in Python.
 - `parser.py`
2. Parse `greetz.fpff`, and report the following information:
    1. When was `greetz.fpff` generated?
     	- 2019-03-27 00:15:05
    2. Who authored `greetz.fpff`?
     	- fl1nch
    3. List each section, giving us the data in it *and* its type.  
  		-  -------  SEC1  -------  
  	`SECTION_ASCII` 
  	Hey you, keep looking :)  
    -------  SEC2  -------
    `SECTION_COORD`
    52.336035 4.880673  
	-------  SEC3  -------  
	`SECTION_PNG`
	PNG file exported as save.png  
	-------  SEC4  -------  
	`SECTION_ASCII`
	}R983CSMC_perg_tndid_u0y_yllufep0h{-R983CSMC  
	-------  SEC5  -------  
	`SECTION_ASCII`
	Q01TQzM4OVIte2hleV9oM3lfeTBVX3lvdV9JX2RvbnRfbGlrZV95b3VyX2Jhc2U2NF9lbmNvZGluZ30=  

4. Report *at least* one flag hidden in `greetz.fpff`. Any other flag found will count as bonus points towards the *competition* portion of the syllabus.  
     - ```CMSC389R-{h0w_2_iNt0_DNS_r3c0Rd5}``` : From txt records of the DNS. 
     - ```CMSC389R-{0M3G4LUL_G3T_pWN3d_N00b}```: From the reddit post on the user  v0idcache  
     - ```}R983CSMC_perg_tndid_u0y_yllufep0h{-R983CSMC``` or revesed ```CMSC389R-{h0pefully_y0udidnt_grep_CMSC389R}```: From greetz.fpff section 3.  
     - `CMSC389R-{w3lc0me_b@ck_fr0m_spr1ng_br3ak}`: From the embeded png file.



