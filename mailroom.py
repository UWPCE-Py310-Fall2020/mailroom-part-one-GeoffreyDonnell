'''Write a small command-line script called mailroom.py. This script should be executable.
The script should accomplish the following goals:

It should have a data structure that holds a list of your donors and a history of the amounts they have donated.
This structure should be populated at first with at least five donors, with between 1 and 3 donations each.
You can store that data structure in the global namespace.

The script should prompt the user (you) to choose from a menu of 3 actions:
“Send a Thank You”, “Create a Report” or “quit”.
'''

donor_list = ['Tony Stark',
              'Steven Rogers',
              'Bruce Wayne',
              'Clark Kent',
              'Geoffrey Donnell']
donation_history = [[10000], [200, 300], [1000, 2000, 3000], [100], [23000]]

def menu():
    # This function will be the one that runs everytime and will point to other functions to compelete
    # the three tasks. (1) Generate a report (2) generate a report (3) or quit.

    print('Welcome to the Automated Mail Room System (AMRS).\n'
          'Please select from the three options below \n'
          'by entering the value contained in the ()\n'
          '(1) Generate a Report\n'
          '(2) Send a Thank You\n'
          '(3) Quit the program')
    choice = (input('What would you like to do? Enter value: '))

    while choice not in ['1', '2', '3']:
        choice = (input('Invalid value. Please enter a valid choice: 1, 2, or 3: '))

    if choice == '1':
        generate_report()
    if choice =='2':
        letter_options()
    if choice == '3':
        print("\n Thanks for using AMRS, Goodbye!")
        quit()
    return

def letter_options():
    count = 0
    while True:
        donor_name = input("Please enter the full name of the donor (case sensitive) or type L for a list of donors: ")
        if donor_name == 'L':
            print(f'The list of donors are: {donor_list}')
            letter_options()
        if donor_name in donor_list:
            print('You have entered an existing donor')
            new_donation = float(input('How much is the additional donation? Please enter a value: '))
            # Start of loop to determine where in the list the donor is and their corresponding amount and freq
            for index in range(0, int(len(donor_list))):
                if donor_list[index] == donor_name:
                    # Adding the additional donation to the data base
                    donation_history[index].append(new_donation)
            # Calls function to generate email
            draft_email(donor_name, new_donation)
        else:
            new_donation = input(f'You have entered a new donor named {donor_name}, '
                                    f'enter an amount in the form 0.00: ')
            donor_list.append((str(donor_name)))
            donation_history.append([float(new_donation)])
            draft_email(donor_name, new_donation)

def draft_email(donor_name, donor_amount):
    print(f'\nEmail to: {donor_name.replace(" ","")}@gmail.com')
    print('Subject:Donation Received')
    print(f'\nThank you {donor_name} for your generous donation of ${donor_amount}! \n'
          f'We greatly appreciate your support to our cause. \n'
          f'Best regards,\n'
          f'Staff Member\n \n')
    menu()
    pass

def generate_report():
    #Need to delcare empty lists to store values that will be calculated
    no_donors = int(len(donor_list))
    donation_freq = [0] * no_donors
    donation_total = [0] * no_donors
    donation_average = [0]*no_donors
    # Finds the average and number of donations
    for index in range(0, no_donors):
        donation_total[index] = sum(donation_history[index])
        donation_freq[index] = len(donation_history[index])
        donation_average[index] = donation_total[index]/donation_freq[index]

    #Formating and Printing for Header
    header = ['Donor Name','Total Given','Number Gifts','Average Gifts']
    header_format = '{:18}|{:16}|{:16}|{:20}|'
    print('\n')
    print(header_format.format(*header))
    print('-'*int(len(header_format.format(*header)))) #dividing line for the report

    #Formating and Printing for Donor List
    donor_format = '{:18}|${:15.2f}|{:16}|${:19.2f}|'

    for step in range(0,no_donors):
        print(donor_format.format(donor_list[step],
                                  donation_total[step],
                                  int(donation_freq[step]),
                                  float(donation_average[step])))
    print('\n') # print a line for spacing between the report and menu
    menu() # after report is generated we will go back to the menu
    pass

if __name__ == '__main__':
    menu()


