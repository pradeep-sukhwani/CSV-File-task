def count_orders():
    """Counting number of order received to the site and then
    subtracting by 1 as we don't want to count 1st line"""
    with open('customerdata.txt') as data:
        count = sum(1 for line in data)-1
        return "1. How many orders did the site receive? \n- %d Orders" %(count)

def total_amount():
    """Calculating total amount of reder received by the site"""
    total = 0

    with open('customerdata.txt', 'r') as data:
        for i in xrange(1):
            data.next() # skip first line

        for line in data:
            line = line.split()
            total += float(line[4])
        return "\n2. What was the total amount of the orders?\n- %d"% (total)

def cus_order_once():
    """Checking who has order only one time"""
    names = [] # Empty list that will be used to append the names of the customers
    
    with open('customerdata.txt', 'r') as data:
        for i in xrange(1):
            data.next() # skip first line

        for line in data:
            line = line.split()
            name = ' '.join(line[2:4]).strip(',')
            if name not in names:
                names.append(name)
        remove = ', '.join(names)
        
        return """
3. List the names of the customers who ordered once and did not order again.\n- %s""" % (remove)

def order_distribution():
    """Order distribution - checking who has order how many times"""
    number = {} # Empty Dictionary for keeping numbers
    once = [] # Empty list that will be used to append the no. of customers ordered once
    twice = [] # Empty list that will be used to append the no. of customers ordered twice
    thrice = [] # Empty list that will be used to append the no. of customers ordered thrice
    four = [] # Empty list that will be used to append the no. of customers ordered four times
    five_n_above = []  # Empty list that will be used to append the no. of customers
    # ordered five and above times
    with open('customerdata.txt', 'r') as data:
        for i in xrange(1):
            data.next()

        for line in data:
            line = line.split()
            name = ' '.join(line[1:2]).strip(',')
            if name not in number:
                number[name] = 1
            elif name in number:
                number[name] += 1
        for name in number:
            if number[name] == 1:
                once.append(name)
            elif number[name] == 2:
                twice.append(name)
            elif number[name] == 3:
                thrice.append(name)
            elif number[name] == 4:
                four.append(name)
            else:
                five_n_above.append(name)

        return """
4. Get a distribution of customers who ordered exactly once, exactly twice and
   so on up to 4 orders and group the rest as 5 orders and above.
-----------------------------------------------------            
            Orders  | Count of Customers
-----------------------------------------------------
                1   |   {0}
                2   |   {1}
                3   |   {2}
                4   |   {3}
                5+  |   {4}
""".format(len(once), len(twice), len(thrice), len(four), len(five_n_above))

def main():
    """This is main function which calls all the other functions"""
    print count_orders()
    print total_amount()
    print cus_order_once()
    print order_distribution()

main()


