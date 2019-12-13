#count the punctuation marks in the txt file

#open and read the file
myfile=open(r"Homework3.txt", "r")
my_file=myfile.read()

#find if there any $ symbol in the text
print(my_file.find('$'))

#if no $ symbol found, go to the next step
#replace all punctuation marks in the file with $ symbol
input=",.?;-:!"
output="$$$$$$$"
transtable=my_file.maketrans(input, output)
my_file_no_punc=my_file.translate(transtable)

#count the $ in the string and give a message about it
punc_mark_count=(my_file_no_punc.count('$'))
text_to_print= "There are"+ " " + str(punc_mark_count) + " " + "punctuation marks used in the text."
print(text_to_print)

#define a function to count each punctuation mark seperately
def count_each_mark(punc_mark):
        print("The number of"+ " " +str(punc_mark) + " " +"mark in the file is" + " " +str(my_file.count(punc_mark))+".")
#count of ","
count_each_mark(punc_mark=",")
#count of ";"
count_each_mark(punc_mark=";")
#count of ":"
count_each_mark(punc_mark=":")
#count of "!"
count_each_mark(punc_mark="!")
#count of "-"
count_each_mark(punc_mark="-")
#count of "."
count_each_mark(punc_mark=".")
