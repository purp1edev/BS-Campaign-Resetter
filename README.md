# BS Campaign Resetter

A simple python program which will reset the progress of your campaign on the windows PC version of Beat Saber

## Instructions

Copy the exe into "C:\Users\YOUR_USERNAME\AppData\LocalLow\Hyperbolic Magnetism\Beat Saber"
(If you have the folder on another drive, use that instead of C:)

Replace YOUR_USERNAME with the name of the user that you have beat saber installed on.

Once in the folder, double click the exe to run it. It will open a black command window, which will close instantly
After you have ran the program, open Beat Saber and the campaign will be reset

If you have any issues, message Purp1e#3076 on discord

## Is this a virus?

### Short Answer

No

### Long answer

No, but it may pick up as malware, depending on your antivirus

I think the cause for this is PyInstaller, which is the module I have used to compile this program

The issue is that while my program and many other programs compiled with PyInstaller are safe, some of them aren't, so antiviruses will recognise the PyInstaller code that is in all PyInstaller programs (including mine), and flag it as malicious due the same code being in malcious PyInstaller programs

There isn't really anything that I can do about this, but you can look at the source code on this github page and you'll see that there isn't really anything malicious

If you still don't trust me, you can install python, put the code in a .py file, and run that file in the directory stated in the instructions
