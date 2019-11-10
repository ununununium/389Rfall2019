# Writeup 9 - Forensics II

Name: *Yuting Zhong*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *Yuting Zhong*


## Assignment details

### Part 1 (45 Pts)
1. Warmup: what IP address has been attacked?
  -  ```142.93.136.81``` Find the IP address from dnsdumpster.
2. What kind of assessment tool(s) were the attackers using against the victim machine? List the name(s) of the tool(s) as well.

3. What are the hackers' IP addresses, and where are they connecting from?

4. What port are they using to steal files on the server?

5. Which file did they steal? What kind of file is it? Do you recognize the file?

6. Which file did the attackers leave behind on the server?

7. What is a countermeasure to prevent this kind of intrusion from happening again? Note: disabling the vulnerable service is *not* an option.

### Part 2 (55 Pts)

After looking at a file that you discovered in #6 above, we were unable to identify its file type or any program that can open it. Fortunately, our friends at UMDCSEC were able to dig up a file specification sheet for this file type! Can you write a parser for us and tell us what the file contains?

Here is file's spec sheet [here](fpff-spec.md). Once you write the parser, report back with what you've found!

Perform the following tasks:

1. Develop the parser, using both the
[specification](fpff-spec.md) and
`greetz.fpff` for reference. [stub.py](stub.py) contains the beginnings of a Python parser, if
you'd like to develop in Python.

2. Parse `greetz.fpff`, and report the following information:
    1. When was `greetz.fpff` generated?
    2. Who authored `greetz.fpff`?
    3. List each section, giving us the data in it *and* its type.
    4. Report *at least* one flag hidden in `greetz.fpff`. Any other flag found will count as bonus points towards the *competition* portion of the syllabus.  
     - ```CMSC389R-{h0w_2_iNt0_DNS_r3c0Rd5}``` : From txt records of the DNS.  
