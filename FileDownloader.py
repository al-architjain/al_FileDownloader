# A single thread file downloader
import requests
import os

file_url = str(input("Enter URL: "))
r = requests.get(file_url, stream = True)

name = str(input("Enter name of file you wanna save it with: "))

#name = file_url.split('/')[-1]

cwd_list = os.listdir(os.getcwd())
if name not in cwd_list:
	f_name = name
else:
	i = 0
	while True:
		i += 1
		f_name = name + str(i)
		if f_name in cwd_list:
			continue
		else:
			break

with open(f_name,"wb") as f:
	for chunk in r.iter_content(chunk_size=1024):
		if chunk:	
			f.write(chunk)

print('File downloaded :)')
