x_input = [0.1, 0.5, 0.2]
w_weights = [0.4, 0.3, 0.6]
threshold = 0.5

def step(weighted_sum):
  if weighted_sum > threshold:
    return 1
  else:
    return 0

