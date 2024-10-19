# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.

def main():
    ######################
    total_rainfall = 0
    average_rainfall = 0
    rainfallindex = []
    monthNames = [
        'January', 'February', 'March',
        'April', 'May', 'June',
        'July', 'August', 'September',
        'October', 'November', 'December'
    ]

    # for row in monthNames:
    #
    #     for months in range(1, 13):
    for month in monthNames:
        #print(f'{months[0].capitalize()} Total: {total_sales}')
            RainfallPerMonth =int(input(f'Enter the total rainfall for {month}: '))
            #RainfallPerMonth = int(input('Enter the number of inches of rain this month: '))
            total_rainfall = total_rainfall + RainfallPerMonth
            rainfallindex.append(RainfallPerMonth)

            average_rainfall = total_rainfall / 12
            maxMonth = max(rainfallindex)
            maxMonthName = monthNames[rainfallindex.index(maxMonth)]
            minMonth = min(rainfallindex)
            minMonthName = monthNames[rainfallindex.index(minMonth)]


    print('Total rainfall:', total_rainfall)
    print('Average rainfall per month: ', average_rainfall)
    print("The max rainfall of", maxMonth, "occured in", maxMonthName)
    print("The min rainfall of", minMonth, "occured in", minMonthName)

if __name__ == '__main__':
    main()
