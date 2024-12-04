cp "utils/day_template.py" "year2024/day_"$2".py"
cp "utils/test_template.py" "year2024/tests/test_day_"$2".py"
touch "year2024/tests/example_data/2024_"$1"_input.txt" 
aocd > "year2024/tests/test_data/2024_"$1"_input.txt"
