import math

def total_surfacearea_spheres(radii):
    total_surface_area = 0
    for r in radii:
        surface_area = 4 * math.pi * r**2
        total_surface_area += surface_area
    return total_surface_area
