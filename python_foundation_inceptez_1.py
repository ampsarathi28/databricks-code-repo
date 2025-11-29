#Refer python_theory/notes for understanding few basics of python...
'''
What we are going to learn in Python???
**1. Basic programming fundamentals -
A. Intent/Block based coding
B. Comments
C. Quotes
D. Variables & Values
E. Naming Conventions

F. Types and Casting
G. Input & Output operations
H. Datatypes (Simple/premetive or Complex/Collection (data structure))

I. Operators
J. Conditional Structure
K. Looping Constructs
L. Complex Types

#Specific to Python
2. Exception Handling

3. **FBP - Dataengineers (eg. leverage the spark functions writtern by somebody)

4. OOPS - Framework developers (eg. commiters/contributors of apache spark)
5. Building Apps/APIs/AI integration using Python Programming

'''

'''
Interpreter
line/line -> compiler -> object code -> vm -> execute
Compiler
entire line -> compiler -> object code -> vm -> execute

#execution example of both
Interpreter Example:
vi python_interpreter.py
name='Inceptez'
age=11
print(name)
#print(something)
print(age)
print("hello")
print("good morning")

#Interpret the line by line of code and execute
python python_interpreter.py

vi scala_compiler.scala
object obj1 extends App
{
var name="Inceptez"
var age=11
println(name)
printlnxyz(age)
println("hello")
println("good morning")
println("thank u")
}

#Compile the complete code and execute
scalac scala_compiler.scala
scala obj1
'''
'''
How to uninstall/install pip packages.
python -m pip freeze
python -m pip uninstall pandas
python -m pip install pandas==2.3.1
'''
print("************** 1. Basics of Python Programing*************")
print("How to run a python program")
#right click this module tab and run the program or go to run menu and run or click on the play button in the right top
#or type ctrl+shift+f10

#Day1:15/10/2025
#Fundamentals of Python Programming:
####################################
print("A. Python is an indent based programming language")
#Why Python uses indend based programing ->
#1. Managing the program more efficiently
#2. Better Readablility of the code
#3. For creating the hierarchy of programming.
#4. By default 4 spaces we will give for indends, but more/less spaces or tabs also can be used...

#Indendation is needed for (hierarchy of programming),
# because we are doing block operation (lines of code) with in the for loop
team=['wd36','we47']
for i in team:
    print(f"hello {i} Team")
    print("thank you")

#Linux is not an intend based program, it is a block based rather:
'''
for i in `ls` 
do #starting a block
 echo "listing files in the folder"
    echo $i
echo "Thanks"
done #Ending the block
        echo "Completed"
'''

#indendation has to be uniform within the block of code (not mandatory across the block of code)
#below prog doesnt work if we are using different number of spaces between lines of code in a given block
for i in range(1,4):
    print("inside i")
    print(i)
    for  j in range(1,2):
      print("inside i")
      print(j)

#optimal number of spaces has to be 4, but any numbers you can give, dont use both tab & spaces

print("B. This is a commented line in Python")
# What is comment? Comment is a info/description/additional information for better understanding,
# which will not affect the program execution
# Usage of Comments: For descriptive purpose & for creating dead codes
#Comments are of 2 types:
# 1. Single line - #
# 2. Multi line or block comments - '''  '''
#print("hello is commented") #single line comment
'''
for i in range(1,4):
    print("inside i")
    print(i)
'''
#Comment is used as description too...
def abcd():
    '''This is a function to do something'''
    for i in range(1, 4):#this for loop is going to iterate 3 times from 1 to 3
        #print("inside i")
        print(i)#printing the value of i in every iteration

print("C. Playing with Quotes: Python treats single quotes the same as double quotes as like triple quotes, but has some differences")
#Python treats single quotes the same as double quotes and triple quotes.
var1='Inceptez'
var2="Inceptez"
var3="""Inceptez"""
print(var1,var2,var3)

##we can use escape sequence also - \ is used to tell python not to consider the following content of \
print('This is an Inceptez\'s property')

#Single quotes example
var1='This is an Inceptez property'

#Double quotes is used for holding single quoted chars
#var2='This is an Inceptez's property' #this is not runnable
var2="This is an Inceptez's property"

#var_with_both_single_double_quotes="This is an "Inceptez's" property" #this is not runnable

#Triple quotes:
#Triple quotes can handle multiple quotes like single or double or any other characters
var_with_both_single_double_quotes="""This is an "Inceptez's" property"""
#Triple double quotes is used for muliline
#For handling paragraph/multilines text, we can use 3 single or doublequotes
var_with_multi_line="""Hi Team,
Good morning"""

#Any programming language learning has to be started first learning about variables
print("D. Let's learn all about VARIABLES")
'''1. Variable Properties - Dynamic Inference, Dynamic Typed, Strongly Typed'''

#Dynamic inference - based on the assigned value to a variable, it will automatically decides/infer/identify/refers the data type dynamically
age=43
print(type(age))
height=5.11
print(type(height))

#Dynamically typed: If a variable is created with a specific data type, can be changed later by performing soe eration
amt=100
print(type(amt))
#<class 'int'>

#below is possible, because python is dynamically typed language (Duck type language)
amt=amt+(amt*.1)
print(type(amt))
#<class 'float'>

