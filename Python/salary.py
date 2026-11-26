# # employee salary calculation

# def da(basic):
#     da = basic * 0.8
#     return da
# def hra(basic):
#     hra = basic * 

# basic = float(input("Enter basic Salary: "))
# hra = basic * 0.20
# ta = basic * 0.10
# study_allow = basic * 0.05

# # gross = basic+hra+ta+study_allow
# gross = basic+hra(basic)+da(basic)
# print(f"Gross salary is :", gross)


# pf = basic *0.12
# itax = gross *0.10
# # net_salary = gross - (pf+itax)
# net = gross - pf(basic) - itax(basic)


# print(f"\n ----- Salary Slip -----")
# print(f"Basic Salary : {basic}")
# print(f"HRA (20%) : {hra}")
# print(f"Travel All : {ta}")
# print(f"Study All : {study_allow}")
# print(f"Gross Salary : {gross}")
# print(f"")



word = "Tomorrow"

result = ""
start_count = 1
for i in word:
    if i  == "o":
        print(start_count)
        print(result,"result")
        result += "*" * start_count
        start_count += 1
    else:
        result += i
print(result)
