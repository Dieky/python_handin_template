import argparse
import csv

def run():
    if(args.file):
        #tag imod path og skriv content af filen til en ny file med "--file" navnet
        result_list = read_file(args.path)
        write_list_to_file(args.file,result_list)
    elif(args.add):
        append_list(args.path,args.add)
    elif(args.path):
        print_file_content(args.path)
    elif(args.halp):
        print("HELP")
    

def append_list(input_file,list_to_add):
    with open(input_file,"a") as f_obj:
        f_obj.write("\n"+list_to_add)
    
    
def read_file(input_file):
    final_list = []
    with open(input_file) as f:
        for line in f:
            final_list.append(line)
    return final_list

def print_file_content(filename):
    with open(filename) as f_obj:
        content = f_obj.readlines()

        for line in content[0:20]:
            print(line.rstrip())

def write_list_to_file(output_file, lst):
    with open(output_file, 'w') as file_object:
        for value in lst:
            for x in value:
                file_object.write(x)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A program that takes a path and if provided with a second filename, will write the content to a new file with filename')
    parser.add_argument('path',help='Enter the name of the file you want to work on. Providing a single file will print the content to the console')
    parser.add_argument('--file','-f',help='Writes the result in a new file with the chosen name')
    parser.add_argument('--add','-a',help='Appends the content of the given list to the end of the file')
    args = parser.parse_args()
    run()