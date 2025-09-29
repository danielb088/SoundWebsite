import math
import time
from nicegui import ui
import numpy as np


with ui.scene().classes('w-full h-64') as scene:
    with scene.group() as group:
            avocado = 'https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Avocado/glTF-Binary/Avocado.glb'
            object = scene.gltf(avocado).scale(240).move(-2, -3, 0.5)


ui.timer(0.1, lambda: group.move(y=math.tan(time.time())).rotate(0, 0, time.time()).move(x= 0,y = 10, z= 0))

def generate_data(frequency: float = 1.0):
    x, y = np.meshgrid(np.linspace(-3, 3), np.linspace(-3, 3))
    z = np.sin(x * frequency) * np.cos(y * frequency) + 1
    points = np.dstack([x, y, z]).reshape(-1, 3)
    colors = points / [6, 6, 2] + [0.5, 0.5, 0]
    return points, colors

with ui.scene().classes('w-full h-64') as scene:
    points, colors = generate_data()
    point_cloud = scene.point_cloud(points, colors, point_size=0.1)

ui.slider(min=0.1, max=3, step=0.1, value=1) \
    .on_value_change(lambda e: point_cloud.set_points(*generate_data(e.value)))



ui.run()