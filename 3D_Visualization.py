import pyvista as pv
import os

# Obtén la ruta del directorio donde está el archivo .py
dir_path = os.path.dirname(os.path.abspath(__file__))

# Cambia el directorio de trabajo a ese directorio
os.chdir(dir_path)



# Crear el plotter
plotter = pv.Plotter(shape=(1, 3))

# Cargar los archivos de la carpeta p2
mesh_core_p2 = pv.read('p2/Core Surface.vtk')
mesh_bz_p2 = pv.read('p2/Border Zone Surface.vtk')
mesh_vt_p2 = pv.read('p2/ventricle_Tagged.vtk')

# Cargar los archivos de la carpeta p5
mesh_core_p5 = pv.read('p5/Core Surface.vtk')
mesh_bz_p5 = pv.read('p5/Border Zone Surface.vtk')
mesh_vt_p5 = pv.read('p5/ventricle_Tagged.vtk')

# Cargar los archivos de la carpeta p36
mesh_core_p36 = pv.read('p36/Core Surface.vtk')
mesh_bz_p36 = pv.read('p36/Border Zone Surface.vtk')
mesh_vt_p36 = pv.read('p36/ventricle_Tagged.vtk')


mesh_vtc_p2 = mesh_vt_p2
mesh_vtc_p5 = mesh_vt_p5
mesh_vtc_p36 = mesh_vt_p36

# Subpanel 1 (p2)
plotter.subplot(0, 0)  # Primer panel
cr_p2 = plotter.add_mesh(mesh_core_p2, color='r')
bz_p2 = plotter.add_mesh(mesh_bz_p2, color='y', opacity=0.3,name='Border Zone P2')
vt_p2 = plotter.add_mesh(mesh_vt_p2, scalars='DistEndoToEpi', name='VT P2', show_scalar_bar=False)

# Añade un título
plotter.add_text("Paciente 2", position="upper_edge", font_size=12)


# Scalar bar personalizada a la izquierda y centradas
plotter.add_scalar_bar(
    title = "    DistEndoToEpi\n",
    vertical=True,
    position_x=0.05,      
    position_y=0.25,      
    width=0.02,           
    height=0.5,           
    title_font_size=10,
    label_font_size=10
)


# Función para cambiar la opacidad del ventrículo para p2
def slider_vt_p2(value):
    vt_p2.GetProperty().SetOpacity(value)
    plotter.render()



# Agregar slider de opacidad para p2
plotter.add_slider_widget(
    callback=slider_vt_p2,
    rng=[0, 1],
    value=1,
    title="Opacidad VT",
    pointa=(0.035, 0.91),
    pointb=(0.41, 0.91),
    style='modern'
)

# Función para actualizar el umbral sin borrar la escena para p2
def update_threshold_p2(value):
    mesh_vt = mesh_vtc_p2.threshold(value, scalars='scalars', invert=False)
    vt_p2.mapper.SetInputData(mesh_vt)
    plotter.render()



# Agregar slider de umbral para p2
plotter.add_slider_widget(
    update_threshold_p2,
    value=0,
    rng=[mesh_vt_p2['scalars'].min(), mesh_vt_p2['scalars'].max()],
    title="Umbral",
    pointa=(0.7, 0.1),
    pointb=(0.95, 0.1)
)

# Funciones de filtrado con checkboxes
def toggle_core_p2(estado):
    cr_p2.SetVisibility(estado)
    plotter.render()

def toggle_bz_p2(estado):
    bz_p2.SetVisibility(estado)
    plotter.render()

def toggle_vt_p2(estado):
    vt_p2.SetVisibility(estado)
    plotter.render()

# Agregar botón de checkbox para controlar la visibilidad de la malla 'Core' del paciente 2
plotter.add_checkbox_button_widget(toggle_core_p2, value=True, position=(10, 10), size=20, color_on='black', color_off='white')
# Agregar texto "Core" cerca del botón de checkbox de 'Core'
plotter.add_text("Core", position=(40, 10), font_size=10, color='red')

# Agregar botón de checkbox para controlar la visibilidad de la malla 'Border Zone' del paciente 2
plotter.add_checkbox_button_widget(toggle_bz_p2, value=True, position=(10, 40), size=20, color_on='black', color_off='white')
# Agregar texto "Border Zone" cerca del botón de checkbox de 'Border Zone'
plotter.add_text("Border Zone", position=(40, 40), font_size=10, color=(204/255, 153/255, 0))

# Agregar botón de checkbox para controlar la visibilidad de la malla 'VT' del paciente 2
plotter.add_checkbox_button_widget(toggle_vt_p2, value=True, position=(10, 70), size=20, color_on='black', color_off='white')
# Agregar texto "VT" cerca del botón de checkbox de 'VT'
plotter.add_text("VT", position=(40, 70), font_size=10, color='black')




# Subpanel 2 (p5)
plotter.subplot(0, 1)  # Segundo panel
cr_p5 =plotter.add_mesh(mesh_core_p5, color='r')
bz_p5 = plotter.add_mesh(mesh_bz_p5, color='y', opacity=0.3)
vt_p5 = plotter.add_mesh(mesh_vt_p5, scalars='DistEndoToEpi', name='VT P5',show_scalar_bar=False)

# Añade un titulo
plotter.add_text("Paciente 5", position="upper_edge", font_size=12)

# Función para cambiar la opacidad del ventrículo para p5
def slider_vt_p5(value):
    vt_p5.GetProperty().SetOpacity(value)
    plotter.render()


