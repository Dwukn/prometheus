#!/bin/bash

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
RED='\033[0;31m'
PURPLE='\033[1;35m'
NC='\033[0m' # No Color

# Display the title with figlet
echo -e "${GREEN}$(figlet -f slant 'GitLite Installer')${NC}"

# Basic Info
echo -e "${BLUE}--- GitLite Version Control System ---${NC}"
echo -e "${YELLOW}Project: Basic VCS (Version Control System)${NC}"
echo -e "${YELLOW}Description: This is a basic implementation of a version control system (VCS) written in C. It allows you to initialize a repository, add files, commit changes, view commit logs, and restore files from specific commits. This VCS does not require any external libraries and provides fundamental version control operations.${NC}"
echo -e "${PURPLE}Author: Dawood${NC}"
echo -e "${BLUE}--------------------------------------${NC}"

# Step 1: Clone the repository
echo -e "${YELLOW}Cloning the gitlite repository...${NC}"
if git clone https://github.com/Dwukn/gitlite.git; then
    echo -e "${GREEN}Cloned successfully!${NC}"
else
    echo -e "${RED}Failed to clone the repository!${NC}"
    exit 1
fi

# Step 2: Navigate to the project directory
cd gitlite || { echo -e "${RED}Failed to navigate into the gitlite directory.${NC}"; exit 1; }

# Step 3: Compile the program
echo -e "${BLUE}Compiling the program...${NC}"
gcc vcs.c -o vcs

# Success message
echo -e "${GREEN}Done! The program has been compiled as 'vcs'.${NC}"
