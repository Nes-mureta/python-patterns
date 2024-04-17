class equalt_triangle:
    def pattern(self,n):
        k = 2*n - 2
        for i in range(0, n):
            for j in range(0, k):
                print(end=" ") 
            k = k-1
            for j in range(0, i+1):
                print("* ", end="")
            
            print("")
   
class updown_triangle:
    def pattern(self,n):
        for i in range(n, 0, -1):
            for j in range(i,n):
                print(' ', end='')
            for j in range(0, i):
                print('*', end=' ')
            print()

class Rtriangle:
    def pattern(self,n):
        for i in range(0,n):
            for j in range(0,i+1):
                print("* ", end="")
            print("\r")
class reverse_Rtriangle:
    def pattern(self,n):
        k=2*n-2
        for i in range(0,n):
            for j in range(0,k):
                print (end=" ")
            k=k-2
            for j in range(0,i+1):
                print("* ", end="")
            print("\r")
class updown_Rtriangle:
    def pattern(self,n):
        for i in range(n,-1,-1):
            for j in range(0,i+1):
                print("* ", end="")
            print("\r")
class reverse_updown_Rtriangle:
    def pattern(self,n):
        k=2*n-2
        for i in range(n,-1,-1):
            for j in range(k,-1,-1):
                print(end=" ")
            k=k+2
            for j in range(0,i+1):
                print("* ", end="")
            print("\r")
def back_to_main():
    print("1. Back to main menu")
    print("2. Exit")
    option=int(input("Enter your choice: "))
    match option:
        case 1:
            main()
        case 2:
            exit()
def main():
    print("##########Enter the shape you want to print###########")
    print("\t\t1. Equal Triangle")
    print("\t\t2. Up Down Triangle")
    print("\t\t3. Right Triangle")
    print("\t\t4. Reverse Right Triangle")
    print("\t\t5. Up Down Right Triangle")
    print("\t\t6. Reverse Up Down Right Triangle\n")
    option=int(input("Enter your choice: "))
    match option:
        case 1:
            shape=equalt_triangle()
            shape.pattern(int(input("Enter the number of rows: ")))
            back_to_main()
            main()
        case 2:
            shape=updown_triangle()
            shape.pattern(int(input("Enter the number of rows: ")))
            back_to_main()
            main()
        case 3:
            shape=Rtriangle()
            shape.pattern(int(input("Enter the number of rows: ")))
            back_to_main()
            main()  
        case 4:
            shape=reverse_Rtriangle()
            shape.pattern(int(input("Enter the number of rows: ")))
            back_to_main()
            main()
        case 5:
            shape=updown_Rtriangle()
            shape.pattern(int(input("Enter the number of rows: ")))
            back_to_main()
            main()
        case 6:
            shape=reverse_updown_Rtriangle()
            shape.pattern(int(input("Enter the number of rows: ")))
            back_to_main()
            main()
            
if __name__ == '__main__':
    main()
    