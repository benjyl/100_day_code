#include <iostream> // input output library which holds cin and cout

int main(){
    int favourite_number;
    // std is a namespace
    // cout writes to console
    std::cout << "Enter your favourite number between 1 and 100: ";
    // cin reads from console
    std::cin >> favourite_number; // >> means extract from console
    std::cout << "Amazing!! That's my favaourite number too" << std::endl;
    return 0;
}