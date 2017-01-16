#/bin/bash
# Run from home
for d in datasets/*/; do
	python fix_ids.py "$(pwd)/$d";
done