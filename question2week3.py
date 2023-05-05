#Create a menu driven program with user defined functions to create a new file, copy contents from file to another and display a file.
def create():
    name=input("Enter the filename: ")
    f=open(name,"w")
    f.close()
    print("File created")
def copy():
    origin_file=input("Enter the filename where the data is taken from: ")
    copy_file=input("Enter the filename to which the data should be copied: ")
    f=open(origin_file,"r")
    data=f.read()
    f.close()
    fcpy=open(copy_file,"a")
    fcpy.write(data)
    fcpy.close()
    print("Data copied")
def display():
    disp_file=input("Enter the file to be displayed: ")
    f=open(disp_file,"r")
    f.seek(0)
    data=f.read()
    print(data)
while(1):
    print("MENU")
    print("1.Create a file")
    print("2.Copy contents between files")
    print("3.Display contents of a file")
    choice=int(input("Enter the option no. : "))
    if choice==1:
        create()
    elif choice==2:
        copy()
    elif choice==3:
        display()
    else:
        print("NOT VALID CHOICE")