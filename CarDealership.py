from tkinter.constants import ROUND

Brand = "Ram"
print("Brand")

models = [
"1500 Classic",
"1500",
"2500",
"3500",
"TRX"]
print(models)

models.append("Limited Longhorn")
print(models)

colors = [
"White",
"Black",
"Silver",
"Red",
"Blue"]
print(colors)

colors[4] = "Granite"
print(colors)

Year = 2026
print(Year)

MSRP_1500_CLASSIC = 33000
MSRP_1500 = 38000
MSRP_2500 = 47000
MSRP_3500 = 56000
MSRP_TRX = 86000
MSRP_LONGHORN = 72000
print(MSRP_1500_CLASSIC)
print(MSRP_1500)
print(MSRP_2500)
print(MSRP_3500)
print(MSRP_TRX)
print(MSRP_LONGHORN)

FOUR_YEAR = 48
FIVE_YEAR = 60
SIX_YEAR = 72
print(FOUR_YEAR)
print(FIVE_YEAR)
print(SIX_YEAR)

Guest = "Thomas"
print(Guest)

message = f"Welcome {Guest} to the RAM Dealership, I hope we can pick out the perfect truck for you"
print(message)

banner = """
          _____                    _____                    _____          
         /\    \                  /\    \                  /\    \         
        /::\    \                /::\    \                /::\____\        
       /::::\    \              /::::\    \              /::::|   |        
      /::::::\    \            /::::::\    \            /:::::|   |        
     /:::/\:::\    \          /:::/\:::\    \          /::::::|   |        
    /:::/__\:::\    \        /:::/__\:::\    \        /:::/|::|   |        
   /::::\   \:::\    \      /::::\   \:::\    \      /:::/ |::|   |        
  /::::::\   \:::\    \    /::::::\   \:::\    \    /:::/  |::|___|______  
 /:::/\:::\   \:::\____\  /:::/\:::\   \:::\    \  /:::/   |::::::::\    \ 
/:::/  \:::\   \:::|    |/:::/  \:::\   \:::\____\/:::/    |:::::::::\____\
\::/   |::::\  /:::|____|\::/    \:::\  /:::/    /\::/    / ~~~~~/:::/    /
 \/____|:::::\/:::/    /  \/____/ \:::\/:::/    /  \/____/      /:::/    / 
       |:::::::::/    /            \::::::/    /               /:::/    /  
       |::|\::::/    /              \::::/    /               /:::/    /   
       |::| \::/____/               /:::/    /               /:::/    /    
       |::|  ~|                    /:::/    /               /:::/    /     
       |::|   |                   /:::/    /               /:::/    /      
       \::|   |                  /:::/    /               /:::/    /       
        \:|   |                  \::/    /                \::/    /        
         \|___|                   \/____/                  \/____/
"""
print(banner)

print(sorted(models) + sorted(colors))

MSRP_1500_CLASSIC_5_Year = round(MSRP_1500_CLASSIC / FIVE_YEAR, 2)
print(f"The Monthly Payment for a 1500 Classic on a 5 year plan is: {MSRP_1500_CLASSIC_5_Year}")

MSRP_1500_CLASSIC_4_Year = round(MSRP_1500 / FOUR_YEAR, 2)
print(f"The Monthly Payment for a 1500 Classic on a 4 year plan is `{MSRP_1500_CLASSIC_4_Year}`")

MSRP_1500_CLASSIC_6_Year = round(MSRP_1500 / SIX_YEAR, 2)
print(f"The Monthly Payment for a 1500 Classic on a 6 year plan is: {MSRP_1500_CLASSIC_6_Year}")

print("If you are interested in our other vehicles, here is a 5 year plan for those")

MSRP_1500_5_Year = round(MSRP_1500 / FIVE_YEAR, 2)
print(f"The Monthly Payment for a Ram 1500 on a 5 year plan is: {MSRP_1500_5_Year}")

MSRP_2500_5_Year = round(MSRP_2500 / FIVE_YEAR, 2)
print(f"The Monthly Payment for a Ram 2500 on a 5 year plan is: {MSRP_2500_5_Year}")

MSRP_3500_5_Year = round(MSRP_3500 / FIVE_YEAR, 2)
print(f"The Monthly Payment for a Ram 3500 on a 5 year plan is: {MSRP_3500_5_Year}")

MSRP_TRX_5_Year = round(MSRP_TRX / FIVE_YEAR, 2)
print(f"The Monthly Payment for a Ram TRX on a 5 year plan is: {MSRP_TRX_5_Year}")

MSRP_LONGHORN_5_Year = round(MSRP_LONGHORN / FIVE_YEAR, 2)
print(f"The Monthly Payment for a Longhorn 1500 on a 5 year plan is: {MSRP_LONGHORN_5_Year}")