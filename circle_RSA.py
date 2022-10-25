import random 
import math
import matplotlib.pyplot as plt
import time 
import numpy as np

def intersection (r1, cen1, r2, cen2, tol):
    #Returns True if circle 1 and 2 overlap
    #Tolerance means min gap between aggregates

    distan = math.sqrt((cen1[0]-cen2[0])**2+(cen1[1]-cen2[1])**2)
    min_Dis = r1+r2+tol

    if distan > min_Dis:
        return False
    else:
        return True   


def any_intersec (cir1, cirList, tol):
    #Returns True if any circle overlaps with circle 1
    #Tolerance means min gap between aggregates

    r1 = cir1[2]
    intersec = False
    for cir2 in cirList:
        r2 = cir2[2]
        check = intersection(r1,cir1[0:2],r2,cir2[0:2],tol)
        if check:
            #If intersection is found, break function
            intersec = True
            return intersec
    
    #If no intersection were found:
    return intersec


def random_gen (x1,x2):
    #Generates a random value between two bounds

    value = (x2-x1)*random.random()+x1
    return value


def plot(cirList,h,w):
    #Plots all circles within h x w box

    plt.figure()
    for cir in cirList:
        circle1 = plt.Circle((cir[0],cir[1]),cir[2], facecolor='tab:brown',edgecolor='k')
        plt.gcf().gca().add_artist(circle1)
    plt.xlim(0, w)
    plt.ylim(0, h)
    plt.gca().set_aspect('equal','box')
    plt.show()


def rsa_circle_minmax(r_min,r_max,req_void,h,w,tol,timeout):
    #Generates random circles with r between r_min & r_max
    #Places them randomly in h x w box until req_void is reached
    #Tolerance means min gap between aggregates
    #Algorithm times out after timeout [s]

    cirList = []
    cur_void = 1
    timeout_start = time.time()
    while req_void < cur_void and time.time() < timeout_start + timeout:
        r_cur = random_gen(r_min,r_max)
        x_cur = random_gen(r_cur,w-r_cur)
        z_cur = random_gen(r_cur,h-r_cur)
        new_Circle = [x_cur,z_cur,r_cur]

        if cirList == []:
            cirList.append(new_Circle)
        else:
            check = any_intersec(new_Circle,cirList,tol)
            if not check:
                cirList.append(new_Circle)
                cur_void = cur_void - math.pi*new_Circle[2]**2/(h*w)
    elapsed_time = round(time.time()-timeout_start,2)
    if elapsed_time >= timeout:
        print("------------------------------------------------")
        print("timed out after ",elapsed_time," seconds")
        print("Current void: ",round(cur_void,4))
        print("Increase timeout or req_void to find a solution")
        print("------------------------------------------------")
    else:
        print("------------------------------------------------")
        print("Found a solution in ",elapsed_time," seconds")
        print("Current void: ",round(cur_void,4))
        print("------------------------------------------------")
    return cirList, cur_void


def rsa_circle_graded(grad_curve, req_void,h,w,tol,timeout):
    #Generates random circles with r between r_min & r_max in selected sieve curve
    #Keeps generating them until it reaches mass procentage of selected sieve curve group
    #Places them randomly in h x w box
    #Tolerance means min gap between aggregates
    #Algorithm times out after timeout [s]

    cirList = []
    cur_void = 1
    req_void_cur = 1
    timeout_start = time.time()
    for i,ele in enumerate(grad_curve):
        req_void_cur -= grad_curve[i,2]*(1-req_void)
        while req_void_cur < cur_void and time.time() < timeout_start + timeout:
            
            r_cur = random_gen(grad_curve[i,1],grad_curve[i,0])
            x_cur = random_gen(r_cur,w-r_cur)
            z_cur = random_gen(r_cur,h-r_cur)
            new_Circle = [x_cur,z_cur,r_cur]

            if cirList == []:
                cirList.append(new_Circle)
            else:
                check = any_intersec(new_Circle,cirList,tol)
                if not check:
                    cirList.append(new_Circle)
                    cur_void = cur_void - math.pi*new_Circle[2]**2/(h*w)
    elapsed_time = round(time.time()-timeout_start,2)
    if elapsed_time >= timeout:
        print("------------------------------------------------")
        print("timed out after ",elapsed_time," seconds")
        print("Current void: ",round(cur_void,4))
        print("Increase timeout or req_void to find a solution")
        print("------------------------------------------------")
    else:
        print("------------------------------------------------")
        print("Found a solution in ",elapsed_time," seconds")
        print("Current void: ",round(cur_void,4))
        print("------------------------------------------------")
    return cirList, cur_void