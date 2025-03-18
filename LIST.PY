my_list =[]
my_list.append((10,20,30,40))

my_list.insert(2,15)

my_list.extend([50,60,70])

my_list.remove(70)
def sort_list():
    my_list.sort()
my_list = [(10, 20, 30, 40), 15, 50 ,60]
for i, item in enumerate(my_list):
    if isinstance(item, tuple) and 30 in item:
        print(f"30 is inside the tuple at index {i}")
        print("final list", my_list)




