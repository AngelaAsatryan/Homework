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
punc_marks=("," "." "?" ";" "-" ":" "!")

for i in range(0, len(punc_marks)):
    count_each_mark(str(punc_marks[i]))

###other way to calculate the sum of the punctuations marks used in the texte file
def sum_punc_marks(punc_mark_a, punc_mark_b, punc_mark_c, punc_mark_d, punc_mark_e, punc_mark_f, punc_park_g):
    a=my_file.count(punc_mark_a)
    b=my_file.count(punc_mark_b)
    c=my_file.count(punc_mark_c)
    d=my_file.count(punc_mark_d)
    e=my_file.count(punc_mark_e)
    f=my_file.count(punc_mark_f)
    g=my_file.count(punc_park_g)
    total_punc_marks=int(a)+int(b)+int(c)+int(d)+int(e)+int(f)+int(g)
    print("There are"+ " " + str(total_punc_marks) + " " + "punctuation marks used in the text.")

sum_punc_marks(punc_mark_a='.', punc_mark_b= ',', punc_mark_c=':', punc_mark_d=';', punc_mark_e='!', punc_mark_f='?', punc_park_g='-')
