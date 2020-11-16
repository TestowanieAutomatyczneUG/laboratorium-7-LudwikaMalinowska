class Hamming:

    def distance(self, a, b):

        if a == "" and b == "":
            return 0

        if len(a) == 0 or len(b) == 0:
            raise ValueError("ValueError")

        if len(a) != len(b):
            raise ValueError("ValueError")

        if a == b:
            return 0
        else:
            count = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    count += 1
            return count