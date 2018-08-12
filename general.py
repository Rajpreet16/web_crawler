import os


#Create a new file 

def write_file(path,data):
	f = open(path, 'w')
	f.write(data)
	f.close()


# Each website we crawl is a new project
def create_project_directory(directory):
	
	if not os.path.exists(directory):
		print('Creating Project' + directory)
		os.makedirs(directory)

# Create queue and crawled files

def create_data_files(project_name , base_url):
	queue = project_name + '/queue.txt'
	crawled = project_name + '/crawled.txt'

	if not os.path.isfile(queue):
		write_file(queue, base_url)

	if not os.path.isfile(crawled):
		write_file(crawled , '')


# Add data onto an existing file

def append_to_file(path, data):

	with open(path, 'a') as file:
		file.write(data + '\n')

# delete the contemt of a file

def delete_file_contents(path):		
	with open(path, 'w') as f:
		f.close()
		


# read a file and convert each line to set items

def file_to_set(file_name):
	resu = set()
	with open(file_name , 'rt') as f:
		for line in f:
			resu.add(line.replace('\n', ''))
	return resu																																																			

# iterate through a set, each item will be a new line in the file 

def set_to_file(links, file_name):
    with open(file_name,"w") as f:
        for l in sorted(links):
            f.write(l+"\n")