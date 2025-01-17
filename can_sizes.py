import math
pi = math.pi

def main():
    names = ['#1 Picnic', '#1 Tall', '#2', '#2.5', '#3 Cylinder', '#5', '#6Z', '#8Z short', '#10', '#211', '#300', '#303']
    radii = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
    heights = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
    cost_per_cans = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]
    
    for i in range(len(names)):
        name = names[i]
        radius = radii[i]
        height = heights[i]
        # cost_per_can = cost_per_cans[i]

        volume = compute_volume(radius, height)
        surface_area = compute_surface_area(radius, height)

        storage_efficiency = volume / surface_area
        # price = storage_efficiency * cost_per_can
    
        print(f'{name} {storage_efficiency:.2f}')

def compute_volume(radius, height):
    volume = pi * (radius ** 2) * height
    return volume

def compute_surface_area(radius, height):
    surface_area = 2 * pi * radius * (radius + height)
    return surface_area

main()