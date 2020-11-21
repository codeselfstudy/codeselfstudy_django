#!/bin/bash


npx parcel static/src/parcel-entry.js \
    --hmr-port 34471 \
    --out-dir static/dist \
    --out-file main
