#!/bin/sh
# Re-add ant project to scrapyd
echo "Removing old version..."
curl -X POST "http://localhost:6800/delproject.json?project=ant" &&
echo "Adding new version..." 
scrapyd-deploy &&
echo "Done."
