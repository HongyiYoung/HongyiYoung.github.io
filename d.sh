#!/bin/bash

# Exit on error
set -e

echo -e "\033[36m==========================================\033[0m"
echo -e "\033[36m   Starting Source Backup & Deployment\033[0m"
echo -e "\033[36m==========================================\033[0m"

echo -e "\n\033[33m[1] Pulling latest changes from 'source' branch...\033[0m"
if git pull origin source; then
    echo -e "  -> \033[32mSource is up to date.\033[0m"
else
    echo -e "  -> \033[31mPull failed! Please resolve conflicts manually.\033[0m"
    exit 1
fi

echo -e "\n\033[33m[2] Committing local changes...\033[0m"
git add .

MSG="Backup & Deploy: $(date +'%Y-%m-%d %H:%M:%S')"
if [ -n "$1" ]; then
    MSG="$1"
fi

if git commit -m "$MSG"; then
    echo -e "  -> \033[32mCommitted successfully: $MSG\033[0m"
else
    echo -e "  -> \033[90mNothing to commit (working tree clean).\033[0m"
fi

echo -e "\n\033[33m[3] Pushing to remote 'source' branch...\033[0m"
if git push -u origin source; then
    echo -e "\n\033[36m========================================================\033[0m"
    echo -e " \033[32m✅ All Done! \033[0m"
    echo -e " \033[36mGitHub Actions will automatically build and deploy the site.\033[0m"
    echo -e " \033[36mSource code is backed up to the 'source' branch.\033[0m"
    echo -e " \033[36mYou can safely switch devices and pull from 'source'!\033[0m"
    echo -e "\033[36m========================================================\033[0m"
else
    echo -e "  -> \033[31mPush failed! Check network/credentials.\033[0m"
    exit 1
fi
