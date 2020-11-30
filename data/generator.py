import random

if __name__ == "__main__":
    cluster = 3
    points = 100
    file = open("mydata.data", "w")
    classes = ['A', 'B', 'C', 'D', 'E']

    for i in range(cluster):
        for j in range(points):
            x = i*10 + random.randint(0, 5)
            """y = i*10 + random.random()"""
            y = i*10 + random.randint(0, 5)

            # file.write(classes[i] + "," + str(x) + "," + str(y) + ",0,0" + "\n")
            file.write(str(x) + "," + str(y) + ",0,0," + classes[i] + "\n")
