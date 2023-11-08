import requests 


s = None #start range
e = None #end range 

file_name = None #enter the desired file name
file_extention = None
save_path = None #save location

for i in range(s,e): # either range or list of paths
    
    url = f'SET URL AND REQUIRED ITERATOR POSITION' #CHANGE THIS
    print(f'url_changed to {i}')

# This requests the resource at the given link, extracts its contents 

    data = requests.get(url)
    print(f'done{i}')

# Opening a new file named img with extension .jpg or any extention
# This file would store the data of the image file 

    with open(f'{save_path}/{file_name}{i}.{file_extention}','wb') as f:
        f.write(data.content) 
    print('img complete')

