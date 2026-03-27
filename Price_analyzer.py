# price_analyzer.py

def calculate_profit(buy_price, sell_price):
    tax = 0.05  # Налог 5%
    final_receive = sell_price * (1 - tax)
    profit = final_receive - buy_price
    roi = (profit / buy_price) * 100
    return profit, roi

players = [
    {"name": "Vinicius Jr", "buy": 450000, "current_market": 510000},
    {"name": "Mbappe", "buy": 900000, "current_market": 930000},
    {"name": "Salah", "buy": 120000, "current_market": 150000}
]

print("--- Анализ рынка EA FC 26 ---")
for p in players:
    profit, roi = calculate_profit(p["buy"], p["current_market"])
    status = "ВЫГОДНО" if profit > 0 else "УБЫТОК"
    print(f"Игрок: {p['name']} | Профит: {profit:.0f} монет | ROI: {roi:.1f}% | Статус: {status}")
