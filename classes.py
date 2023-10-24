class Students:
    def __init__(self, name , course, gender, age):
        self.name = name
        self.course = course
        self.gender = gender
        self.age = age

    def wakurugenzi(self):
        print("Name: %s \n Course: %s\n Gender: %s \n Age : %d" %(self.name, self.course, self.gender, self.age))


std1 = Students("Oranjo Kipi","Computer Science","Male",30)
std1.wakurugenzi()
std2 = Students("Mario Jopa","Acturial Science","Femaale",19)
std2.wakurugenzi()
std3 = Students("Dennis Pulisic","Pure Mathematics","Male",27)
std3.wakurugenzi()
std4 = Students("Dandee Motopa","Hospitality Management","Female",33)
std4.wakurugenzi()
std5 = Students("Banlupa Mhindi","Economics and Finance","Male",20)
std5.wakurugenzi()