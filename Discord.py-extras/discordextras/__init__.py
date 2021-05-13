"""
This __init__.py file allows Python to read your package files
and compile them as a package. It is standard practice to leave 
this empty if your package's modules and subpackages do not share
any code.
(If your package is just a module, then you can put that code here.)
"""
class Utils:
	def mentiontoID(mention):
		temp1 = str(mention).replace("<", "")
		temp2 = temp1.replace('>','')
		temp3 = temp2.replace('!','')
		userid = temp3.replace('@','')
		return userid