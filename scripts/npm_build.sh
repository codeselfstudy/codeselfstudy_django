#!/bin/bash


# TODO: I don't think --no-source-maps is working correctly
npx parcel build static/src/parcel-entry.js \
    --no-source-maps\
    --out-dir static/dist \
    --out-file main
