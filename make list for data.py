"""Make a list"""
def main():
    """Input day"""
    lst = []
    print("How long? (Day)")
    days = int(input())
    for i in range(days):
        lst.append(int(input()))
    print(lst)
main()
