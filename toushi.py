#!/usr/local/bin/python3
initial =  float(input("初期投資額: ").strip())
monthly =  float(input("積立額/月: ").strip())
bonus =    float(input("ボーナス額/回: ").strip())
years =    float(input("運用年数: ").strip())
interest = float(input("想定利回り/年: ").strip())

sumOfInvest = initial
total = initial

interestOfMonth = interest/12/100

for m in range(int(12*years)):
    total *= (1 + interestOfMonth)
    total += monthly
    sumOfInvest += monthly
    if m%6 == 0:
        total += bonus
        sumOfInvest += bonus

print("試算結果: " + "{:,}".format(int(total)))
print("投資総額: " + "{:,}".format(int(sumOfInvest)))
