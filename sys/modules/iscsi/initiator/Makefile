# $FreeBSD: danny/iSCSI/2.2/sys/modules/iscsi/initiator/Makefile 506 2009-04-19 14:45:21Z danny $

S=      ${.CURDIR}/../../..
.PATH: $S/dev/iscsi/initiator

KMOD=iscsi_initiator

SRCS=  iscsi.h iscsivar.h
SRCS+= iscsi.c isc_cam.c isc_soc.c isc_sm.c isc_subr.c iscsi_subr.c
SRCS+= opt_cam.h opt_iscsi_initiator.h
SRCS+= bus_if.h device_if.h
#CFLAGS+= -DNO_USE_MBUF
CFLAGS+= -DISCSI_INITIATOR_DEBUG=2
CFLAGS+= -I$S

.include <bsd.kmod.mk>
