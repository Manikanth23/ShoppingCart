from datetime import datetime
from item import items
from datetime import date

class ShoppingCart:
    storename='Mani Supermarket'
    place='Alwal'
    price=0
    totalprice=0
    finalprice=0
    gst=0
    totalgst=0
    totaldiscount=0
    def __init__(self,name):
        self.name=name
        self.plist=[]
        self.qlist=[]
        self.pricelist=[]
        self.gstlist=[]
        self.ilist=[]
        self.dlist=[]
        
    def additems(self): 
        for i in range(len(items)):
            choice=int(input("Enter 1 to buy or 2 for exit: "))
            if choice==2:
               break
            if choice==1:
                item=input('Enter item name: ')
                quantity=int(input("Enter quantity: "))
                discountper=int(input("Enter Discount perentage:"))
                gstper=int(input('Enter GST percentage: '))
                if item in items.keys():
                    price=quantity*(items[item])
                    
                    discount=price*discountper/100
                    gst=(price-discount)*gstper/100
                    self.pricelist.append((item,quantity,items,price,gst))
                    self.plist.append(price)
                    self.qlist.append(quantity)
                    self.ilist.append(item)
                    self.gstlist.append(gst)
                    self.dlist.append(discount)
                    self.totalprice+=price
                    self.totalgst+=gst
                    self.totaldiscount+=discount
                    self.finalprice=gst+self.totalprice-discount
                    

                else:
                    print("Entered Items Not Available ")
            else:
                print('Please Enter Valid Number') 
                
    def billinginfo(self):
        inp=input("Can I Bill the Items Yes or No: ")
        print()
        if inp.lower()=='yes':
            if self.finalprice!=0:     
               print(25*"=",ShoppingCart.storename,25*"=")
               print(32*"=",ShoppingCart.place,32*"=")
               #print("Name:",name,30*" ","Date:",datetime.now().strftime('%a %b %d %Y  %I:%M:%I%p'))
               print("Name:",name,30*" ","Date:",date.today(),  "Time:",datetime.now().strftime('%H:%M:%S %p'))
               print(75*"-")
               print("S.No ",8*" ","Item name",8*" ","Quantity",3*" ",'Amount')
               for i in range(len(self.pricelist)):
                  print(i, 12*" ", self.ilist[i], 12*" ",  self.qlist[i],8*" ",8*" ",self.plist[i])
               print()
               print(50*" ","Total Amount: ","Rs",self.totalprice)
               print(50*" ","Discount Amount: ",  "Rs",-self.totaldiscount)
               print(50*" ","GST Amount: ",  "Rs",self.totalgst)
               print(75*"-")
               print(50 * " ","Final Amount: ", "Rs", self.finalprice)
               print(75*"-")
               print(20 * " ", "Thanks For Visiting... Visit Again....")
               print(75*"=")                 
print(items)                                      
name=input('Enter name:') 
s=ShoppingCart(name)     
s.additems() 
s.billinginfo()          