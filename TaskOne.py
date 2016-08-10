{"nbformat_minor": 0, "cells": [{"execution_count": 7, "cell_type": "code", "source": "## I am \"Praneet Jain\". ##\n\n\n\n\"\"\" 1) \n    def fizzbuzz(n):\n    If n is divisible by 3, return \"Fizz\"\n    If n is divisible by 5, return \"Buzz\"\n    If n is divisible by 3 and 5, return \"FizzBuzz\"\n    Else, do nothing.\"\"\"\n\ndef fizzbuzz(n):\n    \n    if n%3==0 and n%5==0:\n        return \"FizzBuzz\"\n    elif n%3==0:\n        return \"Fizz\"\n    elif n%5==0:\n        return \"Buzz\"\n    else:\n        return None", "outputs": [], "metadata": {"collapsed": true, "trusted": true}}, {"execution_count": 8, "cell_type": "code", "source": "fizzbuzz(1)", "outputs": [], "metadata": {"collapsed": false, "trusted": true}}, {"execution_count": 9, "cell_type": "code", "source": "fizzbuzz(15)", "outputs": [{"execution_count": 9, "output_type": "execute_result", "data": {"text/plain": "'FizzBuzz'"}, "metadata": {}}], "metadata": {"collapsed": false, "trusted": true}}, {"execution_count": 10, "cell_type": "code", "source": "\"\"\" 2) \n    def snapcrackle(n):\n    If n is an int, print \"Snap\"\n    If n is a float, print \"Crackle\"\n    Else, do nothing.\n\n    Write your own test cases for this function;\n    make sure to test for each of the three possibilities.\n    \"\"\"\n\n\ndef snapcrackle(n):\n    if type(n)==int:\n        print \"Snap\"\n    elif type(n)==float:\n        print \"Crackle\"\n    else:\n        return None", "outputs": [], "metadata": {"collapsed": true, "trusted": true}}, {"execution_count": 11, "cell_type": "code", "source": "snapcrackle(1)", "outputs": [{"output_type": "stream", "name": "stdout", "text": "Snap\n"}], "metadata": {"collapsed": false, "trusted": true}}, {"execution_count": 12, "cell_type": "code", "source": "snapcrackle(1.5)", "outputs": [{"output_type": "stream", "name": "stdout", "text": "Crackle\n"}], "metadata": {"collapsed": false, "trusted": true}}, {"execution_count": 13, "cell_type": "code", "source": "snapcrackle('a')", "outputs": [], "metadata": {"collapsed": false, "trusted": true}}, {"execution_count": 14, "cell_type": "code", "source": "\"\"\" 3)\n    def is_prime(n):\n    Return True if n is prime and False otherwise.\n    Use this function to help write 'nth_prime' below. \"\"\" \n\n\ndef  is_prime(n):\n    if n<2:\n        return False\n    i=1\n    counter=0\n    while i<=n:\n        if n%i==0:\n            counter=counter+1\n        i=i+1\n    if counter>2:\n        return False\n    else:\n        return True", "outputs": [], "metadata": {"collapsed": true, "trusted": true}}, {"execution_count": 15, "cell_type": "code", "source": "is_prime(3)", "outputs": [{"execution_count": 15, "output_type": "execute_result", "data": {"text/plain": "True"}, "metadata": {}}], "metadata": {"collapsed": false, "trusted": true}}, {"execution_count": 16, "cell_type": "code", "source": "is_prime(9)", "outputs": [{"execution_count": 16, "output_type": "execute_result", "data": {"text/plain": "False"}, "metadata": {}}], "metadata": {"collapsed": false, "trusted": true}}, {"execution_count": 17, "cell_type": "code", "source": "\"\"\" 4)\n    def nth_prime(n):\n    Return the nth prime number.\"\"\" \n\n\ndef nth_prime(m):\n    prime_count=0\n    j=2\n    while prime_count<=m:\n        result_is_prime = is_prime(j)\n        if result_is_prime==True:\n            prime_count=prime_count+1\n        if prime_count==m:\n            return j\n        j=j+1", "outputs": [], "metadata": {"collapsed": true, "trusted": true}}, {"execution_count": 18, "cell_type": "code", "source": "nth_prime(4)", "outputs": [{"execution_count": 18, "output_type": "execute_result", "data": {"text/plain": "7"}, "metadata": {}}], "metadata": {"collapsed": false, "trusted": true}}, {"execution_count": 26, "cell_type": "code", "source": "\"\"\" 5)\n    def gcd_iter(n, m):\n    An iterative function that calculates the GCD of n and m.\n    Note that there is a function from the fractions module,\n    fractions.gcd(a, b), that computes this -- do not use this\n    function, but replicate its behavior exactly (including for\n    negative or 0 inputs). See its documentation here:\n    https://docs.python.org/2/library/fractions.html \"\"\"\n\n\ndef gcd_iter(a, b):  \n    if b==0:  \n        return a  \n    return gcd_iter(b, a%b)", "outputs": [], "metadata": {"collapsed": true, "trusted": true}}, {"execution_count": 27, "cell_type": "code", "source": "gcd_iter(15,18)", "outputs": [{"execution_count": 27, "output_type": "execute_result", "data": {"text/plain": "3"}, "metadata": {}}], "metadata": {"collapsed": false, "trusted": true}}, {"execution_count": 28, "cell_type": "code", "source": "gcd_iter(0,0)", "outputs": [{"execution_count": 28, "output_type": "execute_result", "data": {"text/plain": "0"}, "metadata": {}}], "metadata": {"collapsed": false, "trusted": true}}, {"execution_count": 29, "cell_type": "code", "source": "gcd_iter(-15,-18)", "outputs": [{"execution_count": 29, "output_type": "execute_result", "data": {"text/plain": "-3"}, "metadata": {}}], "metadata": {"scrolled": true, "collapsed": false, "trusted": true}}, {"execution_count": 32, "cell_type": "code", "source": "\"\"\" 6)\n    def gcd_rec(n, m):\n    A recursive function that calculates the GCD of n and m.\"\"\"\n\ndef gcd_rec(a, b):\n    x = 0\n    while b!=0:\n        x = b\n        b = a%b\n        a = x\n    return a   ", "outputs": [], "metadata": {"collapsed": false, "trusted": true}}, {"execution_count": 33, "cell_type": "code", "source": "gcd_rec(15,18)", "outputs": [{"execution_count": 33, "output_type": "execute_result", "data": {"text/plain": "3"}, "metadata": {}}], "metadata": {"collapsed": false, "trusted": true}}, {"execution_count": 34, "cell_type": "code", "source": "gcd_rec(0,0)", "outputs": [{"execution_count": 34, "output_type": "execute_result", "data": {"text/plain": "0"}, "metadata": {}}], "metadata": {"collapsed": false, "trusted": true}}, {"execution_count": 35, "cell_type": "code", "source": "gcd_rec(-15,-18)", "outputs": [{"execution_count": 35, "output_type": "execute_result", "data": {"text/plain": "-3"}, "metadata": {}}], "metadata": {"collapsed": false, "trusted": true}}, {"execution_count": 37, "cell_type": "code", "source": "\"\"\" 7)\n    def fib_iter(n):\n    An iterative function that calculates the nth Fibonacci number.\n    By convention we will say that the 1st Fibonacci number is 0\n    and the 2nd Fibonacci number is 1.\"\"\"\n\ndef fib_iter(n):\n    if n <= 1:\n        return 0\n    elif n == 2:\n        return 1\n    else:\n        return fib_iter(n - 1) + fib_iter(n - 2)", "outputs": [], "metadata": {"collapsed": true, "trusted": true}}, {"execution_count": 38, "cell_type": "code", "source": "fib_iter(7)", "outputs": [{"execution_count": 38, "output_type": "execute_result", "data": {"text/plain": "8"}, "metadata": {}}], "metadata": {"collapsed": false, "trusted": true}}, {"execution_count": 40, "cell_type": "code", "source": "\"\"\" 8)\n    def fib_rec(n):\n    A recursive function that calculates the nth Fibonacci number.\"\"\"\n\ndef fib_rec(n):\n    if n <= 1:\n        return 0\n    elif n == 2:\n        return 1\n    else:\n        a = 0\n        b = 1\n        for i in range(n-2):\n            b = a + b\n            a = b - a\n        return b ", "outputs": [], "metadata": {"collapsed": false, "trusted": true}}, {"execution_count": 41, "cell_type": "code", "source": "fib_rec(8)", "outputs": [{"execution_count": 41, "output_type": "execute_result", "data": {"text/plain": "13"}, "metadata": {}}], "metadata": {"collapsed": false, "trusted": true}}, {"execution_count": 42, "cell_type": "code", "source": "fib_rec(7)", "outputs": [{"execution_count": 42, "output_type": "execute_result", "data": {"text/plain": "8"}, "metadata": {}}], "metadata": {"collapsed": false, "trusted": true}}, {"execution_count": 43, "cell_type": "code", "source": "\"\"\" 9)\n    def string_distance(s1, s2):\n    Counts the number of positions at which two strings have different\n    characters. If the strings are of unequal length, you should count\n    the missing characters as disagreements.\"\"\"\n\ndef string_distance(s1,s2):\n    count = 0\n    if len(s1) == len(s2):\n        for i in range(0,len(s1)):\n            if s1[i] != s2[i]:\n                count=count+1\n    elif len(s1) > len(s2):\n    \tfor i in range(0,len(s2)):\n    \t\tif s1[i] != s2[i]:\n    \t\t\tcount=count+1\n    \tcount = count + (len(s1)-len(s2))\n    else:\n    \tfor i in range(0,len(s1)):\n    \t\tif s1[i] != s2[i]:\n    \t\t\tcount=count+1\n    \tcount = count + (len(s2)-len(s1))            \n    return count", "outputs": [], "metadata": {"collapsed": true, "trusted": true}}, {"execution_count": 44, "cell_type": "code", "source": "string_distance(\"abc\", \"bca\")", "outputs": [{"execution_count": 44, "output_type": "execute_result", "data": {"text/plain": "3"}, "metadata": {}}], "metadata": {"collapsed": false, "trusted": true}}, {"execution_count": 46, "cell_type": "code", "source": "string_distance(\"py\", \"Python\")", "outputs": [{"execution_count": 46, "output_type": "execute_result", "data": {"text/plain": "5"}, "metadata": {}}], "metadata": {"collapsed": false, "trusted": true}}, {"execution_count": 50, "cell_type": "code", "source": "\"\"\" 10) \n    def convert_date(s):\n    Converts a date string of the form \"mm/dd/yyyy\" to a string of the\n    form \"Month date, year.\" You should be able to handle (any number of)\n    leading zeros, but can assume the input will correspond to a valid date.\n    The month_name attribute of the calendar module may be useful:\"\"\"\n\nimport calendar\ndef convert_date(s):\n    date_str=s.split(\"/\")\n    month_int=date_str[0].lstrip('0')\n    date_int=date_str[1].lstrip('0')\n    year_int=date_str[2].lstrip('0')\n    month_text=calendar.month_name[int(month_int)]\n    print month_text,date_int+',',year_int", "outputs": [], "metadata": {"collapsed": false, "trusted": true}}, {"execution_count": 51, "cell_type": "code", "source": "convert_date('5/1/1998')", "outputs": [{"output_type": "stream", "name": "stdout", "text": "May 1, 1998\n"}], "metadata": {"collapsed": false, "trusted": true}}, {"execution_count": 52, "cell_type": "code", "source": "convert_date('01/001/2000')", "outputs": [{"output_type": "stream", "name": "stdout", "text": "January 1, 2000\n"}], "metadata": {"collapsed": false, "trusted": true}}, {"execution_count": 53, "cell_type": "code", "source": "\"\"\" 11)\n    def my_sort(l):\n    Sorts a list. Do not use Python's built in sorted method. You may\n    use any sorting algorithm of your choice; running time does not matter.\"\"\" \n\n# Following method has been writtern after referencing below url:\n# http://danishmujeeb.com/blog/2014/01/basic-sorting-algorithms-implemented-in-python\ndef my_sort(l):\n    for i in range(len(l)):\n        for j in range(len(l)-1-i):\n            if l[j]>l[j+1]:\n               l[j],l[j+1]=l[j+1],l[j]\n    return l", "outputs": [], "metadata": {"collapsed": true, "trusted": true}}, {"execution_count": 54, "cell_type": "code", "source": "my_sort([5,2,1,4,3])", "outputs": [{"execution_count": 54, "output_type": "execute_result", "data": {"text/plain": "[1, 2, 3, 4, 5]"}, "metadata": {}}], "metadata": {"collapsed": false, "trusted": true}}, {"execution_count": 55, "cell_type": "code", "source": "my_sort(['c','a','b'])", "outputs": [{"execution_count": 55, "output_type": "execute_result", "data": {"text/plain": "['a', 'b', 'c']"}, "metadata": {}}], "metadata": {"collapsed": false, "trusted": true}}, {"execution_count": 56, "cell_type": "code", "source": "my_sort([-5,-10,0,3,5])", "outputs": [{"execution_count": 56, "output_type": "execute_result", "data": {"text/plain": "[-10, -5, 0, 3, 5]"}, "metadata": {}}], "metadata": {"collapsed": false, "trusted": true}}, {"execution_count": 57, "cell_type": "code", "source": "\"\"\" 12)\n    def frequency_dict(s):\n    First create a dictionary where each key is a character that appears\n    in the input string, and the value is a list of the indices at which that\n    character appears. Then format this dictionary as seen in the examples,\n    and return the resulting string.\n\n    Treat lower and upper case characters the same, and just include the\n    lowercase version in your dictionary. Pairs should be listed in\n    alphabetical order by key (use your my_sort function for this).\"\"\" \n\n#Code in line 4 of this function is referred from below mentioned URL:\n#http://stackoverflow.com/questions/13009675/find-all-the-occurrences-of-a-character-in-a-string\ndef frequency_dict(s):\n    s=s.lower()\n    dict = {}\n    for char in s:\n        dict[char]=[i for i, letter in enumerate(s) if letter == char]\n    index_string = 0\n    display_list=[]\n    for key in my_sort(dict.keys()):\n        display_list.append(\"%s = %s\" % (key, dict[key]))\n    return display_list", "outputs": [], "metadata": {"collapsed": true, "trusted": true}}, {"execution_count": 58, "cell_type": "code", "source": "frequency_dict(\"hello\")", "outputs": [{"execution_count": 58, "output_type": "execute_result", "data": {"text/plain": "['e = [1]', 'h = [0]', 'l = [2, 3]', 'o = [4]']"}, "metadata": {}}], "metadata": {"collapsed": false, "trusted": true}}, {"execution_count": 59, "cell_type": "code", "source": "frequency_dict(\"aA 00\")", "outputs": [{"execution_count": 59, "output_type": "execute_result", "data": {"text/plain": "['  = [2]', '0 = [3, 4]', 'a = [0, 1]']"}, "metadata": {}}], "metadata": {"collapsed": false, "trusted": true}}, {"execution_count": 61, "cell_type": "code", "source": "\"\"\" 13)\n    def my_permute(l):\n    Returns a list of all permutations of a list. Do not use any of\n    Python's builtin functions from the itertools library. Sort the list\n    using my_sort before returning it, and remove any duplicates as well.\"\"\" \n\n# Following code has been referenced from below mentioned URL:\n#http://www.dreamincode.net/forums/topic/239779-finding-all-permutations-of-items-in-a-list/\n#\n      \ndef my_permute(list):\n    if len(list) < 2: return list\n    if len(list) == 2: return [[list[0], list[1]] , [list[1], list[0]]]\n    tempList = []\n    finalList = []\n    index = 0\n    for i in list: #each starting number\n        newList = list[:]\n        del newList[index]\n        nextList = newList\n        for j in range(len(my_permute(nextList))): #each combination of the following values\n            tempList.append(i)\n            for k in range(len(my_permute(nextList)[j])): #focuses on each list in f(nextList)\n                tempList.append(my_permute(nextList)[j][k]) #appends values one by one\n\n            finalList.append(tempList)\n            tempList= []\n        index += 1\n    return finalList", "outputs": [], "metadata": {"collapsed": false, "trusted": true}}, {"execution_count": 62, "cell_type": "code", "source": "my_permute(['a','b'])", "outputs": [{"execution_count": 62, "output_type": "execute_result", "data": {"text/plain": "[['a', 'b'], ['b', 'a']]"}, "metadata": {}}], "metadata": {"collapsed": false, "trusted": true}}, {"execution_count": 63, "cell_type": "code", "source": "my_permute([1,2,3])", "outputs": [{"execution_count": 63, "output_type": "execute_result", "data": {"text/plain": "[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]"}, "metadata": {}}], "metadata": {"collapsed": false, "trusted": true}}, {"execution_count": 64, "cell_type": "code", "source": "my_permute([-1,2,-3])", "outputs": [{"execution_count": 64, "output_type": "execute_result", "data": {"text/plain": "[[-1, 2, -3], [-1, -3, 2], [2, -1, -3], [2, -3, -1], [-3, -1, 2], [-3, 2, -1]]"}, "metadata": {}}], "metadata": {"collapsed": false, "trusted": true}}], "nbformat": 4, "metadata": {"kernelspec": {"display_name": "Python 2", "name": "python2", "language": "python"}, "language_info": {"mimetype": "text/x-python", "nbconvert_exporter": "python", "version": "2.7.9", "name": "python", "file_extension": ".py", "pygments_lexer": "ipython2", "codemirror_mode": {"version": 2, "name": "ipython"}}}}