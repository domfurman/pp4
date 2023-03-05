fifo_fruit = []

fifo_fruit.append("mango")
fifo_fruit.append("apple")
fifo_fruit.append("banana")
fifo_fruit.append("watermelon")

print("Order in a FIFO queue is:")

for i in range(len(fifo_fruit)):
    print(f"{i+1}. {fifo_fruit[i]}")

