#include <iostream>

int main(){
    int x; 
    std::cout << "Enter your favourite number between 1-100: ";
    std::cin >> x;
    std::cout << "Wow that's my favourite number too!" << std::endl;
    std::cout << "No really " << x << " is my favourite number";

    return x;
}