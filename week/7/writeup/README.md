# Writeup 7 - Forensics I

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *PUT YOUR NAME HERE*

## Assignment Writeup

### Part 1 (100 pts)
Answer the following questions regarding [this](../image) file:

1. What kind of file is it?
  -  It is a JPEG.

2. Where was this photo taken? Provide a city, state and the name of the building in your answer.
  -  City: Chicago
  -  State: IL
  -  Name of building: John Hancock Center
3. When was this photo taken? Provide a timestamp in your answer.
  -  2018:08:22 11:33:24
4. What kind of camera took this photo?
  -  iPhone 8
5. How high up was this photo taken? Provide an answer in meters.
  -  539.5 m 
6. Provide any found flags in this file in standard flag format.    
  -  ```CMSC389R-{look_I_f0und_a_str1ng}```  From using strings ```strings image_dup | grep -P  "CMSC389R"```
  -  
