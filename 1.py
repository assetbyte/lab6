import os
# 1
print("Directories:", [d for d in os.listdir(".") if os.path.isdir(os.path.join(".", d))])
print("Files:", [f for f in os.listdir(".") if os.path.isfile(os.path.join(".", f))])
print("All:", os.listdir("."))

# 2
print(f"Existence: {os.path.exists('testfile.txt')}")
print(f"Readability: {os.access('testfile.txt', os.R_OK)}")
print(f"Writability: {os.access('testfile.txt', os.W_OK)}")
print(f"Executability: {os.access('testfile.txt', os.X_OK)}")

# 3
p = "/Users/setbdirahman/JavaScript"

if os.path.exists(p): 
    print(f"Dir: {os.path.dirname(p)}\nName: {os.path.basename(p)}")
else: 
    print("NO")

# 4
f = open("testfile.txt", 'r') 
print(sum(1 for i in f))
f.close()

# 5
arr = ["Asset", "Asset", "Asset"]
f = open("testfile2.txt", "w")
f.write("\n".join(arr))
f.close()

# 6
for i in range(65, 91): 
    open(f"somefolder/{chr(i)}.txt", "x")

# 7
f1 = open('testfile2.txt', 'r')
f2 = open('testfile3.txt', 'w')
f2.write(f1.read())
f1.close()
f2.close()

# 8
f = "testfile4.txt"
if os.path.exists(f):
    if os.access(f, os.W_OK):
        os.remove(f)
    else: 
        print("No access")
else: 
    print("Doesn't exist")
