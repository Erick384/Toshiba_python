class Students:
    def __init__(self, name , course, gender, age):
        self.name = name
        self.course = course
        self.gender = gender
        self.age = age

    def wakurugenzi(self):
        print("Name: %s \n Course: %s\n Gender: %s \n Age : %d" %(self.name, self.course, self.gender, self.age))


std1 = Students("Erick Kamoko","Software Engineering","Male",22)
std1.wakurugenzi()
std2 = Students("Alpha Mwaniki","Acturial Science","Male",19)
std2.wakurugenzi()
std3 = Students("Githaiga Victor","Pure Mathematics","Male",16)
std3.wakurugenzi()
std4 = Students("Jackie Alpha","Hospitality Management","Female",17)
std4.wakurugenzi()
std5 = Students("Alice K","English Literature","Female",20)
std5.wakurugenzi()