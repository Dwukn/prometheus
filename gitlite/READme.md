# Simple Version Control System (Simple VCS)

This is a basic implementation of a version control system (VCS) written in C. It allows you to initialize a repository, add files, commit changes, view commit logs, and restore files from specific commits. This VCS does not require any external libraries and provides fundamental version control operations.

## Features

- **Initialize Repository**: Set up a `.vcs` directory for version control.
- **Add Files**: Add individual files or all files in the directory to version control.
- **Commit Changes**: Commit added files with a custom commit message.
- **View Commit History**: Display a list of commits with their timestamp and message.
- **Restore Files**: Restore files to a specific commit.

## Installation


### Option 1: Manual Installation

1. **Clone the Repository**
   
   First, clone the repository to your local machine using the following command:

   ```bash
   git clone https://github.com/Dwukn/gitlite.git
   ```

2. **Navigate to the Project Directory**

   Change into the project directory:

   ```bash
   cd gitlite
   ```

3. **Compile the Program**

   Compile the C program using `gcc`:

   ```bash
   gcc vcs.c -o vcs
   ```

   After compiling, you can run the program with:

   ```bash
   ./vcs
   ```

### Option 2: One-Step Installation

For a quicker setup, you can use the following one-liner to download and run the installation script directly from the terminal:

```bash
bash <(curl -s https://raw.githubusercontent.com/Dwukn/gitlite/refs/heads/main/install.sh)
```

This will automatically:

- Clone the repository.
- Navigate to the project directory.
- Compile the program.

#### Once the script completes, the `vcs` program will be ready to use.


### Requirements

- A C compiler like **GCC** needs to be installed on your system.

### Key Improvements:

1. **Clarified the Instructions**: 
   - The instructions are now divided into two clear options: **Manual Installation** (Option 1) and **One-Step Installation** (Option 2).
   - Added a brief description of what each option does.

2. **Streamlined Code Blocks**:
   - Used proper code block formatting for each command so that it's easier to copy and execute.
   
3. **Added Requirement Section**:
   - Included a note about the need for a C compiler (GCC) for Option 1, making the README more informative.

4. **Consistency**:
   - Used consistent formatting and clear titles for each section to enhance readability and clarity.

Now the `README.md` is more user-friendly and easy to follow for anyone who wants to use or contribute to the GitLite project.


## Usage

### 1. Initialize a Repository

To initialize a new repository:

```bash
./vcs init
```

This will create a `.vcs` directory to store version control data.

### 2. Add Files to Version Control

#### Add a Single File

```bash
./vcs add <filename>
```

#### Add Multiple Files

```bash
./vcs add-multiple <file1> <file2> <file3> ...
```

#### Add All Files in Current Directory

```bash
./vcs add .
```

This will add all regular files (ignoring hidden files and `.vcs` directory).

### 3. Commit Changes

To commit the changes with a custom message:

```bash
./vcs commit "<commit message>"
```

### 4. View Commit History

To view the list of commits made so far:

```bash
./vcs log
```

### 5. Restore Files from a Specific Commit

To restore files from a specific commit, use the commit timestamp (this is generated when you create a commit):

```bash
./vcs restore <commit_timestamp>
```

This will restore all the files in that commit to the working directory.

## Directory Structure

- **.vcs**: The main directory where version control data is stored.
  - **objects/**: Contains objects (file hashes) for committed files.
  - **index.txt**: Tracks the current files added to version control (but not yet committed).
- **commit_\<timestamp\>**: Commit files that contain metadata about each commit (commit message, files, and hash values).

## Example Workflow

1. Initialize the repository:

   ```bash
   ./vcs init
   ```

2. Add files to version control:

   ```bash
   ./vcs add file1.txt
   ```

3. Commit the changes:

   ```bash
   ./vcs commit "Initial commit"
   ```

4. View commit history:

   ```bash
   ./vcs log
   ```

5. Restore files from a specific commit:

   ```bash
   ./vcs restore <commit_timestamp>
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
