#include <iostream>

using namespace std;

int main(){
    const double price_per_large_room {35};
    const double price_per_small_room {25};
    const double interest {0.06};
    const int days_valid {30};
    
    cout << "Welcome to Benjy's cleaning service" <<endl;
    
    cout << "How many large rooms would you like cleaned? ";
    int no_of_large_rooms {0};
    cin >> no_of_large_rooms;
    
    cout << "How many small rooms would you like cleaned? ";
    int no_of_small_rooms {0};
    cin >> no_of_small_rooms;

    cout << "\nYou have selected " << no_of_large_rooms << " large room(s) and "<< no_of_small_rooms << " small room(s)" << endl;
    
    double cost {no_of_large_rooms * price_per_large_room + no_of_small_rooms * price_per_small_room};
    cout << "Room cost: " << char(156) << cost <<endl;
    
    double tax {cost * interest};
    cout << "Total tax: " <<char(156) << tax << endl;
    cout << "===========================" << endl;
    cout << "Total cost: " << char(156) << cost + tax << endl;
    cout << "This estimate is valid for "<< days_valid <<  " days" <<endl;
    return 0;
}