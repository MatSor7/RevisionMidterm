# Conditional execution. If-statements.
try:
    gross = input("Give me a gross income: ")
    gross = int(gross)
    children = input("How many children do you have? ")
    children = int(children)
    if gross < 1000:
        net = gross - gross*(0.1 - children*0.01)
    elif 1000 <= gross < 2000:
        net = gross - gross*(0.12 - children*0.01)
    elif 2000 <= gross < 4000:
        net = gross - gross*(0.14 - children*0.005)
    elif gross >= 4000:
        net = gross - gross*(0.18 - children*0.05)
except ValueError:
    print("Give me proper number.")
else:
    print("Net income: ", net)
# Not very happy with my execution here. Preben?
