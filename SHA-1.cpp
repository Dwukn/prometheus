// sha-1 algo
#include <iostream>
#include <vector>
#include <iomanip>
#include <sstream>
#include <bitset>
#include <cstdint>  // Add this for uint32_t and uint8_t

class SHA1 {
public:
    SHA1() {
        // Initial hash values (Constants from SHA-1 spec)
        h0 = 0x67452301;
        h1 = 0xEFCDAB89;
        h2 = 0x98BADCFE;
        h3 = 0x10325476;
        h4 = 0xC3D2E1F0;
    }

    // Main method to calculate SHA-1 hash of input message
    std::string compute(const std::string &message) {
        std::vector<uint8_t> messageBits = padMessage(message);

        // Process the message in 512-bit chunks
        for (size_t i = 0; i < messageBits.size() / 64; ++i) {
            std::vector<uint32_t> block(80);
            for (size_t j = 0; j < 16; ++j) {
                block[j] = (messageBits[i * 64 + j * 4] << 24) |
                           (messageBits[i * 64 + j * 4 + 1] << 16) |
                           (messageBits[i * 64 + j * 4 + 2] << 8) |
                           (messageBits[i * 64 + j * 4 + 3]);
            }

            // Extend the 16 words into 80 words
            for (size_t j = 16; j < 80; ++j) {
                block[j] = rotateLeft(block[j - 3] ^ block[j - 8] ^ block[j - 14] ^ block[j - 16], 1);
            }

            uint32_t a = h0, b = h1, c = h2, d = h3, e = h4;

            // Main loop (80 rounds)
            for (size_t j = 0; j < 80; ++j) {
                uint32_t f, k;
                if (j < 20) {
                    f = (b & c) | (~b & d);
                    k = 0x5A827999;
                } else if (j < 40) {
                    f = b ^ c ^ d;
                    k = 0x6ED9EBA1;
                } else if (j < 60) {
                    f = (b & c) | (b & d) | (c & d);
                    k = 0x8F1BBCDC;
                } else {
                    f = b ^ c ^ d;
                    k = 0xCA62C1D6;
                }

                uint32_t temp = rotateLeft(a, 5) + f + e + k + block[j];
                e = d;
                d = c;
                c = rotateLeft(b, 30);
                b = a;
                a = temp;
            }

            h0 += a;
            h1 += b;
            h2 += c;
            h3 += d;
            h4 += e;
        }

        // Return the final hash
        return hashToString();
    }

private:
    uint32_t h0, h1, h2, h3, h4;

    // Rotate left helper function
    uint32_t rotateLeft(uint32_t value, size_t bits) {
        return (value << bits) | (value >> (32 - bits));
    }

    // Pad the message to a multiple of 512 bits
    std::vector<uint8_t> padMessage(const std::string &message) {
        std::vector<uint8_t> bits(message.begin(), message.end());

        // Add the 0x80 (0b10000000) byte
        bits.push_back(0x80);

        // Pad with 0s until the length is 64 bits short of a multiple of 512
        while (bits.size() % 64 != 56) {
            bits.push_back(0x00);
        }

        // Append the length of the original message (in bits) as a 64-bit integer
        uint64_t length = message.size() * 8;
        for (int i = 7; i >= 0; --i) {
            bits.push_back((length >> (i * 8)) & 0xFF);
        }

        return bits;
    }

    // Convert the hash to a hexadecimal string
    std::string hashToString() {
        std::stringstream ss;
        ss << std::hex << std::setw(8) << std::setfill('0') << h0
           << std::setw(8) << std::setfill('0') << h1
           << std::setw(8) << std::setfill('0') << h2
           << std::setw(8) << std::setfill('0') << h3
           << std::setw(8) << std::setfill('0') << h4;
        return ss.str();
    }
};

int main() {
    std::string input = "Hello, world!"; // Input message
    SHA1 sha1;
    std::string hash = sha1.compute(input);

    std::cout << "SHA-1 hash of '" << input << "': " << hash << std::endl;
    return 0;
}
