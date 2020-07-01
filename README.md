# Except Error
- **You can define as many exception blocks as you want**
- **If you want to execute a special block of code for a special kind of error**
- **Type error,Name error,value error**
- **Print one message if the try block raises a NameError and another for other errors**
## sample code for eexcept error
```
try:
   print(c)
except NameError:
   print("Variable c is not defined")
except:
   print("Something else went wrong")
```
## Example Output
```
Enter the value:121
Variable c is not defined
```


