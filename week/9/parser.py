import sys
import struct
import datetime 

def bork(msg):
    sys.exit(msg)

MAGIC = 0x8badf00d
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

magic,version = struct.unpack("<LL", data[0:8])
time,_ = struct.unpack("<LL", data[8:16])
timestamp = datetime.datetime.fromtimestamp(time)
author = struct.unpack("<8s", data[12:20])
section_count,_ = struct.unpack("<LL", data[20: 28])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: %s" % str(timestamp))
print("AUTHOR: %s" % author )
print("SECTION COUNT: %d" % int(section_count))
print("-------  BODY  -------")

offset = 24
for x in range(section_count) :
	print("-------  SEC"+str(x+1)+"  -------")

	offset1 = offset+8
	stype, slen = struct.unpack("<LL", data[offset:offset1])
	print(stype)
	
	if stype == 1:
		sval = struct.unpack("<" + str(slen) + "s", data[offset1:offset1 + slen])
		print(sval[0])
	elif stype == 2:
		sval = struct.unpack("<" + str(slen) + "s", data[offset1:offset1 + slen])
		print(sval)
	elif stype == 3:
		sval = struct.unpack("<" + str(slen / 4) + "L", data[offset1:offset1 + slen / 4])
		print(sval)
	elif stype == 4:
		sval = struct.unpack("<" + str(slen / 8) + "Q", data[offset1:offset1 + slen / 8])
		print(sval)
	elif stype == 5:
		sval = struct.unpack("<" + str(slen / 8) + "Q", data[offset1:offset1 + slen / 8])
		print(sval)
	elif stype == 6:
		f1,f2 = struct.unpack("dd",data[offset1:offset1 + slen])
		print(str(f1) + " " + str(f2))
	elif stype == 7:
		sval = struct.unpack("<L", data[offset1:offset1 + slen])
		print(sval)
	elif stype == 8:
		print("PNG file")

		png_header = "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a"
		with open("save.png", 'wb') as f:
			f.write(png_header)
			f.write(data[offset1:offset1 + slen])
	else:
		bork("fail")

	offset += 8 + slen

print("-------  END   -------")
