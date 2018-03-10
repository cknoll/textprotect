#!/usr/bin/env python3


"""
Concept:



"""

import sys
import shutil
import os
import subprocess
import string
import random

# from ipydex import IPS

# this is not part of the standard library but available via pip
# or apt (python3-gnupg)
import gnupg

home_dir = os.path.expanduser("~")
tpt_dir = os.path.join(home_dir, ".textprotect")
tpt_file = "data.txt.gpg"
tpt_path = os.path.join(tpt_dir, tpt_file)

gpg = gnupg.GPG()

rnd_base_path = "/dev/shm"

msg_new_file = "Es wurde unter dem Pfad <tt>{}</tt> keine Daten-Datei gefunden.<br>" \
               "Es wird jetzt eine neue verschlüsselte Datei angelegt. " \
               "(Das ist das normale Verhalten beim ersten Start.)"
msg_new_file = msg_new_file.format(tpt_path)

msg_new_file_content = "Das ist die neue verschlüsselte Datei.\n"

msg_cancel = "Abbruch."
msg_edit_fail = "Fehler beim Editieren."
msg_set_pw1 = "Neues Passwort setzen:"
msg_set_pw2 = "Neues Passwort (Wiederholung):"


msg_open_file = "textprotect möchte die Datei " \
                "<br><tt>&nbsp;{}</tt><br>öffnen."

msg_wrong_password = "Das eingegebene Passwort war falsch. Ende."
msg_final_success = "Speichern und Verschlüsseln erfolgreich."


msg_pw_mismatch = "Ungleiche Passworte. Nochmal..."

def read_password(txt):

    # quoted_text = '"{}"'.format(txt).replace("\n", r"\n")
    try:
        res = subprocess.check_output(["kdialog", "--password", txt])
    except subprocess.CalledProcessError:
        dialog(msg_cancel)
        exit()
    return res

def dialog(txt):
    subprocess.check_output(["kdialog", "--msgbox", txt])

def random_path(suffix=""):
    N = 12
    chars = string.ascii_lowercase + string.digits
    rnd_string = ''.join(random.choice(chars) for _ in range(N))

    return os.path.join(rnd_base_path, rnd_string + suffix)

def edit_file(path):
    devnull = subprocess.DEVNULL
    try:
        res = subprocess.check_output(["kate", "-n", path], stderr=devnull)
    except subprocess.CalledProcessError:
        dialog(msg_edit_fail)
        exit()

def new_file():

    dialog(msg_new_file)

    while 1:

        pw1 = read_password(msg_set_pw1)
        pw2 = read_password(msg_set_pw2)

        if pw1 == pw2:
            break

        dialog(msg_pw_mismatch)

    open_encrypted_file(pw=pw1, new=True)

def open_encrypted_file(pw=None, new=False):

    if pw is None:
        pw = read_password(msg_open_file.format(tpt_path))

    # store decrypted data in temporary file
    path = random_path("-textprotect-tmp.txt")

    if new:
        with open(path, "wt") as plainfile:
            plainfile.write(msg_new_file_content)
    else:
        # decrypt data
        with open(tpt_path, "rb") as thefile:
            result = gpg.decrypt_file(thefile, passphrase=pw,
                                      output=path)

        if not result.ok:
            dialog(msg_wrong_password)
            exit(0)

    edit_file(path)

    # encrypt data
    with open(path, "rb") as thefile:
        gpg.encrypt_file(thefile, recipients="", symmetric=True,
                         passphrase=pw, output=tpt_path)

    os.remove(path)

    dialog(msg_final_success)


def main():

    # 1. ensure directory exists

    exists = os.path.exists(tpt_dir)
    isdir = os.path.isdir(tpt_dir)

    if not isdir:
        # two possibilities: absent or wrong type (file)
        if exists:
            msg = "The path {} is expected to be a directory " \
                "or absent but not a file.".format(tpt_dir)
            raise FileExistsError(msg)

        # create the expected dir
        os.mkdir(tpt_dir)

    exists = os.path.exists(tpt_path)
    isfile = os.path.isfile(tpt_path)

    # 2. ensure target-file exists (create new or open existing)
    if not isfile:
        # two possibilities: absent or wrong type (dir)
        if exists:
            #
            msg = "The path {} is expected to be a file " \
                "or absent but not a directory.".format(tpt_dir)
            raise FileExistsError(msg)
        else:
            new_file()
            exit()
    else:
        open_encrypted_file()

if __name__ == "__main__":
    main()



