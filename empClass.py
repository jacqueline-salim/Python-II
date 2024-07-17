### Write the class into a separate Python file
# this command writes the file automatically, it hs to be the top of the code chunk, the first line
#codes to write follows below


class Employee:
    def __init__(self, first_name, last_name, emp_number): #Declaring attributes
        self._first_name = first_name #_first_name is a private variable -> attributes here cannot be assessed outside of the class
        self._last_name = last_name 
        self._emp_number = emp_number 
        
    #getter
    @property #decorator for getter
    def first_name(self):
        return self._first_name + "123"
    @property #decorator for getter
    def last_name(self):
        return self._last_name 
    @property
    def emp_number(self):
        return self._emp_number
    @property
    def full_name(self):
        return self.first_name + " " + self.last_name
 
    #setter
    @first_name.setter #the setter allows you to "set" values
    def first_name(self, newName):
        self._first_name = newName
    @last_name.setter
    def last_name(self, newLName):
        self._last_name = newName
    @emp_number.setter
    def emp_number(self, newNum):
        self._last_name = newNum
