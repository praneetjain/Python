# Created by: Praneet Jain

# coding: utf-8

# In[13]:

# importing all the predefined modules
import csv
import os
import time
import matplotlib.pyplot as plt
import random


'''
Following method reads the filename for iran and usa as well as the group of columns for
the purpose of retrieving count of votes for all candidates from all provinces.
Once data is fetched its converted into int data format from string data format.Special character
is removed and None value is filtered.
'''
def extract_election_vote_counts(filename, column_names):
    output = []
    for row in csv.DictReader(open(filename)):
        content = list(row[i] for i in column_names)
        output.extend(content)
        
    output = [w.replace(',','') for w in output]
    output = filter(None, output) # fastest
    output = [int(w) for w in output]

    return output

    
'''
ones_and_tens_digit_histogram(numbers), this method calculates the percentage of ones and tens in entire list.
It counts the number of values from 0 to 9 on ones and tens position. If the value is one digit, it calculates
one extra 0. Eg 3 as 03.
'''    
def ones_and_tens_digit_histogram(numbers):
    length=len(numbers)
    j=0
    flist=[]
    while (j<=9):
          i=0
          count=0
          while(i<length):
                element = numbers[i]
                if(len(str(element))==1 and j==0):
                  count += 1
                  if (element==0):
                     count +=1 
                else:
                  pos=0
                  while (pos<2):
                        if(len(str(element))==1):
                          digit=element%10
                          if(digit==j):
                            count += 1
                          break
                        digit = element % 10
                        if(digit==j):
                          count += 1
                        element /= 10
                        pos += 1
                i += 1
          fnum=(count*1.0)/(length*2)
          flist.append(fnum)
          j += 1       
    return flist
    

'''
plot_iranian_least_digits_histogram(histogram), method plots graph for Iran.
'''
def plot_iranian_least_digits_histogram(histogram):
    
    data =  [(0, histogram[0]), (1, histogram[1]),(2, histogram[2]), (3, histogram[3]),(4, histogram[4]), 
             (5, histogram[5]),(6,histogram[6]),(7,histogram[7]), (8,histogram[8]),(9,histogram[9])]

    x_val = [x[0] for x in data]
    y_val = [x[1] for x in data]
    ideal_line = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]

    plt.xlabel('Digit')
    plt.ylabel('Frequency')
    line_iran,=plt.plot(x_val,y_val,color='green',label='Iran')
    line_ideal,=plt.plot(ideal_line,color='blue',label='Ideal')
    plt.legend(handles=[line_ideal,line_iran])
    plt.savefig("iran-digits.png")
    #plt.show()
    plt.clf()
    return None

