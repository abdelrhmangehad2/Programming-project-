from abc import ABC, abstractmethod

# single responsibility 
class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items  

    def __str__(self):
        return f"Order ID: {self.order_id}, Items: {self.items}"

class OrderRepository:
    def save(self, order):
        print(f"Order {order.order_id} saved to database.")

# open/closed 
class OrderCostCalculator(ABC):
    @abstractmethod
    def calculate_total(self, order):
        pass

class SimpleOrderCostCalculator(OrderCostCalculator):
    def calculate_total(self, order):
        return sum(order.items.values())

# liskov substitution 
class DiscountedOrderCostCalculator(SimpleOrderCostCalculator):
    def __init__(self, discount_rate):
        self.discount_rate = discount_rate

    def calculate_total(self, order):
        total = super().calculate_total(order)
        return total * (1 - self.discount_rate)

# interface segregation 
class Notifier(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass

class EmailNotifier(Notifier):
    def send_notification(self, message):
        print(f"Email sent: {message}")

class SMSNotifier(Notifier):
    def send_notification(self, message):
        print(f"SMS sent: {message}")

# dependency inversion 
class OrderProcessor:
    def __init__(self, cost_calculator, notifier, repository):
        self.cost_calculator = cost_calculator
        self.notifier = notifier
        self.repository = repository

    def process_order(self, order):
        total_cost = self.cost_calculator.calculate_total(order)
        self.repository.save(order)
        self.notifier.send_notification(f"Order {order.order_id} processed with total cost: {total_cost}")
        print(f"Order {order.order_id} processed successfully!")
