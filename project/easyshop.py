import cx_Oracle
class address(object):
  def adde(self):
        self.details()
  def details(self):
        print("......................ADDRESS DETAILS................................")
        print(" ")
        print("ENTER TO SET ADDRESS ID:")
        self.getaddressid()
  def getaddressid(self):
        self.id1=str(input())
        print("ENTER THE  ADDRESS LINE:")
        self.getaddressline()
  def getaddressline(self):
        self.ad=str(input())
        print("ENTER THE CITY:")
        self.getcity()
  def getcity(self):
        self.ci=str(input())
        print("ENTER THE ZIPCODE")
        self.getzip()
  def getzip(self):
        self.zi=int(input())
        print("ENTER THE STATE")
        self.getstate()
  def getstate(self):
        self.cit=str(input())
        self.detail(self.id1,self.ad,self.ci,self.zi,self.cit)
class customer(address):
    def detail(self,id2,ad2,ci2,zi2,cit2):
        self.addi=id2
        con=cx_Oracle.connect("ruban/ruban@127.0.0.1/XE")
        cur=con.cursor()
        sql = "insert into address VALUES('%s','%s','%s','%d','%s')" % (id2,ad2,ci2,zi2,cit2)
        cur.execute(sql)
        con.commit()
        addi=id2
        print("...........................CUSTOMER DETAILS..........................................")
        print(" ")
        print("ENTER TO SET CUSTOMER ID")
        self.getcustid()
    def getcustid(self):
        self.cusid=str(input())
        print("ENTER CUSTOMER NAME")
        self.custname()
    def custname(self):
        self.cusna=str(input())
        print("ENTER MOBILE NUMBER")
        self.mob()
    def mob(self):
        global cardno
        global card
        global card11
        self.mobil=int(input())
        print("ENTER THE ITEM TO BUY")
        self.ite=str(input())
        print("ENTER THE AMOUNT TO BUY :")
        self.amo=int(input())
        if self.amo<=1000:
           print(".................YOU ARE REGULAR CUSTOMER................")
           print(" ")
           ssm=1000-self.amo
           print("TO CHANGE YOUR ACCOUNT TO PREVILEGED BUY PRODUCT FOR RUPEES $",ssm)
           card="REGULAR"
        elif self.amo>1000 and self.amo<=2000:
           print("                ####SILVER MEMBER SHIP CARD IS ALLOCATED                 ")
           print("   ")
           print("-------------------YOU ARE ONE OF OUR PRIVILEGED CUSTOMER-------------------------")
           print("  ")  
           print("ENTER ANY NUMBER FOR MEMBERSHIP CARD SHOULD HAVE 6 CHARACTERS MINIMUM")
           card="silver"
           #print("   ")
        elif self.amo>2000 and self.amo<=5000:
          print("                 #### GOLD MEMBER SHIP CARD IS ALLOCATED            ")
          print("   ")
          print("-------------------YOU ARE ONE OF OUR PRIVILEGED CUSTOMER-------------------------")
          print(" ")
          print("ENTER ANY NUMBER FOR MEMBERSHIP CARD SHOULD HAVE 6 CHARACTERS MINIMUM")
          card="gold"
          #print("   ")
        elif self.amo>5000:
          print("                 ####PLATINUM MEMBER SHIP CARD IS ALLOCATED")
          print("  ")
          print("-------------------YOU ARE ONE OF OUR PRIVILEGED CUSTOMER-------------------------")
          print(" ")
          print("ENTER ANY NUMBER FOR MEMBERSHIP CARD SHOULD HAVE 6 CHARACTERS MINUMUM")
          card="platinum"
          #print("   ")
        else:
          print(" THANK YOU VISIT AGAIN .........................")
        cardno=str(input())
        con=cx_Oracle.connect("ruban/ruban@127.0.0.1/XE")
        cur=con.cursor()
        sql = "insert into cus VALUES('%s','%s','%s','%s','%s','%s','%s')" % (self.cusid,self.cusna,self.mobil,cardno,self.amo,card,self.addi)
        cur.execute(sql)
        con.commit()
