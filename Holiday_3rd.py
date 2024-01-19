def probability_no_collision():
    total_outcomes = 2**3
    favorable_outcomes = 2
    probability = favorable_outcomes / total_outcomes
    rounded_probability = round(probability, 2)
    return rounded_probability

result = probability_no_collision()
print(result)

