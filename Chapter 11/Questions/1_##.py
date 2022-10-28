class c2dVector():
    def __init__(self,i,j):
        self.i = i; self.j = j
    def __str__(self):
            return f"The 2D Vector is: ({self.i},{self.j})"

class c3dVector(c2dVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k
    def __str__(self):
        return f"The 3D Vector is: ({self.i},{self.j},{self.k})"

two = c2dVector(6,9)
print(two)

three = c3dVector(4,2,0)
print(three)

