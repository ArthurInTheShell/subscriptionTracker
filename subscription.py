import csv

def data_read():
    with open('subscription.csv', 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            print(', '.join(row))


def data_entered(sub_name, total, duration):
    with open('subscription.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([sub_name, total, duration])
        
def prompt_for_input():
    sub_name = input('What is the subscription name:\n')
    total = input('How much money you spend on it:\n')
    duration = input('How long in terms of months does this subscription last:\n')
    data_entered(sub_name, total, duration)

def main():
    selection = int(input('Enter 1 to start entering subscription\n2 to read from data\n3 to exit:\n'))
    while selection < 3:
        if selection == 1:
            prompt_for_input()
        elif selection == 2:
            data_read()
        selection = int(input('Enter 1 to start entering subscription\n2 to read from data\n3 to exit:\n'))
    
    

if __name__ == '__main__':
    main()
