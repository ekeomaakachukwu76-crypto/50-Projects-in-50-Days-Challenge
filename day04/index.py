def Calculator(begin):
    while True:
     if begin == "Start":
            print("Starting...")
     else:
            print("Type in 'Start")
     X = input("Type in an X value")
     Y = input("Type in a Y value")
     print(int(X+Y))
     print(int(X-Y))
     print(X*Y)
     print(X/Y)
     
Run = Calculator(input("Type in 'Start'"))
print(Run)
     
    
     