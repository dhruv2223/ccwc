import argparse 
import os 
import sys
def no_of_bytes(file_path):
    return os.path.getsize(file_path)
def no_of_characters(content):
    return len(content)
def word_count(content):
    return len(content.split())
def line_count(content):
    return len(content.splitlines())
def max_line_width(content):
    return max([len(line) for line in content.splitlines()])
    
    

def process_file(file_path):
    if os.path.isdir(file_path):
        print(f"ccwc: {file_path} is a directory")

        return {
            "bytes":0,
            "chars":0,
            "words":0,
            "lines":0,
            "max_line_length":0,
      }
        
    else:
        try:
            with open(file_path,'r') as file:
                content = file.read()
        except FileNotFoundError:
            print(f"ccwc: {file_path}: No such file found")
            sys.exit()
        except PermissionError:
            print(f"ccwc: {file_path}: Permission denied")
        return {
            "bytes":no_of_bytes(file_path),
            "chars":no_of_characters(content),
            "words":word_count(content),
            "lines":line_count(content),
            "max_line_length":max_line_width(content)
      }

parser = argparse.ArgumentParser(description="get info for your file")
parser.add_argument("file",help="path to the file")
parser.add_argument("-c","--bytes",help="print the bytes count",action="store_true")
parser.add_argument("-m","--chars",help="print the character count",action="store_true")
parser.add_argument("-L","--max-line-length",help="print the maximum display width",action="store_true") 
parser.add_argument("-w","--words",help="print the word count",action="store_true")
parser.add_argument("-l","--lines",help="print the no of new-lines",action="store_true")

args = parser.parse_args()
output = "   "
if (not args.lines and not args.words and not args.bytes and not args.chars and not args.max_line_length):
    args.lines = args.words = args.bytes = True

result = process_file(args.file)
if args.lines:
    output = output +"    "+ str(result['lines'])
if args.words:
    output = output +"    "+ str(result['words'])
if args.bytes:
    output = output +"    "+ str(result['bytes'])
if args.chars:
    output = output +"    "+ str(result['chars'])
if args.max_line_length:
    output = output +"    "+ str(result['max_line_length'])
output = output +" "+args.file
print(output)


    
    




        
        

