pozdrav = "Ahoj"
if pozdrav == "Ahoj":
    print("Ahoj")
elif pozdrav =="Čau":
    print("Čau")

match pozdrav:
    case "Ahoj":
        print("Ahoj")
    case"Čau":
        print("Čau")
    case _:
        print("nebyl zvolen pozdrav")