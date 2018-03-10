# textprotect

The program `textprotect` aims to be *very simple password manager*.
It allows to easily create, read and edit a plain text file
which is encrypted before it is written to the physical memory.
The text file is decrypted before shown to the user in the favorite
text editor (currently `kate` is hard coded)

It combines simplicity (plain text, standard editor) and security (`gpg`).

The target audience are people which are only little concerned with
cyber-security and might not yet use any password-manager.
This program offers a simple, understandable way to store sensible
information like passwords, PINs etc. comparatively securely on hard-drives.

Long story short: I created this project for my parents.


## Background
`textprotect` consists of a single python script which uses kdialog to interact with the user.
The encrypted data is stored in `~/textprotect/data.txt.gpg`.
The decrypted data is temporarily stored in `/dev/shm/xxx-textprotect-tmp.txt`, where `xxx`
is some random string. Note that this file lives only in memory but not on the hard drive.
It is immediately deleted after the text editor has been closed.

## Installation (provisional guide)

- run `sudo apt install python3-gnupg kde-baseapps-bin`
- copy the script `textprotect` in your path

## Usage
### First usage

- Notice that the author does not provide any warranty
- Run `textprotect` from the command line.
- Type in twice the password which you want to use for protecting the your text file.
- After the editor has opened type in or paste your secret text.
- Close the editor.

### Normal usage
- Run `textprotect` from the command line.
- Type in the password which you want to use for protecting the your text file.
- After the editor has opened type in or paste your secret text.
- Close the editor.

## Usage Recommendations
- Regularly backup the file `~/textprotect/data.txt.gpg` on a different device.
- There is no password-recovery function: memorize the textprotect-password very well
or better write it down in some trusted place.
- Note that encryption-algorithms are not unbreakable.
The goal of encryption is to increase the necessary effort to break it beyond the benefit
of breaking it. Long keys/passwords greatly help to increase the security.
- For the interested: play around with that: <https://www.my1login.com/resources/password-strength-test/>


### Bad ideas to store passwords (in general)

- Sticky note next next to the display
- Crumpled piece of paper hidden in some creative place
    - Danger of been thrown away during some cleanup and of never to be found again
- Only memorize them
    - Works only for few passwords which are frequently used
    - Might cause stress due to fear of forgetting
    - Encourages to choose too simple passwords and/or reuse of passwords
- Unencrypted on your hard drive
    - Vulnerable due to malware
- Unencrypted on some cloud storage (dropbox)
    - Vulnerable due to abuse by provider

### Good ideas to handle and store passwords

- Encrypted on your computer
- Encrypted on some trusted cloud storage
    - (-> Solution to the backup problem)
- Master-Password: neat piece of paper at secure place (e.g. alongside other important documents)


## Issues (PRs welcome)

- make a backup of the encrypted-files, to prevent complete data loss in case of saving an empty file
- auto-detect the language, refactor the language dependent message-strings to a separate module
- make it installable via pip




## License
This project is licensed under GPLv3. See [LICENSE](LICENSE)

