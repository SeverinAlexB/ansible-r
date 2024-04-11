#!/bin/bash

# First argument required: Folder to backup the file to. 

FILE_NAME="emergency.recover"

NODE_ID="$(lightning-cli getinfo | jq '.id' -r)"
MAIN_DIR="$(lightning-cli getinfo | jq '."lightning-dir"' -r)"
RECOVERY_FILE="$MAIN_DIR/$FILE_NAME"

MAIN_BACKUP_FOLDER=$1
BACKUP_FOLDER="$MAIN_BACKUP_FOLDER/$NODE_ID"
BACKUP_TARGET="$BACKUP_FOLDER/$FILE_NAME"

# Argument sanity check
if [[ ! -d $MAIN_BACKUP_FOLDER ]] ; then
    echo Backup folder does not exist $MAIN_BACKUP_FOLDER.
    exit 1;
fi
mkdir -p "$BACKUP_FOLDER"

echo ------------------------------------------------------------------------------------------
echo Started watcher for $NODE_ID to $BACKUP_FOLDER.
echo

# Backup file if backup not up to date.
HASH_LOCAL=$(shasum -a 256 $RECOVERY_FILE | awk '{print $1}')
HASH_BACKUP=$(shasum -a 256 $BACKUP_TARGET | awk '{print $1}')
if [ "$HASH_LOCAL" != "$HASH_BACKUP" ] ; then
    echo Local $FILE_NAME is different from backup. Backup now!
    cp $RECOVERY_FILE "$BACKUP_TARGET"
    echo Backup successful $BACKUP_TARGET.
    echo
fi

# Start watching for changes
echo $(date) Watching for changes on $RECOVERY_FILE.
echo
inotifywait -q -m -e moved_to $MAIN_DIR | \
    while read event; do
        if [[ $event == *"$FILE_NAME" ]]; then
          MODIFY_DATE="$(date -r $RECOVERY_FILE "+%m-%d-%Y %H:%M:%S:%N")"
          echo "Detected a new $FILE_NAME. $MODIFY_DATE"
          cp $RECOVERY_FILE "$BACKUP_TARGET"
          echo Backup successful $BACKUP_TARGET.
        fi
    done