'''Scala is a statically typed language
scala> amt=100
scala> amt
val res0: Int = 100
 
#below is not possible - because of statically type feature
scala> amt=amt+(amt*.1)
           ^
       error: type mismatch;
        found   : Int
        required: ?{def +(x$1: ? >: Double): ?}
'''

#Strongly typed: Python allow us to operate between the variables of Similar datatype (of the same hierarchy) and doesn't allow to operate between different datatypes.
name='irfan'
amt=100
#print(name+amt)#this fails
#TypeError: can only concatenate str (not "int") to str

#Overcome this property by using type conversion functions
stramt=str(amt)
print(name+stramt)

#Scala is Weakly typed language: Allow us to operate between the variables of Any datatype
'''
scala> var a=10
var a: Int = 10
scala> var b="Inceptez"
var b: String = Inceptez
scala> b+a
val res1: String = Inceptez10
'''

print("E. Naming Conventions")

#MohamedIrfanKader - Pascal/initcap case
#mohamedIrfanKader - Camel case (methods/functions)
#mohamed_irfan_kader - Snake case (n_n_n_)
#MOHAMEDIRFAN - upper case
#mohamedirfan - lower case

#A variable can have camel case or init upper or with underscores snake case
total_number_of_aspirants=69
totalNumberOfAspirants=69

#A variable name must start with a letter or the underscore character
fullName="Inceptez Technologies"
full_name="Inceptez Technologies"
_revenue=1000000#protected for broader group, open for smaller group
__profit=100000#private for intented group

#A variable name cannot start with a number
fullname1="Inceptez Technologies"
fullname2="Inceptez Technologies Pvt Ltd"

#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
full_name_123='inceptez technologies'

#Variable names are case-sensitive
abc=10
Abc=20
ABC=30
print(abc,Abc,ABC)

#Multiple Variables can be assigned in a single line (Multi Assignment)
name,age,city="Irfan",43,"Chennai"
print(name,age,city)

#Variable name should not be a reserved keyword
len1=len(name)#This is not a right naming convention to use

print("F. Type identification & Casting")
#Functions we are learning in this topic (type, isinstance, casting(int,str,float etc.,))
#What we are learning here is the usage of few functions like type, isinstance, casting functions
age=43
#To understand/identify the age is of what type
print(type(age))

#To check wheter the age is of an expected type
age=43
print(isinstance(age,int)) #True
age='43'
print(isinstance(age,int)) #False

#To convert the age to an expected type
age=int(age)
print(type(age))
age=43
age_float=float(age)
print(type(age_float))
age_str=str(age)
print(type(age_str))
#Check for a given type, if it is not as expected then cast it to the expected type programatically using if condition

print("G. Standard Input & output options")
#assigning value statically/hardcoded
name='irfan'
age=input("enter your age")
#any function that we use may have input &/ output arguments/results

#assigning value dynamically using the function called input()
#Default Characteristics this input function has:
#Character1: input will take the input value interactively with the default type of string
#Character2: input will take the input without prompting with anything, but we can add the prompt with some content
name=input()#input without any prompt (character2)
print(type(name))#str (character1)

age=input("enter the age: ")#input with a meaningful prompt (changing the character2)
print(type(age))#str (character1)

#Better to use
age=int(input("enter the age: "))#input with a meaningful prompt (changing the character2) and typecasting input output to integer (changing chararcter1)
print(type(age))#int (character1 changes)


#print statement will be used as a std output function
print("hello")

#semi colon can be used to seperate a statment if we write multiple statements in one line

#below print function is taking only 1 argument (but print can take any number of arguments)
print("good morning team")#one input one output
#below print function is taking multiple arguments and printing them individually as multiple output
name='inceptez'
age=11
print("name of the company",name,"age of the company",age)#4 input and 4 individual output seperated with space

#Formatted string Print statements - positional formatting args - not much important
name='inceptez'
age=11
#Positional arguments
print("name of the company name age of the company age")#1 input and 1 output
#drawback is the above print with print even variable name as a value, not the actual value...
#to overcome, we have a concept of format function...
print("name of the company {0} age of the company {1}".format(name,age))#positional formatting arguments

#keyword/named formatting arguments - not much important
print("name of the company {n} age of the company {a}".format(n=name,a=age))#named formatting arguments

#Formatted string Print statements other way (3x onwards) - named args - important and advance and simple
print(f"name of the company {name} age of the company {age}")

print("H. Datatypes, Mutability & Builtin Functions (later)")
#Simple Types: string, numeric (int, float, complex), misc
#Complex or Collection Types: list, dict, tuple, set
#Simple Type (Sequence Type) -
#string type -
# Definition: Indexed sequenced collection of characters
#eg. name='inceptez'
#01234567 Indexed sequenced collection of chars
#inceptez
# can be assigned with single, double, triple single/double quotes
name='inceptez'
name1="inceptez"
name2="""inceptez"""

#Hints - hints in python is used to identify the type easily or descriptively
name3:str='irfan'
age1:int='43'#This is still a string, the :int is for just descriptive or hinting purpose
print(type(age1))#string
age2:int=int('43')
print(type(age2))#integer

#application of hint
def bonus_calc(sal:int,bon:float):
    return sal+(sal*bon)#Dynamic typing character

