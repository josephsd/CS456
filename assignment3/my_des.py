subKeys,IP,EBIT,P,IPinv,sBox,PC1,PC2,ls = 16*[''],(58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7),(32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1),(16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25),(40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25),((14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7,0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8,4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0,15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13),(15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10,3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5,0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15,13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9),(10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8,13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1,13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7,1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12),(7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15,13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9,10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4,3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14),(2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9,14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6,4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14,11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3),(12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11,10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8,9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6,4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13),(4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1,13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6,1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2,6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12),(13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7,1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2,7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8,2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11)),(57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4),(14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32),(1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1)

def bit_byte(instring):
	return '{0:016x}'.format(int(instring,2))
	
def byte_bit(instring):
	return '{0:064b}'.format(int(instring,16))

def split(instring):
	return instring[:len(instring)/2],instring[len(instring)/2:]

def perm_bit_string(inputstring,permTable):
	output = ''
	for i in permTable:
		output += inputstring[i-1]
	return output

def padData(string):
	padLength = 8-(len(string)%8)
	return string + '\0' * padLength

def unpadData(string):
	return string.replace('\0','')

def setKey(inputstring):

	def leftShift(inkeystring,i):
		left,right = split(inkeystring)
		left = left[ls[i]:] + left[:ls[i]]
		right = right[ls[i]:] + right[:ls[i]]
		return left+right

	permkey = perm_bit_string(inputstring,PC1)
	for i in range(16):
		tempkey = leftShift(permkey,i)
		subKeys[i] = perm_bit_string(tempkey,PC2)
		permkey = tempkey

def sboxval(string, box):
	row, column = string[0] + string[5], string[1:5]
	return '{0:04b}'.format(sBox[box][int(row,2)*16+int(column,2)])

def des(input_block,encrypt):
	input_data = perm_bit_string(input_block,IP)
	left, right = split(input_data)
	for round in range(16):
		if encrypt:
			key = subKeys[round]
		else:
			key = subKeys[15 - round]
		exp_right = '{0:048b}'.format(int(key,2) ^ int(perm_bit_string(right,EBIT),2))
		exp_right_list =  [exp_right[:6],exp_right[6:12],exp_right[12:18],exp_right[18:24],exp_right[24:30],exp_right[30:36],exp_right[36:42],exp_right[42:48]]
		sbox_out = ''
		for i in range(8):
			sbox_out += sboxval(exp_right_list[i],i)	 
		new_right = '{0:032b}'.format(int(perm_bit_string(sbox_out,P),2) ^ int(left,2))
		left = right
		right = new_right
	return perm_bit_string(right+left,IPinv)

def def_key(key):
	deskey = ''
	if len(key)<= 8:
		deskey += padData(key)
	else:
		deskey = key[:8]
	setKey(byte_bit(deskey.encode('hex')))

def encrypt(instring):
	padded = padData(instring)
	content = []
	for i in range(len(padded)/8):
		content.append(padded[i*8:(i+1)*8].encode('hex'))
	outstring = ''
	for i in range(len(content)):
		outstring += bit_byte(des(byte_bit(content[i]),True))
	return outstring

def decrypt(instring):
	content = []
	for i in range(len(instring)/16):
		content.append(instring[i*16:(i+1)*16])
	outputstring = ''
	for i in range(len(content)):
		outputstring += bit_byte(des(byte_bit(content[i]),False)).decode('hex')
	return unpadData(outputstring)