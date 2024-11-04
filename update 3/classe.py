from classes import *
from day import today
class1 =''
class2 =''
class3 =''
class4 =''
class5 =''
class6 =''
class7 =''
if today == "Saturday":
    class1=sun[0]
    class2=sun[1]
    class3=sun[2]
    class4=sun[3]
    class5=sun[4]
    class6=sun[5]
    class7=sun[6]
elif today == "Sunday":
    class1=mon[0]
    class2=mon[1]
    class3=mon[2]
    class4=mon[3]
    class5=mon[4]
    class6=mon[5]
    class7=mon[6]
elif today == "Monday":
    class1=tues[0]
    class2=tues[1]
    class3=tues[2]
    class4=tues[3]
    class5=tues[4]
    class6=tues[5]
    class7='none'
elif today == "Tuesday":
    class1=wednes[0]
    class2=wednes[1]
    class3=wednes[2]
    class4=wednes[3]
    class5=wednes[4]
    class6=wednes[5]
    class7='none'
elif today == "Wednesday":
    class1=thurs[0]
    class2=thurs[1]
    class3=thurs[2]
    class4=thurs[3]
    class5=thurs[4]
    class6=thurs[5]
    class7='none'
else:
    class1=sun[0]
    class2=sun[1]
    class3=sun[2]
    class4=sun[3]
    class5=sun[4]
    class6=sun[5]
    class7=sun[6]
