# 1.Create a dictionary to store the names and ages of 5 people. Access and print the age of one person using their name.
dict={"ram":21,"kavya":24,"rupesh":20,"keerthana":22,"mohan":30}
print(dict["mohan"])


# 2.Write a python program to merge two dictionaries.
dict1={"id":101,"name":"indira","age":30,"department":"data analyst"}
dict2={"item_no":1045783,"product":"bingo"}
# dict4={"id":104,"name":"revathy","age":27,"department":"hr"}
# merged_dict={key:[dict1[key],dict4[key]] for key in dict1}
dict1.update(dict2)
print(dict1)

# print(merged_dict)



# 3.Given a dictionary where the keys are student names and the values are their scores, write a program to calculate the average score.
student_details={"ramya":22,"mohan":30,"kamal":27}
sum=0
for v in student_details.values():
    sum=sum+v
average=sum/3
print(f"Average of student details:{average}")




# 4.Write a dictionary comprehension to create a dictionary where the keys are numbers from 1 to10 and the values are the squares of those numbers.
number=[1,2,3,4,5,6,7,8,9,10]
number_square={num:num**2 for num in number}
print(number_square)



# 5.Write a python program to create a dictionary from a list of keys and values using dictionary comprehension.
list1=[7,3,47,29,35]
keyvalue_dictionary={num:num**3 for num in list1}
print(keyvalue_dictionary)



# 6.Given two lists, one with fruits and the other with prices, write a dictionary comprehension to pair them together into a dictionary.
fruits=["apple","orange","grapes","mango","fig"]
prices=[12,10,26,20,100]
fruitswithprice={k:p for k,p in zip(fruits,prices)}
print(fruitswithprice)



# 7.Write a python program to filter a dictionary, keeping only items with values greater than 50 using dictionary comprehension.

fruitswithprice={'apple': 40, 'orange': 10, 'grapes': 56, 'mango': 32, 'fig': 100}
filter_dict={k for k,v in fruitswithprice.items() if v>50}
print(filter_dict)



# 8.Given a sentence, count the frequency of each word using a dictionary.

text="this is a python programming language interpreter and this language is simple"
word=text.split(" ")                          #converting string to list
words={w:word.count(w) for w in word}
print(words)

# 9.Write a dictionary comprehension to convert all the values in a dictionary to their absolute values.
test_dict = {"Python":3,"is" : -7,"Best":-2}
test={key:abs(num) for key,num in test_dict.items()} 
print(test)

# 10.Given a dictionary of items and their prices, write a program to apply a 10% discount to all the items using dictionary comprehension.

item_withprice={'apple':50,'orange':30,'grapes':56,'banana':45}
discount=0.1
discounted={key:price-price*discount for key,price in item_withprice.items()}
print(discounted)

    