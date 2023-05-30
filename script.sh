#!/bin/bash

# Set the organization and search query parameters
org="code-423n4"
query="findings"

# Get the list of repositories in the organization using the GitHub CLI
repos=$(gh repo list $org --json=nameWithOwner,sshUrl --limit=1000)

# Loop through each repository and check if it matches the search query
echo "$repos" | jq -r '.[] | select(.sshUrl | contains("'"$query"'")) | .sshUrl' | while read url; do
  echo "Cloning $url ..."
  git clone "$url"
  cd "$(basename $url .git)"
  find . ! -name "report.md" -type f -delete
  find . -type d -empty -delete
  cd ..
done
