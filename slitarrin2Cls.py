class Spl:
    # arrlen = 0
    def __init__(self, arr):
        self.arrlen = len(arr)
        self.arr = arr
        # print(self.arr)

    def splitPoint(self):
        # print(self.arrlen) 
        # print(self.arr)
        # lst = []
        left_sum = 0
        for i in range(0, self.arrlen):
            left_sum=left_sum+ self.arr[i]
        right_sum=0
        for i in range(self.arrlen-1, -1, -1):
            right_sum =right_sum+ self.arr[i]
            left_sum = left_sum-self.arr[i]
            if left_sum == right_sum:
                print(i)
                return i
        return -1
    
    def twoPart(self):
        val = self.splitPoint()
        if val == -1:
            print("not found")
        else:
            print(self.arr[:val], self.arr[val:])


if __name__ == "__main__":
    lst = [2,3,4,1]
    new_lst = Spl(lst)
    # Spl.splitPoint(new_lst) #both following lines do same thing
    # new_lst.splitPoint()
    new_lst.twoPart()
    