print("Fahrenheit\tCelsius")
print("---------------------")
for fahr in range(300,-1,-20):
    celsius=(fahr-32)*5/9
    print(f"{fahr}\t{celsius}") 