#include <iostream>
#include <openssl/md5.h>
#include <iomanip>
#include <sstream>

void calculateMD5(const std::string &input, unsigned char *md5_hash) {
    MD5_CTX ctx;
    MD5_Init(&ctx);
    MD5_Update(&ctx, input.c_str(), input.length());
    MD5_Final(md5_hash, &ctx);
}

std::string md5ToString(unsigned char *md5_hash) {
    std::stringstream ss;
    for (int i = 0; i < MD5_DIGEST_LENGTH; ++i) {
        ss << std::hex << std::setw(2) << std::setfill('0') << (int)md5_hash[i];
    }
    return ss.str();
}

int main() {
    std::string input = "Hello, world!";  // The string to hash
    unsigned char md5_hash[MD5_DIGEST_LENGTH];

    calculateMD5(input, md5_hash);
    std::string md5_hash_str = md5ToString(md5_hash);

    std::cout << "MD5 hash of '" << input << "': " << md5_hash_str << std::endl;

    return 0;
}
