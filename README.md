CoPy
====

A small and simple backup tool for coping your data.

![Alt text](https://raw.githubusercontent.com/MilchReis/CoPy/master/screenshot1.png "Screenshot1")

With CoPy you get the possibility to backup your files in a comfortable and fast way. Select all interesting directories for saving and a destination, f. e. a usb-drive. 
The first backup will copies all files and takes possibly a while. Your session (selected directories) will saved for the next time. 
After restarting the tool the last session is loaded. You are able to start the backup process directly. This programm will update all new and modified files and skips the other files. 

### Features ###
 - Backup for files and directories
 - Joins different directories to a target directory (f.e. usb stick)
 - Copies new and modified files only for a faster process
 - Remember session state for easy usage
 - Commandline interface for headless usage
 - Stand-alone builds for linux and windows
 - Languages: English, German

### Download ###
 - Linux: https://github.com/MilchReis/CoPy/raw/master/bin/CoPy
 - Windows: https://github.com/MilchReis/CoPy/raw/master/bin/CoPy.exe
 - Source https://github.com/MilchReis/CoPy/archive/master.zip
    - start with src/main.py
    - see dependencies (https://github.com/MilchReis/CoPy#dependencies)

### Use instructions ###
 - Choose your backup directories
 - Choose a destination directory (maybe a USB-Drive)
 - Backup all files
     - Copies new and modified files

### Commandline Interface ###
If you want to use the tool in bash, as cronjob or something else you can use the headless mode. Start the programm with a commandline argument and the gui will be not loaded. CoPy expects just one argument. Put an individual sessionfile (as absolute or relative path) to the programm and it will be started the backup-process.

`usage: CoPy /path/to/sessionfile`

Create your session file manually in a simpel text editor or by CoPy itself. The sessionfile contains in the first line the path to the target directory. All following lines will be interpreted as source directories. If you start CoPy in GUI Mode (without arguments) you can take you configurations and run the backup process. After clicking on the backup-button, the sessionfile will be created at your home directory like `/home/you/.copySession`.

### Dependencies ###
 - python 2.7
 - wxpython 3.x

### Build ###
Start the build process with the build scripts in build/ for your os.
