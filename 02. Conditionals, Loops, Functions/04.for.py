blog_posts = ["The 10 cooles math functions for python","", "How to make http requests in python", "A tutorial about data types"]

for post in blog_posts:
    if post == "":   #Si el post esta vacio
        continue
    else:
        print(post)

print("--------------------")

myString = "This is a string"

for char in  myString:
    print(char)


print("---------------------")

for x in range (0,10):
    print(x)

print("---------------------")

person = {"Name": "Jose Manuel", "Age" : 25, "Gender":"Male"}

for key in person:
    print(key,":",person[key])

print("-.--------------------")

blog_posts ={ "Python" : ["The 10 cooles math functions for python","", "How to make http requests in python", "A tutorial about data types"], "JavaScript" : ["Algorithms with JS"]}

for category in blog_posts:
    print("Posts about", category)

    for post in blog_posts[category]:
        print(post)