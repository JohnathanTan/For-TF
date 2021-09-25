#!/bin/env bash
project_dir='my-python-project'
cd "./$project_dir"

echo 
echo "-----------"
echo
# Part a.
echo "Part a."
echo "There are $(git ls-files '*.py' | wc -l) .py files in '$project_dir' folder."
echo 
echo "-----------"
echo

# Part b.
echo "Part b."
# Ensure that the for loop operation only delimits by newline
IFS=$'\n'

total_lines=0
total_comment_lines=0
comment_regex='#(?=(?:[^"]*"[^"]*")*[^"]*$)'+"(?=(?:[^']*'[^']*')*[^']*$)"
for py_files in $(git ls-files '*.py')
do
    current_lines=$(grep -vc ^$ $py_files)
    echo "There are $current_lines non-empty lines in $py_files"
    total_lines=$((total_lines+current_lines))

    current_comment_lines=$(grep -c --perl-regex $comment_regex $py_files)
    echo "There are $current_comment_lines lines of comments in $py_files"
    total_comment_lines=$((total_comment_lines+current_comment_lines))

    echo
done

echo "In total, there are $total_comment_lines lines of comments (excluding empty lines) in the '$project_dir' folder."
echo "In total, there are $total_lines lines (excluding empty lines) in the '$project_dir' folder."
echo 
echo "-----------"
echo

# Part c.
echo "Part c."

total_fun=0
fun_regex='^(def).*(:$)'
for py_files in $(git ls-files '*.py')
do
    current_fun=$(grep -c --perl-regex $fun_regex $py_files)
    echo "There are $current_fun functions in $py_files"
    total_fun=$((total_fun+current_fun))

done

echo "In total, there are $total_fun functions in the '$project_dir' folder."
echo 
echo "-----------"
echo

# Part d.
echo "Part d."
echo "These are the lines changed between the current version against HEAD~3."
git diff --stat HEAD~3 HEAD
echo 
echo "-----------"
echo

# Part e.
echo "Part e."
for py_files in $(du --max-depth=2 -H -b | head -n -1)
do
    size_in_bytes=$(cut -d '.' -f1 <<< $py_files)
    size_in_mb=$(perl -e "print $size_in_bytes/1024/1024")
    current_folder=$(cut -d '.' -f2- <<< $py_files)
    echo "The size of "$current_folder" is $size_in_mb MB"
done
echo 
echo "-----------"
echo
