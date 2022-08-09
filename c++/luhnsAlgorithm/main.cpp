#include <iostream>
#include <string>

using namespace std;


bool isValid(string cardNumber)
{
    // Uses Luhn's Algorithm to determine whether or not a Credit Card or Debit Card is valid

    int cardLength = cardNumber.length();

    int summation = 0;
    bool isSecond = false;

    for (int i = cardLength - 1; i >= 0 ; i--)
    {
        int digit = cardNumber[i] - '0';

        if(isSecond)
        {
            digit = digit * 2;
        }

        summation += digit / 10;
        summation += digit % 10;

        isSecond = !isSecond;

    }
    return (summation % 10 == 0);

}


int main()
{
    string cardNumber = "";
    if (isValid(cardNumber))
        printf("This is a valid card\n");
    else
        printf("This is not a valid card\n");
    return 0;
}