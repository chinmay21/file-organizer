import os
from pathlib import Path
import shutil

def validate_file_path(directory):

    if os.path.isfile(directory):
        print("This path is invalid, only accept folder's path")
    elif os.path.isdir(directory):
        read_folder(directory)
    else:
        print("Please enter a valid path, String can't be accepted!")


def read_folder(directory):
    files = os.listdir(directory)
    files = [f for f in files if os.path.isfile(directory / f)]
    create_nested_folder(files, directory)

def create_nested_folder(files, directory):

    is_document = False
    is_video = False
    is_image = False
    is_music = False

    document = directory / "Document"
    video = directory / "Video"
    image = directory / "Image"
    music = directory / "Music"

    for file in files:
        file_extension = file.rsplit(".", 1)[1]

        match file_extension:
            case "pdf" | "txt":
                is_document = True
            case "mp4" | "mkv" | "mov" | "avi":
                is_video = True
            case "png" | "jpeg" | "jpg":
                is_image = True
            case "mp3" | "wav" | "ogg":
                is_music = True
            case _:
                print("No supported file type found!")
    try:
        if is_document:
            os.makedirs(document)
            print("Document created successfully")
        if is_video:
            os.makedirs(video)
            print("Video created successfully")
        if is_image:
            os.makedirs(image)
            print("Image created successfully")    
        if is_music:
            os.makedirs(music)
            print("Music created successfully")
    except FileExistsError:
        print("The folder already exists")
    except PermissionError:
        print("Access denied to create the folder")
    except:
        print("Something went wrong!")  

    populate_nested_folder(directory)

def populate_nested_folder(directory):
    files = os.listdir(directory)
    files = [f for f in files if os.path.isfile(directory / f)]
    document_folder = directory / "Document"
    video_folder = directory / "Video"
    image_folder = directory / "Image"
    music_folder = directory / "Music"
    for file in files:
        if file.rsplit(".", 1)[1] == "pdf" or file.rsplit(".", 1)[1] == "txt":
            shutil.move(directory/file, document_folder)
            print("File moved successfully")
        elif file.rsplit(".", 1)[1] == "mp4" or file.rsplit(".", 1)[1] == "mkv" or file.rsplit(".", 1)[1] == "mov" or file.rsplit(".", 1)[1] == "avi":
            shutil.move(directory/file, video_folder)
            print("File moved successfully")
        if file.rsplit(".", 1)[1] == "png" or file.rsplit(".", 1)[1] == "jpeg" or file.rsplit(".", 1)[1] == "jpg":
            shutil.move(directory/file, image_folder)
            print("File moved successfully")
        if file.rsplit(".", 1)[1] == "mp3" or file.rsplit(".", 1)[1] == "wav" or file.rsplit(".", 1)[1] == "ogg":
            shutil.move(directory/file, music_folder)
            print("File moved successfully")

def main():
    file_path = input("Enter a folder path to organize: ")
    directory = Path(file_path)
    validate_file_path(directory)


if __name__ == "__main__":
    main()