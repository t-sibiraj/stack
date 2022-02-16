#CODE:
max_size = 0             #creating a varible named maz_size  
def create_stack():
    global max_size
    max_size = int(input("Enter the maximum size of the stack:"))
    stack = []
    return stack
    #here we are asking the user for the max_size

def peek(stack):
	if len(stack) == 0:
		print("Underflow")
	else:
		return stack[-1]

def isEmpty(stack):
	if len(stack) == 0:
		return True
	else:
		return False
def isFull(stack):
    if len(stack) == max_size:       #we check if the size of the stazk is full
        return True					#if full we return True
    else:
        return False                  #if not full we return False
    
def push(stack):
    if len(stack) != max_size:       #if the stack is not full we pop(add) elements
        element=int(input("Enter the element:"))
        #int should be used if we want to accept int type elements
    
        stack.append(element)
        print("Element",element,"added successfully to the stack") 
        #the above print statemnt is not used in the newer versions of marking scheme
    else:
        print("Overflow")

def pop(stack):
    if (len(stack) == 0):
        print("Stack empty")    #Based on the question one can also display "Underflow"
    else:
        print ("Deleted element :",stack.pop())
            
'''
#Example 

#Creating a stack
>>> stack_1 = create_stack()
Enter the maximum size of the stack:5

#As the stack is empty we get underflow error
>>> peek(stack_1)
Underflow

#As the stack is empty we get True
>>> isEmpty(stack_1)
True

#pushing element 1 to the stack
>>> push(stack_1)
Enter the element:1
Element 1 added successfully to the stack

#pushing element 2 to the stack
>>> push(stack_1)
Enter the element:2
Element 2 added successfully to the stack

#pushing element 3 to the stack
>>> push(stack_1)
Enter the element:3
Element 3 added successfully to the stack

>>> print(stack_1)
[1, 2, 3]

#displaying the maz size of the stazk
>>> print(max_size)
3

#as the stack full we get Overflow
>>> push(stack_1)
Overflow

#we check if the stack is full or not
>>>isFull(stack_1)
True


#poping elements from the stack
>>> pop(stack_1)
Deleted element : 3   
>>> pop(stack_1)
Deleted element : 2
  
#peeking the topmost element of the stack
>>> peek(stack_1)
1

#checking if the stack is empty or not
>>> isEmpty(stack_1)
False

#poping element from the stack
>>> pop(stack_1)
Deleted element : 1

#as the stack is empty we get Stack empty      
>>> print(stack_1)
[]    
>>> pop(stack_1)
Stack empty
'''
