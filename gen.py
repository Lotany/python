#generators
def square_numbers(nums):
    for i in nums:
        yield(i*i)

my_nums =square_numbers([1,2,3,4,5,6])

# for num in my_nums:
#     print(num)


def csv_reader(file_name):
    for row in open(file_name, 'r'):
        yield row