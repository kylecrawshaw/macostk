# -*- coding: utf-8 -*-

import objc as _objc
import ctypes as _ctypes
import SystemConfiguration as _SC
from Foundation import NSBundle as _NSBundle

def consoleuser():
    return _SC.SCDynamicStoreCopyConsoleUser(None, None, None)[0]


def lockscreen():
    '''
    Immediately lock screen.
    '''
    loginPF = _ctypes.CDLL('/System/Library/PrivateFrameworks/login.framework/Versions/Current/login')
    result = loginPF.SACLockScreenImmediate()
    return result


class UserSession:

    def __init__(self, session_details):
        self._session_details = session_details

    @property
    def has_console(self):
        if self._session_details['kCGSSessionOnConsoleKey'] == 1:
            return True
        return False

    @property
    def user_name(self):
        return self._session_details['kCGSSessionUserNameKey']

    @property
    def long_user_name(self):
        return self._session_details['kCGSessionLongUserNameKey']

    @property
    def is_logged_in(self):
        if self._session_details['kCGSSessionLoginDoneKey'] == 1:
            return True
        return False

    @property
    def user_id(self):
        return self._session_details['kCGSSessionUserIDKey']

    @property
    def group_id(self):
        return self._session_details['kCGSSessionGroupIDKey']

    @property
    def session_id(self):
        return self._session_details['kCGSSessionUserIDKey']

    @property
    def security_session_id(self):
        return self._session_details['kSCGSecuritySessionID']


class FastUserSwitching:

    def __init__(self):
        CG_bundle = _NSBundle.bundleWithIdentifier_('com.apple.CoreGraphics')
        functions = [("CGSSessionCopyAllSessionProperties", b"@"),]
        _objc.loadBundleFunctions(CG_bundle, globals(), functions)
        self._user_sessions = []

    @property
    def user_sessions(self):
        if not self._user_sessions:
            self._user_sessions = [UserSession(user_session)
                           for user_session in CGSSessionCopyAllSessionProperties()]
        return self._user_sessions

    def consoleuser(self):
        for session in self.user_sessions:
            if session.has_console:
                return session.username
        return None
