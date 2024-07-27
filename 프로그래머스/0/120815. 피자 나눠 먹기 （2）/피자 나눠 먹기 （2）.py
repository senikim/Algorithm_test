def solution(n):
    slices_per_pizza = 6
    lcm_value = slices_per_pizza
    while lcm_value % n != 0:
        lcm_value += slices_per_pizza
    pizzas_needed = lcm_value // slices_per_pizza
    return pizzas_needed