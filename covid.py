
def covid(D):
    D = int(D)
    I = 7
    R = 1.2
    total_infection = None
    population = 39740
    for i in range(D):
        I=R*I
        if (i == 14):
            print("Infected Students at drop/add: " + str(round(I)) )
            print("Money lost: $" + str(round((I*9972), 2)))

    print("Total Infected= {}, % Infected= {} ".format(round(I, 1), round(((I/population)*100), 2)))

if __name__ == "__main__":
    # D = input("Enter D: ")
    # covid(D)
    covid(20)