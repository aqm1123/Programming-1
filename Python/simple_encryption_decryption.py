""" Simple Encryption and Decryption techniques """

def is_valid_mapping(mapping):

	list_len_keys = []
	list_len_values = []

	#find length of key
	for x in mapping.keys():
		list_len_keys.append(len(x))
	#find length of value
	for y in mapping.values():
		list_len_values.append(len(y))
	#check that all keys are valid
	if len(set(list_len_keys)) > 1:
		return False
	#check if there is only one length of values
	if len(set(list_len_values)) > 1:
		return False

	list_all_keys = []
	list_all_values = []
	#Ccollection of keys and values
	for x in mapping.keys():
		list_all_keys.append(x)

	for y in mapping.values():
		list_all_values.append(y)

	#count the frequency of keys and values
	counter_keys = []
	counter_values = []
	for x in set(list_all_keys):
		appendlist = []
		appendlist.append(x)
		appendlist.append(list_all_keys.count(x))
		counter_keys.append(appendlist)

	for x in set(list_all_values):
		appendlist = []
		appendlist.append(x)
		appendlist.append(list_all_values.count(x))
		counter_values.append(appendlist)

	for i in range(len(counter_keys)):
		if counter_keys[i][1] > 1:
			return False
	for i in range(len(counter_values)):
		if counter_values[i][1] > 1:
			return False

	return True

def is_valid_mapping_for_message(mapping, message):

	list_all_keys = []
	for x in mapping.keys():
		list_all_keys.append(x)

	#joins all keys to check if valid mapping for message is possible
	
	jointed = ''.join(list_all_keys)

	#check if part of message is in collection of keys
	for i in range(len(message)):
		if message[i] not in jointed:
			return False

	return True

def reverse_mapping(mapping):

	new_dic = {}

	#change locations of keys and values
	for x, y in mapping.items():
		new_dic[y] = x

	return new_dic

def combine_mapping(mapping1, mapping2):

	for x, y in mapping1.items():
		for x1, y1 in mapping2.items():
			if x == x1 or len(x) != len(x1) or len(y) != len(y1):
				return None

	#places the keys and values of mapping2 into mapping1

	for x1, y1 in mapping2.items():
		mapping1[x1] = y1

	return mapping1

def message_statistics(message, encoded_message): 

	all_letters = []
	
	
	letters_message = []
	letters_encoded_message = []
	#seperate letters in message
	for x in message:
		letters_message.append(x)
		all_letters.append(x)
	for y in encoded_message:
		letters_encoded_message.append(y)
		all_letters.append(y)

	message_counter = []
	for x in sorted(set(letters_message)):
		appendlist = []
		appendlist.append(x)
		appendlist.append(letters_message.count(x))
		message_counter.append(appendlist)

	encoded_message_counter = []
	for x in sorted(set(letters_encoded_message)):
		appendlist = []
		appendlist.append(x)
		appendlist.append(letters_encoded_message.count(x))
		encoded_message_counter.append(appendlist)

	return_dictionary = {}

	for x in range(len(message_counter)):
		for i in range(len(encoded_message_counter)):
			if message_counter[x][0] == encoded_message_counter[i][0]:
				return_dictionary[message_counter[x][0]] = [message_counter[x][1], encoded_message_counter[i][1]]
	
	present_key = []
	for key in return_dictionary.keys():
		present_key.append(key)

	for i in range(len(message_counter)):
		if message_counter[i][0] not in present_key:
			return_dictionary[message_counter[i][0]] = [message_counter[i][1], 0]

	for i in range(len(encoded_message_counter)):
		if encoded_message_counter[i][0] not in present_key:
			return_dictionary[encoded_message_counter[i][0]] = [0, encoded_message_counter[i][1]]

	return return_dictionary

def substitution_encode(mapping, message):


	list_keys = []
	list_values = []
	len_key = 0

	#seperate keys and values into list
	for x, y in mapping.items():
		list_keys.append(x)
		len_key = len(x)
		list_values.append(y)

	#changes the key to a value into new message
	new_message = ''
	for i in range(len(message)):
		for x in range(len(list_keys)):
			if i % len_key == 0:
				if message[i: i + len_key] == list_keys[x]:
					new_message += list_values[x]

	return new_message


def substitution_decode(mapping, message):

	#LOL just swtich keys with values
	list_keys = []
	list_values = []
	len_value = 0

	for x, y in mapping.items():
		list_keys.append(x)
		len_value = len(y)
		list_values.append(y)


	new_message = ''
	for i in range(len(message)):
		for x in range(len(list_values)):
			if i % len_value == 0:
				if message[i: i + len_value] == list_values[x]:
					new_message += list_keys[x]

	return new_message

def get_caesar_mapping(shift, message):

	return_dictionary = {}

	list_letters_message = set(list(message))
	
	for x in list_letters_message:
		#checks wether it should rotate or not
		if ord(x) + shift > 126:
			new_shift = ord(x) + shift - 95
			return_dictionary[x] = chr(new_shift)
		elif ord(x) + shift < 32:
			new_shift = 95 + (ord(x) + shift)  
			return_dictionary[x] = chr(new_shift )
		else:
			return_dictionary[x] = chr(ord(x) + shift)

	return return_dictionary

