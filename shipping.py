weight = 8.4
cost = ""

# Ground Shipping(Corrected Logic Error)
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3 + 20
elif weight <10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20

print("Ground Shipping $: ", cost_ground)

# Premium shipping
Premium_cost = 125.00
print("Ground shipping premium$:", Premium_cost)

# Drone Shipping
if weight <= 2:
  cost_drone = weight * 4.50 + 0
elif weight <= 6:
  cost_drone = weight * 9 + 0
elif weight <= 10:
  cost_drone = weight * 12 + 0
else:
  cost_drone = weight * 14.25 + 0

print("Drone shipping $:",cost_drone)
