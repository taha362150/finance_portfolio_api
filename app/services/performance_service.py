class PerformanceService:
    def calculate_performance(self, invested, current_value):
        return round(((current_value - invested) / invested) * 100, 2)