def caesar_encode(shift, message):

	message_dictionary = get_caesar_mapping(shift, message)
	xvalues = []
	yvalues = []

	for x, y in message_dictionary.items():
		xvalues.append(x)
		yvalues.append(y)

	#CHEcks to see if keys match with letter in message
	new_message = ''
	for x in range(len(message)):
		for i in range(len(xvalues)):
			if message[x] == xvalues[i]:
				new_message += yvalues[i]

	return new_message

def caesar_decode(shift, message):

	message_dictionary = get_caesar_mapping(-shift, message)
	yvalues = []
	xvalues = []

	for x, y in message_dictionary.items():
		xvalues.append(x)
		yvalues.append(y)
		
	#simply the reverse for the caesar_encode
	new_message = ''
	for x in range(len(message)):
		for i in range(len(xvalues)):
			if message[x] == xvalues[i]:
				new_message += yvalues[i]

	return new_message



def vigenere_encode(secret, message):

	shift_list = []

	for x in secret:
		shift_list.append(ord(x) - ord('a'))


	divided_words = []

	for x in range(len(message)):
		if x % len(shift_list) == 0:
			divided_words.append(message[x:x+len(shift_list)])

	new_word = ''

	for x in range(len(divided_words)):
		for i in range(len(divided_words[x])):
			if ord(divided_words[x][i]) + shift_list[i] > 126:
				new_shift = ord(divided_words[x][i]) + shift_list[i] - 95
				new_word += chr(new_shift)
			elif ord(divided_words[x][i]) + shift_list[i] < 32:
				new_shift = 95 + (ord(divided_words[x][i]) + shift_list[i]) 
				new_word += chr(new_shift)
			else:
				new_word += chr(ord(divided_words[x][i]) + shift_list[i]) 


	return new_word


def vigenere_decode(secret, message):

	shift_list = []

	for x in secret:
		#just swtich this order
		shift_list.append(ord('a') - ord(x))

	divided_words = []

	for x in range(len(message)):
		if x % len(shift_list) == 0:
			divided_words.append(message[x:x+len(shift_list)])

	new_word = ''

	for x in range(len(divided_words)):
		for i in range(len(divided_words[x])):
			if ord(divided_words[x][i]) + shift_list[i] > 126:
				new_shift = ord(divided_words[x][i]) + shift_list[i] - 95
				new_word += chr(new_shift)
			elif ord(divided_words[x][i]) + shift_list[i] < 32:
				new_shift = 95 + (ord(divided_words[x][i]) + shift_list[i]) 
				new_word += chr(new_shift)
			else:
				new_word += chr(ord(divided_words[x][i]) + shift_list[i]) 


	return new_word



def rail_encode(num_rails, message):
	#WATCHED A VID ON HOW A GUY DID IT BY HAND AND PUT IT INTO CODE
	#preparing message for rail encode by changing default message to correct format 
	upper_case = ''
	#replaces all lower case values with upper case using chr and ord
	#replace anything that is not a letter with '.'
	for i in range(len(message)):
		if ord(message[i]) not in range(97, 123) and ord(message[i]) not in range(65, 91):
			upper_case += '.'
		elif ord(message[i]) in range(97, 123):
			upper_case += chr(ord(message[i]) - 32)

		else:
			upper_case += message[i]
	if num_rails < 2:
		return upper_case

	d = 1
	ud = 0
	r = 0
	drawing = []

	for i in range(num_rails):
		drawing.append(list(' ' * len(message)))

	#place the letters to it's corresponding position on the drawing
	for x in range(len(drawing[0])):
		drawing[ud][r] = upper_case[x]
		ud += d 
		r += 1
		#check to see if it hits an edge so it reverses
		if ud + 2 == 1 + len(drawing):
			d = -1
		elif ud == 0:
			d = 1
		else:
			continue
	
	#goes rail by rail adding any letters or '.' into the message return
	message_return = ''
	for i in range(len(drawing)):
		for x in range(len(drawing[i])):
			if drawing[i][x] != ' ':
				message_return += drawing[i][x]
			else:
				continue
	return message_return

def rail_decode(num_rails, message):

	#return the exact message if number is less than two
	if num_rails < 2:
		return message
	##create a drawing like the one in the pdf provided
	drawing = []
	for i in range(num_rails):
		drawing.append(list(' ' * len(message)))
	
	d = 1
	ud = 0
	r = 0
	p = 0

	#places the * into where the letters will be placed 
	#if it reaches a barrier then swtich the direction
	for x in range(len(drawing[0])):
		drawing[ud][r] = '*'
		ud += d 
		r += 1
		if ud + 2 == 1 + len(drawing):
			d = -1
		elif ud == 0:
			d = 1
		else:
			continue
		
	#checks to see if the 
	for x in range(len(drawing)):
		for i in range(len(drawing[x])):
			if drawing[x][i] == '*':
				drawing[x][i] = message[p]
				p += 1

	message_return = ''
	
	d = 1
	ud = 0
	r = 0
	
	#checks each row and column for the correct place of the letters in drawing and places them into
	#the message return  
	for x in range(len(drawing[0])):
		message_return += drawing[ud][r]
		ud += d 
		r += 1
		if ud + 2 == 1 + len(drawing):
			d = -1
		elif ud == 0:
			d = 1
		else:
			continue
		
	return message_return


