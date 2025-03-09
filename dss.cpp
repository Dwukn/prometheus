
#include <iostream>
#include <fstream>
#include <openssl/dsa.h>
#include <openssl/pem.h>
#include <openssl/sha.h>
#include <openssl/rand.h>
#include <openssl/bio.h>
#include <openssl/err.h>

// Function to generate DSA key pair
bool generate_dsa_keypair(DSA **dsa, EVP_PKEY **private_key, EVP_PKEY **public_key) {
    // Generate DSA parameters (p, q, g)
    *dsa = DSA_new();
    if (!DSA_generate_parameters_ex(*dsa, 2048, nullptr, 0, nullptr, nullptr, nullptr)) {
        std::cerr << "Failed to generate DSA parameters" << std::endl;
        return false;
    }

    // Generate DSA key pair
    if (!DSA_generate_key(*dsa)) {
        std::cerr << "Failed to generate DSA keys" << std::endl;
        return false;
    }

    // Create EVP_PKEY structure for private key
    *private_key = EVP_PKEY_new();
    if (!EVP_PKEY_assign_DSA(*private_key, *dsa)) {
        std::cerr << "Failed to assign private key" << std::endl;
        return false;
    }

    // Create EVP_PKEY structure for public key
    *public_key = EVP_PKEY_new();
    if (!EVP_PKEY_assign_DSA(*public_key, *dsa)) {
        std::cerr << "Failed to assign public key" << std::endl;
        return false;
    }

    return true;
}

// Function to sign the message using DSA private key
bool sign_message(EVP_PKEY *private_key, const std::string &message, std::vector<unsigned char> &signature) {
    EVP_MD_CTX *mdctx = EVP_MD_CTX_new();
    if (!mdctx) {
        std::cerr << "Failed to create MD context" << std::endl;
        return false;
    }

    if (!EVP_DigestSignInit(mdctx, nullptr, EVP_sha256(), nullptr, private_key)) {
        std::cerr << "Failed to initialize signature" << std::endl;
        EVP_MD_CTX_free(mdctx);
        return false;
    }

    if (!EVP_DigestSignUpdate(mdctx, message.c_str(), message.length())) {
        std::cerr << "Failed to update signature" << std::endl;
        EVP_MD_CTX_free(mdctx);
        return false;
    }

    size_t sig_len = 0;
    if (!EVP_DigestSignFinal(mdctx, nullptr, &sig_len)) {
        std::cerr << "Failed to finalize signature" << std::endl;
        EVP_MD_CTX_free(mdctx);
        return false;
    }

    signature.resize(sig_len);
    if (!EVP_DigestSignFinal(mdctx, signature.data(), &sig_len)) {
        std::cerr << "Failed to obtain final signature" << std::endl;
        EVP_MD_CTX_free(mdctx);
        return false;
    }

    EVP_MD_CTX_free(mdctx);
    return true;
}

// Function to verify the message signature using DSA public key
bool verify_signature(EVP_PKEY *public_key, const std::string &message, const std::vector<unsigned char> &signature) {
    EVP_MD_CTX *mdctx = EVP_MD_CTX_new();
    if (!mdctx) {
        std::cerr << "Failed to create MD context" << std::endl;
        return false;
    }

    if (!EVP_DigestVerifyInit(mdctx, nullptr, EVP_sha256(), nullptr, public_key)) {
        std::cerr << "Failed to initialize verification" << std::endl;
        EVP_MD_CTX_free(mdctx);
        return false;
    }

    if (!EVP_DigestVerifyUpdate(mdctx, message.c_str(), message.length())) {
        std::cerr << "Failed to update verification" << std::endl;
        EVP_MD_CTX_free(mdctx);
        return false;
    }

    int verify_status = EVP_DigestVerifyFinal(mdctx, signature.data(), signature.size());
    EVP_MD_CTX_free(mdctx);

    if (verify_status == 1) {
        std::cout << "Verification successful!" << std::endl;
        return true;
    } else if (verify_status == 0) {
        std::cerr << "Verification failed: invalid signature" << std::endl;
        return false;
    } else {
        std::cerr << "Verification error" << std::endl;
        return false;
    }
}

int main() {
    // Initialize OpenSSL library
    OpenSSL_add_all_algorithms();
    ERR_load_crypto_strings();

    // Generate DSA key pair
    DSA *dsa = nullptr;
    EVP_PKEY *private_key = nullptr, *public_key = nullptr;
    if (!generate_dsa_keypair(&dsa, &private_key, &public_key)) {
        std::cerr << "Key generation failed" << std::endl;
        return 1;
    }

    // Sign a message
    std::string message = "This is a secret message";
    std::vector<unsigned char> signature;
    if (!sign_message(private_key, message, signature)) {
        std::cerr << "Signing failed" << std::endl;
        return 1;
    }

    // Verify the signature
    if (!verify_signature(public_key, message, signature)) {
        std::cerr << "Verification failed" << std::endl;
        return 1;
    }

    // Cleanup
    EVP_PKEY_free(private_key);
    EVP_PKEY_free(public_key);
    DSA_free(dsa);

    return 0;
}
