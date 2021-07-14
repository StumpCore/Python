print(10)
print(str(10))
print(repr(10))

test_Str = "Here is a \n newline!"
print(test_Str) #prints the statement including the space
print(repr(test_Str)) #prints statement including the canoncical source-code

print("{}".format(test_Str))
print("{!r}".format(test_Str))

s = format(32.3, "<+08.3f")
print(s) #aling (left,right), sign, 0, width, precision
n1,n2 = 777,999
print("**{:10}**{:2}".format(n1,n2)) # width 10 oder 2, if content > number than maximum of character

print("{:->24}".format("Hey Bill G, pick me")) #working with format method necessary, minus fill character, and align (>) to the right, 24 is the width

print("{:>7}".format("Tom"))
print("{:@>7}".format("Tom"))
print("{:#>7}".format("Tom"))
print("{:#^7}".format("Tom"))

n3 = 7020000458

print("{:012}".format(n3))
print("{:09}".format(n3))