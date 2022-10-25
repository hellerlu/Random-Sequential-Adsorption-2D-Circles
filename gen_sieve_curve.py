import numpy as np

def pick_rand_curve(grad_curve_bounds):
    #Picks a random value with a beta distribution from the given bounds
    #It takes a input matrix of form [sieve diameter, lower bounds, upper bound]


    #Keep the diameter and initalize matrix
    grad_curve = grad_curve_bounds[:,[0,1]]

    #Use of beta distribution to pick a value between sieve bounds 
    grad_curve[:,1] = np.random.beta(2,2)*(grad_curve_bounds[:,2] - grad_curve_bounds[:,1]) + grad_curve_bounds[:,1]

    return grad_curve


def convert_sieve_curve(grad_curve):
    #It converts the sieve curve to a min and max radius with its according mass procentage

    grad_curve_conv = np.zeros([grad_curve.shape[0]-1,3])
    for i in range(grad_curve.shape[0]-1):
        #Convert to radius and calculate relative mass procentages 
        grad_curve_conv[i] = np.array([grad_curve[i,0]/2,grad_curve[i+1,0]/2,grad_curve[i,1]-grad_curve[i+1,1]])
        
    return grad_curve_conv