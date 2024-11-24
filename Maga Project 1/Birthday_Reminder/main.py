import datetime 
import mysql.connector as mysql
import pywhatkit
from plyer import notification

Today = datetime.datetime.now()

mysqlobject = mysql.connect(user='root',database='Birthday',host='Localhost',password='12345')

mycur = mysqlobject.cursor()

mycur.execute("Select * from birthdate where DOB like '{}';".format(str(Today.date()).replace(str(Today.year),"____")))
mydata = mycur.fetchone()

Name = mydata[0]
Number = mydata[3]
wished = mydata[2]


if wished==0:

    pywhatkit.sendwhatmsg_instantly(Number,"Happy Birthday {}".format(Name.title()),wait_time=1)
    mycur.execute("Update birthdate set wished=1 where Number = '{}'".format(Number))
    mysqlobject.commit()

if str(Today.date()).replace(str(Today.year),"____")=='____-12-31':
    mycur.execute("Update birthdate set wished = 0")

notification.notify(title="Birthday Wisher",message="Program Run Successfully")