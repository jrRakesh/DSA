def TOH(n, src = "A", dst = "C", tmp = "B"):
    if(n == 1):
        print(f"Move disk {n} from {src} to {dst},")
    else:
        TOH(n-1, src, tmp, dst)
        print(f"Move disk {n} from {src} to {dst}")
        TOH(n-1, tmp, dst, src)

n = int(input("Enter no. of disks: "))
print(TOH(n))