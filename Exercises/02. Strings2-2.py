#Lets say that your company has a product with this lot number: "037-00901-00027". 027 is the country code. 00901 is the product code. 00027 is the batch number.
#Create a program to print:
#Country code:
#Product code:
#Batch number:

codigo = "037-00901-00027"

print("Country code: " + codigo[:3])

print("Product code: " + codigo[4:-6])

print("Batch number: " + codigo[-5:])