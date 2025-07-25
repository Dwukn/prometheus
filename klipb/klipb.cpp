#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <sqlite3.h>
#include <cstring>
#include <vector>
#include <cstdlib>

const char *DB_PATH = "clipboard.db";

void executeSQL(sqlite3 *db, const char *sql) {
    char *errMsg = nullptr;
    if (sqlite3_exec(db, sql, nullptr, nullptr, &errMsg) != SQLITE_OK) {
        std::cerr << "SQL error: " << errMsg << std::endl;
        sqlite3_free(errMsg);
    }
}

void storeClipboard(sqlite3 *db, const std::string &data) {
    std::string sql = "INSERT INTO clips (data) VALUES ('" + data + "');";
    executeSQL(db, sql.c_str());
}

void listClips(sqlite3 *db) {
    const char *sql = "SELECT id, data FROM clips;";
    sqlite3_stmt *stmt;
    if (sqlite3_prepare_v2(db, sql, -1, &stmt, nullptr) == SQLITE_OK) {
        while (sqlite3_step(stmt) == SQLITE_ROW) {
            int id = sqlite3_column_int(stmt, 0);
            const char *data = (const char *)sqlite3_column_text(stmt, 1);
            std::cout << id << ": " << data << std::endl;
        }
        sqlite3_finalize(stmt);
    } else {
        std::cerr << "Failed to fetch clips." << std::endl;
    }
}

void deleteClip(sqlite3 *db, int id) {
    std::string sql = "DELETE FROM clips WHERE id = " + std::to_string(id) + ";";
    executeSQL(db, sql.c_str());
}

void initializeDB(sqlite3 *&db) {
    if (sqlite3_open(DB_PATH, &db)) {
        std::cerr << "Can't open database: " << sqlite3_errmsg(db) << std::endl;
        return;
    }

    const char *sql = "CREATE TABLE IF NOT EXISTS clips (id INTEGER PRIMARY KEY AUTOINCREMENT, data TEXT);";
    executeSQL(db, sql);
}

int main(int argc, char *argv[]) {
    sqlite3 *db = nullptr;
    initializeDB(db);

    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <store|list|delete> [data|id]" << std::endl;
        return 1;
    }

    std::string command = argv[1];

    if (command == "store") {
        std::string data;
        std::getline(std::cin, data);
        storeClipboard(db, data);
    } else if (command == "list") {
        listClips(db);
    } else if (command == "delete") {
        if (argc < 3) {
            std::cerr << "Please provide an ID to delete." << std::endl;
            return 1;
        }
        int id = std::stoi(argv[2]);
        deleteClip(db, id);
    } else {
        std::cerr << "Unknown command." << std::endl;
        return 1;
    }

    sqlite3_close(db);
    return 0;
}
