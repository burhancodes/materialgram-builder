#!/bin/bash

RPM_PACKAGE="$1"   # Path to the RPM package file
REPO_DIR="$2"      # Path to the directory containing repomd.xml

# Ensure GPG_KEY_ID and GPG_PASSPHRASE are set
if [ -z "$KEY_ID" ] || [ -z "$GPG_PASSPHRASE" ]; then
    echo "KEY_ID and GPG_PASSPHRASE environment variables must be set."
    exit 1
fi

# Sign the RPM package with loopback pinentry
echo "$GPG_PASSPHRASE" | gpg --batch --yes --pinentry-mode loopback --passphrase-fd 0 --detach-sign --default-key "$KEY_ID" "$RPM_PACKAGE"

# Verify if RPM signing was successful
if rpm -Kv "$RPM_PACKAGE" | grep -q "pgp"; then
    echo "RPM package signed successfully."
else
    echo "Failed to sign RPM package."
    exit 1
fi

# Sign repomd.xml in the specified repository directory
REPOMD_XML="$REPO_DIR/repodata/repomd.xml"
if [ -f "$REPOMD_XML" ]; then
    echo "$GPG_PASSPHRASE" | gpg --batch --yes --pinentry-mode loopback --passphrase-fd 0 --detach-sign --default-key "$KEY_ID" "$REPOMD_XML"
    echo "repomd.xml signed successfully."
else
    echo "repomd.xml not found in $REPO_DIR/repodata/"
    exit 1
fi
