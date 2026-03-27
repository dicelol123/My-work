import asyncio
import random

class MarketAnalyzer:
    def __init__(self, platform_tax=0.05):
        self.tax = platform_tax # 5% tax like in EA FC or Steam

    async def fetch_item_data(self, item_name, target_price):
        """Simulates an async API call to a marketplace"""
        print(f"🔍 Scanning market for: {item_name}...")
        await asyncio.sleep(random.uniform(0.5, 1.5)) # Simulates network latency
        
        # Simulating market price fluctuation
        current_price = target_price * random.uniform(0.75, 1.15)
        return {"name": item_name, "current": current_price, "target": target_price}

    def analyze_deal(self, data):
        """Calculates Net Profit and ROI after tax"""
        buy_price = data['current']
        potential_sell = data['target']
        
        net_revenue = potential_sell * (1 - self.tax)
        profit = net_revenue - buy_price
        roi = (profit / buy_price) * 100

        return profit, roi

    async def run_scan(self, items_list):
        print("🚀 Starting Async Market Scanner...\n")
        
        # Executing all network requests IN PARALLEL
        tasks = [self.fetch_item_data(name, price) for name, price in items_list.items()]
        results = await asyncio.gather(*tasks)

        for item in results:
            profit, roi = self.analyze_deal(item)
            
            print(f"📦 Item: {item['name']}")
            print(f"   Price: {item['current']:.0f} | Target: {item['target']:.0f}")
            
            if roi > 12:
                print(f"   🔥 SIGNAL: STRONG BUY! Profit: {profit:.0f} | ROI: {roi:.1f}%\n")
            elif roi > 0:
                print(f"   ✅ SIGNAL: Small Profit. ROI: {roi:.1f}%\n")
            else:
                print(f"   ❌ SIGNAL: No Profit (Tax covers margins).\n")

if __name__ == "__main__":
    # Example items to monitor (e.g., EA FC cards or Crypto assets)
    monitor_list = {
        "Elite Player Card": 450000,
        "Mid-Tier Asset": 85000,
        "Consumable Item": 1200
    }
    
    scanner = MarketAnalyzer()
    asyncio.run(scanner.run_scan(monitor_list))
