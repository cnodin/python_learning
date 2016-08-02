#encoding:utf-8
def get_formatted_name(first_name, last_name):
	"""返回整洁的姓名"""
	full_name = first_name + ' i ' + last_name
	return full_name

def get_formatted_name(first_name, last_name, middle_name=''):
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
