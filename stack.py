#CODE:

def create_stack():
	stack = []
	return stack

def peek(stack):
	if len(stack) == 0:
		return "Underflow"
	else:
		return stack[-1]

def isEmpty(stack):
	if len(stack) == 0:
		return True
	else:
		return False

def push(stack):
    element=int(input("Enter the element:"))
    #int should be used if we want to accept int type elements
    
    stack.append(element)
    print("Element",element,"added successfully to the stack") 
    #the above print statemnt is not used in the newer versions of marking scheme 

def pop(stack):
    if (len(stack) == 0):
        print("Stack empty")    #Based on the question one can also display "Underflow"
    else:
        print ("Deleted element :",stack.pop())
            

