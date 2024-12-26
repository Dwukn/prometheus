// key exchange
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <ctime>

// Function to calculate (x^y) % p using modular exponentiation
long long power_mod(long long x, long long y, long long p) {
    long long result = 1;
    x = x % p;  // In case x is more than p
    while (y > 0) {
        if (y % 2 == 1) {
            result = (result * x) % p;
        }
        y = y / 2;
        x = (x * x) % p;
    }
    return result;
}

// Diffie-Hellman key exchange function
void diffie_hellman_key_exchange(long long p, long long g) {
    // Seed random number generator
    std::srand(std::time(0));

    // Alice's private key (randomly selected)
    long long a = std::rand() % (p - 2) + 2;
    
    // Bob's private key (randomly selected)
    long long b = std::rand() % (p - 2) + 2;

    // Alice computes her public key A
    long long A = power_mod(g, a, p);
    
    // Bob computes his public key B
    long long B = power_mod(g, b, p);

    // Alice and Bob exchange public keys A and B
    
    // Alice computes the shared secret key using Bob's public key B
    long long shared_secret_Alice = power_mod(B, a, p);
    
    // Bob computes the shared secret key using Alice's public key A
    long long shared_secret_Bob = power_mod(A, b, p);

    // Output the results
    std::cout << "Public Parameters: p = " << p << ", g = " << g << std::endl;
    std::cout << "Alice's Public Key: A = " << A << std::endl;
    std::cout << "Bob's Public Key: B = " << B << std::endl;
    std::cout << "Alice's Shared Secret Key: " << shared_secret_Alice << std::endl;
    std::cout << "Bob's Shared Secret Key: " << shared_secret_Bob << std::endl;
    
    // Verify that both shared secret keys are the same
    if (shared_secret_Alice == shared_secret_Bob) {
        std::cout << "Shared secret keys match! Both Alice and Bob have the same secret key." << std::endl;
    } else {
        std::cout << "Shared secret keys do not match. Something went wrong." << std::endl;
    }
}

int main() {
    // Public parameters: prime p and base g
    long long p = 23;  // A small prime number for demonstration
    long long g = 10;   // A primitive root modulo p

    // Perform Diffie-Hellman Key Exchange
    diffie_hellman_key_exchange(p, g);

    return 0;
}
