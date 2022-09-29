def driving_cost(driven_miles, miles_per_gallon, dollars_per_gallon):
    driving_cost = dollars_per_gallon * (driven_miles / miles_per_gallon)
    return driving_cost

if __name__ == '__main__':
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())
    driven_miles = 20
    print('%0.2f' % driving_cost(driven_miles, miles_per_gallon, dollars_per_gallon), end= " ")
    driven_miles = 75
    print('%0.2f' % driving_cost(driven_miles, miles_per_gallon, dollars_per_gallon), end= " ")
    driven_miles = 500
    print('%0.2f' % driving_cost(driven_miles, miles_per_gallon, dollars_per_gallon))
