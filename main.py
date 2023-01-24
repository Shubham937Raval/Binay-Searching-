print("Enter number of  values:")
a = []
n = int(input())
print("Enter numbers:")
for i in range(n):
    q = float(input())
    a.append(q)


def search(m):
    lower = 0
    upper = len(a)

    if m > a[len(a) - 1]:
        print()
    else:
        while lower <= upper:
            mid = (lower + upper)//2

            if a[mid] == m:
                globals()['pos'] = mid
                return True
            else:
                if a[mid] < m:
                    lower = mid + 1

                else:
                    upper = mid - 1
        return False


print("List is:", a)
a.sort()
print("Sorted list:", a)
print("\nWrite the search number:")
m = float(input())
if search(m):
    print("Found at: ", pos + 1)
else:
    print("Not Found")


