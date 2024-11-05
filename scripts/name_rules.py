# Words that should remain uppercase
UPPERCASE_WORDS = {
    "SMK",
    "MM",
    "SK",
    "ILP",
    "SMJKC",
    "JPJ",
    "IPG",
    "KISAS",
    "BTHO",
    "MP",
    "S.K.",
    "S.M.K.",
    "NZX",
    "SJK",
    "SMJK",
    "SMS",
    "MPSJ",
    "NTT",
    "MSC",
    "MSN",
    "MTDC",
    "MPKJ",
    "MPL",
    "KLCC",
    "KM1",
    "KP",
    "KDPN",
    "KWSP",
    "LHDN",
    "LP",
    "MDN",
    "MDKL",
    "MMU",
    "IKBN",
    "SM",
    "PPD",
    "IPD",
    "PPR",
    "MPK",
    "NSK",
    "KTM",
    "LRT",
    "MRT",
    "UITM",
    "KLIA",
    "BSN",
    "CIMB",
    "UOB",
    "MPS",
    "MBSJ",
    "KDU",
    "RTM",
    "SOGO",
    "KPJ",
    "SRJKC",
    "PGA",
    "SJKC",
    "SJKT",
    "SRA",
    "SBP",
    "HKL",
    "KFC",
    "KD",
    "BHP",
    "EDC",
    "IIC",
    "PUSRAWI",
    "PERKIM",
    "TM",
    "TTDI",
    "UIA",
    "PJ",
    "UM",
    "SS2",
    "PKNS",
    "OCBC",
    "PPUM",
    "TNB",
    "HQ",
    "DBKL",
    "BBSB",
    "BMC",
    "BMW",
    "UKM",
    "TK",
    "BP",
    "TSB",
    "TSJ",
    "JKP",
    "BRT",
    "B.T.R",
    "TBS",
    "JKR",
    "JPS",
    "PDRM",
    "K.L",
    "PJS",
    "BP1",
    "BP4",
    "BP5",
    "BPP",
    "RKK1",
    "W.P",
    "DTR",
    "DXC",
    "DXN",
    "GSK",
    "BU",
    "S.E.H",
    "UIA",
    "UIAM",
    "KENMS",
    "UTM",
    "IRKHS",
    "RKK1",
}

# Street types and their proper forms
STREET_TYPES = {
    "JLN": "Jalan",
    "LBH": "Lebuh",
    "LRG": "Lorong",
    "TMN": "Taman",
    "PER": "Persiaran",
    "LTG": "Lebuhraya",
    "SS": "SS",  # Keep SS as is (common in Selangor addresses)
    "PJU": "PJU",  # Keep PJU as is (common in Petaling Jaya addresses)
    "PERS": "Persiaran",
    "KG": "Kampung",
    "L/UTAMA": "Lebuh Utama",
    "L/RAYA": "Lebuhraya",
    "MRR2": "MRR2",
    "PERS.": "Persiaran",
    "LDP": "LDP",
    "SPRINT": "SPRINT",
    "CKE": "CKE",
    "DUKE": "DUKE",
    "LKSA": "LKSA",
    "PSSAAS": "PSSAAS",
    "JSM": "Jalan Sultan Mohamed",
    "JIN": "Jalan",
    "SILK": "SILK",
}

# Combined rules dictionary
NAME_RULES = {
    "uppercase": UPPERCASE_WORDS,
    "street_types": STREET_TYPES,
}
