# SPDX-License-Identifier: GPL-2.0
# Copyright (c) 2019 Blu Wireless Technology

"""
Incomplete schema for NL80211 commands

This just defines enough of the attributes to test this library's basic
functionality. You may need to add more attributes to the schema for your own
purposes (please send a PR if you do!).

    https://elixir.bootlin.com/linux/latest/source/include/uapi/linux/nl80211.h
    https://elixir.bootlin.com/linux/latest/source/net/wireless/nl80211.c
"""

from . import NlAttrSchema


nl80211_constants = {
    "NL80211_CMD_GET_WIPHY": 1,
    "NL80211_CMD_GET_INTERFACE": 5,
    "NL80211_ATTR_WIPHY": 1,
    "NL80211_ATTR_WIPHY_NAME": 2,
    "NL80211_ATTR_IFINDEX": 3,
    "NL80211_ATTR_IFNAME": 4,
    "NL80211_ATTR_IFTYPE": 5,
    "NL80211_ATTR_MAC": 6,
    "NL80211_ATTR_KEY_DATA": 7,
    "NL80211_ATTR_KEY_IDX": 8,
    "NL80211_ATTR_KEY_CIPHER": 9,
    "NL80211_ATTR_KEY_SEQ": 10,
    "NL80211_ATTR_KEY_DEFAULT": 11,
    "NL80211_ATTR_BEACON_INTERVAL": 12,
    "NL80211_ATTR_DTIM_PERIOD": 13,
    "NL80211_ATTR_BEACON_HEAD": 14,
    "NL80211_ATTR_BEACON_TAIL": 15,
    "NL80211_ATTR_STA_AID": 16,
    "NL80211_ATTR_STA_FLAGS": 17,
    "NL80211_ATTR_STA_LISTEN_INTERVAL": 18,
    "NL80211_ATTR_STA_SUPPORTED_RATES": 19,
    "NL80211_ATTR_STA_VLAN": 20,
    "NL80211_ATTR_STA_INFO": 21,
    "NL80211_ATTR_WIPHY_BANDS": 22,
    "NL80211_ATTR_MNTR_FLAGS": 23,
    "NL80211_ATTR_MESH_ID": 24,
    "NL80211_ATTR_STA_PLINK_ACTION": 25,
    "NL80211_ATTR_MPATH_NEXT_HOP": 26,
    "NL80211_ATTR_MPATH_INFO": 27,
    "NL80211_ATTR_BSS_CTS_PROT": 28,
    "NL80211_ATTR_BSS_SHORT_PREAMBLE": 29,
    "NL80211_ATTR_BSS_SHORT_SLOT_TIME": 30,
    "NL80211_ATTR_HT_CAPABILITY": 31,
    "NL80211_ATTR_SUPPORTED_IFTYPES": 32,
    "NL80211_ATTR_REG_ALPHA2": 33,
    "NL80211_ATTR_REG_RULES": 34,
    "NL80211_ATTR_MESH_CONFIG": 35,
    "NL80211_ATTR_BSS_BASIC_RATES": 36,
    "NL80211_ATTR_WIPHY_TXQ_PARAMS": 37,
    "NL80211_ATTR_WIPHY_FREQ": 38,
    "NL80211_ATTR_WIPHY_CHANNEL_TYPE": 39,
    "NL80211_ATTR_KEY_DEFAULT_MGMT": 40,
    "NL80211_ATTR_MGMT_SUBTYPE": 41,
    "NL80211_ATTR_IE": 42,
    "NL80211_ATTR_MAX_NUM_SCAN_SSIDS": 43,
    "NL80211_ATTR_SCAN_FREQUENCIES": 44,
    "NL80211_ATTR_SCAN_SSIDS": 45,
    "NL80211_ATTR_GENERATION": 46,
    "NL80211_ATTR_BSS": 47,
    "NL80211_ATTR_REG_INITIATOR": 48,
    "NL80211_ATTR_REG_TYPE": 49,
    "NL80211_ATTR_SUPPORTED_COMMANDS": 50,
    "NL80211_ATTR_FRAME": 51,
    "NL80211_ATTR_SSID": 52,
    "NL80211_ATTR_AUTH_TYPE": 53,
    "NL80211_ATTR_REASON_CODE": 54,
    "NL80211_ATTR_KEY_TYPE": 55,
    "NL80211_ATTR_MAX_SCAN_IE_LEN": 56,
    "NL80211_ATTR_CIPHER_SUITES": 57,
    "NL80211_ATTR_FREQ_BEFORE": 58,
    "NL80211_ATTR_FREQ_AFTER": 59,
    "NL80211_ATTR_FREQ_FIXED": 60,
    "NL80211_ATTR_WIPHY_RETRY_SHORT": 61,
    "NL80211_ATTR_WIPHY_RETRY_LONG": 62,
    "NL80211_ATTR_WIPHY_FRAG_THRESHOLD": 63,
    "NL80211_ATTR_WIPHY_RTS_THRESHOLD": 64,
    "NL80211_ATTR_TIMED_OUT": 65,
    "NL80211_ATTR_USE_MFP": 66,
    "NL80211_ATTR_STA_FLAGS2": 67,
    "NL80211_ATTR_CONTROL_PORT": 68,
    "NL80211_ATTR_TESTDATA": 69,
    "NL80211_ATTR_PRIVACY": 70,
    "NL80211_ATTR_DISCONNECTED_BY_AP": 71,
    "NL80211_ATTR_STATUS_CODE": 72,
    "NL80211_ATTR_CIPHER_SUITES_PAIRWISE": 73,
    "NL80211_ATTR_CIPHER_SUITE_GROUP": 74,
    "NL80211_ATTR_WPA_VERSIONS": 75,
    "NL80211_ATTR_AKM_SUITES": 76,
    "NL80211_ATTR_REQ_IE": 77,
    "NL80211_ATTR_RESP_IE": 78,
    "NL80211_ATTR_PREV_BSSID": 79,
    "NL80211_ATTR_KEY": 80,
    "NL80211_ATTR_KEYS": 81,
    "NL80211_ATTR_PID": 82,
    "NL80211_ATTR_4ADDR": 83,
    "NL80211_ATTR_SURVEY_INFO": 84,
    "NL80211_ATTR_PMKID": 85,
    "NL80211_ATTR_MAX_NUM_PMKIDS": 86,
    "NL80211_ATTR_DURATION": 87,
    "NL80211_ATTR_COOKIE": 88,
    "NL80211_ATTR_WIPHY_COVERAGE_CLASS": 89,
    "NL80211_ATTR_TX_RATES": 90,
    "NL80211_ATTR_FRAME_MATCH": 91,
    "NL80211_ATTR_ACK": 92,
    "NL80211_ATTR_PS_STATE": 93,
    "NL80211_ATTR_CQM": 94,
    "NL80211_ATTR_LOCAL_STATE_CHANGE": 95,
    "NL80211_ATTR_AP_ISOLATE": 96,
    "NL80211_ATTR_WIPHY_TX_POWER_SETTING": 97,
    "NL80211_ATTR_WIPHY_TX_POWER_LEVEL": 98,
    "NL80211_ATTR_TX_FRAME_TYPES": 99,
    "NL80211_ATTR_RX_FRAME_TYPES": 100,
    "NL80211_ATTR_FRAME_TYPE": 101,
    "NL80211_ATTR_CONTROL_PORT_ETHERTYPE": 102,
    "NL80211_ATTR_CONTROL_PORT_NO_ENCRYPT": 103,
    "NL80211_ATTR_SUPPORT_IBSS_RSN": 104,
    "NL80211_ATTR_WIPHY_ANTENNA_TX": 105,
    "NL80211_ATTR_WIPHY_ANTENNA_RX": 106,
    "NL80211_ATTR_MCAST_RATE": 107,
    "NL80211_ATTR_OFFCHANNEL_TX_OK": 108,
    "NL80211_ATTR_BSS_HT_OPMODE": 109,
    "NL80211_ATTR_KEY_DEFAULT_TYPES": 110,
    "NL80211_ATTR_MAX_REMAIN_ON_CHANNEL_DURATION": 111,
    "NL80211_ATTR_MESH_SETUP": 112,
    "NL80211_ATTR_WIPHY_ANTENNA_AVAIL_TX": 113,
    "NL80211_ATTR_WIPHY_ANTENNA_AVAIL_RX": 114,
    "NL80211_ATTR_SUPPORT_MESH_AUTH": 115,
    "NL80211_ATTR_STA_PLINK_STATE": 116,
    "NL80211_ATTR_WOWLAN_TRIGGERS": 117,
    "NL80211_ATTR_WOWLAN_TRIGGERS_SUPPORTED": 118,
    "NL80211_ATTR_SCHED_SCAN_INTERVAL": 119,
    "NL80211_ATTR_INTERFACE_COMBINATIONS": 120,
    "NL80211_ATTR_SOFTWARE_IFTYPES": 121,
    "NL80211_ATTR_REKEY_DATA": 122,
    "NL80211_ATTR_MAX_NUM_SCHED_SCAN_SSIDS": 123,
    "NL80211_ATTR_MAX_SCHED_SCAN_IE_LEN": 124,
    "NL80211_ATTR_SCAN_SUPP_RATES": 125,
    "NL80211_ATTR_HIDDEN_SSID": 126,
    "NL80211_ATTR_IE_PROBE_RESP": 127,
    "NL80211_ATTR_IE_ASSOC_RESP": 128,
    "NL80211_ATTR_STA_WME": 129,
    "NL80211_ATTR_SUPPORT_AP_UAPSD": 130,
    "NL80211_ATTR_ROAM_SUPPORT": 131,
    "NL80211_ATTR_SCHED_SCAN_MATCH": 132,
    "NL80211_ATTR_MAX_MATCH_SETS": 133,
    "NL80211_ATTR_PMKSA_CANDIDATE": 134,
    "NL80211_ATTR_TX_NO_CCK_RATE": 135,
    "NL80211_ATTR_TDLS_ACTION": 136,
    "NL80211_ATTR_TDLS_DIALOG_TOKEN": 137,
    "NL80211_ATTR_TDLS_OPERATION": 138,
    "NL80211_ATTR_TDLS_SUPPORT": 139,
    "NL80211_ATTR_TDLS_EXTERNAL_SETUP": 140,
    "NL80211_ATTR_DEVICE_AP_SME": 141,
    "NL80211_ATTR_DONT_WAIT_FOR_ACK": 142,
    "NL80211_ATTR_FEATURE_FLAGS": 143,
    "NL80211_ATTR_PROBE_RESP_OFFLOAD": 144,
    "NL80211_ATTR_PROBE_RESP": 145,
    "NL80211_ATTR_DFS_REGION": 146,
    "NL80211_ATTR_DISABLE_HT": 147,
    "NL80211_ATTR_HT_CAPABILITY_MASK": 148,
    "NL80211_ATTR_NOACK_MAP": 149,
    "NL80211_ATTR_INACTIVITY_TIMEOUT": 150,
    "NL80211_ATTR_RX_SIGNAL_DBM": 151,
    "NL80211_ATTR_BG_SCAN_PERIOD": 152,
    "NL80211_ATTR_WDEV": 153,
    "NL80211_ATTR_USER_REG_HINT_TYPE": 154,
    "NL80211_ATTR_CONN_FAILED_REASON": 155,
    "NL80211_ATTR_AUTH_DATA": 156,
    "NL80211_ATTR_VHT_CAPABILITY": 157,
    "NL80211_ATTR_SCAN_FLAGS": 158,
    "NL80211_ATTR_CHANNEL_WIDTH": 159,
    "NL80211_ATTR_CENTER_FREQ1": 160,
    "NL80211_ATTR_CENTER_FREQ2": 161,
    "NL80211_ATTR_P2P_CTWINDOW": 162,
    "NL80211_ATTR_P2P_OPPPS": 163,
    "NL80211_ATTR_LOCAL_MESH_POWER_MODE": 164,
    "NL80211_ATTR_ACL_POLICY": 165,
    "NL80211_ATTR_MAC_ADDRS": 166,
    "NL80211_ATTR_MAC_ACL_MAX": 167,
    "NL80211_ATTR_RADAR_EVENT": 168,
    "NL80211_ATTR_EXT_CAPA": 169,
    "NL80211_ATTR_EXT_CAPA_MASK": 170,
    "NL80211_ATTR_STA_CAPABILITY": 171,
    "NL80211_ATTR_STA_EXT_CAPABILITY": 172,
    "NL80211_ATTR_PROTOCOL_FEATURES": 173,
    "NL80211_ATTR_SPLIT_WIPHY_DUMP": 174,
    "NL80211_ATTR_DISABLE_VHT": 175,
    "NL80211_ATTR_VHT_CAPABILITY_MASK": 176,
    "NL80211_ATTR_MDID": 177,
    "NL80211_ATTR_IE_RIC": 178,
    "NL80211_ATTR_CRIT_PROT_ID": 179,
    "NL80211_ATTR_MAX_CRIT_PROT_DURATION": 180,
    "NL80211_ATTR_PEER_AID": 181,
    "NL80211_ATTR_COALESCE_RULE": 182,
    "NL80211_ATTR_CH_SWITCH_COUNT": 183,
    "NL80211_ATTR_CH_SWITCH_BLOCK_TX": 184,
    "NL80211_ATTR_CSA_IES": 185,
    "NL80211_ATTR_CSA_C_OFF_BEACON": 186,
    "NL80211_ATTR_CSA_C_OFF_PRESP": 187,
    "NL80211_ATTR_RXMGMT_FLAGS": 188,
    "NL80211_ATTR_STA_SUPPORTED_CHANNELS": 189,
    "NL80211_ATTR_STA_SUPPORTED_OPER_CLASSES": 190,
    "NL80211_ATTR_HANDLE_DFS": 191,
    "NL80211_ATTR_SUPPORT_5_MHZ": 192,
    "NL80211_ATTR_SUPPORT_10_MHZ": 193,
    "NL80211_ATTR_OPMODE_NOTIF": 194,
    "NL80211_ATTR_VENDOR_ID": 195,
    "NL80211_ATTR_VENDOR_SUBCMD": 196,
    "NL80211_ATTR_VENDOR_DATA": 197,
    "NL80211_ATTR_VENDOR_EVENTS": 198,
    "NL80211_ATTR_QOS_MAP": 199,
    "NL80211_ATTR_MAC_HINT": 200,
    "NL80211_ATTR_WIPHY_FREQ_HINT": 201,
    "NL80211_ATTR_MAX_AP_ASSOC_STA": 202,
    "NL80211_ATTR_TDLS_PEER_CAPABILITY": 203,
    "NL80211_ATTR_SOCKET_OWNER": 204,
    "NL80211_ATTR_CSA_C_OFFSETS_TX": 205,
    "NL80211_ATTR_MAX_CSA_COUNTERS": 206,
    "NL80211_ATTR_TDLS_INITIATOR": 207,
    "NL80211_ATTR_USE_RRM": 208,
    "NL80211_ATTR_WIPHY_DYN_ACK": 209,
    "NL80211_ATTR_TSID": 210,
    "NL80211_ATTR_USER_PRIO": 211,
    "NL80211_ATTR_ADMITTED_TIME": 212,
    "NL80211_ATTR_SMPS_MODE": 213,
    "NL80211_ATTR_OPER_CLASS": 214,
    "NL80211_ATTR_MAC_MASK": 215,
    "NL80211_ATTR_WIPHY_SELF_MANAGED_REG": 216,
    "NL80211_ATTR_EXT_FEATURES": 217,
    "NL80211_ATTR_SURVEY_RADIO_STATS": 218,
    "NL80211_ATTR_NETNS_FD": 219,
    "NL80211_ATTR_SCHED_SCAN_DELAY": 220,
    "NL80211_ATTR_REG_INDOOR": 221,
    "NL80211_ATTR_MAX_NUM_SCHED_SCAN_PLANS": 222,
    "NL80211_ATTR_MAX_SCAN_PLAN_INTERVAL": 223,
    "NL80211_ATTR_MAX_SCAN_PLAN_ITERATIONS": 224,
    "NL80211_ATTR_SCHED_SCAN_PLANS": 225,
    "NL80211_ATTR_PBSS": 226,
    "NL80211_ATTR_BSS_SELECT": 227,
    "NL80211_ATTR_STA_SUPPORT_P2P_PS": 228,
    "NL80211_ATTR_PAD": 229,
    "NL80211_ATTR_IFTYPE_EXT_CAPA": 230,
    "NL80211_ATTR_MU_MIMO_GROUP_DATA": 231,
    "NL80211_ATTR_MU_MIMO_FOLLOW_MAC_ADDR": 232,
    "NL80211_ATTR_SCAN_START_TIME_TSF": 233,
    "NL80211_ATTR_SCAN_START_TIME_TSF_BSSID": 234,
    "NL80211_ATTR_MEASUREMENT_DURATION": 235,
    "NL80211_ATTR_MEASUREMENT_DURATION_MANDATORY": 236,
    "NL80211_ATTR_MESH_PEER_AID": 237,
    "NL80211_ATTR_NAN_MASTER_PREF": 238,
    "NL80211_ATTR_BANDS": 239,
    "NL80211_ATTR_NAN_FUNC": 240,
    "NL80211_ATTR_NAN_MATCH": 241,
    "NL80211_ATTR_FILS_KEK": 242,
    "NL80211_ATTR_FILS_NONCES": 243,
    "NL80211_ATTR_MULTICAST_TO_UNICAST_ENABLED": 244,
    "NL80211_ATTR_BSSID": 245,
    "NL80211_ATTR_SCHED_SCAN_RELATIVE_RSSI": 246,
    "NL80211_ATTR_SCHED_SCAN_RSSI_ADJUST": 247,
    "NL80211_ATTR_TIMEOUT_REASON": 248,
    "NL80211_ATTR_FILS_ERP_USERNAME": 249,
    "NL80211_ATTR_FILS_ERP_REALM": 250,
    "NL80211_ATTR_FILS_ERP_NEXT_SEQ_NUM": 251,
    "NL80211_ATTR_FILS_ERP_RRK": 252,
    "NL80211_ATTR_FILS_CACHE_ID": 253,
    "NL80211_ATTR_PMK": 254,
    "NL80211_ATTR_SCHED_SCAN_MULTI": 255,
    "NL80211_ATTR_SCHED_SCAN_MAX_REQS": 256,
    "NL80211_ATTR_WANT_1X_4WAY_HS": 257,
    "NL80211_ATTR_PMKR0_NAME": 258,
    "NL80211_ATTR_PORT_AUTHORIZED": 259,

    "NL80211_BSS_BSSID": 1,
    "NL80211_BSS_FREQUENCY": 2,
    "NL80211_BSS_TSF": 3,
    "NL80211_BSS_BEACON_INTERVAL": 4,
    "NL80211_BSS_CAPABILITY": 5,
    "NL80211_BSS_INFORMATION_ELEMENTS": 6,
    "NL80211_BSS_SIGNAL_MBM": 7,
    "NL80211_BSS_SIGNAL_UNSPEC": 8,
    "NL80211_BSS_STATUS": 9,
    "NL80211_BSS_SEEN_MS_AGO": 10,
    "NL80211_BSS_BEACON_IES": 11,
    "NL80211_BSS_CHAN_WIDTH": 12,
    "NL80211_BSS_BEACON_TSF": 13,
    "NL80211_BSS_PRESP_DATA": 14,
    "NL80211_BSS_LAST_SEEN_BOOTTIME": 15,
    "NL80211_BSS_PAD": 16,
    "NL80211_BSS_PARENT_TSF": 17,
    "NL80211_BSS_PARENT_BSSID": 18,

    "NL80211_KEY_DATA": 1,
    "NL80211_KEY_IDX": 2,
    "NL80211_KEY_CIPHER": 3,
    "NL80211_KEY_SEQ": 4,
    "NL80211_KEY_DEFAULT": 5,
    "NL80211_KEY_DEFAULT_MGMT": 6,
    "NL80211_KEY_TYPE": 7,
    "NL80211_KEY_DEFAULT_TYPES": 8,

    "NL80211_IFACE_COMB_LIMITS": 1,
    "NL80211_IFACE_COMB_MAXNUM": 2,
    "NL80211_IFACE_COMB_STA_AP_BI_MATCH": 3,
    "NL80211_IFACE_COMB_NUM_CHANNELS": 4,
    "NL80211_IFACE_COMB_RADAR_DETECT_WIDTHS": 5,
    "NL80211_IFACE_COMB_RADAR_DETECT_REGIONS": 6,
    "NL80211_IFACE_COMB_BI_MIN_GCD": 7,

    "NL80211_IFACE_LIMIT_MAX": 1,
    "NL80211_IFACE_LIMIT_TYPES": 2,

    "NL80211_BAND_ATTR_FREQS": 1,
    "NL80211_BAND_ATTR_RATES": 2,
    "NL80211_BAND_ATTR_HT_MCS_SET": 3,
    "NL80211_BAND_ATTR_HT_CAPA": 4,
    "NL80211_BAND_ATTR_HT_AMPDU_FACTOR": 5,
    "NL80211_BAND_ATTR_HT_AMPDU_DENSITY": 6,
    "NL80211_BAND_ATTR_VHT_MCS_SET": 7,
    "NL80211_BAND_ATTR_VHT_CAPA": 8,
    "NL80211_BAND_ATTR_IFTYPE_DATA": 9,

    "NL80211_BAND_IFTYPE_ATTR_IFTYPES": 1,
    "NL80211_BAND_IFTYPE_ATTR_HE_CAP_MAC": 2,
    "NL80211_BAND_IFTYPE_ATTR_HE_CAP_PHY": 3,
    "NL80211_BAND_IFTYPE_ATTR_HE_CAP_MCS_SET": 4,
    "NL80211_BAND_IFTYPE_ATTR_HE_CAP_PPE": 5,

    "NL80211_BITRATE_ATTR_RATE": 1,
    "NL80211_BITRATE_ATTR_2GHZ_SHORTPREAMBLE": 2,


    "NL80211_FREQUENCY_ATTR_FREQ": 1,
    "NL80211_FREQUENCY_ATTR_DISABLED": 2,
    "NL80211_FREQUENCY_ATTR_NO_IR": 3,
    "__NL80211_FREQUENCY_ATTR_NO_IBSS": 4,
    "NL80211_FREQUENCY_ATTR_RADAR": 5,
    "NL80211_FREQUENCY_ATTR_MAX_TX_POWER": 6,
    "NL80211_FREQUENCY_ATTR_DFS_STATE": 7,
    "NL80211_FREQUENCY_ATTR_DFS_TIME": 8,
    "NL80211_FREQUENCY_ATTR_NO_HT40_MINUS": 9,
    "NL80211_FREQUENCY_ATTR_NO_HT40_PLUS": 10,
    "NL80211_FREQUENCY_ATTR_NO_80MHZ": 11,
    "NL80211_FREQUENCY_ATTR_NO_160MHZ": 12,
    "NL80211_FREQUENCY_ATTR_DFS_CAC_TIME": 13,
    "NL80211_FREQUENCY_ATTR_INDOOR_ONLY": 14,
    "NL80211_FREQUENCY_ATTR_IR_CONCURRENT": 15,
    "NL80211_FREQUENCY_ATTR_NO_20MHZ": 16,
    "NL80211_FREQUENCY_ATTR_NO_10MHZ": 17,
    "NL80211_FREQUENCY_ATTR_WMM": 18,
}
globals().update(nl80211_constants)


