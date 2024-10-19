#Have the user input (using a loop) various
#information that contains three pieces of data:
        #year, name of state, and population.
#Store all of this information in a list
#of lists. For example it might be stored like this:'''


def main():
    all_entered_values = []

    while True:
        year = input("Enter the year or 'STOP' to stop: ")
        if year.upper() == 'STOP':
            break
        state = input("Enter state name: ")
        population = int(input("Enter the population: "))
        all_entered_values.append([int(year), state, population])

        # [ [2010, "Maine", 1987435], [2010, "Minnesota", 6873202], [2011, "Iowa",3421988]]
        # all entered values = []

        # Now have the user enter a year.
    year_to_sum = int(input("Enter a specific year you would like information for: "))

    sum_population_for_year(all_entered_values, year_to_sum)
    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the


def sum_population_for_year(all_entered_values, year_to_sum):
    totalPopulation = 0
    for entry in all_entered_values:
        year, state, population = entry
        if year == year_to_sum:
            totalPopulation += population
    print("Total population for the year is", totalPopulation)

    # Loop through and sum the populations for the appropriate year.


# e.g. for the list on line 7 the total would be 8,860,637 if the user enterd 2010 for the year to sum,
# or 3,421,988 if they enterd 2011 for the year to sum.

if __name__ == '__main__':
    main()
