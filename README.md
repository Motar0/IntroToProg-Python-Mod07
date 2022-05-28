Dustin Holland

05/22/2022

IT FDN 110A

Assignment 07

# Pickling and Structured Error Handling

#### Introduction:

In this week’s assignment, my task is to create a script that demonstrates how Pickling and Structured Error Handling work in Python.

#### Pickling:
The first part of this assessment is to demonstrate how pickling works. To start, I must first use the import feature to import “Pickle.” Next, I will create some data using the list and dictionary function.

![Result in Pycharm](https://github.com/Motar0/IntroToProg-Python-Mod07/blob/main/Picture1.png)
 
I will then create a file and use the the ‘wb’ mode to write to a binary file. Since I’m not gathering user input for this example, the wb mode is fine. Next, I will use the pickle.dump function to store the contents of my list and dictionary and tell the program which file to store the data in:

![Result in Pycharm](https://github.com/Motar0/IntroToProg-Python-Mod07/blob/main/Picture2.png)
 
#### Unpickling:
To unpickle the file and retrieve the data, I used the pickle.load() function. I used that function for both my list and dictionary data. 
	 
![Result in Pycharm](https://github.com/Motar0/IntroToProg-Python-Mod07/blob/main/Picture3.png)

#### This is the content of the binary file:

![Result in Pycharm](https://github.com/Motar0/IntroToProg-Python-Mod07/blob/main/Picture4.png)
 
#### Structured Error Hanlding:
For this example, I tried doing something a bit more fun than the arithmatic examples I saw over the internet. 
To start I created a variable called ‘valid’ to ensure that my code wont produce an infinite loop and/or break and assigned it as False. Next, I used while not functions to loop and get user input. However, the user input can only be intergers and not strings. I used the try function to gather user input, if the input is ‘True’ (valid=True) then it will print a specific message. If it’s not, I have an except ValueError: that will print a message: 
```python
valid = False
while not valid:
    try:
        UserInput =int(input('Please Enter a number:'))
        valid = True
        print('Thank you for following my instructions :)')
    except ValueError:
        print('I SAID ENTER A NUMBER!!')
``` 

Results in Pycharm:

![Result in Pycharm](https://github.com/Motar0/IntroToProg-Python-Mod07/blob/main/Picture5.png)

Results in OS Command:

![Result in OS Command](https://github.com/Motar0/IntroToProg-Python-Mod07/blob/main/Picture6.png)

#### Research:
1. https://www.toppr.com/guides/python-guide/tutorials/python-files/python-exception-handling/
I enjoyed reading and referring back to this article as it was very simple to understand. I appreciate how the author provided screenshots and the reasoning/logic behind each example. Lastly, I liked how the author provided context in the beginning of the article for new programmers. 

2.	https://www.tutorialspoint.com/python-pickling
Although short, I thought this article was brilliant. The succinctness of it allowed me to grasp the concept fairly quickly (also the professors video aided). Moreover, I liked how the author broke up the code into screenshots  that were extremely straightforward and didn’t contain code I didn’t understand.

#### Summary: 
In summary, I really enjoyed this assignment as it allowed me to take a break and research and code something. I do think I will start using the structured error more in my code as this was completely new for me. 
