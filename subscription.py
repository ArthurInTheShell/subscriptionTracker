import csv

def data_read():
    with open('subscription.csv', 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        sum = 0
        with open('subscription.md','w',newline='') as mdout:
            mdout.write('| Subscription Name | Total Cost | Duration(Month) | Cost per Month |\n')
            mdout.write('| ----------- | ----------- | ----------- | ----------- |\n')
            for row in spamreader:
                print(', '.join(row))
                cpm = float(row[1])/float(row[2])
                mdout.write('| ' + ' | '.join(row) + ' | ' + '{:04.2f}'.format(cpm) +' |\n')
                sum += cpm
            print('Monthly subscription cost is '+ '{:04.2f}'.format(sum))
            mdout.write('**Monthly subscription cost is '+ '{:04.2f}'.format(sum)+'**')

def data_output():
    with open('subscription.csv', 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        sum = 0
        with open('subscription.md','w',newline='') as mdout:
            mdout.write('| Subscription Name | Total Cost | Duration(Month) | Cost per Month |\n')
            mdout.write('| ----------- | ----------- | ----------- | ----------- |\n')
            for row in spamreader:
                print(', '.join(row))
                cpm = float(row[1])/float(row[2])
                mdout.write('| ' + ' | '.join(row) + ' | ' + '{:04.2f}'.format(cpm) +' |\n')
                sum += cpm
            print('Monthly subscription cost is '+ '{:04.2f}'.format(sum))
            mdout.write('**Monthly subscription cost is '+ '{:04.2f}'.format(sum)+'**')

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
    selection = int(input('Enter\n1 - enter subscription\n'+
    '2 - read, update subscription\n3 - read, update subscription and exit\n4 - exit:\n'))
    while selection < 4:
        if selection == 1:
            prompt_for_input()
        elif selection == 2:
            data_read()
        elif selection == 3:
            data_output()
            break
        selection = int(input('Enter\n1 - enter subscription\n'+
        '2 - read, update subscription\n3 - read, update subscription and exit\n4 - exit:\n'))
    
    

if __name__ == '__main__':
    main()
