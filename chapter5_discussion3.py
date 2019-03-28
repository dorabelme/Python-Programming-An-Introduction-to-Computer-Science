msg = ""
for s in "secret".split("e"):
	msg = msg + s
print(msg)

msg = ""
for ch in "secret":
	msg = msg + chr(ord(ch)+1)
print(msg)

