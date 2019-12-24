#count the punctuation marks in the txt file

#open and read the file
myfile=open(r"Homework3.txt", "r")
my_file=myfile.read()

#define punctuation marks
punc_marks=("," "." "?" ";" "-" ":" "!")
#define a function to count each punctuation mark seperately
def count_each_mark(punc_mark):
        print("The number of"+ " " +str(punc_mark) + " " +"mark in the file is" + " " +str(my_file.count(punc_mark))+".")

#print each mark
for i in range(0, len(punc_marks)):
    count_each_mark(str(punc_marks[i]))

#calculate the sum of the punctuations marks used in the texte file
def sum_punc_marks(punc_mark):
        total_punc_marks=my_file.count(str(punc_mark[0]))+my_file.count(str(punc_mark[1]))+my_file.count(str(punc_mark[2]))+my_file.count(str(punc_mark[3]))+my_file.count(str(punc_mark[4]))+my_file.count(str(punc_mark[5]))+my_file.count(str(punc_mark[6]))
        print("There are" + " " + str(total_punc_marks) + " " + "punctuation marks used in the text.")
sum_punc_marks(str(punc_marks))

