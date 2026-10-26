# INVENTORY MANAGEMENT SYSTEM
# Welcome 

print("\n======== INVENTORY MANAGEMENT ========")

products = []

while True:
   print("\n1. Add Product")
   print("2. View Product")
   print("3. Search Product")
   print("4. Update Product")
   print("5. Cancel Order")
   print("6. Exit")
   print("-----------------------------------------------------------------")
   
   choice = input("Enter Your Choice: ")
   
   #spideyshahid
   
   if choice == "1":
       product_id = input("Enter Product ID: ")
       name = input("Enter Product Name: ")
       price = float(input("Enter Product Price: "))
       quantity = int(input("Enter Product Quantity: "))
       
       product = {
           "id" : product_id,
           "name" : name,
           "price" : price,
           "quantity" : quantity
       }
       
       products.append(product)
       print("Product added successfully!")
       print("-----------------------------------------------------------------")
       
    #Nobita
    
   elif choice == "2":
       
        if len(products) == "0":
           print("No Products Available.")
        else:
            print("\n ---------- Product List ----------")
            
            for product in products:
                print("ID:", product["id"])
                print("Name:", product["name"])
                print("Price:", product["price"])
                print("Quantity:", product["quantity"])
        print("-----------------------------------------------------------------")
        
        #Spiderman
          
  
   elif choice == "3":
        search_id = input("Enter Product ID TO Search: ")
        found = False
        
        for product in products:
            
            if product["id"] == search_id:
             print("ID:", product["id"])
             print("Name:", product["name"])
             print("Price:", product["price"])
             print("Quantity:", product["quantity"]) 
             
             found = True
             break  
             
        if found == False:
            print("Product not found!")
        print("-----------------------------------------------------------------")

       #Doraemon

   elif choice == "4":
       search_id = input("Enter Search ID to Update: ")
       found = False
       
       for product in products:
           if product["id"] == search_id:
              print("1. Update Price")
              print("2. Update Quantity")
              
           update_choice = input("Enter Your choice: ")
           
           if update_choice == "1":
               new_price = float(input("Enter New Price: "))
               product["price"] = new_price
               print("Price Updated Successfully!")
               
           elif update_choice == "2":
               new_quantity = int(input("Enter New Quantity: "))
               product["quantity"] = new_quantity
               print("Quantity Updated successfully!")
           else:
               print("INVALID CHOICE!")
               
           found = True
           break
       
       if found == False:
           print("Product not found!")
           
           #Shinchan
       
   elif choice == "5":
       search_id = input("Enter Product ID to Cancel Order: ")
       
       found = False
       
       for product in products:
           if product["id"] == search_id:
               products.remove(product)
               found = True
               print("Order Cancelled !")
               break
           
       if found == False:
           print("Product not found !")
           
        #Naruto 
        
   elif choice == "6":
       print("Thank you for using Inventory Management System!")
       break
   
   else:
       print("Invalid choice! Please sleect 1-6")
               
               