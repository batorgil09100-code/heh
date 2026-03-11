while True:
    print("\n1.show students\n2.add student\n3.update students\n4.delete student\n5.Exit")
    a = input("Choose: ")
    if a == "1":
        with open("data.txt", "r") as file:
            print(file.read())

    elif a == "2":
        x = input("enter name: ")
        a = int(input("enter age: "))
        with open("data.txt", "a") as file:
            print(file.write(f"{x}, {a}"))
        # with open("data.txt", "a") as file:
        #     print(file.write(a))


    # elif a == "3":
    #     # w = input("enter name: ")
    #     # q = input("new name: ")

    #     with open("data.txt", "r") as file:
    #         lines = file.readlines()
    #         for line in lines:
    #             print(line)
                # if line == 


                


        # with open("data.txt", "w") as file:
        #     for i in lines:
        #         if i.split() == w:
        #             file.write(q)
        #         else:
        #             file.write(i)

    elif a == "5":
        break



