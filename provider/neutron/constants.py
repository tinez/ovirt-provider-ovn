# Copyright 2018 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#
# Refer to the README and COPYING files for full details of the license

INGRESS_DIRECTION = 'ingress'
EGRESS_DIRECTION = 'egress'

PROTO_NAME_AH = 'ah'
PROTO_NAME_DCCP = 'dccp'
PROTO_NAME_EGP = 'egp'
PROTO_NAME_ESP = 'esp'
PROTO_NAME_GRE = 'gre'
PROTO_NAME_ICMP = 'icmp'
PROTO_NAME_IGMP = 'igmp'
PROTO_NAME_IPIP = 'ipip'
PROTO_NAME_IPV6_ENCAP = 'ipv6-encap'
PROTO_NAME_IPV6_FRAG = 'ipv6-frag'
PROTO_NAME_IPV6_ICMP = 'ipv6-icmp'
PROTO_NAME_IPV6_ICMP_LEGACY = 'icmpv6'
PROTO_NAME_IPV6_NONXT = 'ipv6-nonxt'
PROTO_NAME_IPV6_OPTS = 'ipv6-opts'
PROTO_NAME_IPV6_ROUTE = 'ipv6-route'
PROTO_NAME_OSPF = 'ospf'
PROTO_NAME_PGM = 'pgm'
PROTO_NAME_RSVP = 'rsvp'
PROTO_NAME_SCTP = 'sctp'
PROTO_NAME_TCP = 'tcp'
PROTO_NAME_UDP = 'udp'
PROTO_NAME_UDPLITE = 'udplite'
PROTO_NAME_VRRP = 'vrrp'

PROTO_NUM_AH = 51
PROTO_NUM_DCCP = 33
PROTO_NUM_EGP = 8
PROTO_NUM_ESP = 50
PROTO_NUM_GRE = 47
PROTO_NUM_ICMP = 1
PROTO_NUM_IGMP = 2
PROTO_NUM_IPIP = 4
PROTO_NUM_IPV6_ENCAP = 41
PROTO_NUM_IPV6_FRAG = 44
PROTO_NUM_IPV6_ICMP = 58
PROTO_NUM_IPV6_NONXT = 59
PROTO_NUM_IPV6_OPTS = 60
PROTO_NUM_IPV6_ROUTE = 43
PROTO_NUM_OSPF = 89
PROTO_NUM_PGM = 113
PROTO_NUM_RSVP = 46
PROTO_NUM_SCTP = 132
PROTO_NUM_TCP = 6
PROTO_NUM_UDP = 17
PROTO_NUM_UDPLITE = 136
PROTO_NUM_VRRP = 112

IP_PROTOCOL_MAP = {
    PROTO_NAME_AH: PROTO_NUM_AH,
    PROTO_NAME_DCCP: PROTO_NUM_DCCP,
    PROTO_NAME_EGP: PROTO_NUM_EGP,
    PROTO_NAME_ESP: PROTO_NUM_ESP,
    PROTO_NAME_GRE: PROTO_NUM_GRE,
    PROTO_NAME_ICMP: PROTO_NUM_ICMP,
    PROTO_NAME_IGMP: PROTO_NUM_IGMP,
    PROTO_NAME_IPIP: PROTO_NUM_IPIP,
    PROTO_NAME_IPV6_ENCAP: PROTO_NUM_IPV6_ENCAP,
    PROTO_NAME_IPV6_FRAG: PROTO_NUM_IPV6_FRAG,
    PROTO_NAME_IPV6_ICMP: PROTO_NUM_IPV6_ICMP,
    PROTO_NAME_IPV6_ICMP_LEGACY: PROTO_NUM_IPV6_ICMP,
    PROTO_NAME_IPV6_NONXT: PROTO_NUM_IPV6_NONXT,
    PROTO_NAME_IPV6_OPTS: PROTO_NUM_IPV6_OPTS,
    PROTO_NAME_IPV6_ROUTE: PROTO_NUM_IPV6_ROUTE,
    PROTO_NAME_OSPF: PROTO_NUM_OSPF,
    PROTO_NAME_PGM: PROTO_NUM_PGM,
    PROTO_NAME_RSVP: PROTO_NUM_RSVP,
    PROTO_NAME_SCTP: PROTO_NUM_SCTP,
    PROTO_NAME_TCP: PROTO_NUM_TCP,
    PROTO_NAME_UDP: PROTO_NUM_UDP,
    PROTO_NAME_UDPLITE: PROTO_NUM_UDPLITE,
    PROTO_NAME_VRRP: PROTO_NUM_VRRP
}

PROTOCOL_NAME_TO_NUM_MAP = {
    k: str(v) for k, v in
    IP_PROTOCOL_MAP.items()
}

PROTOCOL_NUM_TO_NAME_MAP = {
    v: k for k, v in
    PROTOCOL_NAME_TO_NUM_MAP.items()
}

API_TO_OVN_DIRECTION_MAPPER = {
    INGRESS_DIRECTION: 'from-lport',
    EGRESS_DIRECTION: 'to-lport'
}

OVN_TO_API_DIRECTION_MAPPER = {
    v: k for k, v in API_TO_OVN_DIRECTION_MAPPER.items()
}

# all allowed transport protocols values as per networking api v2
# both name & protocol number are added to the array
TRANSPORT_PROTOCOLS = (
    PROTO_NAME_TCP,
    PROTO_NAME_UDP,
    PROTO_NAME_SCTP,
    PROTOCOL_NAME_TO_NUM_MAP[PROTO_NAME_TCP],
    PROTOCOL_NAME_TO_NUM_MAP[PROTO_NAME_UDP],
    PROTOCOL_NAME_TO_NUM_MAP[PROTO_NAME_SCTP]
)

# allowed transport protocols as per networking api v2
# both name & protocol number are added to the array
ICMP_PROTOCOLS = (
    PROTO_NAME_ICMP,
    PROTO_NAME_IPV6_ICMP,
    PROTO_NAME_IPV6_ICMP_LEGACY,
    PROTOCOL_NAME_TO_NUM_MAP[PROTO_NAME_ICMP],
    PROTOCOL_NAME_TO_NUM_MAP[PROTO_NAME_IPV6_ICMP],
    PROTOCOL_NAME_TO_NUM_MAP[PROTO_NAME_IPV6_ICMP_LEGACY]
)

# higher priority for ALLOW than for DROP
ACL_ALLOW_PRIORITY = 1001
ACL_DROP_PRIORITY = 1000
