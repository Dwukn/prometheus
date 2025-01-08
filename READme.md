# Simple Version Control System (Simple VCS)

This is a basic implementation of a version control system (VCS) written in C. It allows you to initialize a repository, add files, commit changes, view commit logs, and restore files from specific commits. This VCS does not require any external libraries and provides fundamental version control operations.

## Features

- **Initialize Repository**: Set up a `.vcs` directory for version control.
- **Add Files**: Add individual files or all files in the directory to version control.
- **Commit Changes**: Commit added files with a custom commit message.
- **View Commit History**: Display a list of commits with their timestamp and message.
- **Restore Files**: Restore files to a specific commit.

## Installation

To use this simple version control system, you need to have a C compiler (such as GCC) installed.

### 1. Clone or download the repository to your local machine.
``` bash
git clone https://github.com/Dwukn/gitlite.git
```
### 2. Navigate to the project directory in the terminal.
```bash
cd gitlite
```
### 3. Compile the program:

```bash
gcc vcs.c -o vcs
```

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
