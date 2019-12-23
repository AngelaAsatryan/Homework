#count the punctuation marks in the txt file

#open and read the file
myfile=open(r"Homework3.txt", "r")
my_file=myfile.read()

#find if there any $ symbol in the text, if yes, replace and go to the next step
find_symbol = my_file.find('$')
input = ",.?;-:!"
output = "$$$$$$$"
transtable = my_file.maketrans(input, output)
input1 = "$"
output1 = "#"
transtable1 = my_file.maketrans(input1, output1)
replace_symbol = my_file.translate(transtable1)
if find_symbol == -1:
        my_file_no_punc=my_file.translate(transtable)
else:
        my_file_no_punc = replace_symbol.translate(transtable)

#count the $ in the string and give a message about it
punc_mark_count=(my_file_no_punc.count('$'))
text_to_print= "There are"+ " " + str(punc_mark_count) + " " + "punctuation marks used in the text."
print(text_to_print)

#define a function to count each punctuation mark seperately
def count_each_mark(punc_mark):
        print("The number of"+ " " +str(punc_mark) + " " +"mark in the file is" + " " +str(my_file.count(punc_mark))+".")

punc_markss=("," "." "?" ";" "-" ":" "!")
#print each mark
for i in range(0, len(punc_markss)):
    count_each_mark(str(punc_markss[i]))



###other way to calculate the sum of the punctuations marks used in the texte file
# print(sum(my_file.count(str(punc_marks[0]));my_file.count(str(punc_marks[6]))))
def sum_punc_marks(punc_mark):
        total_punc_marks=my_file.count(str(punc_mark[0]))+my_file.count(str(punc_mark[1]))+my_file.count(str(punc_mark[2]))+my_file.count(str(punc_mark[3]))+my_file.count(str(punc_mark[4]))+my_file.count(str(punc_mark[5]))+my_file.count(str(punc_mark[6]))
        print("There are" + " " + str(total_punc_marks) + " " + "punctuation marks used in the text.")
sum_punc_marks(str(punc_marks))
