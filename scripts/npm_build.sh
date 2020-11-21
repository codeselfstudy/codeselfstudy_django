#!/bin/bash


# delete the existing build files
echo 'removing old build'
rm -rf ./static/dist

echo 'rebuilding the assets'
# TODO: I don't think --no-source-maps is working correctly
npx parcel build static/src/parcel-entry.js \
    --no-source-maps\
    --out-dir static/dist \
    --out-file main