# Agregar slider de opacidad para p5
plotter.add_slider_widget(
    callback=slider_vt_p5,
    rng=[0, 1],
    value=1,
    title="Opacidad VT",
    pointa=(0.035, 0.91),
    pointb=(0.41, 0.91),
    style='modern'
)

# Función para actualizar el umbral sin borrar la escena para p5
def update_threshold_p5(value):
    mesh_vt = mesh_vtc_p5.threshold(value, scalars='scalars', invert=False)
    vt_p5.mapper.SetInputData(mesh_vt)
    plotter.render()


# Agregar slider de umbral para p5
plotter.add_slider_widget(
    update_threshold_p5,
    value=0,
    rng=[mesh_vt_p5['scalars'].min(), mesh_vt_p5['scalars'].max()],
    title="Umbral",
    pointa=(0.7, 0.1),
    pointb=(0.95, 0.1)
)


# Funciones de filtrado con checkboxes
def toggle_core_p5(estado):
    cr_p5.SetVisibility(estado)
    plotter.render()

def toggle_bz_p5(estado):
    bz_p5.SetVisibility(estado)
    plotter.render()

def toggle_vt_p5(estado):
    vt_p5.SetVisibility(estado)
    plotter.render()

# Agregar botón de checkbox para controlar la visibilidad de la malla 'Core' del paciente 5
plotter.add_checkbox_button_widget(toggle_core_p5, value=True, position=(10, 10), size=20, color_on='black', color_off='white')
# Agregar texto "Core" cerca del botón de checkbox de 'Core'
plotter.add_text("Core", position=(40, 10), font_size=10, color='red')

# Agregar botón de checkbox para controlar la visibilidad de la malla 'Border Zone' del paciente 5
plotter.add_checkbox_button_widget(toggle_bz_p5, value=True, position=(10, 40), size=20, color_on='black', color_off='white')
# Agregar texto "Border Zone" cerca del botón de checkbox de 'Border Zone'
plotter.add_text("Border Zone", position=(40, 40), font_size=10, color=(204/255, 153/255, 0))

# Agregar botón de checkbox para controlar la visibilidad de la malla 'VT' del paciente 5
plotter.add_checkbox_button_widget(toggle_vt_p5, value=True, position=(10, 70), size=20, color_on='black', color_off='white')
# Agregar texto "VT" cerca del botón de checkbox de 'VT'
plotter.add_text("VT", position=(40, 70), font_size=10, color='black')




# Subpanel 3 (p36)
plotter.subplot(0, 2)  # Tercer panel
cr_p36 = plotter.add_mesh(mesh_core_p36, color='r')
bz_p36 = plotter.add_mesh(mesh_bz_p36, color='y', opacity=0.3)
vt_p36 = plotter.add_mesh(mesh_vt_p36, scalars='DistEndoToEpi', name='VT P36', show_scalar_bar=False)

# Añade un titulo
plotter.add_text("Paciente 36", position="upper_edge", font_size=12)


# Función para cambiar la opacidad del ventrículo para p36
def slider_vt_p36(value):
    vt_p36.GetProperty().SetOpacity(value)
    plotter.render()



# Agregar slider de opacidad para p36
plotter.add_slider_widget(
    callback=slider_vt_p36,
    rng=[0, 1],
    value=1,
    title="Opacidad VT",
    pointa=(0.035, 0.91),
    pointb=(0.41, 0.91),
    style='modern'
)

# Función para actualizar el umbral sin borrar la escena para p36
def update_threshold_p36(value):
    mesh_vt = mesh_vtc_p36.threshold(value, scalars='scalars', invert=False)
    vt_p36.mapper.SetInputData(mesh_vt)
    plotter.render()

# Agregar slider de umbral para p36
plotter.add_slider_widget(
    update_threshold_p36,
    value=0,
    rng=[mesh_vt_p36['scalars'].min(), mesh_vt_p36['scalars'].max()],
    title="Umbral",
    pointa=(0.7, 0.1),
    pointb=(0.95, 0.1)
)


# Funciones de filtrado con checkboxes
def toggle_core_p36(estado):
    cr_p36.SetVisibility(estado)
    plotter.render()

def toggle_bz_p36(estado):
    bz_p36.SetVisibility(estado)
    plotter.render()

def toggle_vt_p36(estado):
    vt_p36.SetVisibility(estado)
    plotter.render()

# Agregar botón de checkbox para controlar la visibilidad de la malla 'Core' del paciente 36
plotter.add_checkbox_button_widget(toggle_core_p36, value=True, position=(10, 10), size=20, color_on='black', color_off='white')
# Agregar texto "Core" cerca del botón de checkbox de 'Core'
plotter.add_text("Core", position=(40, 10), font_size=10, color='red')

# Agregar botón de checkbox para controlar la visibilidad de la malla 'Border Zone' del paciente 36
plotter.add_checkbox_button_widget(toggle_bz_p36, value=True, position=(10, 40), size=20, color_on='black', color_off='white')
# Agregar texto "Border Zone" cerca del botón de checkbox de 'Border Zone'
plotter.add_text("Border Zone", position=(40, 40), font_size=10, color=(204/255, 153/255, 0))

# Agregar botón de checkbox para controlar la visibilidad de la malla 'VT' del paciente 36
plotter.add_checkbox_button_widget(toggle_vt_p36, value=True, position=(10, 70), size=20, color_on='black', color_off='white')
# Agregar texto "VT" cerca del botón de checkbox de 'VT'
plotter.add_text("VT", position=(40, 70), font_size=10, color='black')


# Mostrar la ventana dividida
plotter.show()