nl80211_spec = [
    {
        "name": "NL80211_ATTR_WIPHY",
        "type": "u32",
    },
    {
        "name": "NL80211_ATTR_IFNAME",
        "type": "str",
    },
    {
        "name": "NL80211_ATTR_IFTYPE",
        "type": "u32",
    },
    {
        "name": "NL80211_ATTR_WIPHY",
        "type": "u32",
    },
    {
        "name": "NL80211_ATTR_MAC",
        "type": "bytes",
    },
    {
        "name": "NL80211_ATTR_IFINDEX",
        "type": "u32"
    },
    {
        "name": "NL80211_ATTR_GENERATION",
        "type": "u32"
    },
    {
        "name": "NL80211_ATTR_WIPHY_CHANNEL_TYPE",
        "type": "u32"
    },
    {
        "name": "NL80211_ATTR_CHANNEL_WIDTH",
        "type": "u32"
    },
    {
        "name": "NL80211_ATTR_CENTER_FREQ1",
        "type": "u32"
    },
    {
        "name": "NL80211_ATTR_WIPHY_TX_POWER_LEVEL",
        "type": "u32"
    },
    {
        "name": "NL80211_ATTR_WIPHY_FREQ",
        "type": "u32"
    },
    {
        "name": "NL80211_ATTR_VENDOR_ID",
        "type": "u32"
    },
    {
        "name": "NL80211_ATTR_VENDOR_SUBCMD",
        "type": "u32",
    },
    {
        "name": "NL80211_ATTR_VENDOR_DATA",
        "type": "bytes",
    },
    {
        "name": "NL80211_ATTR_WDEV",
        "type": "u64",
    },
    {
        "name": "NL80211_ATTR_WIPHY_NAME",
        "type": "str",
    },
    {
        "name": "NL80211_ATTR_SSID",
        "type": "str",
    },
    {
        "name": "NL80211_ATTR_WIPHY_RETRY_SHORT",
        "type": "u8",
    },
    {
        "name": "NL80211_ATTR_NOACK_MAP",
        "type": "u16",
    },
    {
        "name": "NL80211_ATTR_CIPHER_SUITES",
        "type": "array",
        "subelem_type": "u32",
    },
    {
        "name": "NL80211_ATTR_SUPPORTED_COMMANDS",
        "type": "list",
        "subelem_type": "u32",
    },
    {
        "name": "NL80211_ATTR_STA_SUPPORTED_RATES",
        "type": "array",
        "subelem_type": "u8",
    },
    {
        "name": "NL80211_ATTR_IFTYPE_EXT_CAPA",
        "type": "list",
        "subelem_type": [
            {
                "name": "NL80211_ATTR_IFTYPE",
                "type": "u32",
            },
            {
                "name": "NL80211_ATTR_EXT_CAPA",
                "type": "bytes",
            },
            {
                "name": "NL80211_ATTR_EXT_CAPA_MASK",
                "type": "bytes"
            }
        ]
    },
    {
        "name": "NL80211_ATTR_KEY",
        "type": [
            {
                "name": "NL80211_KEY_DEFAULT",
                "type": "flag",
            },
            {
                "name": "NL80211_KEY_IDX",
                "type": "u8",
            },
        ]
    },
    {
        "name": "NL80211_ATTR_SUPPORTED_IFTYPES",
        "type": "flags"
    },
    {
        "name": "NL80211_ATTR_WIPHY_RETRY_LONG",
        "type": "u8"
    },
    {
        "name": "NL80211_ATTR_WIPHY_FRAG_THRESHOLD",
        "type": "u32"
    },
    {
        "name": "NL80211_ATTR_WIPHY_RTS_THRESHOLD",
        "type": "u32"
    },
    {
        "name": "NL80211_ATTR_WIPHY_COVERAGE_CLASS",
        "type": "u8"
    },
    {
        "name": "NL80211_ATTR_MAX_NUM_SCAN_SSIDS",
        "type": "u8"
    },
    {
        "name": "NL80211_ATTR_MAX_SCAN_IE_LEN",
        "type": "u16"
    },
    {
        "name": "NL80211_ATTR_MAX_MATCH_SETS",
        "type": "u8"
    },
    {
        "name": "NL80211_ATTR_MAX_SCAN_PLAN_INTERVAL",
        "type": "u32"
    },
    {
        "name": "NL80211_ATTR_MAX_SCAN_PLAN_ITERATIONS",
        "type": "u32"
    },
    {
        "name": "NL80211_ATTR_SUPPORT_IBSS_RSN",
        "type": "flag"
    },
    {
        "name": "NL80211_ATTR_SUPPORT_AP_UAPSD",
        "type": "flag"
    },
    {
        "name": "NL80211_ATTR_TDLS_SUPPORT",
        "type": "flag"
    },
    {
        "name": "NL80211_ATTR_MAX_NUM_PMKIDS",
        "type": "u8"
    },
    {
        "name": "NL80211_ATTR_WIPHY_ANTENNA_AVAIL_TX",
        "type": "u32"
    },
    {
        "name": "NL80211_ATTR_WIPHY_BANDS",
        "type": "list",
        "subelem_type": [
            {
                "name": "NL80211_BAND_ATTR_FREQS",
                "type": "list",
                "subelem_type": [
                    {
                        "name": "NL80211_FREQUENCY_ATTR_FREQ",
                        "type": "u32"
                    },
                    {
                        "name": "NL80211_FREQUENCY_ATTR_DISABLED",
                        "type": "flag"
                    },
                    {
                        "name": "NL80211_FREQUENCY_ATTR_NO_IR",
                        "type": "flag"
                    },
                    {
                        "name": "NL80211_FREQUENCY_ATTR_RADAR",
                        "type": "flag"
                    },
                    {
                        "name": "NL80211_FREQUENCY_ATTR_MAX_TX_POWER",
                        "type": "u32"
                    },
                    {
                        "name": "NL80211_FREQUENCY_ATTR_DFS_STATE",
                        "type": "u32"
                    },
                    {
                        "name": "NL80211_FREQUENCY_ATTR_DFS_TIME",
                        "type": "u32"
                    },
                    {
                        "name": "NL80211_FREQUENCY_ATTR_NO_HT40_MINUS",
                        "type": "flag"
                    },
                    {
                        "name": "NL80211_FREQUENCY_ATTR_NO_HT40_PLUS",
                        "type": "flag"
                    },
                    {
                        "name": "NL80211_FREQUENCY_ATTR_NO_80MHZ",
                        "type": "flag"
                    },
                    {
                        "name": "NL80211_FREQUENCY_ATTR_NO_160MHZ",
                        "type": "flag"
                    },
                    {
                        "name": "NL80211_FREQUENCY_ATTR_DFS_CAC_TIME",
                        "type": "u32"
                    },
                    {
                        "name": "NL80211_FREQUENCY_ATTR_INDOOR_ONLY",
                        "type": "flag"
                    },
                    {
                        "name": "NL80211_FREQUENCY_ATTR_IR_CONCURRENT",
                        "type": "flag"
                    },
                    {
                        "name": "NL80211_FREQUENCY_ATTR_NO_20MHZ",
                        "type": "flag"
                    },
                    {
                        "name": "NL80211_FREQUENCY_ATTR_NO_10MHZ",
                        "type": "flag"
                    },
                    {
                        "name": "NL80211_FREQUENCY_ATTR_WMM",
                        "type": "u32"
                    },
                ]
            },
            {
                "name": "NL80211_BAND_ATTR_HT_MCS_SET",
                "type": "bytes"  # 16-byte structure
            },
            {
                "name": "NL80211_BAND_ATTR_HT_CAPA",
                "type": "u16"
            },
            {
                "name": "NL80211_BAND_ATTR_HT_AMPDU_FACTOR",
                "type": "u8"
            },
            {
                "name": "NL80211_BAND_ATTR_HT_AMPDU_DENSITY",
                "type": "u8"
            },
            {
                "name": "NL80211_BAND_ATTR_VHT_MCS_SET",
                "type": "bytes"  # 32-byte structure
            },
            {
                "name": "NL80211_BAND_ATTR_VHT_CAPA",
                "type": "bytes"  # From 802.11 IE structure
            },
            {
                "name": "NL80211_BAND_ATTR_IFTYPE_DATA",
                "type": "list",
                "subelem_type": [
                    {
                        "name": "NL80211_BAND_IFTYPE_ATTR_IFTYPES",
                        "type": "flags"
                    },
                    {
                        "name": "NL80211_BAND_IFTYPE_ATTR_HE_CAP_MAC",
                        "type": "bytes"
                    },
                    {
                        "name": "NL80211_BAND_IFTYPE_ATTR_HE_CAP_PHY",
                        "type": "bytes"
                    },
                    {
                        "name": "NL80211_BAND_IFTYPE_ATTR_HE_CAP_MCS_SET",
                        "type": "bytes"
                    },
                    {
                        "name": "NL80211_BAND_IFTYPE_ATTR_HE_CAP_PPE",
                        "type": "bytes"
                    },
                ]
            },
            {
                "name": "NL80211_BAND_ATTR_RATES",
                # TODO these start from 0!
                "type": "list",
                "subelem_type": [
                    {
                        "name": "NL80211_BITRATE_ATTR_RATE",
                        "type": "u32"
                    },
                    {
                        "name": "NL80211_BITRATE_ATTR_2GHZ_SHORTPREAMBLE",
                        "type": "flag"
                    }
                ]
            }
        ]
    },
    {
        "name": "NL80211_ATTR_MAX_REMAIN_ON_CHANNEL_DURATION",
        "type": "u32",
    },
    {
        "name": "NL80211_ATTR_OFFCHANNEL_TX_OK",
        "type": "flag",
    },
]
nl80211_schema = NlAttrSchema.from_spec(nl80211_spec, nl80211_constants)
