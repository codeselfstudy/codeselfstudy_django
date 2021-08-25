#!/bin/sh


# delete the existing build files
echo 'removing old build'
rm -rf ./codeselfstudy/static/dist

# build the assets and watch for changes
echo 'rebuilding the assets'
npx parcel codeselfstudy/static/src/parcel-entry.js \
    --hmr-port 34471 \
    --out-dir codeselfstudy/static/dist \
    --public-url /static/dist/ \
    --out-file main
