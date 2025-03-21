def total_Volume(prisms):
    total_volume = 0
    for prism in prisms:
        length, base, height = prism
        volume = 0.5 * base * height * length
        total_volume += volume
    return total_volume
