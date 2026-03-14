"""
Curated list of NSE-listed stocks for the Indian Stock Screener.
Covers Nifty 50, Nifty Next 50, and select mid-cap stocks across sectors.
Each entry: (Yahoo Finance ticker, Company Name, Sector)
"""

NSE_STOCKS = [
    # ──────────────── NIFTY 50 ────────────────
    # IT / Technology
    ("TCS.NS", "Tata Consultancy Services", "Information Technology"),
    ("INFY.NS", "Infosys", "Information Technology"),
    ("HCLTECH.NS", "HCL Technologies", "Information Technology"),
    ("WIPRO.NS", "Wipro", "Information Technology"),
    ("TECHM.NS", "Tech Mahindra", "Information Technology"),
    ("LTIMindtree.NS", "LTIMindtree", "Information Technology"),

    # Banking
    ("HDFCBANK.NS", "HDFC Bank", "Banking"),
    ("ICICIBANK.NS", "ICICI Bank", "Banking"),
    ("KOTAKBANK.NS", "Kotak Mahindra Bank", "Banking"),
    ("SBIN.NS", "State Bank of India", "Banking"),
    ("AXISBANK.NS", "Axis Bank", "Banking"),
    ("INDUSINDBK.NS", "IndusInd Bank", "Banking"),

    # Financial Services
    ("BAJFINANCE.NS", "Bajaj Finance", "Financial Services"),
    ("BAJAJFINSV.NS", "Bajaj Finserv", "Financial Services"),
    ("SBILIFE.NS", "SBI Life Insurance", "Financial Services"),
    ("HDFCLIFE.NS", "HDFC Life Insurance", "Financial Services"),

    # Oil & Gas / Energy
    ("RELIANCE.NS", "Reliance Industries", "Oil & Gas"),
    ("ONGC.NS", "Oil & Natural Gas Corp", "Oil & Gas"),
    ("NTPC.NS", "NTPC", "Power"),
    ("POWERGRID.NS", "Power Grid Corp", "Power"),
    ("ADANIENT.NS", "Adani Enterprises", "Conglomerate"),
    ("ADANIPORTS.NS", "Adani Ports", "Infrastructure"),
    ("COALINDIA.NS", "Coal India", "Mining"),

    # FMCG
    ("HINDUNILVR.NS", "Hindustan Unilever", "FMCG"),
    ("ITC.NS", "ITC", "FMCG"),
    ("NESTLEIND.NS", "Nestle India", "FMCG"),
    ("BRITANNIA.NS", "Britannia Industries", "FMCG"),
    ("TATACONSUM.NS", "Tata Consumer Products", "FMCG"),

    # Pharma / Healthcare
    ("SUNPHARMA.NS", "Sun Pharma", "Pharma"),
    ("DRREDDY.NS", "Dr. Reddy's Labs", "Pharma"),
    ("CIPLA.NS", "Cipla", "Pharma"),
    ("DIVISLAB.NS", "Divi's Laboratories", "Pharma"),
    ("APOLLOHOSP.NS", "Apollo Hospitals", "Healthcare"),

    # Automobile
    ("MARUTI.NS", "Maruti Suzuki", "Automobile"),
    ("TATAMOTORS.NS", "Tata Motors", "Automobile"),
    ("M&M.NS", "Mahindra & Mahindra", "Automobile"),
    ("BAJAJ-AUTO.NS", "Bajaj Auto", "Automobile"),
    ("EICHERMOT.NS", "Eicher Motors", "Automobile"),
    ("HEROMOTOCO.NS", "Hero MotoCorp", "Automobile"),

    # Metals & Materials
    ("TATASTEEL.NS", "Tata Steel", "Metals"),
    ("JSWSTEEL.NS", "JSW Steel", "Metals"),
    ("HINDALCO.NS", "Hindalco Industries", "Metals"),

    # Cement & Construction
    ("ULTRACEMCO.NS", "UltraTech Cement", "Cement"),
    ("GRASIM.NS", "Grasim Industries", "Cement"),
    ("SHREECEM.NS", "Shree Cement", "Cement"),

    # Telecom
    ("BHARTIARTL.NS", "Bharti Airtel", "Telecom"),

    # Others Nifty 50
    ("ASIANPAINT.NS", "Asian Paints", "Paints"),
    ("TITAN.NS", "Titan Company", "Consumer Durables"),
    ("LTTS.NS", "L&T Technology Services", "Information Technology"),
    ("LT.NS", "Larsen & Toubro", "Infrastructure"),
    ("WIPRO.NS", "Wipro Ltd", "Information Technology"),

    # ──────────────── NIFTY NEXT 50 (selected) ────────────────
    ("HAVELLS.NS", "Havells India", "Consumer Durables"),
    ("PIDILITIND.NS", "Pidilite Industries", "Chemicals"),
    ("GODREJCP.NS", "Godrej Consumer Products", "FMCG"),
    ("DABUR.NS", "Dabur India", "FMCG"),
    ("MARICO.NS", "Marico", "FMCG"),
    ("COLPAL.NS", "Colgate-Palmolive India", "FMCG"),
    ("BERGEPAINT.NS", "Berger Paints", "Paints"),
    ("SIEMENS.NS", "Siemens", "Capital Goods"),
    ("ABB.NS", "ABB India", "Capital Goods"),
    ("BOSCHLTD.NS", "Bosch", "Automobile"),
    ("SBICARD.NS", "SBI Cards", "Financial Services"),
    ("CHOLAFIN.NS", "Cholamandalam Inv & Fin", "Financial Services"),
    ("MUTHOOTFIN.NS", "Muthoot Finance", "Financial Services"),
    ("BANDHANBNK.NS", "Bandhan Bank", "Banking"),
    ("IDFCFIRSTB.NS", "IDFC First Bank", "Banking"),
    ("FEDERALBNK.NS", "Federal Bank", "Banking"),
    ("ICICIPRULI.NS", "ICICI Prudential Life", "Financial Services"),
    ("NAUKRI.NS", "Info Edge (Naukri)", "Information Technology"),
    ("DMART.NS", "Avenue Supermarts (DMart)", "Retail"),
    ("TRENT.NS", "Trent", "Retail"),
    ("ZOMATO.NS", "Zomato", "Internet"),
    ("PAYTM.NS", "One97 Communications (Paytm)", "Internet"),
    ("POLICYBZR.NS", "PB Fintech (Policybazaar)", "Internet"),

    # ──────────────── MID-CAP PICKS ────────────────
    # Chemicals
    ("SRF.NS", "SRF", "Chemicals"),
    ("ATUL.NS", "Atul", "Chemicals"),
    ("DEEPAKNTR.NS", "Deepak Nitrite", "Chemicals"),

    # Pharma
    ("AUROPHARMA.NS", "Aurobindo Pharma", "Pharma"),
    ("BIOCON.NS", "Biocon", "Pharma"),
    ("LALPATHLAB.NS", "Dr Lal PathLabs", "Healthcare"),
    ("METROPOLIS.NS", "Metropolis Healthcare", "Healthcare"),

    # IT Mid-cap
    ("MPHASIS.NS", "Mphasis", "Information Technology"),
    ("PERSISTENT.NS", "Persistent Systems", "Information Technology"),
    ("COFORGE.NS", "Coforge", "Information Technology"),

    # Infrastructure / Capital Goods
    ("IRCTC.NS", "IRCTC", "Infrastructure"),
    ("BEL.NS", "Bharat Electronics", "Defence"),
    ("HAL.NS", "Hindustan Aeronautics", "Defence"),

    # Auto Ancillary
    ("MOTHERSON.NS", "Samvardhana Motherson", "Automobile"),
    ("BALKRISIND.NS", "Balkrishna Industries", "Automobile"),

    # Consumer
    ("VOLTAS.NS", "Voltas", "Consumer Durables"),
    ("WHIRLPOOL.NS", "Whirlpool of India", "Consumer Durables"),
    ("CROMPTON.NS", "Crompton Greaves CE", "Consumer Durables"),
    ("BATAINDIA.NS", "Bata India", "Consumer Durables"),
    ("PAGEIND.NS", "Page Industries", "Textile"),
    ("TATAELXSI.NS", "Tata Elxsi", "Information Technology"),

    # Power & Utilities
    ("TATAPOWER.NS", "Tata Power", "Power"),
    ("ADANIGREEN.NS", "Adani Green Energy", "Power"),
    ("NHPC.NS", "NHPC", "Power"),
    ("IEX.NS", "Indian Energy Exchange", "Power"),

    # Real Estate
    ("DLF.NS", "DLF", "Real Estate"),
    ("GODREJPROP.NS", "Godrej Properties", "Real Estate"),
    ("OBEROIRLTY.NS", "Oberoi Realty", "Real Estate"),

    # Miscellaneous
    ("PIIND.NS", "PI Industries", "Chemicals"),
    ("INDIGO.NS", "InterGlobe Aviation (IndiGo)", "Aviation"),
    ("JUBLFOOD.NS", "Jubilant FoodWorks", "Food & Beverages"),
    ("UPL.NS", "UPL", "Chemicals"),
    ("MCDOWELL-N.NS", "United Spirits", "Beverages"),
    ("VBL.NS", "Varun Beverages", "Beverages"),
    ("ASTRAL.NS", "Astral", "Building Products"),
    ("POLYCAB.NS", "Polycab India", "Capital Goods"),
    ("CUMMINSIND.NS", "Cummins India", "Capital Goods"),
    ("MAXHEALTH.NS", "Max Healthcare", "Healthcare"),
    ("MANKIND.NS", "Mankind Pharma", "Pharma"),
    ("JSWENERGY.NS", "JSW Energy", "Power"),
    ("ACC.NS", "ACC", "Cement"),
    ("AMBUJACEM.NS", "Ambuja Cements", "Cement"),
    ("PETRONET.NS", "Petronet LNG", "Oil & Gas"),
    ("BPCL.NS", "Bharat Petroleum", "Oil & Gas"),
    ("IOC.NS", "Indian Oil Corp", "Oil & Gas"),
    ("HINDPETRO.NS", "Hindustan Petroleum", "Oil & Gas"),
    ("GAIL.NS", "GAIL India", "Oil & Gas"),
    ("VEDL.NS", "Vedanta", "Metals"),
    ("NMDC.NS", "NMDC", "Mining"),
    ("SAIL.NS", "Steel Authority of India", "Metals"),
    ("BANKBARODA.NS", "Bank of Baroda", "Banking"),
    ("PNB.NS", "Punjab National Bank", "Banking"),
    ("CANBK.NS", "Canara Bank", "Banking"),
    ("UNIONBANK.NS", "Union Bank of India", "Banking"),
]

# Build a lookup dict: ticker -> (name, sector)
STOCK_INFO = {ticker: (name, sector) for ticker, name, sector in NSE_STOCKS}

# Unique tickers only (remove duplicates like WIPRO appearing twice)
TICKERS = list(dict.fromkeys(t for t, _, _ in NSE_STOCKS))

# All unique sectors for filter dropdowns
SECTORS = sorted(set(s for _, _, s in NSE_STOCKS))
