#Functions
def ip_input():
    inp = input("Input the ip adresses seperated by a space (ex. 1.1.1.1 1.1.1.2) \n")
    if inp == "":
        print("Input is empty, try again")
        ip_input()
    elif inp.islower() == True:
        print("Found letters")
        ip_input()

    calc_distance(inp)

def calc_distance(inp):
    ip = inp.split()
    try:
        ip1 = ip[0].split(".")
        ip2 = ip[1].split(".")
    except ValueError:
        print("Not a valid ip adress(es)")
    for i in range(4):
        if i == 0:
            dist1 = int(ip2[i]) - int(ip1[i])
        elif i == 1:
            dist2 = int(ip2[i]) - int(ip1[i])
        elif i == 2:
            dist3 = int(ip2[i]) - int(ip1[i])
        elif i == 3:
            dist4 = int(ip2[i]) - int(ip1[i])


    if dist1 != 0:
        dist1 = dist1 * 2**24
    if dist2 != 0:
        dist2 = dist2 * 2**16
    if dist3 != 0:
        dist3 = dist3 * 2**8
        
    finaldist = dist1 + dist2+ dist3+ dist4
    if finaldist < 0:
        print("The 2nd ip address was not greater then the 1st one")
    else:
        print("Distance between " + '.'.join(ip1) + " and " + '.'.join(ip2) + " => " + str(finaldist))
    
#----------

ip_input()





