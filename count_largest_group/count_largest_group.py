def countLargestGroup(n):
        def calculate_size(n):
            str_of_n = str(n)
            total = 0
            for digit in str_of_n:
                total += int(digit)
            return total


        sizes = {}
        for i in range(1, n + 1):
            size = calculate_size(i)
            if size in sizes:
                sizes[size].append(i)
            else:
                sizes[size] = [i]

        groups = [y for x, y in sizes.items()]
        groups.sort()
        groups = list(filter(lambda x: len(x) == len(groups[0]), groups))

        return len(groups)


print(countLargestGroup(4) == 4)
print(countLargestGroup(13) == 4)
print(countLargestGroup(2) == 2)
print(countLargestGroup(1) == 1)

