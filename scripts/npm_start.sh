#!/bin/bash


# delete the existing build files
echo 'removing old build'
rm -rf ./static/dist

# build the assets and watch for changes
echo 'rebuilding the assets'
npx parcel static/src/parcel-entry.js \
    --hmr-port 34471 \
    --dist-dir codeselfstudy/static/dist \
    --public-url /static/dist/ #\
    # --out-file main
