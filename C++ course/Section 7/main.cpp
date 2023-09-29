#include <iostream>
#include <vector>
using namespace std;

int main(){
    vector <int> vector1 {};
    vector <int> vector2 {};

    vector1.push_back(10);
    vector1.push_back(20);
    cout << "Element 1: " << vector1.at(0) << " Element 2: " << vector1.at(1) << " Vector Size: " << vector1.size() << endl;

    vector2.push_back(100);
    vector2.push_back(200);
    cout << "Element 1: " << vector2.at(0) << " Element 2: " << vector2.at(1) << " Vector Size: " << vector2.size() << endl;

    vector <vector<int>> vector_2d {};
    vector_2d.push_back(vector1);
    vector_2d.push_back(vector2);

    cout << "Element at position 1,1: " << vector_2d.at(0).at(0) << " Element at position 2,2: "<< vector_2d.at(1).at(1) << endl;

    vector1.at(0) = 1000;
    cout << "Vector 1 at position 1: " <<vector1.at(0) <<endl;
    cout << "2d vector at position 1 ,1: " <<vector_2d.at(0).at(0) << endl;

    return 0;
}
