namelist = []
surnamelist = []
userlist = []
pwlist = []
idlist = []

print("Welcome Employee System Program".center(80, "="))
print("1 Register Employee")
print("2 Delete Employee")
print("3 Show Data Employee")
print("4 Exit Program")
menu = int(input("Please select menu[1-3] : "))
while menu != 4:
    if menu == 1 :
        print("="*80)
        print("REGISTER EMPLOYEE".center(80))
        print("="*80)
        fullname = input("Enter firstname and lastname : ").split(' ')
        first_name,last_name = fullname[0].lower(), fullname[1].lower()
        username = first_name + "." + last_name[0]
        pwd = first_name[1]+first_name[3].upper()+first_name[2].upper()+str(len(fullname))+first_name[4]
        while True:
            id_card = input("Enter ID card [13 digits]: ")
            if(id_card.isnumeric() and len(id_card) == 13):
                print("Register Completed")
                break;
            else:
                print("Invalid ID card")
        namelist.append(first_name)
        surnamelist.append(last_name)
        userlist.append(username)
        pwlist.append(pwd)
        idlist.append(id_card)
    elif menu == 2 :
        print("="*80)
        print("DELETE EMPLOYEE".center(80))
        print("="*80)
        while True:
            delete_name = input("Enter name employee to delete : ").lower()
            try:
                index = namelist.index(delete_name)
                del namelist[index]
                del surnamelist[index]
                del userlist[index]
                del pwlist[index]
                del idlist[index]
                # namelist.remove(delete_name) #ต้องการลบแค่ตัวเดียว
                print("Delete Completed")
                break
            except:
                print("Invalid name !!")
    elif menu == 3 :
        print("="*80)
        print("SHOW DATA EMPLOYEE".center(80))
        print("="*80)
        print("%-6s %-12s %-18s %-12s %-12s %s "%("No.","Name","Surname","Username","Password","ID Card"))
        for i in range(len(namelist)) :
          print("%-6s %-12s %-18s %-12s %-12s %s "%(i+1,namelist[i],surnamelist[i],userlist[i],pwlist[i],idlist[i]))
    else :
        print("Incorrect menu!!") 
    print("="*80)
    print("1 Register Employee")
    print("2 Delete Employee")
    print("3 Show Data Employee")
    print("4 Exit Program")
    menu = int(input("Please select menu[1-3] : "))
print("Exit Program".center(80,"="))
