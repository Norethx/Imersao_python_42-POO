import string
import re

def space_case(name: str) -> bool:
	name_trim = name.strip()
	if not len(name_trim):
		return False
	return True

def empty_name(name: str) -> bool:
	if name == "":
		return False
	return True

def digit_case(name: str) -> bool:
	result = any(x.isdigit() for x in name)
	return not result

def special_case(name: str) -> bool:
	result = set(name).intersection(set(string.punctuation))
	return not result

def format_name(name : str) -> str:
	formated_name = space_between(name).upper()
	return formated_name

def space_between(name: str) -> str:
	name_trimmed = " ".join(name.split())
	print(name_trimmed)
	return name_trimmed

def remove_suffix(name: str) -> str:
	suffix = ["DOS", "DAS", "DE", "DA", "VON"]
	result = name.split()
	for i in result:
		for x in suffix:
			if x == i:
				result.remove(i)
	format_string = " ".join(result)
	return format_string

def abbreviation_undername(name: str) -> str:
	suffix = {
		"JUNIOR": "JR",
		"NETO": "N",
		"FILHO": "F"
	}
	result = name.split()
	for i in range(0, len(result)):
		for key, value in suffix.items():
			if key == result[i]:
				result[i] = value
	format_string = " ".join(result)
	return format_string

def fit(name: str) -> str:
	name = format_name(name)
	if not space_case(name):
		print("Error")
	if not empty_name(name):
		print("Error")
	if not digit_case(name):
		print("Error")
	if not special_case(name):
		print("Error")
	if not space_between(name):
		print("Error")
	name = remove_suffix(name)
	name = abbreviation_undername(name)
	if len(name) > 26:
		return name[0:26]
	return name