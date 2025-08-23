* __auto_zip.py__: takes the task files in solutions/, packs them, and puts into submission.zip
* __golf_utils.py__: library functions
* __local_judge.py__: validate solutions locally
* __merge.py__: merge solutions from one directory into another, if the packed length is an improvement
* __scores.py__: print current solution lengths (intended to be run after auto_zip)
* __solver_notes.py__: reference solutions to tasks

# How to add solutions

* Git pull to be sure you have the best existing solutions.
* Put my unpacked (no zlib) solutions into some directory, e.g. `my_solutions/`. Make sure your solutions are valid because the script doesn't (yet) check them.
* Run `merge.py`, first editing the config variables if needed.
* Git commit and push.
