//
//  main.cpp
//  InvoiceProgram
//
//  Created by Breydon Brennan on 3/25/21.
//

#include <iostream>

using namespace std;

void showResults(double dPercent, double dDiscount, double dTotal){
    dDiscount = floor(dDiscount * 100+.5)/100;
    dTotal = floor(dTotal * 100+.5)/100;
    cout << "Discount Percent:\t" << (dPercent*100) << "%\n";
    cout << "Discount Amount:\t$" << dDiscount << "\n";
    cout << "Invoice Total:\t$" << dTotal << "\n";
}

void calcR(char cCust, double dSubtotal){
    double dPercent;
    double dDiscount;
    double dTotal;
    if(dSubtotal >= 250 && dSubtotal < 500){
        dPercent = .2;
        dDiscount = dSubtotal * dPercent;
        dTotal = dSubtotal - dDiscount;
        showResults(dPercent,dDiscount,dTotal);
    }
    else if(dSubtotal >= 500){
        dPercent = .3;
        dDiscount = dSubtotal * dPercent;
        dTotal = dSubtotal - dDiscount;
        showResults(dPercent,dDiscount,dTotal);
        
    }
    else{
        dPercent = 0;
        dDiscount = dSubtotal;
        dTotal = dSubtotal;
        showResults(dPercent,dDiscount,dTotal);
    }
}
void calcW(char cCust, double dSubtotal){
    double dPercent;
    double dDiscount;
    double dTotal;
    
    if(dSubtotal < 500){
        dPercent = .4;
        dDiscount = dSubtotal * dPercent;
        dTotal = dSubtotal - dDiscount;
        showResults(dPercent,dDiscount,dTotal);
    }
    else{
        dPercent = .5;
        dDiscount = dSubtotal * dPercent;
        dTotal = dSubtotal - dDiscount;
        showResults(dPercent,dDiscount,dTotal);
    }
}
void calcC(char cCust, double dSubtotal){
    double dPercent = .25;
    double dDiscount = dSubtotal * dPercent;
    double dTotal = dSubtotal-dDiscount;
    
    showResults(dPercent,dDiscount,dTotal);
}

int main() {
    char cCust;
    string sSubtotal;
    double dSubtotal;
    
    cout << "The Invoice Total Calculator 2.0\n\n";
    
    cout << "Enter customer type as character(r/w/c):\t";
    cin >> cCust;
    cCust = tolower(cCust);
    switch(cCust){
        case 'r':
            cout << "Please provide the subtotal for the products ordered:\t";
            cin >> sSubtotal;
            dSubtotal = stod(sSubtotal);
            //cout << cCust << "\nYou have entered r\n";
            calcR(cCust,dSubtotal);
            break;
        case 'w':
            cout << "Please provide the subtotal for the products ordered:\t";
            cin >> sSubtotal;
            dSubtotal = stod(sSubtotal);
            //cout << cCust << "\nYou have entered w\n";
            calcW(cCust,dSubtotal);
            break;
        case 'c':
            cout << "Please provide the subtotal for the products ordered:\t";
            cin >> sSubtotal;
            dSubtotal = stod(sSubtotal);
            //cout << cCust << "\nYou have entered c\n";
            calcC(cCust,dSubtotal);
            break;
        default:
            cout << "Please provide one of the 3 destinguished characters (r/w/c)\n";
            return 1;
            break;
    }
    cout << "\n\nBye!\n";
    return 0;
}


