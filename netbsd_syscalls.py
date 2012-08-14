# netbsd http://fxr.watson.org/fxr/source/sys/syscall.h?v=NETBSD
# cat netbsd.txt | apy 1: | grep ^#define | awk '{print "\""$2"\"",":", $3","}'| sed -e 's/SYS_//g'}
syscalls = {
"syscall" : 0,
"exit" : 1,
"fork" : 2,
"read" : 3,
"write" : 4,
"open" : 5,
"close" : 6,
"compat_50_wait4" : 7,
"compat_43_ocreat" : 8,
"link" : 9,
"unlink" : 10,
"chdir" : 12,
"fchdir" : 13,
"compat_50_mknod" : 14,
"chmod" : 15,
"chown" : 16,
"break" : 17,
"compat_20_getfsstat" : 18,
"compat_43_olseek" : 19,
"getpid" : 20,
"compat_40_mount" : 21,
"unmount" : 22,
"setuid" : 23,
"getuid" : 24,
"geteuid" : 25,
"ptrace" : 26,
"recvmsg" : 27,
"sendmsg" : 28,
"recvfrom" : 29,
"accept" : 30,
"getpeername" : 31,
"getsockname" : 32,
"access" : 33,
"chflags" : 34,
"fchflags" : 35,
"sync" : 36,
"kill" : 37,
"compat_43_stat43" : 38,
"getppid" : 39,
"compat_43_lstat43" : 40,
"dup" : 41,
"pipe" : 42,
"getegid" : 43,
"profil" : 44,
"ktrace" : 45,
"compat_13_sigaction13" : 46,
"getgid" : 47,
"compat_13_sigprocmask13" : 48,
"__getlogin" : 49,
"__setlogin" : 50,
"acct" : 51,
"compat_13_sigpending13" : 52,
"compat_13_sigaltstack13" : 53,
"ioctl" : 54,
"compat_12_oreboot" : 55,
"revoke" : 56,
"symlink" : 57,
"readlink" : 58,
"execve" : 59,
"umask" : 60,
"chroot" : 61,
"compat_43_fstat43" : 62,
"compat_43_ogetkerninfo" : 63,
"compat_43_ogetpagesize" : 64,
"compat_12_msync" : 65,
"vfork" : 66,
"sbrk" : 69,
"sstk" : 70,
"compat_43_ommap" : 71,
"vadvise" : 72,
"munmap" : 73,
"mprotect" : 74,
"madvise" : 75,
"mincore" : 78,
"getgroups" : 79,
"setgroups" : 80,
"getpgrp" : 81,
"setpgid" : 82,
"compat_50_setitimer" : 83,
"compat_43_owait" : 84,
"compat_12_oswapon" : 85,
"compat_50_getitimer" : 86,
"compat_43_ogethostname" : 87,
"compat_43_osethostname" : 88,
"compat_43_ogetdtablesize" : 89,
"dup2" : 90,
"fcntl" : 92,
"compat_50_select" : 93,
"fsync" : 95,
"setpriority" : 96,
"compat_30_socket" : 97,
"connect" : 98,
"compat_43_oaccept" : 99,
"getpriority" : 100,
"compat_43_osend" : 101,
"compat_43_orecv" : 102,
"compat_13_sigreturn13" : 103,
"bind" : 104,
"setsockopt" : 105,
"listen" : 106,
"compat_43_osigvec" : 108,
"compat_43_osigblock" : 109,
"compat_43_osigsetmask" : 110,
"compat_13_sigsuspend13" : 111,
"compat_43_osigstack" : 112,
"compat_43_orecvmsg" : 113,
"compat_43_osendmsg" : 114,
"compat_50_gettimeofday" : 116,
"compat_50_getrusage" : 117,
"getsockopt" : 118,
"readv" : 120,
"writev" : 121,
"compat_50_settimeofday" : 122,
"fchown" : 123,
"fchmod" : 124,
"compat_43_orecvfrom" : 125,
"setreuid" : 126,
"setregid" : 127,
"rename" : 128,
"compat_43_otruncate" : 129,
"compat_43_oftruncate" : 130,
"flock" : 131,
"mkfifo" : 132,
"sendto" : 133,
"shutdown" : 134,
"socketpair" : 135,
"mkdir" : 136,
"rmdir" : 137,
"compat_50_utimes" : 138,
"compat_50_adjtime" : 140,
"compat_43_ogetpeername" : 141,
"compat_43_ogethostid" : 142,
"compat_43_osethostid" : 143,
"compat_43_ogetrlimit" : 144,
"compat_43_osetrlimit" : 145,
"compat_43_okillpg" : 146,
"setsid" : 147,
"compat_50_quotactl" : 148,
"compat_43_oquota" : 149,
"compat_43_ogetsockname" : 150,
"nfssvc" : 155,
"compat_43_ogetdirentries" : 156,
"compat_20_statfs" : 157,
"compat_20_fstatfs" : 158,
"compat_30_getfh" : 161,
"compat_09_ogetdomainname" : 162,
"compat_09_osetdomainname" : 163,
"compat_09_ouname" : 164,
"sysarch" : 165,
"compat_10_osemsys" : 169,
"compat_10_omsgsys" : 170,
"compat_10_oshmsys" : 171,
"pread" : 173,
"pwrite" : 174,
"compat_30_ntp_gettime" : 175,
"ntp_adjtime" : 176,
"setgid" : 181,
"setegid" : 182,
"seteuid" : 183,
"lfs_bmapv" : 184,
"lfs_markv" : 185,
"lfs_segclean" : 186,
"compat_50_lfs_segwait" : 187,
"compat_12_stat12" : 188,
"compat_12_fstat12" : 189,
"compat_12_lstat12" : 190,
"pathconf" : 191,
"fpathconf" : 192,
"getrlimit" : 194,
"setrlimit" : 195,
"compat_12_getdirentries" : 196,
"mmap" : 197,
"__syscall" : 198,
"lseek" : 199,
"truncate" : 200,
"ftruncate" : 201,
"__sysctl" : 202,
"mlock" : 203,
"munlock" : 204,
"undelete" : 205,
"compat_50_futimes" : 206,
"getpgid" : 207,
"reboot" : 208,
"poll" : 209,
"compat_14___semctl" : 220,
"semget" : 221,
"semop" : 222,
"semconfig" : 223,
"compat_14_msgctl" : 224,
"msgget" : 225,
"msgsnd" : 226,
"msgrcv" : 227,
"shmat" : 228,
"compat_14_shmctl" : 229,
"shmdt" : 230,
"shmget" : 231,
"compat_50_clock_gettime" : 232,
"compat_50_clock_settime" : 233,
"compat_50_clock_getres" : 234,
"timer_create" : 235,
"timer_delete" : 236,
"compat_50_timer_settime" : 237,
"compat_50_timer_gettime" : 238,
"timer_getoverrun" : 239,
"compat_50_nanosleep" : 240,
"fdatasync" : 241,
"mlockall" : 242,
"munlockall" : 243,
"compat_50___sigtimedwait" : 244,
"sigqueueinfo" : 245,
"modctl" : 246,
"_ksem_init" : 247,
"_ksem_open" : 248,
"_ksem_unlink" : 249,
"_ksem_close" : 250,
"_ksem_post" : 251,
"_ksem_wait" : 252,
"_ksem_trywait" : 253,
"_ksem_getvalue" : 254,
"_ksem_destroy" : 255,
"mq_open" : 257,
"mq_close" : 258,
"mq_unlink" : 259,
"mq_getattr" : 260,
"mq_setattr" : 261,
"mq_notify" : 262,
"mq_send" : 263,
"mq_receive" : 264,
"compat_50_mq_timedsend" : 265,
"compat_50_mq_timedreceive" : 266,
"__posix_rename" : 270,
"swapctl" : 271,
"compat_30_getdents" : 272,
"minherit" : 273,
"lchmod" : 274,
"lchown" : 275,
"compat_50_lutimes" : 276,
"__msync13" : 277,
"compat_30___stat13" : 278,
"compat_30___fstat13" : 279,
"compat_30___lstat13" : 280,
"__sigaltstack14" : 281,
"__vfork14" : 282,
"__posix_chown" : 283,
"__posix_fchown" : 284,
"__posix_lchown" : 285,
"getsid" : 286,
"__clone" : 287,
"fktrace" : 288,
"preadv" : 289,
"pwritev" : 290,
"compat_16___sigaction14" : 291,
"__sigpending14" : 292,
"__sigprocmask14" : 293,
"__sigsuspend14" : 294,
"compat_16___sigreturn14" : 295,
"__getcwd" : 296,
"fchroot" : 297,
"compat_30_fhopen" : 298,
"compat_30_fhstat" : 299,
"compat_20_fhstatfs" : 300,
"compat_50_____semctl13" : 301,
"compat_50___msgctl13" : 302,
"compat_50___shmctl13" : 303,
"lchflags" : 304,
"issetugid" : 305,
"utrace" : 306,
"getcontext" : 307,
"setcontext" : 308,
"_lwp_create" : 309,
"_lwp_exit" : 310,
"_lwp_self" : 311,
"_lwp_wait" : 312,
"_lwp_suspend" : 313,
"_lwp_continue" : 314,
"_lwp_wakeup" : 315,
"_lwp_getprivate" : 316,
"_lwp_setprivate" : 317,
"_lwp_kill" : 318,
"_lwp_detach" : 319,
"compat_50__lwp_park" : 320,
"_lwp_unpark" : 321,
"_lwp_unpark_all" : 322,
"_lwp_setname" : 323,
"_lwp_getname" : 324,
"_lwp_ctl" : 325,
"sa_register" : 330,
"sa_stacks" : 331,
"sa_enable" : 332,
"sa_setconcurrency" : 333,
"sa_yield" : 334,
"sa_preempt" : 335,
"__sigaction_sigtramp" : 340,
"pmc_get_info" : 341,
"pmc_control" : 342,
"rasctl" : 343,
"kqueue" : 344,
"compat_50_kevent" : 345,
"_sched_setparam" : 346,
"_sched_getparam" : 347,
"_sched_setaffinity" : 348,
"_sched_getaffinity" : 349,
"sched_yield" : 350,
"fsync_range" : 354,
"uuidgen" : 355,
"getvfsstat" : 356,
"statvfs1" : 357,
"fstatvfs1" : 358,
"compat_30_fhstatvfs1" : 359,
"extattrctl" : 360,
"extattr_set_file" : 361,
"extattr_get_file" : 362,
"extattr_delete_file" : 363,
"extattr_set_fd" : 364,
"extattr_get_fd" : 365,
"extattr_delete_fd" : 366,
"extattr_set_link" : 367,
"extattr_get_link" : 368,
"extattr_delete_link" : 369,
"extattr_list_fd" : 370,
"extattr_list_file" : 371,
"extattr_list_link" : 372,
"compat_50_pselect" : 373,
"compat_50_pollts" : 374,
"setxattr" : 375,
"lsetxattr" : 376,
"fsetxattr" : 377,
"getxattr" : 378,
"lgetxattr" : 379,
"fgetxattr" : 380,
"listxattr" : 381,
"llistxattr" : 382,
"flistxattr" : 383,
"removexattr" : 384,
"lremovexattr" : 385,
"fremovexattr" : 386,
"compat_50___stat30" : 387,
"compat_50___fstat30" : 388,
"compat_50___lstat30" : 389,
"__getdents30" : 390,
"compat_30___fhstat30" : 392,
"compat_50___ntp_gettime30" : 393,
"__socket30" : 394,
"__getfh30" : 395,
"__fhopen40" : 396,
"__fhstatvfs140" : 397,
"compat_50___fhstat40" : 398,
"aio_cancel" : 399,
"aio_error" : 400,
"aio_fsync" : 401,
"aio_read" : 402,
"aio_return" : 403,
"compat_50_aio_suspend" : 404,
"aio_write" : 405,
"lio_listio" : 406,
"__mount50" : 410,
"mremap" : 411,
"pset_create" : 412,
"pset_destroy" : 413,
"pset_assign" : 414,
"_pset_bind" : 415,
"__posix_fadvise50" : 416,
"__select50" : 417,
"__gettimeofday50" : 418,
"__settimeofday50" : 419,
"__utimes50" : 420,
"__adjtime50" : 421,
"__lfs_segwait50" : 422,
"__futimes50" : 423,
"__lutimes50" : 424,
"__setitimer50" : 425,
"__getitimer50" : 426,
"__clock_gettime50" : 427,
"__clock_settime50" : 428,
"__clock_getres50" : 429,
"__nanosleep50" : 430,
"____sigtimedwait50" : 431,
"__mq_timedsend50" : 432,
"__mq_timedreceive50" : 433,
"___lwp_park50" : 434,
"__kevent50" : 435,
"__pselect50" : 436,
"__pollts50" : 437,
"__aio_suspend50" : 438,
"__stat50" : 439,
"__fstat50" : 440,
"__lstat50" : 441,
"____semctl50" : 442,
"__shmctl50" : 443,
"__msgctl50" : 444,
"__getrusage50" : 445,
"__timer_settime50" : 446,
"__timer_gettime50" : 447,
"__ntp_gettime50" : 448,
"__wait450" : 449,
"__mknod50" : 450,
"__fhstat50" : 451,
"__quotactl50" : 452,
"MAXSYSCALL" : 453,
"NSYSENT" : 512,
}
