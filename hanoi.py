

def moveTower(height, A, B, C):
    if height >= 1:
        moveTower(height - 1, A, C, B)  # Move smaller disks
        print(f"Moving disk {height} from {A} to {B}")  # Move current disk
        moveTower(height - 1, C, B, A)  # Move the rest

# Solve Tower of Hanoi with 3 disks
moveTower(3, "A", "B", "C")



def moveTower(height,A,B,C):
    if height >= 1:
        moveTower(height-1,A,C,B)
        moveDisk(A,B)
        moveTower(height-1,C,B,A) 
        
def moveDisk(fp,tp): 
    print("moving disk from",fp,"to",tp) 
moveTower(3,"A","B","C")


def mov(h,a,b,c):
    if h >=1:
        mov(h-1,a,c,b)
        print(f"disk no {h} moved from {a} to {b}")
        mov(h-1,c,b,a)

mov(3,'A','B','C')
