import os
import shutil

def organize_files(directory_path):


# Maping my folders 

    extension_map = {
        'Images': ['.png', '.jpg', '.jpeg', '.gif', '.webp'],
        'Videos': ['.mov', '.mp4'],
        'Audios': ['.mp3'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.pptx'],
        'Code': ['.py', '.js', '.html', '.css'],
        'Compressed': ['.zip', '.rar', '.7z'],
        'Installers': ['.exe', '.msi'],
        'Others': ['.ini', '.rmskin']
    }
    
#Create a destination folder if they don't exists

    for folder in extension_map.keys():
        destination_folder = os.path.join(directory_path, folder)
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
            print(f"Folder '{folder}' created.")

# Iterates through all files in the directory

    for file_name in os.listdir(directory_path):

        if os.path.isdir(os.path.join(directory_path, file_name)):
            continue

        base_name, extension = os.path.splitext(file_name)
        extension = extension.lower()  

        found = False
        for folder, extensions in extension_map.items():
            if extension in extensions:
                source_path = os.path.join(directory_path, file_name)
                destination_path = os.path.join(directory_path, folder, file_name)
                
                shutil.move(source_path, destination_path)
                print(f"File '{file_name}' moved to the folder '{folder}'.")
                found = True
                break
        
# Move to "Others" folder when not find

        if not found and extension == '':
            source_path = os.path.join(directory_path, file_name)
            destination_path = os.path.join(directory_path, 'Others', file_name)
            shutil.move(source_path, destination_path)
            print(f"File '{file_name}' moved to the folder 'Others'.")
        elif not found:
            print(f"No folder found for the file '{file_name}'.")




directory_to_organize = r"C:\Users\coffe\Downloads"

# call the function
organize_files(directory_to_organize)