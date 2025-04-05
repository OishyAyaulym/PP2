import pygame

# Define shape names
SQUARE = 'SQUARE'
RECTANGLE = 'RECTANGLE'
CIRCLE = 'CIRCLE'
RIGHT_TRIANGLE = 'RIGHT_TRIANGLE'
EQUILATERAL_TRIANGLE = 'EQUILATERAL_TRIANGLE'
RHOMBUS = 'RHOMBUS'
ERASER = 'ERASER'

# Display setup
dis_width = 800
dis_height = 600
main_screen_size = (dis_width, dis_height)
elements_to_draw = []

# Icon layout
icon_top_bar_height = 50
icon_size = 50

# Shape icon X positions
icon_positions = {
    SQUARE: (0, 50),
    RECTANGLE: (50, 100),
    CIRCLE: (100, 150),
    RIGHT_TRIANGLE: (150, 200),
    EQUILATERAL_TRIANGLE: (200, 250),
    RHOMBUS: (250, 300),
    ERASER: (300, 350),
}

# Color icon Y positions (on right sidebar)
icon_red_color_start_y = 50
icon_blue_color_start_y = 100
icon_orange_color_start_y = 150
icon_color_shape_width = 40
icon_color_shape_height = 30

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
orange = (255, 165, 0)
purple = (128, 0, 128)

top_tab_color = (100, 100, 100)
right_tab_color = (80, 80, 80)

# Draw all saved shapes
def draw_all_shapes(screen):
    for element in elements_to_draw:
        shape = element['shape']
        color = element['color']

        if shape == SQUARE:
            pygame.draw.rect(screen, color, [element['x'], element['y'], 50, 50])

        elif shape == RECTANGLE:
            pygame.draw.rect(screen, color, [element['x'], element['y'], 80, 40])

        elif shape == CIRCLE:
            pygame.draw.circle(screen, color, (element['x'], element['y']), element['radius'])

        elif shape == RIGHT_TRIANGLE:
            x, y = element['x'], element['y']
            vertices = [(x, y), (x, y + 50), (x + 50, y + 50)]
            pygame.draw.polygon(screen, color, vertices)

        elif shape == EQUILATERAL_TRIANGLE:
            x, y = element['x'], element['y']
            height = 50
            vertices = [(x, y), (x - 25, y + height), (x + 25, y + height)]
            pygame.draw.polygon(screen, color, vertices)

        elif shape == RHOMBUS:
            x, y = element['x'], element['y']
            vertices = [(x, y - 30), (x - 30, y), (x, y + 30), (x + 30, y)]
            pygame.draw.polygon(screen, color, vertices)

# Add shape functions
def add_element(shape, x, y, color):
    if shape == SQUARE:
        elements_to_draw.append({'shape': SQUARE, 'x': x, 'y': y, 'color': color})
    elif shape == RECTANGLE:
        elements_to_draw.append({'shape': RECTANGLE, 'x': x, 'y': y, 'color': color})
    elif shape == CIRCLE:
        elements_to_draw.append({'shape': CIRCLE, 'x': x, 'y': y, 'color': color, 'radius': 25})
    elif shape == RIGHT_TRIANGLE:
        elements_to_draw.append({'shape': RIGHT_TRIANGLE, 'x': x, 'y': y, 'color': color})
    elif shape == EQUILATERAL_TRIANGLE:
        elements_to_draw.append({'shape': EQUILATERAL_TRIANGLE, 'x': x, 'y': y, 'color': color})
    elif shape == RHOMBUS:
        elements_to_draw.append({'shape': RHOMBUS, 'x': x, 'y': y, 'color': color})

# Eraser logic
def erase_element(x, y):
    for element in elements_to_draw[:]:  # copy for safe removal
        shape = element['shape']
        if shape in [SQUARE, RECTANGLE]:
            if element['x'] <= x <= element['x'] + 80 and element['y'] <= y <= element['y'] + 50:
                elements_to_draw.remove(element)
        elif shape == CIRCLE:
            if (x - element['x'])**2 + (y - element['y'])**2 <= element['radius']**2:
                elements_to_draw.remove(element)
        elif shape in [RIGHT_TRIANGLE, EQUILATERAL_TRIANGLE, RHOMBUS]:
            temp_surface = pygame.Surface(main_screen_size, pygame.SRCALPHA)
            pygame.draw.polygon(temp_surface, (0, 0, 0, 255), get_vertices(element))
            if temp_surface.get_at((x, y)) != (0, 0, 0, 0):
                elements_to_draw.remove(element)