class account(customer,address):
  def aco(self):
    global val1
    global dis
    global idn
    print("ENTER THE CUSTOMER ID")
    idn=str(input())
    con=cx_Oracle.connect("ruban/ruban@127.0.0.1/XE")
    cur=con.cursor()
    sql = "select cusname from cus where cuid='%s'" % (idn)
    cur.execute(sql)
    valu=cur.fetchone()
    if valu is None:
      print("ID YOU ENTERED IS WRONG PLEASE ENTER THE VALID ID")
      vv=str(input())
      idn=vv
      sql = "select amount from cus where cuid='%s'" % (vv)
      cur.execute(sql)
      valu1=cur.fetchone()
      #hh=valu1[0]
      print("YOUR CURRENT BALANCE IS: ")
      print(valu1[0])
      con=cx_Oracle.connect("ruban/ruban@127.0.0.1/XE")
      cur=con.cursor()
      sql = "select cardt from cus where cuid='%s'" % (vv)
      cur.execute(sql)
      au1=cur.fetchone()
      print("YOUR MEMBER SHIP CARD BELONG TO ")
      print(au1[0])
    else:
       sql = "select amount from cus where cuid='%s'" % (idn)
       cur.execute(sql)
       valu1=cur.fetchone()
       print("YOUR CURRENT BALANCE IS: ")
       print(valu1[0])
       print(" ")
       sql = "select cardt from cus where cuid='%s'" % (idn)
       cur.execute(sql)
       au1=cur.fetchone()
       print("YOUR MEMBER SHIP CARD BELONG TO ")
       print(au1[0])
    print(" ")
    print("ENTER ANY ITEM TO BUY :")
    bbb=str(input())
    print("ENTER THE AMOUNT TO BUY: ")
    amoun=str(input())
    amoun1=int(valu1[0])+int(amoun)
    round(amoun1)
    if amoun1<2499:
      val1=amoun1
      dis=0
    elif amoun1>2500 and amoun1<5000:
      dis=(2/100)*amoun1
      val=amoun1-dis
      val1=val
    elif amoun1>5000 and amoun1<8000:
      dis=(5/100)*amoun1
      val=amoun1-dis
      val1=val
    elif amoun1>8000:
      dis=(10/100)*amoun1
      val=amoun1-dis
      val1=val
    else:
      print("SORRY YOU ARE NOT ELIGIBLE FOR DISCOUNT")
    sql = "update cus set amount='%s' where cuid='%s'" % (round(val1),idn)
    cur.execute(sql)
    con.commit()
    if val1<=1000:
      print("YOU ARE REGULAR CUSTOMER")
      card11="REGULAR"
      dis=0
    if val1>1000 and val1<=2000:
      print("YOUR CARD IS CHANGED TO SILVER")
      print(" ")
      card11="Silver"
    elif val1>2000 and val1<=5000:
      print("YOUR CARD IS CHANGED TO GOLD")
      print(" ")
      card11="Gold"
    elif val1>5000:
      print("YOUR CARD IS CHANGED TO PLATINUM")
      print(" ")
      card11="Platinum"
    con=cx_Oracle.connect("ruban/ruban@127.0.0.1/XE")
    cur=con.cursor()
    sql = "update cus set cardt='%s' where cuid='%s'" % (card11,idn)
    cur.execute(sql)
    con.commit()
    print("   ")
    print("THANK YOU FOR PURCHASE.................... ")
    print(" ")
    print("---------------------------------------------------")
    print("..............CUSTOMER INFORMATION..................")
    print("---------------------------------------------------")
    sql = "select cusname from cus where cuid='%s'" % (idn)
    cur.execute(sql)
    au2=cur.fetchone()
    x1=au2[0]
    print("CUSTOMER NAME : ",x1)
    sql = "select tpnoo from cus where cuid='%s'" % (idn)
    cur.execute(sql)
    au3=cur.fetchone()
    x2=au3[0]
    print("CUSTOMER MOBILE NUMBER  : ",x2)
    sql = "select memid from cus where cuid='%s'" % (idn)
    cur.execute(sql)
    au4=cur.fetchone()
    x3=au4[0]
    print("CUSTOMER MEMBERSHIP ID NO : ",x3)
    sql = "select amount from cus where cuid='%s'" % (idn)
    cur.execute(sql)
    au5=cur.fetchone()
    x13=au5[0]
    print("CUSTOMER AMOUNT IN CARD: ",x13)
    print("CUSTOMER DISCOUNT AMOUNT : ",dis)
    sql = "select cardt from cus where cuid='%s'" % (idn)
    cur.execute(sql)
    au6=cur.fetchone()
    x4=au6[0]
    print("CUSTOMER CARD TYPE : ",x4)
    sql = "select addressid from cus where cuid='%s'" % (idn)
    cur.execute(sql)
    au7=cur.fetchone()
    x5=au7[0]
    print("CUSTOMER ADDRESS ID: ",x5)
    sql = "select city from address where addressid='%s'" % (x5)
    cur.execute(sql)
    au8=cur.fetchone()
    x6=au8[0]
    print("CUSTOMER ADDRESS : ",x6)
    sql = "select addressline from address where addressid='%s'" % (x5)
    cur.execute(sql)
    au9=cur.fetchone()
    x7=au9[0]
    print("CUSTOMER ADDRESS LINE : ",x7)
    sql = "select zip from address where addressid='%s'" % (x5)
    cur.execute(sql)
    au10=cur.fetchone()
    x8=au10[0]
    print("CUSTOMER ZIP CODE : ",x8)
    sql = "select state from address where addressid='%s'" % (x5)
    cur.execute(sql)
    au11=cur.fetchone()
    x9=au11[0]
    print("CUSTOMER STATE : ",x9)
    print("----------------------------------------------------")
    print(" ")
    if x4!="REGULAR":
      print("***************ONLY FOR PREVILIGED CUSTOMER*******")
      print(" ")
      print("DO YOU WANT TO SEND ITEM THROUGH DELIVARY yes/no...")
      da=str(input())
      if da=="yes":
        print(" ")
        print("-------------------------")
        print("ADDRESS : ",x7)
        print("STATE : ",x9)
        print("ITEM TO SEND ARE: ",bbb)
        print("  ")
        print(" YOUR ITEMS ARE SEND SHORTLY.............")
        print("-----------------------------")
