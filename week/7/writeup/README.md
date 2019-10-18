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
  -  ```CMSC389R-{look_I_f0und_a_str1ng}```  From using strings  
          root@kali:~/389Rfall2019/week/7# strings image_dup | grep -P  CMSC389R
          You found the hidden message! CMSC389R-{look_I_f0und_a_str1ng}

  -  ```CMSC389R-{abr@cadabra}``` From the PNG file embed in the image file.  
    -  Use binwalk to find if there is any file embeded in image  
              root@kali:~/389Rfall2019/week/7# binwalk -e image_dup
              DECIMAL       HEXADECIMAL     DESCRIPTION
              --------------------------------------------------------------------------------
              0             0x0             JPEG image data, EXIF standard
              12            0xC             TIFF image data, big-endian, offset of first image directory: 8
              9899          0x26AB          Copyright string: "Copyright Apple Inc., 2017"
              2395936       0x248F20        PNG image, 960 x 720, 8-bit/color RGBA, non-interlaced
              2395977       0x248F49        Zlib compressed data, best compression
    -  Extract the PNG image
              root@kali:~/389Rfall2019/week/7# dd if=image_dup of=image_hid bs=1 skip=2395936
              63924+0 records in
              63924+0 records out
              63924 bytes (64 kB, 62 KiB) copied, 0.231168 s, 277 kB/s
    -  Flag is inside the PNG image.
