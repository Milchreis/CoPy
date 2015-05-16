# -*- coding: utf-8 -*-

import locale
l, _ = locale.getdefaultlocale()

if l.startswith('de'):
    BUTTON_ADD_SOURCE="Hinzufügen"
    BUTTON_REMOVE_SOURCE="Entfernen"
    BUTTON_REMOVE_ALL="Alle entfernen"
    BUTTON_SET_DESTINATION="Wähle ein Ziel"
    BUTTON_BACKUP="Backup"
    
    DIALOG_SURE_REMOVE_ALL="Sind Sie sicher, dass alle Datensätze aus der Liste entfernt werden sollen? \n(Dateien bleiben erhalten)'"
    DIALOG_CHOOSE_DIRECTORY="Einen Ordner wählen"
    LABEL_REMOVE="Löschen"
    LABEL_TARGET="Ziel:"
    LABEL_WAIT_HEADER="Bitte warten"
    LABEL_CALC_FILES="Dateien werden ermittelt"
    LABEL_READY_HEADER="Erfolgreich"
    LABEL_CANCEL="Abbrechen"
    LABEL_CLOSE="Schließen"
    LABEL_FILE_OF="Datei {} von {}"

else:
    BUTTON_ADD_SOURCE="Add directory"
    BUTTON_REMOVE_SOURCE="Remove entry"
    BUTTON_REMOVE_ALL="Remove all"
    BUTTON_SET_DESTINATION="Choose a destination"
    BUTTON_BACKUP="Backup"
    
    DIALOG_SURE_REMOVE_ALL="Are you sure to remove all directory entries from list? \n(Files will not removed)'"
    DIALOG_CHOOSE_DIRECTORY="Choose a directory"
    LABEL_REMOVE="Delete"
    LABEL_TARGET="Destination:"
    LABEL_WAIT_HEADER="Please wait"
    LABEL_CALC_FILES="Searching for files"
    LABEL_READY_HEADER="Successful"
    LABEL_CANCEL="Cancel"
    LABEL_CLOSE="Close"
    LABEL_FILE_OF="File {} of {}"
