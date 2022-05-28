#----------------------------------------------------------------------------
#Title: Assignment07
#Description: Provide examples on pickling and structured error handling
#Changelog: (Who, When, What)
#DHolland, 5.28/2022, Created Script
#------------------------------------------------------------------------------

#Pickling
import pickle
MyList = ['Dustin Holland', 'John Smith', 'Luke Collins', 'John Doe']
MyDictionary = {'Name':'Dustin', 'Occupation': 'Student'}
Myfile = open('MyPickleTest.dat', 'wb')

pickle.dump(MyList, Myfile)
pickle.dump(MyDictionary, Myfile)
Myfile.close()

#Unpickling
Myfile=open('MyPickleTest.dat', 'rb')
MyList = pickle.load(Myfile)
MyDictionary = pickle.load(Myfile)
print(MyList)
print(MyDictionary)
Myfile.close()
print('We have now pickled and unpickled data. Moving on to Structured Error Handling')

#Structured Error Handling Example
valid = False
while not valid:
    try:
        UserInput =int(input('Please Enter a number:'))
        valid = True
        print('Thank you for following my instructions :)')
    except ValueError:
        print('I SAID ENTER A NUMBER!!')

