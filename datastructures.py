#We are learning different types of list of data input
#When creating lists, we use []
#when creating tuples, we use ()
#When creating sets, we use {}



#list are ordered
fruits = ["Mangoes","Oranges","Banana","Watermelon",67]
num =[11, 2, 7, 4, 8, 0]
num.sort()
num[3] =9
rep=num*2
print(len(num))

print(fruits)
fruits[1] = "Apples"
print(f"I love eating {fruits[1]}")
print(num)
print(sorted(num))
print(rep)


#Tuples immutables ordered
cars =("Toyota","Mercedes","nissan")
#cars[0]="vw"
print(cars[0])
tup=cars*3
print(tup)
print(tup.count("nissan"))

# sets unordered
days = {"Monday","Tuesday","Wednesday","Thursday","Friday"}
print(days)

# dictionaries (Dict)
staff_details = {"Name": "Owen", "Age": "48", "Company": "Huawei", "Gender": "Male", "Salary": 100000}
print(f"Name %s" %staff_details)
print("Name %s" %staff_details["Name"])
print("salary %s" %staff_details["Salary"])
print("Age %s" %staff_details["Age"])
print("Company %s" %staff_details["Company"])