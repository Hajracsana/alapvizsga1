tvf=""
with open('szamok.txt', 'w') as f:
    f.write("Private bool IsEven(int number){ \n if (number==1): return False;" '\n')
    for i in range(2,205,1):
        if i%2!=0:
            tvf="true"
        else:
            tvf="false"
        f.write(f"else if (number == {str(i)}): return {tvf};" '\n')
    f.write("}")
    f.close
