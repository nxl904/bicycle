model = {
    "Huffy" :["Crusier", 129.99,15.9],
    "Schwinn":["Panther", 505.99,8.2],
    "Trek":["Fuel Ex",8999.99, 6.1],
    "Nashboar":["Carbon 105",1999.99, 7.0],
    "Haro":["Steel Reserve 1.2",179.99, 14.3],
    "Megalith":["Fat Bike",199.99, 12.1]
}

cust ={
    "Jim" :[200], 
    "Sara":[700],
    "Rick":[11000]
}

remaining_inventory = {}

class bicycle (object): 
    
    def inventory(self): 
        for i in model: 
            inv = (i, model[i][2])
            print (inv)
        print()
        

class shop(object):

    def Margin (self, markup):
        markup = 1.20
        if markup > 0: 
          for markup in model:
            markup = round(((model[markup][1])*1.20))
            return


class customers(object):
    
    def cust_budget(self, cust_name):
        #cust_name = input("Enter a customer's name: ")
        while cust_name =="Jim" or cust_name =="Rick" or cust_name =="Sara":
            if cust_name =="Jim":
                for cost in model: 
                    if int(((model[cost][1]))) <= 200: 
                        Jim_Afford = (cost)
                        print  (Jim_Afford)
                    
                           
            elif cust_name =="Sara": 
                for cost in model: 
                    if int(((model[cost][1]))) <= 700 :
                        Sara_Afford = (cost)
                        print (Sara_Afford)
                        
            elif cust_name =="Rick": 
                for cost in model: 
                    if int(((model[cost][1]))) <= 11000 :
                        Rick_Afford = (cost)
                        print (Rick_Afford)
            
            else: 
                print ("You didn't enter the correct name, try again")
                
            break
          
    def cust_purchase(self, cust_name):
        global cust_select_q
        global bike_cost
        global wholesale
        print(cust_name, "can afford the following: ")
        (self.cust_budget(cust_name))
        cust_select_q = input("Which one would you like to purchase? ")
        for cost in model:
            wholesale = int((model[cost][1]))
            bike_cost = round(wholesale * 1.20)
            if (cost) == cust_select_q:
                print("Ok, the", cust_select_q, "is", bike_cost )
                for budget in cust:
                    cust_bud_name = (budget)
                    cust_bud_cost = int((cust[budget][0]))
                    if cust_name == cust_bud_name:
                        cust_funds = cust_bud_cost - bike_cost
                        print(cust_bud_name, "now has", cust_funds, "dollars left in the account")
      
    def remaining_inventory(self):
        print ("The following is left in the stores inventory: ")
        for purchase in model: 
            while cust_select_q != (purchase):
                 remaining_inventory = purchase
                 print(remaining_inventory)
                 break
                 
    def profit(self):
        print ("The store made the following profit on the sale: ")
        money = bike_cost - wholesale
        print (money)
         
 
        
        
            
            
            
            
        

#shp = shop()
#shp.Inventory()
#shp.Margin(1.20)


cst = customers()
#cst.cust_budget()
cst.cust_purchase("Sara")
cst.remaining_inventory()
cst.profit()

#bic = bicycle()
#bic.inventory()