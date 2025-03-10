# Nelson Oseguera

# March 12, 2023

# Programming Project 4

# This program will allow a grocery store to keep track of the total number of bottles collected for recycling for seven days. The program will allow the user to input the number of bottles for each of the seven days. The program will calculate the total number of bottles returned for the week and the amount paid out (the total returned times 10 cents). The output of the program should include the total number of bottles returned and the total paid out.

# Variables Declared: totalBottles, todayBottles, counter, and totalPayout

totalBottles=0
todayBottles=0
counter=1

# Loop created for user to enter number of bottles for each of the seven days.

while counter <= 7:
    print('Enter the number of bottles for today: ')
    todayBottles = int(input())
    totalBottles = totalBottles + todayBottles
    counter = counter + 1

# Calculate the total payout time 10 cents

totalPayout = totalBottles * 0.10

# Print the outputs of the results

print('The total number of bottles collected was ', totalBottles)

print('The total paid out was $', totalPayout)
