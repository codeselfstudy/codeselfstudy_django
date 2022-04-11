#!/bin/bash


# delete the existing build files
echo 'removing old build'
rm -rf ./assets/dist/*

# build the assets and watch for changes
echo 'rebuilding the assets'
npx parcel assets/src/main.js \
    --hmr-port 34471 \
    --dist-dir assets/dist \
    --public-url /static/dist/
