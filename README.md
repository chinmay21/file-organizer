# File Organizer

A simple Python program that organizes files in a selected folder into separate categories based on their file extensions.

## Features

* Accepts a folder path from the user.
* Validates whether the provided path is a directory.
* Detects supported file types using their extensions.
* Automatically creates category folders when required.
* Moves supported files into their respective folders.
* Handles common file-system errors such as invalid paths, permission issues, and existing folders.

## Supported File Types

| Category | Extensions                     |
| -------- | ------------------------------ |
| Document | `.pdf`, `.txt`                 |
| Video    | `.mp4`, `.mkv`, `.mov`, `.avi` |
| Image    | `.png`, `.jpeg`, `.jpg`        |
| Music    | `.mp3`, `.wav`, `.ogg`         |

## How It Works

1. The program asks the user to enter a folder path.
2. The path is validated to ensure it points to a directory.
3. Files directly inside the directory are identified.
4. The program checks their extensions against the supported file types.
5. Required category folders are created:

   * `Document`
   * `Video`
   * `Image`
   * `Music`
6. Supported files are moved into their corresponding folders.

## Technologies Used

* Python
* `pathlib`
* `os`
* `shutil`

## How to Run

Make sure Python is installed on your system.

Clone the repository:

```bash
git clone https://github.com/chinmay21/file-organizer.git
```

Navigate into the project:

```bash
cd file-organizer
```

Run the program:

```bash
python main.py
```

Enter the path of the folder you want to organize when prompted.

## Example

Before running the program:

```text
Downloads/
├── movie.mp4
├── song.mp3
├── image.jpg
├── notes.txt
└── document.pdf
```

After running the program:

```text
Downloads/
├── Document/
│   ├── notes.txt
│   └── document.pdf
├── Video/
│   └── movie.mp4
├── Image/
│   └── image.jpg
└── Music/
    └── song.mp3
```

## What I Practiced

This project helped me practice:

* Functions
* Loops and conditional statements
* File and directory handling
* `pathlib`
* `os`
* `shutil`
* Pattern matching with `match`
* Exception handling
* Basic input validation

## Limitations

Currently, the organizer supports a predefined set of file extensions and only organizes files located directly inside the selected folder. Unsupported file types are not moved.

## Future Improvements

* Support more file extensions.
* Make file categories configurable.
* Handle files without extensions safely.
* Prevent filename conflicts when moving files.
* Add recursive organization for files inside subdirectories.
* Improve validation and error handling.