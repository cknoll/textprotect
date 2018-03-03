# textprotect

The program `textprotect` allows to easily create, read and edit a plain
text file which is encrypted before it is written to the physical memory.
The text file is decrypted before shown to the user in the favorite
text editor.

It combines simplicity (plain text, standard editor) and security (gpg).

The target audience are people which are only little concerned with
cyber-security and might not yet use any password-manager.
This program offers a simple, understandable way to store sensible
information like passwords, PINs etc. comparatively securely on hard-drives.

Long story short: I created this project for my parents.




## Issues

- make a backup of the encrypted-files, to prevent complete data loss in case of saving an empty file
- autodetect the language, refactor the strings to a separate module


## License
This project is licenced under GPLv3. See [LICENSE](LICENSE)

