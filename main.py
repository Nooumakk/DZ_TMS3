data = [5,6,7,4,3,1,55,44,22,66,77,44,335,664,354,465,3546,4646,3546,4666]


def func():
    n = 1
    while n < len(data):
        for i in range(len(data) - 1):
            if data[i] > data[i+1]:
                data [i], data[i+1] = data[i+1], data[i]
        n += 1
    print(data)


if __name__ == "__main__":
    func()