print(bonus_calc(100000,.20))
#Immutability - non changable
company_name='inceptez'
#company_name[0]='I' #Item assignments/modification in a string is not possible because of immutability

#Numeric Types (int, float, complex)
#int type - single whole number, it is non indexed/sequenced, it is immutable (non modifiable)
age=43
age_hint:int=43
'''
age[0]=5#will not work because int is immutable
print(age[0])#will not work because it is non indexed
for i in age:#will not work because it is non sequenced
   print(i)
'''
#float type: single decimal number with scale and precision, it is non indexed/sequenced, it is immutable (non modifiable)
height=5.11#5 is the scale and 11 is the precision
height_hint:float=5.11
#as like integer, float also is immutable, non indexed and non sequenced

# complex numbers: Contains the real and imaginary part in a format of 10.5j (where is 10 is real and 5j is imaginary)
#especially used in the scientific, electrical, data science environments, applied maths (ensemble model).
complextype=complex(5.11)
complexvalue=5.10+2j
print("real value is",complexvalue.real)
print("imaginary value is",complexvalue.imag)
print("conjugate of complex value",complexvalue.conjugate())

#Misc Types (bool, none, exp, bytes)
#bool types: Boolean is a true or false return value of operations we performed
boolout:bool=1>2
print(boolout)#return boolean of false
print(1<2)#return boolean of true

#None types: It is a type represents the value is not available
a=None
#print is a function that return none
type(print())

def a():
    print("hello team")
    #return 'something' #If i dont have return then it will return none

#exponential - Exponent of 0's
#1.5j #complex number
exponential_value=2e3 #exponents e3 means 10 to the exponent of 3 = 10*10*10 = 1000
#result 2000

#bytes - used for converting the values to byte/binary format before transfer across the network or for processing in a secured fashion
byte_a=bytes(100)#Converting a number to a bytes type before tranfering across the network...
print(type(byte_a))
print(byte_a.decode('utf-8'))

#Complex/Collection types - list, dict, tuples, set we learn later

print('G. Operators')
#Python supports operators -> assignment, arithmatic, comparison/relational, logical,
# unary (least priority), binary (least priority), ternary (least priority), bitwise (least priority)

#Assignment Operators (= or += or -=)- used to assign some values to a variable - return the value/reference as a result
age=43#here variable age is assigned with a value of 43
age+=1#here variable age is assigned with a value of 43+1 (value is operated with an arithmetic operator)
#or
age=age+1#here variable age is assigned with a value of 43+1 (value is operated with an arithmetic operator)
name=name.capitalize()#Here i am assigning the result of a function as a value to the name variable
i=int#i is a variable referring a program called int
#conclusion is an assignment operator can be used to assign a value or refer a program

#Arithmatic Operators (*/+- ** % ()) - will returns operated value as a result
#BODMAS rule (Precedence order -> Brackets, Orders (exponent/sqrt), Division or Mul, Add or  Sub
mul=5*10
div=10/2
add=100+200
sub=100-200

final_res=100+200/100-200#without using BODMAS
final_res=(100+200)/(100-200)#using BODMAS

power_val=2**4#2 to the power of 4 ie 16
mod_val=10%3 #Result is 1

#Relational operators (==, !=, >, <, <=, >=) - Used for comparing variables and values and returns boolean type as a result
print(5!=10)
print(5==10)
result:bool=5==10#We are assigning and comparing
print(result)
print(type(result))

#Logical Operators () - apply logic between multiple output of the relational operators and Returns boolean
#or - will check for the first occurance of true and return true
print("this will just print true once 1==1 is identified, it wont got to 3==4 check",1==1 or 3==4)

#and - will check for the first occurance of false and return false
print("this will print false after validating 1==1 and 3==4",1==1 and 3==4)
print("this will just print false after validating 3==4, it wont validate 1==1",3==4 and 1==1)

#not - It is negation/opposite of the and and or result
x=not(True)#return False
y=not(False)#return True
print(x,y)
print("this will print false after validating 1==1 and 3==4",not(1==1 and 3==4))

#Least bother, but know about these operators once for all...
#Unary (-) = an operator used to identify the sign of a value assigned
bank_balance=-10000
tax=-.18
gross_sal=100000+10000
print(f"final salary {gross_sal+(gross_sal*tax)}")

#Binary - If I operate between 2 or more variables/values using an operand
a=100
b=200
print(a+b)#binary operator example

#Ternary - Short form of using the operators to achieve SIMPLE conditional/looping outputs in a
# single line short form
#Typical control (conditional) structure
if a<b:
    print("true output of a is lesser")
else:
    print("false output of b is lesser")

#Ternary - above conditional structure can be writterned using the ternary operator in a single line short form
#Ternary operator breaks the rule of indent and block based programming, we will write all simple functionality in one line
print("true output of a is lesser",a) if a<b else print("false output of b is lesser")

print('J. Conditional Structure')

#I may/must have if condition minimum - must
#I must have if condition with else statement - false (may)
#I can have only elif or else statement - false (if is mandatory)
#I can have if condition with else condition alone - true
#I can have if condition with elif condition alone - true
#I may have if condition with else if condition and else statement also - true
#I should have my conditional structure started with if - True
#if should be used only once in a conditional structure - False (we can use nested if)
# We can have multiple elif and should have only one else in a given block (not nested) - True
#signature of if is completed with colon (:)

