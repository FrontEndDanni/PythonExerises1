#Using the given list, print out a filtered version of the list with only the numbers that are less than ten.
alist = [1,11,14,5,8,9]
num = [i for i in alist if i < 10]
print(num)
#output: [1, 5, 8, 9]

#Merge and sort the two lists below.
l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]
l_3 = l_1 + l_2
print(l_3.sort())
print(l_3)
#output: 
#None
#[1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8, 10]