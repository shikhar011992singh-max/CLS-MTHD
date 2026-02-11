class ChaiOrder:
      def __init__(self, tea_type, size):
            self.tea_type = tea_type
            self.size = size

      @classmethod   # MTHD/DECORATOR
      def from_dict(cls, order_data):
            return cls(
                  order_data["tea_type"],
                  order_data["size"],
            )

class ChaiUtils:
      @staticmethod
      def is_valid_size(size):
            return size in ["small","medium","large"]

print(ChaiUtils.is_valid_size("medium"))

order1 = ChaiOrder.from_dict({"tea_type": "masala", 
"size": "large"})

print(order1.__dict__)