#Minimal Conditional Structure
#simple example
if True:#use either or both relational or logical operators to get boolean
    print("execute the if block code...")

#Conditional Structure with multiple conditions (if and elif)
if 0>1:
    print("execute if block code...")
elif 2>1:
    print("execute first elif block code...")
elif 3>2:
    print("execute second elif block code...")

#Conditional Structure with multiple conditions and unconditional also (if and elif and else)
if 0>1:
    print("execute if block code...")
elif 2>3:
    print("execute first elif block code...")
elif 2>4:
    print("execute second elif block code...")
else:
    print("None of the above conditions are met")

#Nested conditional structure, which has to be used appropriately,
# needs lot of iterative testing
if 0>1:
    print("execute if block code...")
    if True:
        print("execute nested if block code in the if block...")
elif 2>3:
    print("execute first elif block code...")
elif 2>4:
    print("execute second elif block code...")
else:
    print("None of the above conditions are met")

#Reallife example of nested if
time=9.30
month='october'
if month=='october':
    if (time > 9 and time <= 10) or (time >= 6.30 and time < 7):
        print("Restarting the zoom for one on one video connect")
    else:
        print("it is a different time >10 or <6.30")

#Quick Usecases:
#Usecase1: Find the greatest of 2 and then 3 numbers not by using built in functions
a=int(input("enter value for a"))
b=int(input("enter value for b"))
if a>b:
    print("a is greater than b")
elif a<b:
    print("a is less than b")
else:
    print("both are same")

#greatest of 3 numbers
a=int(input("enter value for a"))
b=int(input("enter value for b"))
c=int(input("enter value for c"))
# logical operators or nested conditional structure
if a==b==c:
    print("a, b and c are equal")
elif a>b and a>c:
    print("a is greater than b and c")
elif b>a and b>c:
    print("b is greater than a and c")
else:
    print("c is greater than a and b")

#Usecase2: Pseudo code (www.inceptez.in)
# "if" user clicked on the popup then provide the options available upcoming batch or ask anything
# "if" user choosen upcoming batch -> ask user to choose either de or ds or cloud or devops else inform course is not available
# "if" user choosen ask anything ->
# "if" user clicked on the popup then provide the options available upcoming batch or ask anything
popup=True
if popup:
    print("choose either up bat or ask anything")
    tab_clicked=input("choose either up bat or ask anything")
    if tab_clicked=='up bat':
        course_interested=input("choose de or ds or cloud or devops")
        if course_interested=='de':
            print("Data engineering course has been chosen","weekday  7 to 9","weekend 9 to 1.30")
        if course_interested=='ds':
            print("Data science course has been chosen","weekend 9 to 1.30")
    elif tab_clicked=='ask anything':
        print("provide your question, we will get back to you")
        msg=input()
        #msg wil be mailed to inceptez team
else:
    print("other page clicks happened")

#CASE WHEN Suspicious THEN 'FLAGGED' ELSE 'NORMAL' END
'''
if suspicious:
   transaction_flag="flagged"
   print("flagged")
else:
   transaction_flag="normal"
   print("normal")   
'''

#Usecase3:
#Strategic1
#One program covers almost all these concepts including operators and all the a to j
###########One Reallife usecase program to bring all types of operators in one Program###########
#Swiggy food purchase -> coupon max discount of 100 or 10% which ever is lesser
#Get 10% discount using RuPay Credit Cards Maximum discount up to ₹100 on orders above ₹600
#pseduo code:
'''Create a program to apply discount of 10% if the min amt is 600 and max cap of discount is 100 rupees
1.check for cart amt >= min cap amt else print the difference amout to add in the cart
2.further check for the disc percent applied cart amt is exceeding offer max amt, then apply flat offer max amt
3.else check for the disc percent applied cart amt is not exceeding offer max amt, then apply disc percentage
'''
total_cart_amt=int(input("enter total cart amount"))#get this input from the cart value of the webgui
offer_disc_pct:float=.10
min_cap_amt=600
offer_max_amout=-100#unary operator

if total_cart_amt>=min_cap_amt:#conditional struct
    offer_pct_applied_amt=total_cart_amt*offer_disc_pct
    print(offer_pct_applied_amt)
    if offer_pct_applied_amt>=-offer_max_amout :
        final_cart_amt=total_cart_amt+offer_max_amout#binary operator
        print(f"applying flat offer, customer have to pay {final_cart_amt}")
    else:
        final_cart_amt = total_cart_amt - offer_pct_applied_amt
        print(f"applying offer percentage of 10, customer have to pay {final_cart_amt}")
else:
    print(f"sorry you are not eligible for this offer, add the amt of this much {min_cap_amt-total_cart_amt} to avail offer")#bin operator/format function/output

#ternary operator
if total_cart_amt>=min_cap_amt:#conditional struct
    offer_pct_applied_amt=total_cart_amt*offer_disc_pct
    print(f"customer have to pay {total_cart_amt+offer_max_amout}") if offer_pct_applied_amt>=offer_max_amout else print(f"customer have to pay {total_cart_amt - offer_pct_applied_amt}")
else:
    print(f"sorry you are not eligible for this offer, add the amt of this much {total_cart_amt-min_cap_amt} to avail offer")#bin operator/format function/output

