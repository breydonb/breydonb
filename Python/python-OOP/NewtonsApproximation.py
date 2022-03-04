import math

def NewtonsApproximation(x,guess):
    bool = True
    tolerance = 0.001
    avg = guess

    # we first calculate the power of the tolerance
    # i.e 0.001 = 1 *  1- ^ -3
    base10 = math.log10(abs(tolerance))

    # Then we convert to absolute values and round

    base10 = abs(math.floor(base10))
    answer = round(math.sqrt(x), base10)

    while bool:     

        # We then calculate the quotent and average as per Newton's approximation    

        quotient = float(x / avg)
        avg = (quotient + avg + guess) / x

        # we then round off the values calculated based on the base10 values

        
        avg = round(avg,(base10))

        # Entirely for testing!

        print("Average: " + str(avg))
        print("exponents: "+str(base10))
        print("Rounded Average: " + str(round(avg, base10)))
        print("Rounded Answer: " + str(answer))

        
        # Lastly, we return the value if the rounded average is equal to the rounded answer

        if(avg == answer):
            bool = False
            return avg

        # else, we set the guess equal to the average further iterate

        else:
            guess = avg
        print()
        
def main():
    print("Newton's Approximation: " + str(NewtonsApproximation(3,1.0)))

main()