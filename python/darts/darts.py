def score(x, y):
    cart_dist = (x**2 + y**2)**0.5

    if cart_dist <= 1:
        return 10
    elif cart_dist <= 5:
        return 5
    elif cart_dist <= 10:
        return 1
    else:
        return 0