'''
**1. Basic programming fundamentals -
    A. Intent/Block based coding
    B. Comments
    C. Quotes
    D. Variables & Values
    E. Naming Conventions - snake case
    F. Types and Casting (float, int)
    G. Input & Output operations
    H. Datatypes (Simple/premetive or Complex/Collection (data structure))
    I. Operators - unary, binary, ternary, logical, arithmetic, assignment, relational/comparison
    J. Conditional Structure - simple and nested conditional structure
'''

print('K. Looping Constructs')
#Looping Construct concepts ->
'''
Category -> 
Conditional looping (entry & exit) eg.  
Un Conditional looping - for loop
Types ()
break ->  
& continue -> 
'''
#Control structure (conditional struct, looping constructs)
#What is a loop: Iterative or repetitive execution of similar tasks across data or programs is called loops
#1.Categories of loops:
#Conditional looping (entry controlled (while) and exit controlled (do while))
#UnConditional looping (for loop) #important
#2. Names of looping:
#for and while loop, do while loop
#3. For controlling the flow of the loops:
#break & continue & pass

#1.Categories of loops: for & while
######################All about For loop#######################################
#Characteristics of For Loop:
#For loop will run on an iterable type only (list, string, dict, tuple, set)
#For loop is a unconditional looping - number of iterations are already known
#UnConditional looping (for loop) #important
#Example1:
list_of_courses_str="DS DE CL DO"#not advisable, to store multiple values
#                      0    1    2    3
list_of_courses_inanycase:list=['DS','de','Cl','dO']#very important collection type
for course in list_of_courses_inanycase:#unconditionally we are iterating on the known number of items
    print(course.upper())

#for loop is an unconditional looping
#A Realtime Example of for loop (Unconditional Looping)
#If Inceptez has only 1 employee
#Example2:
sal=10000
deduction=.8
print(f"depositing salary of {sal-(sal*deduction)} amount in the bank account")

#If Inceptez has 5 employees
sal_lst=[10000,50000,5000,20000,10000]
deduction=.08
for sal in sal_lst:#signature of for loop
    print(f"depositing salary of {sal-(sal*deduction)} amount in the bank account")#body of for loop

#Real Example of For loop:
#Usecase1: Try reading the data from our filesystem (accounts, customer, loan) and print the data in the screen
'''
import pandas
list_of_files=['accounts.csv','branches.csv','creditcard.csv']
path="C:\\dataset1\\"
#memtable=pandas.read_csv(path+list_of_files[0])
#memtable.sample(2)
for file in list_of_files:
    print(f"sample of 2 rows from each files in the list {file}")
    memtable=pandas.read_csv(path+file)
    memtable.sample(2)
'''
'''
I tried ,but i I had one doubt while executing the code ,
The code which i ran in CLI executed but it asked to install pandas  again in PyCharm — 
does this happen because PyCharm uses a separate virtual environment from the Python setup?
so for everytime do we need to install the new lib if we use new IDE (VENV)
'''
######################All about For loop#######################################

######################All about While loop#######################################
#Characteristics of While Loop:
#While loop will run based on a condition
#While is a conditional looping - number of iterations are not known already, it varies based on the incremental value and the condition used
#We have to use while loop causiously, if we miss the condition, it will run infinately...
#Conditional looping (while loop) #not much important as like for loop
#While is an Entry controlled loop
#Example1:
sttime=7
endtime=9
while sttime<=endtime:#Signature of while loop requires a condition that returns boolean
   print(f"run the session every 30 mins upto {sttime}")
   sttime=sttime+.5

#Strategic2
#I wanted to rewrite/enrich the above program to engage the session only on weekdays or weekend?
#Using conditional structure and both looping construct in one program...
#Example2: Marrying unconditional & conditional looping with conditional structure (if condition)
lst_weekdays=['mon','tue','wed','thu','fri']
lst_weekends=['sat','sun']
endtime = 9
endtimewe=14
batch_flag=input("pls let me know the batch id WD/WE")
if batch_flag=='WD':
    for days in lst_weekdays:
        sttime = 7
        print("running the session for day ",days)
        while sttime<=endtime:#Signature of while loop requires a condition that returns boolean
           print(f"check the session every 60 mins upto {sttime}")
           sttime=sttime+1
elif batch_flag=='WE':
    for days in lst_weekends:
        sttime = 9
        print("running the weekend session for day ",days)
        while sttime<=endtimewe:#Signature of while loop requires a condition that returns boolean
           print(f"check the session every 60 mins upto {sttime}")
           sttime=sttime+1
else:
    print("no such batch")

#Conditional looping (entry controlled (while) and exit controlled (do while))

#do while loop

######################All about While loop#######################################

#Concept of Nested loops using for and while:
#Example1:
batches=['wd36','we47','ds22','devops1']
common_tools=['github','sql','python']
for batch in batches:
    print(f"for the batch {batch}")
    for tools in common_tools:
        print(f"tool {tools}")
        print(f"Batch {batch} is learning the tool {tools} ")

#Nested While loop:
#Example:I wanted to rewrite the for loop code using while loop by making it conditional, but more complex to handle.
daycnt=1
batch_flag=input("pls let me know the batch id WD/WE")
while batch_flag=='WD' and daycnt<=5:#If we dont have the fixed days of session we are engaging for eg. sometime mon, tue, fri, sat, sun
    print("running for day",daycnt)
    sttime = 7
    endtime = 9
    while sttime<=endtime:
         print(f"check the session every 60 mins upto {sttime}")
         sttime=sttime+1
    daycnt += 1
