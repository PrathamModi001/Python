for i in range(2,21):
    with open(f"{i}.txt" ,"w") as f:
        for j in range(1,11):
            f.write(f"{j} X {i} = {j*i}\n")