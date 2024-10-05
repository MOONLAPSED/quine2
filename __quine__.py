#!/usr/bin/env python
# -*- coding: utf-8 -*-
# STATE_START
{
  "current_step": 0
}
# STATE_END
import tracemalloc
import logging
tracemalloc.start()
tracemalloc.Filter(False, "<frozen importlib._bootstrap>")
import ctypes
import os
import sys
import stat
# platforms: Ubuntu-22.04LTS (posix), Windows-11 (nt)
if os.name == 'posix':
    from ctypes import cdll
    def detailedPermissions(filePath):
        """Get detailed file permissions using stat."""
        fileStats = os.stat(filePath)
        mode = fileStats.st_mode
        permissionsInfo = {
            "readable": bool(mode & stat.S_IRUSR),
            "writable": bool(mode & stat.S_IWUSR),
            "executable": bool(mode & stat.S_IXUSR),
            "octal": oct(mode)
        }
        return permissionsInfo
    filePath = sys.argv[0]
    permissionsInfo = detailedPermissions(filePath)
elif os.name == 'nt':
    from ctypes import windll
    def windowsPermissions(filePath):
        """Get detailed file permissions using Windows API."""
        fileHandle = windll.kernel32.CreateFileW(file_path, 0x80000000, 0, None, 3, 0x80, None)
        if fileHandle == -1:
            return None
        READ_CONTROL = 0x00020000
        DACL_SECURITY_INFORMATION = 0x00000004
        queryInfo = ctypes.windll.advapi32.GetFileSecurityW(file_path, DACL_SECURITY_INFORMATION, None, 0, None)
        permissionsInfo = {
            "readable": bool(windll.kernel32.GetFileSecurityW(file_path, 0x00000001, None, 0, 0) & 0x00000001),
            "writable": bool(windll.kernel32.GetFileSecurityW(file_path, 0x00000001, None, 0, 0) & 0x00000002),
            "executable": bool(windll.kernel32.GetFileSecurityW(file_path, 0x00000001, None, 0, 0) & 0x0000000)}
        fileHandle.Close()
# HOMOICONISTIC morphological source code displays 'modified quine' behavior
# within a validated runtime, if and only if the valid python interpreter
# has r/w/x permissions to the source code file and some method of writing
# state to the source code file is available. Any interruption of the
# '__exit__` method or misuse of '__enter__' will result in a runtime error
print(f"File: {filePath}")
print(f"Readable: {permissionsInfo['readable']}")
print(f"Writable: {permissionsInfo['writable']}")
print(f"Executable: {permissionsInfo['executable']}")
print(f"Octal Permissions: {permissionsInfo['octal']}")
