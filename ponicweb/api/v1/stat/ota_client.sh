#!/bin/bash

set -ex

OTA_LOGIN=grobox
OTA_PASSWORD=+_bXJ9SaH
OTA_DIR=/root/cloudponics

DOWNLOAD_URL="https://$OTA_LOGIN:$OTA_PASSWORD@github.com/cloudponics/gen2.git"
DOWNLOAD_BRANCH="master"
VERSION_FILE="$OTA_DIR/.ota_version"
DOWNLOAD_DIR="$OTA_DIR/firmware"
LOG_FILE="/tmp/ota_log"

echo "Update check at $(date +%Y-%m-%d:%H:%M:%S)" >> $LOG_FILE
REMOTE_HASH=$(git ls-remote "$DOWNLOAD_URL" | head -1 | cut -f 1)
if [ -f $VERSION_FILE ]
then
SAVED_HASH=$(cat "$VERSION_FILE")
fi

if [ -z "$REMOTE_HASH" ]
then
echo "Can't check remote repository, I will try later" >> $LOG_FILE
elif [ "$REMOTE_HASH" = "$SAVED_HASH" ]
then
echo "Same firmare, exit silently" >> $LOG_FILE
else
echo "New firmware script, Let's download it" >> $LOG_FILE
sudo rm -rf "$DOWNLOAD_DIR"
mkdir "$DOWNLOAD_DIR"
git clone -b "$DOWNLOAD_BRANCH" --depth 1 "$DOWNLOAD_URL" "$DOWNLOAD_DIR"
echo "$REMOTE_HASH" > "$VERSION_FILE"
sudo service firmware restart
echo "New firmware launched" >> $LOG_FILE
fi

