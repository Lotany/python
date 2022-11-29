#context managers

# f = open('sample.txt', 'w')
# f.write("My name is lotan,I am a software developer")
# f.close()

# with open('sample.txt','w') as f:
#     f.write('I am fully commited to working with python')

#Context manager using a class
# class Open_file():

#     def __init__(self,filename,mode):
#         self.filename =filename
#         self.mode =mode

#     def __enter__(self):
#         self.file =open(self.filename, self.mode)
#         return self.file

#     def __exit__(self, exc_type, exc_val,traceback):
#         self.file.close()

# with Open_file('sample.txt', 'w') as f:
#     f.write("Tesing")

# print(f.closed)


#context manager using a function and generator
from contextlib import contextmanager

@contextmanager
def open_file(file, mode):
    f =open(file, mode)
    yield f
    f.close()

with open_file('sample.txt','w') as f:
    f.write('I am a programer, a decent programer ')

print(f.closed)