'''
plot_distribution_by_sample_size(), method plots graph using random numbers and ideal dimensions.
'''
def plot_distribution_by_sample_size():
    
    templist_10=[]

    templist_50=[]

    templist_100=[]

    templist_1000=[]

    templist_10000=[]
    
    result_list_10=[]

    result_list_50=[]

    result_list_100=[]

    result_list_1000=[]

    result_list_10000=[]


    i=0
    while(i<10):
        templist_10.append(random.randint(0,99))
        i += 1
    result_list_10=ones_and_tens_digit_histogram(templist_10)
    
    i=0
    while(i<50):
        templist_50.append(random.randint(0,99))
        i += 1
    result_list_50=ones_and_tens_digit_histogram(templist_50)

    
    i=0
    while(i<100):
        templist_100.append(random.randint(0,99))
        i += 1
    result_list_100=ones_and_tens_digit_histogram(templist_100)

        
    i=0
    while(i<1000):
        templist_1000.append(random.randint(0,99))
        i += 1
    result_list_1000=ones_and_tens_digit_histogram(templist_1000)

    i=0
    while(i<10000):
        templist_10000.append(random.randint(0,99))
        i += 1
    result_list_10000=ones_and_tens_digit_histogram(templist_10000)
 
    data1 =  [(0, result_list_10[0]), (1, result_list_10[1]),(2, result_list_10[2]), (3, result_list_10[3]),(4, result_list_10[4]), 
             (5, result_list_10[5]),(6,result_list_10[6]),(7,result_list_10[7]), (8,result_list_10[8]),(9,result_list_10[9])]

    
    data2 =  [(0, result_list_50[0]), (1, result_list_50[1]),(2, result_list_50[2]), (3, result_list_50[3]),(4, result_list_50[4]), 
             (5, result_list_50[5]),(6,result_list_50[6]),(7,result_list_50[7]), (8,result_list_50[8]),(9,result_list_50[9])]

    data3 =  [(0, result_list_100[0]), (1, result_list_100[1]),(2, result_list_100[2]), (3, result_list_100[3]),(4, result_list_100[4]), 
             (5, result_list_100[5]),(6,result_list_100[6]),(7,result_list_100[7]), (8,result_list_100[8]),(9,result_list_100[9])]

    data4 =  [(0, result_list_1000[0]), (1, result_list_1000[1]),(2, result_list_1000[2]), (3, result_list_1000[3]),(4, result_list_1000[4]), 
             (5, result_list_1000[5]),(6,result_list_1000[6]),(7,result_list_1000[7]), (8,result_list_1000[8]),(9,result_list_1000[9])]

    data5 =  [(0, result_list_10000[0]), (1, result_list_10000[1]),(2, result_list_10000[2]), (3, result_list_10000[3]),(4, result_list_10000[4]), 
             (5, result_list_10000[5]),(6,result_list_10000[6]),(7,result_list_10000[7]), (8,result_list_10000[8]),(9,result_list_10000[9])]


    
    
    x_val1 = [x[0] for x in data1]
    y_val1 = [x[1] for x in data1]

    x_val2 = [x[0] for x in data2]
    y_val2 = [x[1] for x in data2]

    x_val3 = [x[0] for x in data3]
    y_val3 = [x[1] for x in data3]

    x_val4 = [x[0] for x in data4]
    y_val4 = [x[1] for x in data4]

    x_val5 = [x[0] for x in data5]
    y_val5 = [x[1] for x in data5]

    
    
    ideal_line = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]

    plt.xlabel('Digit')
    plt.ylabel('Frequency')
    plt.title('Distribution of last two digits')
    
    line_10,=plt.plot(x_val1,y_val1,color='green',label='10 random numbers')

    line_50,=plt.plot(x_val2,y_val2,color='red',label='50 random numbers')

    line_100,=plt.plot(x_val3,y_val3,color='cyan',label='100 random numbers')

    line_1000,=plt.plot(x_val4,y_val4,color='magenta',label='1000 random numbers')

    line_10000,=plt.plot(x_val5,y_val5,color='yellow',label='10000 random numbers')

    line_ideal,=plt.plot(ideal_line,color='blue',label='Ideal')
    plt.legend(handles=[line_ideal,line_10,line_50,line_100,line_1000,line_10000])
    plt.savefig("random-digits.png")
    #plt.show()
    plt.clf()
    
    return None

'''
Calculating mean_squared_error for the two lists, passed here. One list is the ideal one and second is the one
obtained from calculate_mse_with_uniform.
'''
def mean_squared_error(numbers1, numbers2):
    
    i=0
    length=len(numbers1)
    mean_squared_error_value=0
    sums=0
    while(i<length):
        sums = sums + (numbers1[i]-numbers2[i])**2
        i += 1
    mean_squared_error_value = (sums*1.0)/length
    
    return mean_squared_error_value

'''
calculate_mse_with_uniform(histogram),method calculates mse with respect to uniform list.

'''
def calculate_mse_with_uniform(histogram):
    
    ideal_line = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
    mse_value = mean_squared_error(histogram,ideal_line)
    return mse_value

'''
compare_iranian_mse_to_samples(iranian_mse, number_of_iranian_samples), method calculates mse for IRAN.
'''
def compare_iranian_mse_to_samples(iranian_mse, number_of_iranian_samples):
    
    list_10000 = create_list_10000(number_of_iranian_samples)
    final_list_returned_from_MSE_WITH_UNIFORM = get_MSE_with_uniform_list(list_10000)

    max_group=10000
        
    count_list_val_is_greater=0
    count_list_val_is_smaller=0
        
    check_val_i=0
    while(check_val_i < max_group):
        
              
        if(final_list_returned_from_MSE_WITH_UNIFORM[check_val_i]>iranian_mse):
            count_list_val_is_greater += 1
        else:
            count_list_val_is_smaller += 1

        check_val_i += 1
                
    p_value_iranian = count_list_val_is_greater*1.0/(count_list_val_is_greater+count_list_val_is_smaller)
     
    print "\n"
    print "2009 Iranian election MSE: " + str(iranian_mse)
    print "Quantity of MSEs larger than or equal to the 2009 Iranian election MSE: " + str(count_list_val_is_greater)
    print "Quantity of MSEs smaller than the 2009 Iranian election MSE: " + str(count_list_val_is_smaller)
    print "2009 Iranian election null hypothesis rejection level p: " + str(p_value_iranian)
    print "\n"
    return None
 
