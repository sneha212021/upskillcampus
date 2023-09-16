#!/usr/bin/env python
# coding: utf-8

# In[1]:


#creation of database and table
import mysql.connector as ms
mycon=ms.connect(host='localhost', user='root',passwd='root@123')
cursor=mycon.cursor()
cursor.execute("create database if not exists project")
cursor.execute("use project")
cursor.execute('''create table if not exists transport(name varchar(50),bookingid int(20),contact decimal(65), taxi varchar(50), pickup varchar(50),dropdown varchar(50),distance int(50), price int(50), date date)''')
mycon.commit()
mycon.close()
#menu driven program starts here
g='y'
while g=='y':
   print("Welcome to TRANSPORT MANAGEMENT SYSTEM")
   print("1. Enter 1 to add passenger's details")
   print("2. Enter 2 to search passenger's details")
   print("3. Enter 3 to update passenger's details")
   print("4. Enter 4 to delete passenger's details")
   print("5. Enter 5 to display passenger's details")
   print("6. Enter 6 to exit")
   print()
   a=int(input("PLEASE ENTER YOUR CHOICE==> "))
#taking the user's choice
   if a==1:
       n='y'
       while n=='y':
           import mysql.connector as ms
           mycon=ms.connect(host="localhost",user="root",passwd="root@123",database="project")
           cursor=mycon.cursor()
           name=input("Enter the passenger's name==>")
           bid=int(input("Enter the booking id of the passenger==>"))
           contact=int(input("Enter the passenger's contact number==>"))
           pup=input("Enter the pickup location==>")
           ddn=input("Enter the dropdown location==>")
           distance=float(input("Enter the net distance travelled==>"))
           date=input("Enter the date of travel in the format yyyy-mm-dd==>")
           print("Choose the taxi types")
           print("1.Mini")
           print("2.Micro")
           print("3.Macro")
           print("4.Sedan")
           print("5.Suv")
           print("6.Luxury")
           print("7.Tempo traveller")
           print("8.Ordinary bus")
           print("9.Volvo A/C bus")
           print("10.Volvo sleeper coach A/C bus")
           b=int(input("enter the type of taxi"))
           if b==1:
               taxi="mini"
               price=distance*5
           elif b==2:
               taxi="micro"
               price=distance*6
           elif b==3:
               taxi="macro"
               price=distance*8
           elif b==4:
               taxi="sedan"
               price=distance*10
           elif b==5:
               taxi="suv"
               price=distance*14
           elif b==6:
               taxi="luxury"
               price=distance*20
           elif b==7:
               taxi="tempo_traveller"
               price=distance*20
           elif b==8:
               taxi="ordinary_bus"
               price=distance*18
           elif b==9:
               taxi="volvo_A/C_bus"
               price=distance*25
           elif b==10:
               taxi="volvo_sleeper_A/C_bus"
               price=distance*30
           cursor.execute('''insert into transport values('{0}',{1},{2},'{3}','{4}','{5}',{6},{7},'{8}')'''.format(name,bid,contact,taxi,pup,ddn,distance,price,date))
           mycon.commit()
           mycon.close()
           print("data successfully added")
           n=input("Enter y if you want to add more details otherwise enter n (y/n)==>")
           print() 
#choice no.1 done
   elif a==2:
       import mysql.connector as ms
       mycon=ms.connect(host="localhost",user="root",passwd="root@123",database="project")
       cursor=mycon.cursor()
       z="y"
       while z=='y':
           bid=int(input("Enter the booking id of the customer whose details have to be displayed==>"))
           cursor.execute('''select * from transport where bookingid={}'''.format(bid))
           data=cursor.fetchone()
           if data!=None:
               print(data)
               print()
           else:
               print("EMPTY/BOOKING ID DOES NOT EXIST")
               print()
           z=input("Enter y if you want to search again otherwise enter n==>")
