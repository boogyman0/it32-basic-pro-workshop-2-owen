quantity = int(input("จำนวนปืน :"))
cost = float(input("ต้นทุนปืนที่รับมา :"))
sell = float(input("ราคาขาย : "))
team_members = int(input("จำนวนลูกน้อง :"))
cost_price = quantity * cost
sell_price = quantity * sell
total = sell_price - cost_price
boss_recive = total * 20/100
member_recive = (total - boss_recive)/team_members
print(f"จำนวนปืน {quantity}")
print(f"ต้นทุนที่รับมา {cost}")
print(f"ราคาขาย{sell}")
print(f"จำนวนลูกน้อง {team_members}")
print(f"ต้นทุนราคา {cost_price}")
print(f"มีรายได้รวม {sell_price}")
print(f"เงินของบอส {boss_recive}")
print(f"ลูกน้องจะได้คนล่ะ{member_recive}")

