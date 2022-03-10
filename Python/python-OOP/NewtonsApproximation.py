import math

def NewtonsApproximation(n,guess) -> float:
    # root = 0.5 * (X + (N / X)) where X is the guess and N is the value
    tolerance = 0.000001 

    # we first calculate the power of the tolerance
    # i.e 0.001 = 1 *  1- ^ -3
    base10 = math.log10(abs(tolerance))

    # Then we convert to absolute values and round

    base10 = abs(math.floor(base10))
    answer = round(math.sqrt(n), base10)

    while True:     

        # We then calculate the quotent and average as per Newton's approximation    

        root = 0.5 * (guess + (n / guess))

        # Entirely for testing!
        # print("Average: " + str(root))
        # print("exponents: "+str(base10))
        # print("Rounded Average: " + str(round(root, base10)))
        # print("Rounded Answer: " + str(round(answer, base10)))

        # Lastly, we return the value if the rounded average is equal to the rounded answer

        if(round(guess,base10) == round(answer,base10)):
            break

        # else, we set the guess equal to the average further iterate

        else:
            guess = root
    return round(root,base10)
        
def main():
    print("Newton's Approximation: " + str(NewtonsApproximation(100,10.0)))

main()