#choice no.2 done
   elif a==3:
       import mysql.connector as ms 
       mycon=ms.connect(host="localhost",user="root",passwd="root@123",database="project")
       cursor=mycon.cursor()
       z="y"
       while z=='y':
           print("1. Update name")
           print("2. Update contact")
           print("3. Update taxi")
           print("4. Update pickup location")
           print("5. Update drop location")
           print("6. Update total distance travelled")
           print("7. Update date travelled")
           c=int(input("Please enter your choice==>"))
           print()
           if c==1:
               name=input("Enter the modified name==>")
               bid=int(input("Enter the booking id of the customer whose name has to be changed==>"))
               cursor.execute('''select * from transport where bookingid={}'''.format(bid))
               data=cursor.fetchone()
               if data!=None:
                   print("Here are the details of the booking id",bid)
                   print(data)
                   print()
                   a=input("Confirm to update:(y/n)==>")
                   if a=='y':
                       cursor.execute('''update transport set name='{0}' where bookingid={1}'''.format(name,bid))
                       mycon.commit()
                       print("Successfully updated")
                       print()
                   else:
                       print("Updation cancelled")
               else:
                   print("EMPTY/BOOKING ID DOES NOT EXIST")
                   print()
           elif c==2:
               contact=int(input("Enter the modified contact number==>"))
               bid=int(input("Enter the booking id of the customer whose contact has to be changed==>"))
               cursor.execute('''select * from transport where bookingid={}'''.format(bid))
               data=cursor.fetchone()
               if data!=None:
                   print("Here are the details of the booking id", bid)
                   print(data)
                   print()
                   a=input("Confirm to update:(y/n)==>")
                   if a=='y':
                       cursor.execute('''update transport set contact={0} where bookingid={1}'''.format(contact,bid))
                       mycon.commit()
                       print("Successfully updated")
                       print()
                   else:
                       print("Updation cancelled")
               else:
                   print("EMPTY/BOOKING ID DOES NOT EXIST")
                   print()
           elif c==3:
               bid=int(input("Enter the booking id of the customer whose taxi type has to be changed==>"))
               cursor.execute('''select distance from transport where bookingid={}'''.format(bid))
               o=cursor.fetchone()
               distance=o[0]
               print("Choose the taxi types")
               print("1.Mini")
               print("2.Micro")
               print("3.Macro")
               print("4.Sedan")
               print("5.Suv")
               print("6.Luxury")
               print("7.Tempo traveller")
               print("8.Ordinary bus")
               print("9.Volvo A/C bus")
               print("10.Volvo sleeper coach A/C bus")
               print()
               b=int(input("Enter the type of taxi==>"))
               print()
               if b==1:
                   taxi="mini"
                   price=distance*5
               elif b==2:
                   taxi="micro"
                   price=distance*6
               elif b==3:
                   taxi="macro"
                   price=distance*8
               elif b==4:
                   taxi="sedan"
                   price=distance*10
               elif b==5:
                   taxi="suv"
                   price=distance*14
               elif b==6:
                   taxi="luxury"
                   price=distance*20
               elif b==7:
                   taxi="tempo_traveller"
                   price=distance*20
               elif b==8:
                   taxi="ordinary_bus"
                   price=distance*18
               elif b==9:
                   taxi="volvo_A/C_bus"
                   price=distance*25
               elif b==10:
                       taxi="volvo_sleeper_A/C_bus"
                       price=distance*30
               cursor.execute('''select * from transport where bookingid={}'''.format(bid))
               data=cursor.fetchone()
               if data!=None:
                   print("Here are the details of the booking id",bid)
                   print(data)
                   print()
                   a=input("Confirm to update:(y/n)==>")
                   if a=='y':
                       cursor.execute('''update transport set taxi='{0}',price={1} where bookingid={2}'''.format(taxi,price,bid))
                       mycon.commit()
                       print("Successfully updated")
                       print()
                   else:
                       print("Updation cancelled") 
               else:
                   print("EMPTY/BOOKING ID DOES NOT EXIST")
                   print()
           elif c==4:
               pup=input("Enter the modified pickup location==>")
               bid=int(input("Enter the booking id of the customer whose pickup location has to be changed==>"))
               cursor.execute('''select * from transport where bookingid={}'''.format(bid))
               data=cursor.fetchone()
               if data!=None:
                   print("Here are the details of the booking id",bid)
                   print(data)
                   print()
                   a=input("Confirm to update:(y/n)==>")
                   if a=='y':
                       cursor.execute('''update transport set pickup='{0}' where bookingid={1}'''.format(pup,bid))
                       mycon.commit()
                       print("Successfully updated")
                       print()
                   else:
                       print("Updation cancelled")
               else:
                   print("EMPTY/BOOKING ID DOES NOT EXIST")
                   print()
           elif c==5:
               ddn=input("Enter the modified dropdown location==>")
               bid=int(input("Enter the booking id of the customer whose dropdown location has to be changed==>"))
               cursor.execute('''select * from transport where bookingid={}'''.format(bid))
               data=cursor.fetchone()
               if data!=None:
                   print("Here are the details of the booking id",bid)
                   print(data)
                   print()
                   a=input("Confirm to update:(y/n)==>")
                   if a=='y':
                       cursor.execute('''update transport set dropdown='{0}' where bookingid={1}'''.format(ddn,bid))
                       mycon.commit()
                       print("Successfully updated")
                       print()
                   else:
                       print("Updation cancelled")
               else:
                   print("EMPTY/BOOKING ID DOES NOT EXIST")
                   print()
           elif c==6:
               distance=float(input("Enter the modified distance==>"))
               bid=int(input("Enter the booking id of the customer whose total distance has to be changed==>"))
               cursor.execute('''select * from transport where bookingid={}'''.format(bid))
               data=cursor.fetchone()
               if data!=None:
                   print("Here are the details of the booking id",bid)
                   print(data)
                   print()
                   a=input("Confirm to update:(y/n)==>")
                   if a=='y':
                       cursor.execute('''select distance from transport where bookingid={}'''.format(bid))
                       o=cursor.fetchone()
                       ord=o[0]
                       cursor.execute('''select price from transport where bookingid={}'''.format(bid))
                       p=cursor.fetchone()
                       price=p[0]
                       price=(price/ord)*distance
                       cursor.execute('''update transport set distance={0}, price={1} where bookingid={2}'''.format(distance, price,bid))
                       mycon.commit()
                       print("Successfully updated")
                       print()
                   else:
                       print("Updation cancelled")
               else:
                   print("EMPTY/BOOKING ID DOES NOT EXIST")
                   print()
           elif c==7:
               date=input("Enter the modified date of travel in the format yyyy-mm-dd==>")
               bid=int(input("Enter the booking id of the customer whose date of travel has to be changed==>"))
               cursor.execute('''select * from transport where bookingid={}'''.format(bid))
               data=cursor.fetchone()
               if data!=None:
                   print("Here are the details of the booking id",bid)
                   print(data)
                   print()
                   a=input("Confirm to update:(y/n)==>")
                   if a=='y':
                       cursor.execute('''update transport set date='{0}' where bookingid={1}'''.format(date,bid))
                       mycon.commit()
                       print("Successfully updated")
                       print()
                   else:
                       print("Updation cancelled") 
               else:
                   print("EMPTY/BOOKING ID DOES NOT EXIST")
                   print()
           z=input("Enter y if you want to update anything else otherwise enter n==>")
           print()
