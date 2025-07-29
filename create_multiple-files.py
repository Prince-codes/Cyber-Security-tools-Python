# Program to create multiple files in series
import os
def create(n):
    for i in range (1,n+1):
        fname=f"program_{i}.c"
        with open(fname,"w") as f:
            f.write("// hello")
        
v=int(input("Enter no. of files : "))
create(v)