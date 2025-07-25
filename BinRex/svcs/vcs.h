#ifndef SIMPLE_VCS_H
#define SIMPLE_VCS_H


#include <time.h>


#define MAX_PATH 1024
#define MAX_MSG_LEN 256
#define VCS_DIR ".vcs"
#define OBJECTS_DIR ".vcs/objects"
#define INDEX_FILE ".vcs/index"
#define BRANCHES_DIR ".vcs/branches"
#define CONFIG_FILE ".vcs/config"
#define TAGS_FILE ".vcs/tags"

// Structure to store file metadata
typedef struct {
    char path[MAX_PATH];
    char hash[41];  // SHA-1 hash is 40 chars + null terminator
    time_t timestamp;
} FileEntry;

// Structure to store commit metadata
typedef struct {
    time_t timestamp;
    char message[MAX_MSG_LEN];
    char hash[41];  // SHA-1 hash for commit
} CommitEntry;

// Structure to store branch information
typedef struct {
    char branch_name[MAX_PATH];
    char commit_hash[41];
} BranchEntry;

// Function declarations
int vcs_init(void);
int vcs_add(const char* path);
int vcs_commit(const char* message);
char* calculate_file_hash(const char* path);
int copy_file(const char* source, const char* destination);
int save_to_index(FileEntry* entry);
int read_from_index(FileEntry** entries, int* count);
int check_vcs_exists(void);
int vcs_add_all(void);
int vcs_add_multiple(int count, char** files);
int is_hidden_file(const char* path);
int is_vcs_directory(const char* path);
int vcs_log(void);
int vcs_restore(const char* commit_hash);
int list_commits(CommitEntry** commits, int* count);
int restore_file_from_commit(const char* commit_hash);
int vcs_create_branch(const char* branch_name);
int vcs_checkout_branch(const char* branch_name);
int vcs_merge_branch(const char* branch_name);
int vcs_create_tag(const char* tag_name);
int vcs_list_tags(void);
int vcs_push(const char* remote_url);
int vcs_pull(const char* remote_url);
int vcs_gc(void);
int vcs_undo_last_commit(void);
int vcs_status(void);
int vcs_unstage(const char* path);
int vcs_snapshot(const char* snapshot_name);
int vcs_file_history(const char* path);
int vcs_configure(void);
int vcs_set_hook(const char* hook_type, const char* script_path);
int vcs_diff(const char* commit_hash1, const char* commit_hash2);

#endif // SIMPLE_VCS_H
