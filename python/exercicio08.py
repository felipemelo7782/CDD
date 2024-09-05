print("----------------------------------")
time1 = input("Qual o nome do time 1 ? \n")
gols1 = int(input("Quantos gols Marcou? \n"))
print("----------------------------------")
time2 = input("Qual o nome do time 2 ?\n")
gols2 = int(input("Quantos ele gols Marcou? \n"))

vencendor = ""

if (gols1>gols2) :
    print("----------------------------------")
    print(f"O time vencendor foi : {time1}")
    print("----------------------------------")
    print(f"----{time1}:{gols1} VS {gols2}:{time2}-------")
elif (gols1<gols2 ) :
    print("----------------------------------")
    print(f"O time vencendor foi : {time2}")
    print("----------------------------------")
    print(f"----{time1}:{gols1} VS {gols2}:{time2}-------")
else:
    print("----------------------------------")
    print(f"EMPATE DE {gols1} GOLS")
    print("----------------------------------")

