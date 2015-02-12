#!/usr/bin/env python

class Country:
	def __init__(self, name):
		self.name = name
		
	def NameLen(self):
		return len(self.name)
		
	def Encoder(self):
		self.encoded = []
		for i in self.name:
			lettercode = str(ord(i) + 3)
			self.encoded.append(lettercode)
		return "".join(self.encoded)
		
	def Decoder(self):
		decoded = []
		for i in self.encoded:
			letter = chr(int(i)-3)
			decoded.append(letter)
		return "".join(decoded)
		
	def __str__(self):
		string = ("Hello from {}".format(self.name))
		return string

def main():
	land = Country("Nederland")
	print(land)
	print (land.NameLen())
	print (land.Decoder())
	
main()
