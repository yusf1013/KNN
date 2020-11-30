import math
import random

track = 0
n_fold = 10


def calc_distance(point1, point2):
    sum_result = 0
    dim1 = point1.split(",")
    dim2 = point2.split(",")
    for i in range(1, len(dim1)):

        temp = (float(dim1[i]) - float(dim2[i]))
        temp *= temp
        sum_result += temp

    return math.sqrt(sum_result)


def prepare_array(array, n):

    global track

    for i in range(len(array)):
        if len(array[i]) == 0:
            array.pop(i)

    new_array = []
    times = math.ceil(len(array) / n)

    for i in range(times):
        # index = random.randint(0, len(array) - 1)
        index = track + i
        new_array.append(array[index])
        array.pop(index)
    track += 1

    return new_array


def n_fold_cross_val(array, n_fold, nn):
    new_array = prepare_array(array, n_fold)
    correct, incorrect = 0, 0

    for new_point in new_array:
        shortest_n = []
        for data_point in array:
            distance = calc_distance(new_point, data_point)
            """if distance >= 1:
                print("dp: " + data_point)"""
            element = {
                "d": distance,
                "point": data_point
            }
            insert_in_array(shortest_n, element, nn)
        # print(new_point)
        actual_class = (new_point.split(","))[0]
        print(new_point)
        print(shortest_n)
        print("")

        predicted_class = take_poll(new_point, shortest_n)

        if actual_class == predicted_class:
            correct += 1
        else:
            incorrect += 1

    return correct / (correct + incorrect)


def calc_weight(element, item_in_array, count_element):
    # count_element["count"] += 1
    count_element["count"] += (1/calc_distance(element, item_in_array))


def take_poll(element, array):
    count = []
    for item in array:
        temp = item["point"].split(",")
        flag = False
        for i in range(len(count)):
            if count[i]["class"] == temp[0]:
                # count[i]["count"] += 1
                calc_weight(element, item["point"], count[i])
                flag = True
        if not flag:
            new_item = {
                "class": temp[0],
                "count": 1
            }
            count.append(new_item)
            flag = True

    cl = ""
    cnt = 0
    for item in count:
        if cnt < item["count"]:
            cl = item["class"]
            cnt = item["count"]

    return cl


def insert_in_array(array, element, nn):
    if len(array) < nn:
        array.append(element)
        return True

    for i in range(len(array)):
        item = array[i]
        if item["d"] > element["d"]:
            array.insert(i, element)
            array.pop(len(array)-1)
            return True
    return False


if __name__ == "__main__":
    file = open("data/iris.csv", "r")
    entire_file_string = file.read()
    file_in_array = entire_file_string.split("\n")

    if len(file_in_array[len(file_in_array)-1]) == 0:
        file_in_array.pop()

    print(len(file_in_array))
    # random.shuffle(file_in_array)

    for yo in range(n_fold):
        accuracy = n_fold_cross_val(file_in_array, n_fold, 5)
        print(accuracy * 100)

