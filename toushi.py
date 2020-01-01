#!/usr/local/bin/python3
initial =  float(input("初期投資額: ").strip())
monthly =  float(input("積立額/月: ").strip())
years =    float(input("運用年数: ").strip())
interest = float(input("想定利回り/年: ").strip())

sumOfInvest = initial
total = initial

interestOfMonth = interest/12/100

for m in range(12*int(years)):
    sumOfInvest += monthly
    total *= (1 + interestOfMonth)
    total += monthly

print("試算結果: " + "{:,}".format(int(total)))
print("投資総額: " + "{:,}".format(int(sumOfInvest)))
