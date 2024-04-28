import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import FancyArrowPatch

class VectorCalculator:
    @staticmethod
    def calculate_angle_between_vectors(vec1, vec2):
        dot_product = np.dot(vec1, vec2)
        magnitude_vec1 = np.linalg.norm(vec1)
        magnitude_vec2 = np.linalg.norm(vec2)
        cos_angle = dot_product / (magnitude_vec1 * magnitude_vec2)
        angle = np.arccos(cos_angle)
        return np.degrees(angle)

def update(frame):
    # Vary the direction of the second vector
    angle = frame * 2  # Increment angle by 2 degrees per frame
    vec2 = [np.cos(np.radians(angle)), np.sin(np.radians(angle))]
    
    # Define the length of the first vector
    length_vec1 = 1.5
    
    # Define the first vector (horizontal)
    vec1 = [length_vec1, 0]
    
    # Calculate the angle between the vectors
    angle_between = VectorCalculator.calculate_angle_between_vectors(vec1, vec2)
    
    # Calculate the projection of vec2 onto vec1
    projection_length = np.dot(vec1, vec2) / np.linalg.norm(vec1)
    projection = (projection_length / np.linalg.norm(vec1)) * np.array(vec1)
    
    # Update the plot
    ax.clear()
    
    # Create arrow-shaped vectors
    arrow_vec1 = FancyArrowPatch((0, 0), (vec1[0], vec1[1]), mutation_scale=20, color='r', arrowstyle='-|>')
    arrow_vec2 = FancyArrowPatch((0, 0), (vec2[0], vec2[1]), mutation_scale=20, color='b', arrowstyle='-|>')
    
    ax.add_patch(arrow_vec1)
    ax.add_patch(arrow_vec2)
    
    # Plot the projection of vec2 onto vec1
    ax.plot([0, projection[0]], [0, projection[1]], 'g--', label='Projection of Vector 2')
    
    # Annotate vectors with their magnitudes
    ax.annotate(f'|V1| = {length_vec1}', xy=(vec1[0], vec1[1]), xytext=(vec1[0]+0.1, vec1[1]+0.1), color='r')
    ax.annotate(f'|V2| = 1', xy=(vec2[0], vec2[1]), xytext=(vec2[0]+0.1, vec2[1]+0.1), color='b')
    
    ax.legend()
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_title(f'Angle between vectors: {angle_between:.2f} degrees')

# Create a figure and axis
fig, ax = plt.subplots()
# Create the animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 360, 180), interval=50, repeat=True)
plt.show()
