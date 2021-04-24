'''Write a small command-line script called mailroom.py. This script should be executable.
The script should accomplish the following goals:

It should have a data structure that holds a list of your donors and a history of the amounts they have donated.
This structure should be populated at first with at least five donors, with between 1 and 3 donations each.
You can store that data structure in the global namespace.

The script should prompt the user (you) to choose from a menu of 3 actions:
“Send a Thank You”, “Create a Report” or “quit”.
'''
'''Global variables, I've seperated the data so that it feeds into one variable. Trying to predict that I will have to
pull directly from a spreadsheet soon thus eliminating the variables donor_list, donor_amount, and donor_freq

'''
donor_list = ('Tony Stark',
              'Steven Rogers',
              'Bruce Wayne',
              'Clark Kent ',
              'Geoffrey Donnell')
donor_amount = [6537854, 16396.10, 877.33, 708.42, 91250000]
donor_freq = [2, 3, 1, 3, 365]

# donor data, i used dd for short



'''
dd = (donor_list[0], donor_amount[0], donor_freq[0],
      donor_list[1], donor_amount[1], donor_freq[1],
      donor_list[2], donor_amount[2], donor_freq[2],
      donor_list[3], donor_amount[3], donor_freq[3],
      donor_list[4], donor_amount[4], donor_freq[4])
      
    '''

print(dd)

def menu():
    # This function will be the one that runs everytime and will point to other functions to compelete
    # the three taks. (1) send a thank you (2) generate a report (3) or quit.

    print('Welcome to the Automated Mail Room System (AMRS).\n'
          'Please select from the three options below \n'
          'by entering the value contained in the ()\n'
          '(1) Send a Thank You\n'
          '(2) Create a Report\n'
          '(3) Quit the program')
    choice = (input('What would you like to do? Enter value: '))

    while choice not in ['1', '2', '3']:
        choice = (input('Please enter a valid choice: 1, 2, or 3: '))

    if choice == '1':
        send_letter()
    if choice =='2':
        generate_report()
    if choice == '3':
        print("\n Thanks for using AMRS, Goodbye!")
    return

def send_letter():
    count = 0
    while True:
        choice = input("Please enter the full name of the donor (case sensitive) or type L for a list of donors: ")
        if choice == 'L':
            print(f'The list of donors are: {donor_list}')
            send_letter()
        if choice in donor_list:
            print('You have entered an existing donor')

        else:
            donor_name = choice
            donation_amount = input(f'You have entered a new donor named {donor_name}, enter an amount in th'
                                    f'the form 0.00: ')
            print(f'Thank for your donation {donor_name} of {donation_amount}')

            print()
            menu()
        break
        pass

def generate_report():
    #Formating and Printing for Header
    header = ['Donor Name','Total Given','Number Gifts','Average Gifts']
    header_format = '{:18}|{:16}|{:16}|{:20}|'
    print(header_format.format(*header))
    print('-'*int(len(header_format.format(*header)))) #dividing line for the report

    #Formating and Printing for Donor List
    donor_format = '{:18}|${:15.2f}|{:16}|${:19.2f}|'

    for step in range(0,5):
        print(donor_format.format(dd[step*3], dd[step*3+1], dd[step*3+2], (dd[step*3+1] / dd[step*3+2])))
    menu() #after report is generated we will go back to the menu
    pass


#send_letter()
#generate_report()
#menu()