def read_mapping_file(file_name):

	filereader = open(file_name, 'r')
	key_value = filereader.readlines()
	filereader.close()
	dictionary = {}

	for x in range(1, len(key_value)):
		#checks to see wether it's the last one
		if x + 1 == len(key_value):
			dictionary[key_value[x][:int(key_value[0][0])]] =  key_value[x][int(key_value[0][0]) + 1:]
		else:
			dictionary[key_value[x][:int(key_value[0][0])]] =  key_value[x][int(key_value[0][0]) + 1:-1]
	return dictionary




def write_mapping_file(file_name, mapping):

	f = open(file_name, 'w')

	len_key = 0
	len_value = 0

	for x, y in mapping.items():
		len_key = len(x)
		len_value = len(y)

	f.write(str(len_key) + ',' + str(len_value) + '\n')

	key_value_list = []
	for key, value in mapping.items():
		key_value_list.append(str(key) + ',' + str(value) + '\n')
	
	#are you reading this?
	for i in range(len(key_value_list)):
		if i + 1 == len(key_value_list):
			f.write(key_value_list[i][:-1])

		else:

			f.write(key_value_list[i])

	f.close()


def encode_to_file(cipher_name, cipher_info, file_name):

	#write to file to specified encoding type
	if cipher_name == "substitution":
		encoded_message = substitution_encode(cipher_info[0], cipher_info[1])
		write_mapping_file('encoding_'+file_name,cipher_info[0])
		f = open(file_name, 'w')
		f.write("substitution\n")
		f.write('encoding_' + file_name + '\n')
		f.write(encoded_message)
		f.close()

	elif cipher_name == "caesar":
		encoded_message = caesar_encode(cipher_info[0], cipher_info[1])
		f = open(file_name, 'w')
		f.write("caesar\n")
		f.write(str(cipher_info[0])+'\n')
		f.write(encoded_message)
		f.close()


	elif cipher_name == "vigenere":
		encoded_message = vigenere_encode(cipher_info[0], cipher_info[1])
		f = open(file_name, 'w')
		f.write("vigenere\n")
		f.write(cipher_info[0]+'\n')
		f.write(encoded_message)
		f.close()


	elif cipher_name == "rail":
		encoded_message = rail_encode(cipher_info[0], cipher_info[1])
		f = open(file_name, 'w')
		f.write("rail\n")
		f.write(str(cipher_info[0])+'\n')
		f.write(encoded_message)
		f.close()

def decode_from_file(file_name):

	filereader = open(file_name, 'r')
	cipher_type = filereader.readline()
	variable = filereader.readline()[:-1]
	message = filereader.readline()
	filereader.close()
	#calls previous written functions
	if cipher_type == "substitution\n":
		dictionary = read_mapping_file('encoding_'+file_name)
		return substitution_decode(dictionary, message)

	elif cipher_type ==  "caesar\n":
		return caesar_decode(int(variable), message)

	elif cipher_type == "vigenere\n":
		return vigenere_decode(variable, message)

	elif cipher_type == "rail\n":
		return rail_decode(int(variable), message)
	else:
		return None

def main():

	encode_or_decode = input('What would you like to do, encode or decode? (e, d): ')
	if encode_or_decode == 'e':
		cipher_type = input('Which of three ciphers would you like to use: Caesar, Vigenère, or rail fence? (c, v, r): ')
		
		if cipher_type == 'c':
			message = input('Message: ')
			file_name = input("Filename to output to: ")
			shift = int(input("Shift: "))

			encoded_message = caesar_encode(shift, message)
			encode_to_file('caesar', (shift, message), file_name)
			print(encoded_message)
		
		elif cipher_type == 'v':
			message = input('Message: ')
			file_name = input("Filename to output to: ")
			secret = input("Secret phrase: ")

			encoded_message = vigenere_encode(secret, message)
			encode_to_file('vigenere', (secret, message), file_name)
			print(encoded_message)

		elif cipher_type == 'r':
			message = input('Message: ')
			file_name = input("Filename to output to: ")
			rail_number = int(input("Number of rails: "))

			encoded_message = rail_encode(rail_number, message)
			encode_to_file('rail', (rail_number, message), file_name)
			print(encoded_message)

	elif encode_or_decode == 'd':
		file_to_decode = input("What file would you like to decode?: ")
		new_file = input("Name of file to write the decoded message to: ")

		decoded_message = decode_from_file(file_to_decode)
		if decoded_message == None:
			print('unable to decode')

		else:
			print(decoded_message)
			filehandler = open(new_file, 'w').write(decoded_message)
			#filehandler.close()
			
main()