class modify():
  def modif(self):
    print("ENTER THE CUSTOMER ID")
    jl=str(input())
    print(" ")
    print("ENTER THE ADDRESS ID")
    km=str(input())
    print(" ")
    print("PLEASE CHOOSE NUMBER TO MODIFY")
    print("1-PHONE NUMBER")
    print("2-ADDRESS LINE")
    print("3-CITY")
    print("4-ZIPCODE")
    vv=str(input())
    con=cx_Oracle.connect("ruban/ruban@127.0.0.1/XE")
    cur=con.cursor()
    if vv=="1":
      print("ENTER THE NEW PHONE NUMBER")
      ph=str(input())
      sql = "update cus set tpnoo='%s' where cuid='%s'" % (ph,jl)
      cur.execute(sql)
      con.commit()
    elif vv=="2":
      print("ENTER THE NEW ADDRESS LINE")
      ph=str(input())
      sql = "update address set addressline='%s' where addressid='%s'" % (ph,km)
      cur.execute(sql)
      con.commit()
    elif vv=="3":
      print("ENTER THE NEW CITY")
      ph=str(input())
      sql = "update address set city='%s' where addressid='%s'" % (ph,km)
      cur.execute(sql)
      con.commit()
    elif vv=="4":
      print("ENTER THE NEW ZIPCODE")
      ph=int(input())
      sql = "update address set zip='%d' where addressid='%s'" % (ph,km)
      cur.execute(sql)
      con.commit()
    print("-----THANK YOU  YOUR MODIFICATIONS ARE DONE-------")
    print(" ")
class demo():
       while(1):
        print("..............................WELCOME TO EASY SHOP APPLICATION................")
        print("      ")
        print("--------#############An exciting place for whole family to shop##############--")
        print("      ")
        print("Already have account yes/no :")
        j=str(input())
        print("    ")
        if j=="yes":
          print(" ..............................LOGIN WITH YOUR ACCOUNT .......................")
          print(" ")
          mm=account()
          mm.aco()
        else:
          #print(" ")
          print(" CREATE ACCOUNT") 
          mm=customer()
          on=account()
          on.adde()
        print(" ")
        print("DO YOU WANT TO ALTER THE YOUR DATABASE yes/no :")
        hg=str(input())
        if hg=="yes":
          dd=modify()
          dd.modif()
        else:
          print("----------------------THANK TOU-------------------------------------")
          print(" ")
        print("DO YOU WANT TO VIEW REGULAR AND PREVILEGED CUSTOMERS OF OUR SHOP yes/no")
        yy1=str(input())
        if yy1=="yes":
           con=cx_Oracle.connect("ruban/ruban@127.0.0.1/XE")
           cur=con.cursor()
           dd1="REGULAR"
           a1="Gold"
           a2="Silver"
           a3="Platinum"
           sql = "select cusname from cus where cardt='%s'" % (dd1)
           sq8 = "select cusname from cus where cardt='%s' or cardt='%s' or cardt='%s'  " % (a1,a2,a3)
           cur.execute(sql)
           #cur.execute(sq8)
           sq=cur.fetchall()
           #sq3=cur.fetchall()
           print(" ");
           print("##########REGULAR CUSTOMER OF OUR SHOP ARE##########")
           for i in sq:
             print(i[0])
           print(" ")
           print("##########PREVILEGED CUSTOMERS OF OUR SHOP ARE##########")
           cur.execute(sq8)
           sq3=cur.fetchall()
           for j in sq3:
             print(j[0])
          
      
         

       
