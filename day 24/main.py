# using absolute file path
# with open("/Users/benjy/Desktop/my_file.txt") as file:
#     content = file.read()
#     print(content)

# if using terminal and says directory is C:\Users\benjy\OneDrive\Coding then only ../../Desktop/myfile.txt needed
# if using computer command line and running code from day 24 then need 4 ../
with open("../../../../Desktop/my_file.txt") as file:
    content = file.read()
    print(content)
# with open("new_file.txt", mode='a') as file:
#     file.write("\nNew text.")
