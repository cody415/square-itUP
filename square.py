def separate_squares(begin, end):
    # Generate the list of squares
    squares = [i**2 for i in range(begin, end + 1)]
    
    # Separate the squares into odd and even
    odd_squares = [sq for sq in squares if sq % 2 != 0]
    even_squares = [sq for sq in squares if sq % 2 == 0]
    
    # Print the results
    print("Odd squares:", odd_squares)
    print("Even squares:", even_squares)


separate_squares(1, 10)
