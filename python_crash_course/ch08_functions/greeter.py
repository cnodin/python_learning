#encoding:utf-8
def greet_user(username):
	print("Hello, " + username.title() + "!")

def get_formatted_name(first_name, last_name):
	"""返回整洁的姓名"""
	full_name = first_name + ' ' + last_name
	return full_name.title()

while True:
	print("\nPlease tell me your name:")
	print("(enter 'q' at any time to quit)")

	f_name = input("First name:")
	l_name = input("Last name:")

	if (f_name == 'q' or l_name == 'q'):
		break

	formatted_name = get_formatted_name(f_name, l_name)
	print("\nHello, " + formatted_name + "!")

