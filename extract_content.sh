#!/bin/bash
find multivol_snapshot/ -type f -printf '%h\0' | \
sort -uz | \
xargs -0 -n 1 sh -c 'cd "$1"; cat $(ls | sort -n) > content' spacer
