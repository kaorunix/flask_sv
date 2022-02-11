#!/usr/bin/env sh

# abort on errors
set -e

# build
npm run build

aws s3 sync dist s3://spa-study.colibrifw.org/ --delete --include "*"
