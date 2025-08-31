"""
list is a collection/group of items/values/elements
they can be enclosed within the square brackets[]seperated by (,)
list methods: append/extend/count/mutability/index/remove/pop/insert
syntax: listname.methodname()
"""
#append: this method is used to add the elements at the end
#program
list1=["edinburgh","scotland","london"]
print(list1)
list1.append("brihingam")
print(list1)
#extend:this method is used to added the elements at the end but
# as a sublist
#program
list1.extend(["paris","malta"])
print(list1)
#count: this method counts the number of repeated elements in a list
#program
flowers=["rose","mary","rose","jasmine","hibiscus"]
flowers.count(("rose"))
print(flowers)
#mutability::changing the elements
#program
mylist4=["hello","ece",630,67,26+07j]
print(mylist4)
mylist4[2]="agr"
print(mylist4) 
#pop--remove the element using index
#program
mylist5=[34,45,768,89.90,67+45j] 
print(mylist5)
mylist5.pop(2)
print(mylist5)
#remove--it remove the element directly
#program
mylist5.remove(34)
print(mylist5)
#count--it count the number of occurance
#of a item in a list
#program
mylist6=[45,67,89,78,90,43,12]
print(mylist6.count(45))
#note: i will take at most only one argument is allowed

#insert--it just insert the elements into the list
#using the index
#program
mylist7=[20,40,50,60,90]
print(mylist7)
mylist7.insert(1,"hello")
print(mylist7)

"""Note:In insert method no element is removed
"they just replaces the position"
"""
#index--this method tells the
#index of first occurance of a element

mylist8=[56,78,56,90,90,34,12]
print(mylist8.index(56))#0
print(mylist8.index(90))#3
#reverse--it ust reverse the elements
#program
mylist8.reverse()
print(mylist8)
#copy--it just copy the element in a list from
#one list to other
#program
mylist9=[78,90,67,56,77,33,21]
print(mylist9)
mylist10=mylist9.copy()
print(mylist10)
#clear--it clear the element in a list
#program
print(mylist10.clear())
print(mylist10)
#sort--it just arrange the elements in a strong way
#program
mylist11=[44,88,66,22]
mylist11.sort()
print(mylist11)
mylist12=["s","r","u","j","i"]
mylist12.sort()
print(mylist12)
mylist13=[13,143,"hello"]
print(mylist13)
print(mylist13)


