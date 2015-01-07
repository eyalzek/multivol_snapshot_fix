WHEN ALL IS LOST - restoring deja-dup backup that fails using deja-dup/duplicity

Steps
-----
1. Restore by hand according to the bottom of the page in the following article:
https://wiki.gnome.org/Apps/DejaDup/Help/Restore/WorstCase
You should be left a snapshot directory (all info inside can be used immediately) and a multivol_snapshot directory which requires you to extract the files.

2. Put "extract_content.sh" and "fix_content.py" in the parent directory of the multivol_snapshot folder.

3. Run "extract_content.sh".
You now have the content of each file inside it's directory, it should be named "content" (along the numbered files that it's consisted of).

4. Run "fix_content.py".

5. All files should be fixed!

** the source of the "extract_content.sh" script is this:
http://sashikasuren.blogspot.in/2013/01/duplicity-backup-restore-process.html

Enjoy
