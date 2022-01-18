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
            

