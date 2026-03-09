import pygame
import math

pygame.init()

WIDTH = 900
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Go-To-Goal Robot Controller")

clock = pygame.time.Clock()

# Robot state
robot_x = WIDTH // 2
robot_y = HEIGHT // 2
robot_theta = 0.0  # orientation (radians)

# Fixed target
target_x = 700
target_y = 200

# Controller gains
Kp = 2.0      # angular gain
Kv = 0.8      # linear gain

# Thresholds
angle_threshold = 0.1
distance_threshold = 5

running = True

while running:
    dt = clock.tick(60) / 1000.0  # seconds per frame

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # =============================
    # CONTROL LOGIC
    # =============================

    # Desired heading
    desired_theta = math.atan2(target_y - robot_y,
                               target_x - robot_x)

    # Angular error
    error = desired_theta - robot_theta

    # Normalize error to [-pi, pi]
    error = math.atan2(math.sin(error), math.cos(error))

    # Distance to target
    distance = math.sqrt((target_x - robot_x)**2 +
                         (target_y - robot_y)**2)

    # -----------------------------
    # BLOCK 4: Sequential Control
    # -----------------------------

    if abs(error) > angle_threshold:
        # Step 1: Rotate only
        linear_velocity = 0
        angular_velocity = Kp * error

    else:
        # Step 2: Move forward only
        linear_velocity = Kv * distance
        angular_velocity = 0

    # Stop when close to target
    if distance < distance_threshold:
        linear_velocity = 0
        angular_velocity = 0

    # Update robot orientation
    robot_theta += angular_velocity * dt

    # Update robot position
    robot_x += linear_velocity * math.cos(robot_theta) * dt
    robot_y += linear_velocity * math.sin(robot_theta) * dt

    # =============================
    # DRAWING
    # =============================

    screen.fill((30, 30, 30))

    # Draw target
    pygame.draw.circle(screen, (255, 0, 0),
                       (target_x, target_y), 10)

    # Draw robot
    pygame.draw.circle(screen, (0, 255, 0),
                       (int(robot_x), int(robot_y)), 25)

    # Orientation line
    line_length = 40
    end_x = robot_x + line_length * math.cos(robot_theta)
    end_y = robot_y + line_length * math.sin(robot_theta)

    pygame.draw.line(screen, (255, 255, 255),
                     (robot_x, robot_y),
                     (end_x, end_y), 3)

    pygame.display.flip()

pygame.quit()