# Get vertices for triangles and rhombus
def get_vertices(element):
    x, y = element['x'], element['y']
    shape = element['shape']
    if shape == RIGHT_TRIANGLE:
        return [(x, y), (x, y + 50), (x + 50, y + 50)]
    elif shape == EQUILATERAL_TRIANGLE:
        return [(x, y), (x - 25, y + 50), (x + 25, y + 50)]
    elif shape == RHOMBUS:
        return [(x, y - 30), (x - 30, y), (x, y + 30), (x + 30, y)]

# UI icons
def draw_main_icons(screen):
    pygame.draw.rect(screen, top_tab_color, (0, 0, dis_width, icon_top_bar_height))
    pygame.draw.rect(screen, right_tab_color, (dis_width - 80, 0, 80, dis_height))

    for shape, (x1, x2) in icon_positions.items():
        center_x = x1 + 25
        center_y = 25

        if shape == SQUARE:
            pygame.draw.rect(screen, white, (x1 + 5, 5, 40, 30))
            pygame.draw.rect(screen, black, (center_x - 10, center_y - 10, 20, 20))

        elif shape == RECTANGLE:
            pygame.draw.rect(screen, white, (x1 + 5, 5, 40, 30))
            pygame.draw.rect(screen, black, (center_x - 15, center_y - 7, 30, 14))

        elif shape == CIRCLE:
            pygame.draw.rect(screen, white, (x1 + 5, 5, 40, 30))
            pygame.draw.circle(screen, black, (center_x, center_y), 10)

        elif shape == RIGHT_TRIANGLE:
            pygame.draw.rect(screen, white, (x1 + 5, 5, 40, 30))
            points = [(center_x - 10, center_y - 10),
                      (center_x - 10, center_y + 10),
                      (center_x + 10, center_y + 10)]
            pygame.draw.polygon(screen, black, points)

        elif shape == EQUILATERAL_TRIANGLE:
            pygame.draw.rect(screen, white, (x1 + 5, 5, 40, 30))
            points = [(center_x, center_y - 12),
                      (center_x - 12, center_y + 10),
                      (center_x + 12, center_y + 10)]
            pygame.draw.polygon(screen, black, points)

        elif shape == RHOMBUS:
            pygame.draw.rect(screen, white, (x1 + 5, 5, 40, 30))
            points = [(center_x, center_y - 12),
                      (center_x - 12, center_y),
                      (center_x, center_y + 12),
                      (center_x + 12, center_y)]
            pygame.draw.polygon(screen, black, points)

        elif shape == ERASER:
            pygame.draw.rect(screen, white, (x1 + 5, 5, 40, 30))
            pygame.draw.line(screen, black, (x1 + 10, 10), (x1 + 30, 30), 5)

    # Color selection (right sidebar)
    pygame.draw.rect(screen, red, (dis_width - 70, icon_red_color_start_y, icon_color_shape_width, icon_color_shape_height))
    pygame.draw.rect(screen, blue, (dis_width - 70, icon_blue_color_start_y, icon_color_shape_width, icon_color_shape_height))
    pygame.draw.rect(screen, orange, (dis_width - 70, icon_orange_color_start_y, icon_color_shape_width, icon_color_shape_height))

# Main loop
def main():
    pygame.init()
    screen = pygame.display.set_mode(main_screen_size)
    clock = pygame.time.Clock()

    current_shape = SQUARE
    color = black

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                # Handle top bar icon selection
                for shape, (start_x, end_x) in icon_positions.items():
                    if start_x <= x < end_x and y < icon_top_bar_height:
                        current_shape = shape

                # Handle color buttons
                if dis_width - 70 <= x <= dis_width - 30:
                    if icon_red_color_start_y <= y < icon_red_color_start_y + icon_color_shape_height:
                        color = red
                    elif icon_blue_color_start_y <= y < icon_blue_color_start_y + icon_color_shape_height:
                        color = blue
                    elif icon_orange_color_start_y <= y < icon_orange_color_start_y + icon_color_shape_height:
                        color = orange

                # Draw or erase based on selected tool
                elif current_shape == ERASER:
                    erase_element(x, y)
                else:
                    add_element(current_shape, x, y, color)

        screen.fill(white)
        draw_all_shapes(screen)
        draw_main_icons(screen)
        pygame.display.flip()
        clock.tick(60)

main()