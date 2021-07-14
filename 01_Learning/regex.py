import re
pattern = r"\d\d\d[ -]\d\d\d[ -]\d\d\d\d$" #$restricted the pattern # [ -]pattern sets " " and "-"
#s = input("Enter tel.number: ")
"""
if re.match(pattern, s): #or re.fullmatch for exact match
    print("number accepted.")
else:
    print("incorrect format.")

"""

reg1 = re.compile(r"[a-z]*.[a-z]*@[a-z]*.(.de|.com)")

def test_item(s):
    if re.match(reg1,s):
        print(s, " is a match.")
    else:
        print(s," is not a match.")

test_item("marc.schinschel@online.de")
test_item("marc.hauser@hsbc.com")

def text_number(n):
    reg2 = r"\d{1,3}(,\d{3})*(\.\d*)"
    if re.match(reg2, n):
        print("success")

text_number("1.00")
text_number("100,000.00")
