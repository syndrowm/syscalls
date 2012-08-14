#!/usr/bin/env python

# Look mah no class!

def freebsd(call):
    from freebsd_syscalls import syscalls
    return _resolv(call, syscalls)

def linux(call):
    from linux_syscalls import syscalls
    return _resolv(call, syscalls)

def netbsd(call):
    from netbsd_syscalls import syscalls
    return _resolv(call, syscalls)

def openbsd(call):
    from openbsd_syscalls import syscalls
    return _resolv(call, syscalls)

def osx(call):
    from osx_syscalls import syscalls
    return _resolv(call, syscalls)

def _resolv(call, syscalls):
    """return syscall name"""
    for k,v in syscalls.iteritems():
        if type(call) == int:
            if call == v:
                return k 
        else:
            if call == k:
                return v
    

if __name__ == "__main__":
    pass

