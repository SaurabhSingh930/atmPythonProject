#JAI SHREE RAM
import time as t
f=0
while True:
    account_no = eval(input('Enter your account no.'))
    print()
    account_no1 = str(account_no)
    if account_no1 in['9305616339','9262558599','8381071642','8630020177','6387629012','9302858844','9779898610','6386572729']:
        if account_no1 == '9305616339':
            user_pin = 6339
            user_balance = 97432.69
            user_name = 'Mr. Saurabh Singh'
            print('Welcome to your bank acount',user_name,end="\n\n")
            f=1
            break
        elif account_no1 == '6387629012':
            user_pin = 9012
            user_balance = 94621.69
            user_name = 'Mr. Amit Prajapati'
            print('Welcome to your bank acount',user_name,end="\n\n")
            f=1
            break
        elif account_no1 == '9302858844':
            user_pin = 8844
            user_balance = 104621.69
            user_name = 'Mr. Sujal Gupta'
            print('Welcome to your bank acount',user_name,end="\n\n")
            f=1
            break
        elif account_no1 == '9779898610':
            user_pin = 8610
            user_balance = 804621.69
            user_name = 'Mr. Gurwinder Singh'
            print('Welcome to your bank acount',user_name,end="\n\n")
            f=1
            break
        elif account_no1 == '9262558599':
            user_pin = 8599
            user_balance = 84621.69
            user_name = 'Mr. Ashutosh Kumar Jha'
            print('Welcome to your bank acount',user_name,end="\n\n")
            f=1
            break
        elif account_no1 == '8381071642':
            user_pin = 1642
            user_balance = 84856.69
            user_name = 'Ms. Krithy Kumari'
            print('Welcome to your bank acount',user_name,end="\n\n")
            f=1
            break
        elif account_no1 == '8630020177':
            user_pin = 1177
            user_balance = 765611.69
            user_name = 'Ms. Roopali Sukhija'
            print('Welcome to your bank acount',user_name,end="\n\n")
            f=1
            break
        elif account_no1 == '6386572729':
            user_pin = 2729
            user_balance = 769911.69
            user_name = 'Ms. Anjali Rawat'
            print('Welcome to your bank acount',user_name,end="\n\n")
            f=1
            break
        else:
            print('This',account_no,'Account no. not found in system')
            print()
    
    else:
        print('This',account_no,'Account no. not found in system')
        print()


if f==1:
    while True:
        print('\t\t0. Logout and exit')
        print('\t\t1. View Account Balance')
        print('\t\t2. Withdraw Cash')
        print('\t\t3. Deposit Cash')
        print('\t\t4. Change PIN')

        choice=int(input('Enter number to proceed > '))
        print("\n\n")

        if choice in (1,2,3,4):
            num_of_tries = 3
            while (num_of_tries!=0):
                input_pin = int(input('Please enter your 4-digit PIN > '))
                
                if input_pin == user_pin:
                    print('Account auhtorized!\n\n')

                    if choice == 1:
                        print('Loading Account Balance...')
                        t.sleep(1.5)
                        print('Your current balance is Rs.',user_balance,end='\n\n\n')
                        if user_balance<5000:
                            print('Your balance is less than mininum amount')
                        break
                    elif choice == 2:
                        print('Opening Cash Withdrawal...')
                        t.sleep(1.5)

                        while (True):
                            withdraw_amt = float(input('Enter the amount you wish to withdraw > '))

                            if withdraw_amt>user_balance:
                                print("Can't withdraw Rs.',withdraw_amt")
                                print('Please enter a lower amount !')
                                Continue

                            else:
                                print('Withdrawing Rs.',withdraw_amt)
                                confirm = input('Confirm? Y/N > ')
                                if confirm in ('Y','y'):
                                    user_balance-=withdraw_amt
                                    print('Amount withdraw - Rs.',withdraw_amt)
                                    print('Remaining balance - Rs.',user_balance ,end='\n\n\n')
                                    break

                        break

                    elif choice == 3:
                        print('Loading Cash Deposit...')
                        t.sleep(1.5)

                        deposit_amt = float(input('Enter the amount you wish to deposit > '))
                        print('Depositing Rs.',deposit_amt)
                        confirm = input('Confirm? Y/N > ')
                        if confirm in ('Y','y'):
                            user_balance+=deposit_amt
                            print('Amount deposited - Rs.',deposit_amt)
                            print('Updated balance - Rs.',user_balance,end = '\n\n\n')
                        else:
                            print('Cancelling transaction...')
                            t.sleep(1)
                            print('Transaction Cancelled!\n\n')

                        break

                    else:
                        print('Loading PIN Change...')
                        t.sleep(1.5)
                        pin_new = int(input('Enter your new PIN'))

                        print('Changing PIN to ',pin_new)
                        confirm = input('Confirm? Y/N > ')
                        if confirm in ('Y','y'):
                            user_pin = pin_new
                            print('PIN changed succesfully !\n\n')
                        else:
                            print('Cancelling PIN change...')
                            t.sleep(1)
                            print('Process Cancelled!\n\n')

                        break

                else:
                    if input_pin != user_pin:
                        print('Invalid PIN\n')
                        num_of_tries-=1
                    else:
                        print('Exiting...')
                        t.sleep(2)
                        print('You have been logged out. Thank you!\n\n')
                        break
        
            else:
                print('Exiting...')
                t.sleep(2)
                print('You have been logged out. Thank you!\n\n')
                break
    
        elif choice==0:
            print("Exiting...")
            t.sleep(2)
            print("You have been logged out. Thank you!\n\n")
            break

        else:
            print('Invalid input!')
            print('\t\t0. Enter 0 to Logout and Exit!')
            break
        
       

            