#choice no.3 done
   elif a==4:
       import mysql.connector as ms
       mycon=ms.connect(host="localhost",user="root",passwd="root@123",database="project")
       cursor=mycon.cursor()
       z="y"
       while z=='y':
           bid=int(input("Enter the booking id of the customer whose details has to be deleted==>"))
           cursor.execute('''select * from transport where bookingid={}'''.format(bid))
           data=cursor.fetchone()
           if data!=None:
               print(data)
               print()
               c=input("are you sure you want to delete the details (y/n)")
               if c=='y':
                   cursor.execute('''delete from transport where bookingid={}'''.format(bid))
                   mycon.commit()
                   print("Successfully deleted")
                   print()
           else:
               print("EMPTY/BOOKING ID DOES NOT EXIST")
               print()
           z=input("Enter y if you want to delete more details otherwise enter n==>")
           print()
#choice no.4 done
   elif a==5:
       import mysql.connector as ms
       mycon=ms.connect(host="localhost",user="root",passwd="root@123",database="project")
       cursor=mycon.cursor()
       z="y"
       while z=='y':
           cursor.execute('''select * from transport''')
           a=cursor.fetchall()
           if a!=None:
               for i in a:
                   print(i)
           else:
               print("EMPTY/NO RECORD TO BE DISPLAYED")
               print()
           z=input("Enter y if you want to display again otherwise enter n==>")
           print()
#choice no.5 done
   elif a==6:
       print("Thank you for using TRANSPORT MANAGEMENT SYSTEM")
       print()
       break
   else:
       print("You have entered wrong choice")
       print()
       g=input("Enter y if you want to continue otherwise enter n (y/n)==>")
       print()
#choice no.6 done
#menu ends here
#program ends here


# In[ ]:




