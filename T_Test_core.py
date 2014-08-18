# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 15:04:59 2014

@author: Daniel Cleveland
T- Test automator machine
"""

#import matrices 
from numpy import zeros
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab




##ANY USER INPUT/HARDCODED VALUES ARE PURELY FOR TEST PURPOSES

a = 633, 616,659,535,666,675,524,746,585,748,696,609
b = 790 , 587 , 997 , 735 , 852 ,686, 839, 545, 724, 554, 889 , 797 , 722 ,483, 579

#grab imported matrix and rename to local variable 
New_size_A = len(a)
New_size_B = len(b)
new_a = zeros([New_size_A,0])
new_b = zeros([New_size_B,0])
new_a = a
new_b = b
t_values = 6.314,2.920,2.353,2.132,2.015,1.943,1.895,1.860,1.833,1.812,1.796,1.782,1.771,1.761,1.753,1.746,1.740,1.734,1.729,1.725,1.721,1.717,1.714,1.711,1.708,1.706,1.703,1.701,1.699,1.645
t_values_two_test = 12.706, 4.303, 3.182, 2.776, 2.571, 2.447,2.365,2.306,2.262,2.228,2.201,2.179,2.160,2.145,2.131,2.12,2.110,2.101,2.093,2.086,2.080,2.074,2.069,2.064,2.06,2.056,2.052,2.048,2.045,1.960
#Calculate Size, Mean, and Standard Deviation of each
def get_size(data_list): #returns decimal
    return len(data_list)
def get_mean(data_list, n): #returns decimal
    total_list = 0.0
    for i in data_list:
        total_list += i
    return total_list / n
def get_stdev(data_list,calc_mean,n):#returns decimal
    STD_a = 0.0
    for i in data_list:
        STD_a += (i - calc_mean)**2.0
    STD_a = ((1.000/n)*STD_a)**.500
    return STD_a
    
    
Size_a = New_size_A
Size_b = New_size_B
#calculate A total
total_a = 0
for i in new_a:
    total_a += i 
#Find mean
Mean_a = total_a / Size_a

#Calculate B Total
total_b = 0
for i in new_b:
    total_b += i 
#Find mean of b
Mean_b = total_b / Size_b

#calculate Standard Deviation of a
STD_a = 0
for i in new_a:
    STD_a += (i - Mean_a)**2
STD_a = ((1.000/Size_a)*STD_a)**.50000

#calculate Standard Deviation of a
STD_b = 0
for k in new_b:
    STD_b += (k - Mean_b)**2
STD_b = ((1.000/Size_b)*STD_b)**.50000

#Ask for Significance level
alpha = (raw_input("Enter Desired Significance level in Decimal Format: "))
if alpha >= 0.00 or alpha <= .99:
    c = True
    print c
else:
    alpha = float(raw_input("Incorrect: Enter in a decimal value between 0 and 1 please: "))

def ask_tail():#returns decimal
    return float(raw_input("Enter in Desired Tail test(1 = single left, 2 = single right, 3 = two tail): "))
def get_deg_of_free(stdev_a,size_a,stdev_b,size_b):#returns decimal
    top_eq = ((stdev_a**2.0 / size_a)+ (stdev_b **2.0 / size_b))**2.0
    bot_eq = ((stdev_a**2.0 / size_a)**2.0 / (size_a - 1.0)) + ((stdev_b**2.0 / size_b)**2.0/(size_b-1.0))
    return top_eq/bot_eq
def get_t_value_single_tail(deg_free):# returns decimal for plotting
    deg_free *= 100.00
    deg_free = round(deg_free,0)
    deg_free /= 100
    return t_values[deg_free -1]
def get_t_value_double_tail(deg_free):# returns decimal for plotting
    deg_free *= 100.00
    deg_free = round(deg_free,0)
    deg_free /= 100
    return t_values_two_test[deg_free - 1]
    
def calc_bound_left(t_value):#returns decimal for signifigance
    both = .05 * t_value
    return -t_value + both
def calc_bound_right(t_value): #returns decimal for signifance
    both = .05 * t_value
    return t_value - both
    
#Ask for Tails
#FIX ERROR CORRECTION
Tail_num = float(raw_input("Enter in Desired Tail test(1 = single left, 2 = single right, 3 = two tail): "))

#Calculate degrees of freedom(or critical values)
top_eq = ((STD_a**2 / Size_a)+(STD_b**2/Size_b))**2
bot_eq = ((STD_a**2 / Size_a)**2 / (Size_a - 1)) + ((STD_b**2 / Size_b)**2/(Size_b-1))
deg_of_free = top_eq/bot_eq

alpha = float(alpha)
deg_of_free *=100.0
rounded_deg_of_free = round(deg_of_free,0)
rounded_deg_of_free /= 100.0
#calc t value for T value
rounded_deg_of_free = int(rounded_deg_of_free)

if Tail_num == 3:
    calc_t = t_values_two_test[rounded_deg_of_free - 1]
else:
    calc_t = t_values[rounded_deg_of_free- 1]

new_deg_both = alpha * calc_t
deg_of_free_left = -calc_t + new_deg_both
deg_of_free_right = calc_t - new_deg_both
#else:
   # print "Error"
#
#Calculate test statistic(confidence)
t = 0
t_top = Mean_a - Mean_b
t_bottom = (STD_a**2/Size_a) + (STD_b**2/Size_b)
t = t_top / (t_bottom**.5)

def get_t(mean_a, stdev_a,size_a,mean_b,stdev_b,size_b): #returns decimal
    t_top = mean_a - mean_b
    t_bottom = (stdev_a**2.0 /size_a) + (stdev_a**2.0 / size_b)
    t = t_top / (t_bottom **.500)
    return t
def check_sig(tail_num, deg_left,deg_right): #returns str
    if tail_num == 3:
        if t <= deg_left or t >= deg_right:
            return "reject null hypothesis 3"
        else:
            return "do not reject null hypothesis 3"
    elif tail_num ==2:
        if  t >= deg_right:
            return"reject null hypothesis 2"
        else:
                return "do not reject null hypothesis 2"
    elif tail_num == 1:
        if t <= deg_left:
            return "reject null hypothesis 1"
        else:
            return "do not reject null hypothesis 1"
#See where t lies
if Tail_num == 3:
    if t <= deg_of_free_left or t >= deg_of_free_right:
        print"reject null hypothesis 3"
    else:
        print "do not reject null hypothesis 3"
elif Tail_num ==2:
    if  t >= deg_of_free_right:
        print"reject null hypothesis 2"
    else:
        print "do not reject null hypothesis 2"
elif Tail_num == 1:
    if t <= deg_of_free_left:
        print"reject null hypothesis 1"
    else:
        print "do not reject null hypothesis 1"

def gen_visual(t_value, tail_num, deg_left, deg_right):
    gen_base(t_value)    
    gen_fill(tail_num, deg_left,deg_right) 
   
def gen_base(t_value):   
    mean = 0
    var = 1
    sigma = np.sqrt(var)
    x = np.linspace(-t_value,t_value,100000)
    plt.plot(x,mlab.normpdf(x,mean,sigma))
def gen_fill(tail_num, deg_left, deg_right):
    if tail_num == 3:
        plt.fill_betweenx(mlab.normpdf(x,mean,sigma),deg_left,x, where = ( x <= deg_left))
        plt.fill_betweenx(mlab.normpdf(x,mean,sigma), x,deg_right, where = ( x >= deg_right))    
        plt.draw()
        plt.show()
    elif tail_num ==  2: #right
        plt.fill_betweenx(mlab.normpdf(x,mean,sigma), x,deg_right, where = ( x >= deg_right))    
        plt.draw()
        plt.show()
    elif tail_num == 1 :
        plt.fill_betweenx(mlab.normpdf(x,mean,sigma),deg_left,x, where = ( x <= deg_left))
        plt.draw()
        plt.show()

#Generate Visual
mean = 0
variance = 1
sigma = np.sqrt(variance)
x = np.linspace(-calc_t,calc_t,100000)
plt.plot(x,mlab.normpdf(x,mean,sigma))

#plot t



if Tail_num == 3:
    plt.fill_betweenx(mlab.normpdf(x,mean,sigma),deg_of_free_left,x, where = ( x <= deg_of_free_left))
    plt.fill_betweenx(mlab.normpdf(x,mean,sigma), x,deg_of_free_right, where = ( x >= deg_of_free_right))    
    plt.draw()
    plt.show()
elif Tail_num ==  2: #right
    plt.fill_betweenx(mlab.normpdf(x,mean,sigma), x,deg_of_free_right, where = ( x >= deg_of_free_right))    
    plt.draw()
    plt.show()
elif Tail_num == 1 :
    plt.fill_betweenx(mlab.normpdf(x,mean,sigma),deg_of_free_left,x, where = ( x <= deg_of_free_left))
    plt.draw()
    plt.show()
else:
    d=True

#mark where calculated T value is 