else:#since while is a conditional looping, it supports else also...
    print("no such batch")#Yes we can have else in while loop, because it is a conditional looping


#Usecase1: Try create tables for our kids from 2 to how many tables (get as an input)?
# Using while loop, lets create a table
# Using simple or nested for loop, skip the 5 and 10 tables
#Table has to created upto 12 numbers
tot_tables=5
for i in range(2,tot_tables+1):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")

#Additional usecase: Try to enrich the above program with dynamically getting the input from the user to control
#starting table, maximum table output and total number of tables

#For Loop with Break and Continue constructs/clauses:
#Break is used to break the execution of the loop by come out of the loop if a given condition matches
#Continue is used to skip the given iteration of the loop (and execute the next iteration) if a given condition matches
allteam=['DEV','TEST','SECURITY','HR','SYSADMIN']
for teams in allteam:
    if teams in ('SECURITY','SYSADMIN'):
        print("should not take wfh",teams)
        #continue#continue to the next item in the list, skipping the current item
    print("you can take wfh", teams)

#Usecase: Write a program to apply tax 10% for all the states, other than pondy and goa
states_lst=['tn','po','ke','ka','go']
product_price=15000

#break construct usage : Eg. give only bonus to employees who is getting salary <15000
sal_lst=[5000,7000,9000,12000,15000,20000,30000,40000,50000]
import time
for sal in sal_lst:
    if sal>=15000:
        print("breaking the loop, since i reached the condition",sal)
        break
    elif sal<=7000:
        pass#i dont have anything to do (empty statement)
    else:
        print(f"1000 bonus applied to salary {sal} =",sal+1000)
        time.sleep(2)

#Looping constructs available in Common Prog languages -
#Looping constructs available in Python language -
#Types of Looping - Entry Control & Exit Control loops

#conditional & unconditional
#nested looping (for for/ for while/while for)
#constructs - break & continue & pass
#conditional (entry controlled & exit controlled)

#Realtime Example of using While loop: Entry controlled & Exit controlled loop
#Login username/password used in our routine life

#Do while loop (least bother) workaround in python to demonstrate "exit control loop"
#i am checking the condition in the exit, if  it doesn't met, i am breaking the loop
#after running the loop atleast once
sttime=8
endtime=9
while True:#conditional looping - exit controlled loop (using while itself, since no do while is avilable in python)
   print(f"Start the zoom meeting, check the session every 60 mins upto {sttime}")
   sttime=sttime+1
   if sttime<=endtime:
       #print("you are legitimate to continue")
       pass
   else:
       print("you are not legitimate to continue the session, time up")
       break

##############################################Condition Structure & Looping Constructs completed####################################


##############################################Condition Structure & Looping Constructs completed####################################

print('K. Collection (complex) Types')
#Strategic3
#Application of using collection types in realtime world?
#Self served metadata driven Data movement automation (DMA) tool
#{"process":"ETL Process1","source":["hive","Bigquery"],"target":["HDFS","GCS"],"cols":["custid","upper(custname) as upper_custname"],"tablename":"customer","where":"(city='chennai')","gcs_uri":"gcs://abc/xyz_bucket/"}
#rec1={"process":"ETL Process1","source":["hive","Bigquery"],"target":["HDFS","GCS"],"cols":["custid","upper(custname) as upper_custname"],"tablename":"customer","where":"(city='chennai')","gcs_uri":"gcs://abc/xyz_bucket/"}
import json
read_file_disk=open("C:\\dataset1\\dma.json",'r')
json_formatted_memory_file=json.load(read_file_disk)
#usecase:
#1. try to print from bigquery to gcs we are loading data
#2. try changing the query
#3. try using where clause also
#sqlquery="select custid,upper(custname) as upper_custname from customer where (city='chennai');"

#What is a collection type? Semi structured data
#Collection is a datatype which is going to help us collect different data items/values in a collection format
#It leads to the next dimensions of data
#it is flexible, dynamic, performant, complex, occupies less space in the storage and network transfer of data

#list, dictionary, tuple, set

#Simple Examples of Collection Types:
#list []: collection of similar items
#indexed sequenced collection of homogeneous/similar elements/items - eg. column
#                            0          1           2       3
name_of_aspirants:list[str]=['nivetha','prathap','dinesh','poongothai']
#name_of_aspirants:list[str]=[30,'chennai','prathap','dinesh','poongothai'] #works but dont prefer

#dictionary {k1:v1,k2:v2} eg. key column and value(s) column: collection of key and value pair, key is unique and key is of similar type and value can be of other similar
dict1={"id": 1,"first": "Harshitha","last": "devi"}

#tuple (): Indexed sequenced Collection of hetrogeneous elements/items - eg. row
address_of_aspirants: tuple[int, str, str, str, int]=(139,'5th main road','velachery','chennai',600042)

#set {values} : collection of unique values, eligible for performing set operations...
phone_number_aspirants:set={9840800131,9840800221,9840800131}

