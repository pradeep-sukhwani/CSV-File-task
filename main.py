import sqlite3
import pandas

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
    once = [] # Empty list that will be used to append the no. of customers ordered once
    twice = [] # Empty list that will be used to append the no. of customers ordered twice
    thrice = [] # Empty list that will be used to append the no. of customers ordered thrice
    four = [] # Empty list that will be used to append the no. of customers ordered four times
    five_and_above = []  # Empty list that will be used to append the no. of customers
    # ordered five and above times
    connection = sqlite3.connect(':memory:') # To create a database in RAM
    connection.text_factory = str # To remove the unicode need to convert to string
    c = connection.cursor()
    create_table = """CREATE TABLE customer_data (date text,
                 Phone text, Named text, Amount Int)"""
    c.execute(create_table)
    
    with open('customerdata.txt') as data: # importing data from csv file to database
        df = pandas.read_csv(data)
        df.to_sql('customer_data', connection, if_exists='append', index=False)

    output = c.execute("""SELECT Named, Phone, count(Phone) From customer_data
         GROUP BY Named ORDER BY count(Phone) desc""")

    # Looping over the data to get the appropriate result such as customer ordered once
    # twice, thrice, four times and five and above times
    for item in output.fetchall():
        if item[2] == 1:
            once.append(item)
        elif item[2] == 2:
            twice.append(item)
        elif item[2] == 3:
            thrice.append(item)
        elif item[2] == 4:
            four.append(item)
        else:
            five_and_above.append(item)
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

    """.format(len(once), len(twice), len(thrice), len(four), len(five_and_above))

def main():
    """This is main function which calls all the other functions"""
    print count_orders()
    print total_amount()
    print cus_order_once()
    print order_distribution()

main()


