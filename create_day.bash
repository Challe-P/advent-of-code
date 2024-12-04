#!/bin/bash
cp "utils/template_day.py" "year2024/day_"$2".py"
sed -i "" -e "s/XX/${2^}/g" "year2024/day_"$2".py"
sed -i "" -e "s/xx/"$2"/g" year2024/day_"$2".py
cp "utils/template_test.py" "year2024/tests/test_day_"$2".py"
sed -i "" -e "s/XX/${2^}/g" "year2024/tests/test_day_"$2".py"
sed -i "" -e "s/xx/"$2"/g" year2024/tests/test_day_"$2".py
touch "year2024/tests/example_data/2024_"$1"_input.txt" 
aocd > "year2024/tests/test_data/2024_"$1"_input.txt"
