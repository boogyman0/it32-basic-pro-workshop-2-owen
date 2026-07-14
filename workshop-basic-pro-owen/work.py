quantity = int(input("จำนวนปืน :"))
cost = float(input("ต้นทุนปืนที่รับมา :"))
sell = float(input("ราคาขาย : "))
team_members = int(input("จำนวนลูกน้อง :"))
cost_price = quantity * cost
sell_price = quantity * sell
total = sell_price - cost_price
gumrai = total - sell_price
boss_recive = total * 20/100
member_recive = (total - boss_recive)/team_members
print(f"จำนวนปืน {quantity}")
print(f"ต้นทุนที่รับมา {cost}")
print(f"ราคาขาย{sell}")
print(f"จำนวนลูกน้อง {team_members}")
print(f"{cost_price}")
print(f"{sell_price}")
print(f"{total}")
print(f"{gumrai}")
print(f"{boss_recive}")
print(f"{member_recive}")
