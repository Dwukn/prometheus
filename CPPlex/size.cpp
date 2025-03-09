#include <iostream>
#include <complex>
#include <vector>
using namespace std;

constexpr double sqaure(double x){
    return x * x;
}
void print_sqaure(double x){
    cout << "the square is " <<sqaure(x) << endl;
}
template <typename T>
void printVector(const std::vector<T>& vec) {
    for (const auto& val : vec) {
        std::cout << val << " ";
    }
    std::cout << std::endl;
}

bool accept(){
    char a;
    int tries = 0;
    while (tries<4 ){
    cout << "Enter 'y' or 'n': " <<endl;
    cin >> a;
    if (a == 'y'){
        cout << "y" << endl;
        return true;
        // exit(0);
    }else if(a == 'n'){
        cout << "n" << endl;
        return false;
        // exit(0);
        }else{
        tries++;
        cout << "Invalid input. Please try again. "  << tries << endl;
        // accept();
        // exit(0);
    }
    }
    cout<< "Too many tries"<<endl;
    exit(0);
}

bool accept2(){
    cout<<"Enter(y or n)"<<endl;
    int tries = 1;
    while (tries <= 4){
    char answer = 0;
    cin >> answer;
    switch(answer){
        case 'y':
            return true;
        case 'n':
            return false;
        default:
           cout << "Invalid input. Please try again. "  << (4 - tries) <<" left" << endl;
           tries++;
    }
    }
    cout<< "Too many tries" << endl;
    exit(0);
}



int main() {
    int x;
    char a;
    bool t;
    double d;
    float f;

    const int dmv = 17; // dmv is a named constant
    int var = 17; //var is not a constant
constexpr double max1 = 1.4 * sqaure(dmv); // OK if square(17) is a constant expression    // constexpr double max2 = 1.4 ∗ square(var); //error : var is not a constant expression

    // const vs constexpr
    // const int ci = 7; // Correct initialization and assignment
    // constexpr int cci = 7; // Correct initialization and assignment

    // // Incorrect assignment for const and constexpr types
    // // ci = 9; // Error: cannot assign to a variable declared as const
    // // cci = 9; // Error: cannot assign to a variable declared as constexpr

    // // Correct assignment for const and constexpr types
    // const int ci2 = 9;  // Correct assignment (9 is an integer, no error)
    // constexpr int cci2 = 9; // Correct assignment (9 is an integer, no error)

    // Correct assignment for integer and floating-point types
    int i1 = 7;  // Direct assignment (7 is an integer, no error)
    float i2 = 7.2; // Use the correct type for float
    float i3 = 7.2; // Correct initialization of float

    t = true;
    double d1 = 2.3;
    double d2 {2.3}; // Both these are correct ways to initialize doubles
    complex<double> z = 1;  // Single value, real part is 1
    complex<double> z2 {d1, d2}; // Complex number with two values (real and imaginary parts)
    complex<double> z3 = {1, 2}; // Complex number with real part 1 and imaginary part 2

    vector<int> v {1, 2, 3, 4, 5, 6, 9}; // Correct vector initialization

    // Output sizes of different data types
    cout << "Size of char is " << sizeof(a) << " bytes" << endl;
    cout << "Size of bool is " << sizeof(t) << " bytes" << endl;
    cout << "Size of int is " << sizeof(x) << " bytes" << endl;
    cout << "Size of float is " << sizeof(f) << " bytes" << endl;
    cout << "Size of double is " << sizeof(d) << " bytes" << endl;
    // cout << t << endl;
    // Output values of i1, i2, and i3
    cout << "i1: " << i1 << endl;
    cout << "i2: " << i2 << endl;
    cout << "i3: " << i3 << endl;

    // Output the complex numbers
    cout << "Complex z: " << z << endl;
    cout << "Complex z2: " << z2 << endl;
    cout << "Complex z3: " << z3 << endl;

    // Output the vector
    cout << "Vector v: ";
    for (int num : v) {
        cout << num << " ";
    }
    cout << endl;
    // printing by calling template functions
    printVector(v);
    cout << max1 << endl;
    print_sqaure(dmv);
    bool result = accept2();
    cout << "You entered: " << (result ? "yes" : "no") << endl;
    return 0;
}
