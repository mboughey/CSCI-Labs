# Matt Boughey
# CSCI102 Section B
# Assessment 11
# References: None
# Time: 30 Minutes


import math

def print_output(string):
    print(f"OUTPUT {string}")

def cylinder_vol(x,y):
    vol= (3.1415 * (x**2)) * y
    volume = round(vol, 2)
    print(f"OUTPUT {volume}")
    
def lbs_to_kg(x):
    kg = x * 0.45360
    print("OUTPUT {:.4f}".format(kg))

def polar_coords(x,y):
    r = str(math.sqrt((x**2)+(y**2)))
    r.ljust(4, '0')
    theta = math.degrees(math.atan(y/x))
    theta = round(theta, 2)
    print(f"OUTPUT r: {r}")
    print(f"OUTPUT theta: {theta}")
    


def pesos_to_dollars(x):
    dollars = x * 0.049
    dollars = round(dollars, 2)
    print(f"OUTPUT {dollars}")
    
def quad_form(x,y,z):
    inner = (math.sqrt(y**2 - (4*x*z)))
    x1 = int((-y + float((inner)))/2*x)
    x2 = int((-y - float((inner)))/2*x)
             
    if x1 > x2:
        print(f"OUTPUT {x2}")
        print(f"OUTPUT {x1}")
    else:
        print(f"OUTPUT {x1}")
        print(f"OUTPUT {x2}")        

