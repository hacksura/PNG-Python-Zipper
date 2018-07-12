import os
import zipfile
import datetime

def get_month():

	now = datetime.datetime.now()

	month_number = int(now.month)
	month_name = ""

	if(month_number == 1):
		month_name = "January"
	elif(month_number == 2):
		month_name = "February"
	elif(month_number == 3):
		month_name = "March"
	elif(month_number == 4):
		month_name = "April"
	elif(month_number == 5):
		month_name = "May"
	elif(month_number == 6):
		month_name = "June"
	elif(month_number == 7):
		month_name = "July"
	elif(month_number == 8):
		month_name = "August"
	elif(month_number == 9):
		month_name = "September"
	elif(month_number == 10):
		month_name = "October"
	elif(month_number == 11):
		month_name = "November"
	elif(month_number == 12):
		month_name = "December"

	return month_name

def get_day():
	now = datetime.datetime.now()
	current_day = now.day
	return current_day

def get_year():
	now = datetime.datetime.now()
	current_year = now.year
	return current_year

def get_file_name():
	current_day = str(get_day())
	current_month_name = get_month()
	current_year = str(get_year())
	return current_day + " " + current_month_name + " " + current_year + ".zip"
	
def construct_zip():
	zip_file_name = get_file_name()

	file_zipping = zipfile.ZipFile(zip_file_name, 'w')
 
	for folder, subfolders, files in os.walk('./'):
	    for file in files:
		if file.endswith('.png'):
			file_zipping.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), './'), compress_type = zipfile.ZIP_DEFLATED)
	
	file_zipping.close()

def delete_contents():
	for folder, subfolders, files in os.walk('./'):
	    for file in files:
		if file.endswith('.png'):
			os.remove(file)


def main():
	construct_zip()
	delete_contents()

if __name__ == "__main__":
	main() 

