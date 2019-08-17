#!/bin/sh
# Delete ant project from scrapyd
curl -X POST http://localhost:6800/delproject.json?project=ant