#Example of all collection types used:
#{'process': 'ETL Process1', 'source': {'hive', 'Bigquery'}, 'target': ['HDFS', 'GCS'], 'cols': ['custid', 'upper(custname) as upper_custname'], 'tablename': 'customer', 'where': "(city='chennai')", 'uris': ('gcs://abc/xyz_bucket/', 100)}

#Different types of collection types? in the order of importance
#list, dict, tuple, set

#Why we need collection types?
#To manage/store/parse the complex dataset in a hirarchical/nested/complex structure stored or to process semi structure data, nested data,
# dynamic schema-ful data (avro), variable data/metadata, for a data or metadata/configuration driven approaches..

#Different characteristics of collection types? we are going to learn in detail below..
#Iterable (looping), mutable (changable) - updatable (modifyable) & resizable (added/removed), accessible (select using index, position, value, key)

######What are the topics we have to learn in collection types#######
#Iterable? Yes, all collection types are iterable in python.
for i in [10,20]:
   print(i)
for i in {1:10,2:20}:
   print(i)
for i in (10,20):
   print(i)
for i in {10,20}:
   print(i)

#Notation, access, resizable/mutable/immutable?  insert/update/delete, built in functions to apply
#All the above we are going to see in detail
#Notation:[], {k,v}, (), {v1,v2}
#Accessed using ? index/key
# list - index
print([1,2,3][0])
# tuple - index - eg.
print((1,2,3)[0])
# dict - key - eg.
print({10:1,20:2}[10])
# set - items cannot be accessed individually because it is a set - eg.
#using iterator we can access all elements of the set
for i in {1,2,3}:
    print(i)

print("Deepdive into - list operations")
#Definition: Indexed, sequenced collection of HOMOGENEOUS elements
name_lst=['irfan','siva','jaffer','suganya']
#List can be hetrogeneous too (but not suggested, why ? because while operate between the elements of the list, program fails because python is a strongly typed language)
name_age_lst=['irfan','siva','jaffer','suganya',43,30,25,31]#not preferred
for i in name_age_lst:
   #print(i.upper()) #it will error out
   print(i)
name_age_dict={'irfan':43,'siva':30,'jaffer':24,'suganya':31}#preferable format
#All the python collections are iterable -
for i in [10,20]:
   print(i)

#select/access - using index starts from 0
print("first element",name_lst[0])#access left to right
print("last element",name_lst[-1])#access right to left
print("last element",name_lst[len(name_lst)-1])

#insert/update/delete (list is mutable, hence updating and resizing (add/removing) is possible)
#append in the last (proves list is mutable/resizable/can be inserted)
name_lst=['irfan','siva','jaffer','suganya']
print(len(name_lst))
name_lst.append('vivek')
print(len(name_lst))
print(name_lst)

#insert in the index position
name_lst=['irfan','siva','jaffer','suganya']
name_lst.insert(2,'ashok')
print("after resized",name_lst)

#update the list elements (mutable)
name_lst[0]=name_lst[0].capitalize()
print("after updated",name_lst)
#delete the elements of the list using value
name_lst.insert(2,'Irfan')
name_lst.remove('Irfan')#remove first occurance of the value

#pop (delete) the elements of the list using index
name_lst.pop()#delete(pop) last element from right to left
name_lst.pop(0)#delete(pop) a particular index item

#search for a value with in the given index (range) value and pop(remove) it
name_lst=['irfan','siva','jaffer','suganya','jaffer','siva','jaffer']
capture_idx=name_lst.index('jaffer',3,5)
name_lst.pop(capture_idx)

#Wanted to remove the duplicate in a given list?
name_lst=list(set(name_lst))#since set is a collection of unique elements, converting to set then reverting to lst back

print("Dictionaries (mutable) - {k:v, k:v}")
#It is a collection of key value pair, items are terminated by ',' and key value terminated by :
#Key is unique and value can be duplicated
dict1={"id": 1,"first": "Harshitha","last": "devi","age":30}

#Access a dictionary - using key
print(dict1["age"])#returns the value of 30

#Adding Items - if the key is not found (if the key is found it will not update the value, because key is unique)
dict2={}
dict2.setdefault(1,'irfan')
dict2.setdefault(2,'senthil')
dict2.setdefault(2,'irfan')#it will not work, because key is unique
dict2.setdefault(3,'irfan')#it will work, because value is non unique

#Updating/Inserting (merge/upsert) Items - if the key is found (it updates), if the key is not found (it inserts)
dict1={"id": 1,"first": "Harshitha","last": "devi","age":30}
dict1.update({'age':31})#update the age to 31
dict1.update({'city':'Chennai'})#insert city as chennai

#Removing an Item (from the last)
dict1.popitem()
print(dict1)

#Delete(pop) the given key
dict1.pop('first')
print(dict1)

#Delete all the elements of a dict
dict1.clear()
print(dict1)

#Iteration of Dictionary
dict1={"id": 1,"first": "Harshitha","last": "devi","age":30}
#Iterate on the items of the Dict - will return what datatype???
#dictitems=tuple(dict1.items())
print(dict1.items())#return type is a form of list of tuples
for key,value in dict1.items():
    print(key,value)

dict_items_k_v=dict1.items()

#where did we used in realtime: in the database environments
'''
1,irfan
2,balaji
3,poongothai
'''
#[(1,irfan),(2,balaji),(3,poongothai)]

