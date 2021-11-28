# AUTO-FILE-ORAGNIZATION-BANDISH-SHAH
Here I am going to explain about the code and how to execute it.....
So starting with the header files, they are predefined Python libraries that will be used to execute this code.
Moving on to '\\' section it will directly enter into the source and dsetination folder while giving path in GUI window. It will get linked with the GUI code.
Now moving on to looping, os.listdir will move the files in (i) which is temp variable from source folder one by one.
Now using by using split_tuple(which is also a predefined library) we will split the the file name and extension, by placing 'file-name' on 0th index and '.extension' on 1st index.
Now we will be storing the elements of 1st index in variable named extension.
Now by using slicing method on Extension variable, we will place '.' on 0th index and 'extension' on first index, and move the file on basis of extension.
Now by placing 'if' condition we will check for a folder in the source folder, if there will be any folder in source folder it will skip that and will return back to file extensions.
Now again by placing if statement again for destination folder, we will be checking for any existing folder in destination source, then it will carry the same procedure, which is used in source folder, here it will paste the files by exetension group, and will skip the file whose folder already exist in destination folder.
Now moving to os.path, it will create a folder path for the files on basis of there extension whose folder is not existing in the destination folder.
Now we will be giving path for source folder(from where the files will be copied) and destination(where are the files will get moved) for the GUI window.
Now again by placing if statement for GUI window, it will transfer the files and will skip the already existing files.
And lastly using Shutil(which is again a predefied library) we will move the file from source folder to destination folder.