'''
This function creates a list of 10000 lists, where each list has 120 random numbers between 0 and 99, inclusive.
'''
def create_list_10000(number_of_samples):
    
    list_10000 = []
    
    groups=0
    max_group=10000
    while(groups<max_group):
        list_120 = []
        temp_num=0
        while (temp_num<number_of_samples):
                random_num = random.randint(0,99)
                list_120.append(random_num)
                temp_num += 1
        list_10000.append(list_120)
        groups += 1
    return list_10000
    
'''
This function creates a new list from values returned from function "ones_and_tens_digit_histogram", and then 
MSE is computed using function "calculate_mse_with_uniform". Thereafter final_list_MSE_WITH_UNIFORM has 10000 values
in it which is returned.
'''
def get_MSE_with_uniform_list(list_10000):
    
    max_group=10000
    index_i=0
    
    # list of 10000 values - after values were returned form MSE with uniform
    final_list_MSE_WITH_UNIFORM = []
        
    while(index_i<max_group):
        ten_val_list=ones_and_tens_digit_histogram(list_10000[index_i])
        temp_val = calculate_mse_with_uniform(ten_val_list)
        final_list_MSE_WITH_UNIFORM.append(temp_val)
        index_i += 1
    return final_list_MSE_WITH_UNIFORM
    
    
'''
compare_us_mse_to_samples(us_mse, number_of_us_samples), method calculates mse for US.
'''   
def compare_us_mse_to_samples(us_mse, number_of_us_samples):

    list_10000 = create_list_10000(number_of_us_samples)
    max_group=10000

    final_list_returned_from_MSE_WITH_UNIFORM = get_MSE_with_uniform_list(list_10000)
     
    count_list_val_is_greater=0
    count_list_val_is_smaller=0
        
    check_val_i=0
    while(check_val_i < max_group):
        
              
        if(final_list_returned_from_MSE_WITH_UNIFORM[check_val_i]>us_mse):
            count_list_val_is_greater += 1
        else:
            count_list_val_is_smaller += 1

        check_val_i += 1
        
        p_value_us = count_list_val_is_greater*1.0/(count_list_val_is_greater+count_list_val_is_smaller)


    print "2008 United States election MSE: " + str(us_mse)
    print "Quantity of MSEs larger than or equal to the 2008 United States election MSE: "  + str(count_list_val_is_greater)
    print "Quantity of MSEs smaller than the 2008 United States election MSE: " + str(count_list_val_is_smaller)
    print "2008 United States election null hypothesis rejection level p: " + str(p_value_us)
 
'''
computeForCountry(country, list_votes_of_country), method is used for both IRAN and USA mse_value calculation.
Value is then returned to main() method. Also, plot is required only for IRAN and not for US, so we have checked the
country using "if" condition.
'''
def compute_list_votes(list_votes,country):
    flist = ones_and_tens_digit_histogram(list_votes)
    if country == "IRAN":
        plot_iranian_least_digits_histogram(flist)
        plot_distribution_by_sample_size()
    mse_value = calculate_mse_with_uniform(flist)
    return mse_value
    
def main():
    #Program execution starts from main() method.
    
    # extract and get list of votes for Iran 2009
    list_votes_iran = extract_election_vote_counts("election-iran-2009.csv", ["Ahmadinejad", "Rezai", "Karrubi", "Mousavi"]) 
    mse_value_iran = compute_list_votes(list_votes_iran,"IRAN")
    compare_iranian_mse_to_samples(mse_value_iran,len(list_votes_iran))

    # extract and get list of votes for US 2008
    list_votes_us = extract_election_vote_counts("election-us-2008.csv", ["Obama", "McCain", "Nader", "Barr", "Baldwin", "McKinney"])  
    mse_value_us = compute_list_votes(list_votes_us,"US")
    compare_us_mse_to_samples(mse_value_us,len(list_votes_us))    
    
if __name__ == "__main__":
    main()
 