#Iterate on the keys of the Dict - will return what datatype???
print(dict1.keys())#return type is a form of list of tuples
for key in dict1:#dict1 or dict1.keys()
    print(key)

dict_keys=dict1.keys()

#Iterate on the values of the Dict - will return what datatype???respective value's datatype
dict_values=dict1.values()
for value in dict1.values():
    print(value)
print(dict_values)#default dict_values([list of values])
print(list(dict_values))#cast it [list of values]
print(tuple(dict_values))#cast it (tuple of values)

#To form or create a dictionary with the keys from list and value from the second argument
empty_dict={}
empty_dict=empty_dict.fromkeys([1,2,3,4],10000)

print("Tuples (immutable?)")
#Definition of Tuple:Tuple is an indexed sequenced collection of hetrogeneous elements, tuples are immutable (non updatable and non resizable)
#Notation is - ()
#real life example of using tuple in Database - tuples are otherwise called as row/record
'''
id,name,age
1,irfan,43
2,balaji,35
3,poongothai,30
'''
any_collection_in_anysystems=[(1,'irfan',43),(2,'balaji',35),(3,'poongothai',30)]
#whether we are fulfilling the character of list indexed seq collection of homogeneous elements - true
for lstitems in any_collection_in_anysystems:
    print(type(lstitems))#all items in the list is of same type
#whether we are fulfilling the  character of tuple indexed seq collection of hetrogenous elements - true
for lstitems in any_collection_in_anysystems:
    for tupitems in lstitems:
        print(type(tupitems))#items in the tuple can be of type

row1_tup=(1,'irfan',43,'irfan')

#select/access - using index
print("I want to print the name of employee",row1_tup[1])

#count of some element in the given tuple
print("return the total number of time 'irfan' is present in this tuple",row1_tup.count('irfan'))

#search for some element in the given tuple to identify the index
print("return the index of where the 43 value present",row1_tup.index(43))

#Resizable? No (insert/delete)
#Try to Add some elements to the tuple
#Insert/Append? No
row1_tup=(1,'irfan',43,'irfan')
#row1_tup.append(10000)

#delete? No
#row1_tup.remove('irfan')

#Modify (update) - Not possible
#row1_tup[0]=2

#I want to achieve Insert/update/Delete in a tuple? Not possible by default,
# but we can do some workaround to achieve it?
row1_tup=(1,'irfan',43,'irfan')
row1_lst=list(row1_tup)
row1_lst[2]=row1_tup[2] + 1
row1_lst.remove('irfan')
row1_lst.append(10000)
row1_tup=tuple(row1_lst)
print(row1_tup)

print("Set (mutable) (least bothered)- Notation {} - "
      "Set is a distinct/de duplicated collection of elements, sorted(upto 255 value in memory), cannot be accessed using index ?? Why? because it is a set")

#how to access the element of a set (cant be access directly by using index/key/values)- Index can't be used why?
#The number of elements/items in the set is not fixed in the numbers or sort order
#Notation: {}
cust_store1={1,2,3,4}

#set is iterable?yes
for i in cust_store1:
    print("customer ids of store1",i)
    if i<4 and i>2:
        print(i)

#How to access the elements of a set?
#set1[0] #not possible to access using index
#print(cust_store1[0])#because set is not a indexed/sequenced collection or not a key based collection, its just a set of collection
#print(cust_store1[2])

#set is mutable/Resizable? Yes, it is updatable and resizable
#add will help add/update an element on the set
cust_store1={1,2,3,4}
cust_store2= {2,4,5,6}
#update will help add/update another set
cust_store1.update(cust_store2)#inserting/Updating (Merge) (affect the original set)

#set is mutable (resizable) - Removing/popping/cleaning
cust_store1.pop()
cust_store1.remove(4)
cust_store1.clear()

#set is supported with set operation (If we use set, we use it for these purposes in real time)
#Learning the set operation in python may not be used much, but the concept of the set operation
#will help us improve our analytical functions capabilities on the data

#Core Set functions
#Requirement of combine the customers of both stores - union
cust_store1={1,2,3,4}
cust_store2= {2,4,5,6}
cust_store1=cust_store1.union(cust_store2)

#Requirement of identifying the common the customers of both stores
cust_store1={1,2,3,4}
cust_store2= {2,4,5,6}
cust_store1.intersection_update(cust_store2)

#Identify the excessive non common customers in store1
cust_store1={1,2,3,4}
cust_store2= {2,4,5,6}
cust_store1.difference(cust_store2)

#some addition Set functions (least bother) about these function usage in python, but concept try to understand once..
#subset & superset
cust_city1={1,2,3,4}
cust_store1= {1,2}
cust_store2= {1,3,4}
print(cust_store1.issubset(cust_city1))#whether store1 customer is present in the city1
print(cust_city1.issuperset(cust_store1))#whether city1 contains the customer of store1

#Symmetric difference - opposite of intersection
#Return a new set with elements in either the set or other but not both
cust_store1.symmetric_difference(cust_store2)

#Return True if two sets have a null intersection.
#Before joining multiple datasets, we want to know whether they have connections?
cust_store1= {1,2}
cust_store2= {3,4}
cust_store1.isdisjoint(cust_store2)

#Become a core Python Developer...
#Give you one more usecase to cover this collection type..