import sys
import os
import argparse


# 1 first function takes a path to a folder and writes all filenames in the folder to a specified output file
# Default path is current directory
def write_all_filenames_in_folder(path, outputfilename):
    filelist = os.listdir(path)
    filename = outputfilename
    with open(filename, 'w') as file_object:
        for file in filelist:
            file_object.write(file+'\n')

# 2 takes a path to a folder and write all filenames recursively (files of all sub folders to)
def write_all_filenames_and_sub_dirs_recursive(path, outputfilename):
    filename = outputfilename
    with open(outputfilename, "w") as file_object:
        for root, dirs, files in os.walk(path):
            for name in dirs:
                    file_object.write("Directories: " + os.path.join(root,name)+"\n")
            for name in files:
                    file_object.write("File path: " + os.path.join(root,name)+"\n")

# 3 takes a list of filenames and print the first line of each file
def first_line_from_files(filelist):
    final_list = []
    for file in filelist:
        with open(file, "r") as file_object:
            final_list.append(file_object.readlines(1))
    return final_list


# 4 takes a list of filenames and print each line that contains an email (just look for @)
def look_for_email_in_filelist(filelist):
    for file in filelist:
        with open(file, "r") as file_object:
            for line in file_object.readlines():
                if "@" in line:
                    print("Email found: " + line)
                


def read_headline_fromMD(filelist, outfile):
    headline_list = []
    for file in filelist:
        with open(file, "r") as file_object:
            for line in file_object.readlines():
                result = line.find("#")
                if(result == 0):
                    headline_list.append(line)

    with open(outfile, "w") as file_object:
        for line in headline_list:
            file_object.write(line+"\n")


def read_csv(filelist, outfile):
    content_list = []
    for file in filelist:
        with open(file, "r") as file_obj:
            for line in file_obj.readlines():
                content_list.append(line)

    with open(outfile, 'w') as file_object:
        for file in content_list:
            file_object.write(file)


def run():
    path = args.path
    if(args.folder):
        write_all_filenames_in_folder(path, args.outfile)
    if(args.subfolder):
        write_all_filenames_and_sub_dirs_recursive(path, args.outfile)
    if(args.firstline):
        print(first_line_from_files(args.firstline))
    if(args.email):
        look_for_email_in_filelist(args.email)
    if(args.readmd):
        read_headline_fromMD(args.readmd,args.outfile)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='A program that takes up to 3, first 2 are important. Reads a file ')
    parser.add_argument('inputfile', nargs="*",help="File to read from - REQUIRES ATLEAST 1 ARGUMENT")
    parser.add_argument("--subfolder","-sb",help="Reads all folders and subfolders in the selected directory and prints to outfile if provided.")
    parser.add_argument("--folder", help="takes a path to a folder and writes all filenames in the folder to a specified output file")
    parser.add_argument("--firstline","-fl",help="Takes a list of filenames and prints the first line in each file",nargs="*")
    parser.add_argument("--outfile", default="tmp.txt",nargs="?", help="Provide a more accurate name for creating files using this program. default is tmp.txt")
    parser.add_argument('--email',nargs="*", help="takes a list of files and prints each line containing an @")
    parser.add_argument('--path', help="uses current working directory as default path if none is provided",
                        nargs="?", default=os.getcwd())  # Use nargs="?" to use default if no path is given
    parser.add_argument('--readmd','-md',nargs="*", help="takes a list of md files and writes all headlines (lines starting with #) to a file")
    args = parser.parse_args()
    run()


# HUSK R foran path. Det forcer at det bliver formateret som string
# https://stackoverflow.com/questions/37400974/unicode-error-unicodeescape-codec-cant-decode-bytes-in-position-2-3-trunca
#write_all_filenames_and_sub_dirs_recursive(r'C:\Users\Patrick\Desktop\Python\week2', 'listoffiles2.txt')
#write_all_filenames_in_folder(r'C:\Users\Patrick\Desktop\Python\week2', 'listoffiles2.txt')
# look_for_email_in_filelist(listtilfiler)
# read_headline_fromMD(listtilfilermd)
