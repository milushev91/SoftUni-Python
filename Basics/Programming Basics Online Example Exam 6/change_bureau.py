BITCOIN_TO_BGN = 1168 
YUAN_TO_USD = 0.15
USD_TO_BGN = 1.76 
EUR_TO_BGN = 1.95 

bitcoins_count = int(input())
yuans_count = int(input())
commission_percent = float(input()) / 100

#calculate bitcoins in bgn 
bitcoins_to_bgn = bitcoins_count * BITCOIN_TO_BGN

#calculate yuans to usd 
yuans_to_bgn = (yuans_count * YUAN_TO_USD) * USD_TO_BGN

#calculate total bgns 
bgns = bitcoins_to_bgn + yuans_to_bgn

#calculate bgns to euro 

euros = bgns / EUR_TO_BGN

#calculate commission 
commission = euros * commission_percent

#subtract commission
euros -= commission

#print euro
print(f"{euros:.2f}")
