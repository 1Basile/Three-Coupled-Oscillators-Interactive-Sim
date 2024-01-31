# Import necessary libraries
import warnings
import matplotlib
import seaborn as sns
from vpython import *
import tkinter as tk
from tkinter import ttk, messagebox
import sys

# Suppress specific warnings from matplotlib
warnings.filterwarnings("ignore", category=matplotlib.MatplotlibDeprecationWarning)

# Set the style for seaborn plots
sns.set_style("darkgrid", {"grid.color": ".6", "grid.linestyle": ":"})

# Initialize the VPython scene
scene = canvas()
# Initialize global variables for buttons and state flags
run_button = None
paused = False
terminated = False

# Function to update the label with the slider's value
def update_label(value, var):
    var.set(f"{float(value):.2f}")

# Function to create a slider with a label in the tkinter frame
def create_slider(frame, label, from_, to, row, var):
    ttk.Label(frame, text=label, font=('Helvetica', 10)).grid(column=0, row=row, pady=5, sticky='w')
    slider = ttk.Scale(frame, from_=from_, to=to, orient='horizontal', length=200, command=lambda v: update_label(v, var))
    slider.grid(column=1, row=row, padx=10, pady=5, sticky='ew')
    ttk.Label(frame, textvariable=var, font=('Helvetica', 10)).grid(column=2, row=row, pady=5, sticky='w')
    return slider

# Function to pause the simulation on VPython canvas click
def pause_simulation(evt):
    global paused
    paused = not paused

# Function to handle key press events in tkinter window
def on_key_press(event):
    if event.keysym == 'Escape':
        sys.exit()

# Function to handle key down events in VPython canvas
def handle_keydown(evt):
    global paused
    global terminated
    if evt.key == ' ':  # Spacebar to toggle pause
        paused = not paused
    if evt.key == 'q':  # 'q' key to terminate
        terminated = True
    if evt.key == 'esc':  # 'esc' key to exit
        sys.exit()

# Function to display help instructions
def show_help():
    help_text = ("To pause the simulation, click on the VPython canvas.\n"
                 "To terminate the simulation, so be able to start with new parameters, press the 'q' key.\n"
                 "To start a new simulation with new parameters, press the 'Run Simulation' button.\n"
                 "To exit the application, press the 'Esc' key.")
    messagebox.showinfo("Help", help_text)

# Function to clear the VPython scene and plots
def clear_scene_and_plots():
    global pos1, pos2, pos3, vel1, vel2, vel3, acc1, acc2, acc3, gpos, gvel, gacc
    for obj in scene.objects:
        obj.visible = False
    if 'pos1' in globals():
        for plot in [pos1, pos2, pos3, vel1, vel2, vel3, acc1, acc2, acc3]:
            plot.delete()

# Main application window for tkinter interface
root = tk.Tk()
root.title("Initial Conditions for Simulation")
root.geometry('415x750')

# Apply a style to tkinter elements
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12), borderwidth='4')
style.configure('TLabel', font=('Helvetica', 12), background='lightgray', padding=10)
root.configure(bg='lightgray')

# Main frame for tkinter widgets
mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(column=0, row=0, sticky=('N', 'W', 'E', 'S'))

# StringVars for slider values
value_x1 = tk.StringVar(value='0.00')
value_x2 = tk.StringVar(value='0.00')
value_x3 = tk.StringVar(value='0.00')
value_v1 = tk.StringVar(value='0.00')
value_v2 = tk.StringVar(value='0.00')
value_v3 = tk.StringVar(value='0.00')

value_m1 = tk.StringVar(value='0.2')
value_m2 = tk.StringVar(value='0.2')
value_m3 = tk.StringVar(value='0.2')
value_k1 = tk.StringVar(value='10.0')
value_k2 = tk.StringVar(value='5.0')
value_k3 = tk.StringVar(value='5.0')
value_k4 = tk.StringVar(value='10.0')

# Create sliders with labels and value display
slider_x1 = create_slider(mainframe, "Initial Position x1:", -0.1, 0.1, 0, value_x1)
slider_x2 = create_slider(mainframe, "Initial Position x2:", -0.1, 0.1, 1, value_x2)
slider_x3 = create_slider(mainframe, "Initial Position x3:", -0.1, 0.1, 2, value_x3)
slider_v1 = create_slider(mainframe, "Initial Velocity v1:", -1, 1, 3, value_v1)
slider_v2 = create_slider(mainframe, "Initial Velocity v2:", -1, 1, 4, value_v2)
slider_v3 = create_slider(mainframe, "Initial Velocity v3:", -1, 1, 5, value_v3)

slider_m1 = create_slider(mainframe, "Mass m1:", 0.1, 1.0, 6, value_m1)
slider_m2 = create_slider(mainframe, "Mass m2:", 0.1, 1.0, 7, value_m2)
slider_m3 = create_slider(mainframe, "Mass m3:", 0.1, 1.0, 8, value_m3)
slider_k1 = create_slider(mainframe, "Spring k1:", 1, 20, 9, value_k1)
slider_k2 = create_slider(mainframe, "Spring k2:", 1, 20, 10, value_k2)
slider_k3 = create_slider(mainframe, "Spring k3:", 1, 20, 11, value_k3)
slider_k4 = create_slider(mainframe, "Spring k4:", 1, 20, 12, value_k4)

# Create graph windows for position, velocity, and acceleration
gpos = graph(title="Positions", xtitle="Time", ytitle="Position", width=600, height=200)
gvel = graph(title="Velocities", xtitle="Time", ytitle="Velocity", width=600, height=200)
gacc = graph(title="Accelerations", xtitle="Time", ytitle="Acceleration", width=600, height=200)

# Create plots for each mass
pos1 = gcurve(graph=gpos, color=color.blue, label="x1")
vel1 = gcurve(graph=gvel, color=color.blue, label="v1")
acc1 = gcurve(graph=gacc, color=color.blue, label="a1")

pos2 = gcurve(graph=gpos, color=color.red, label="x2")
vel2 = gcurve(graph=gvel, color=color.red, label="v2")
acc2 = gcurve(graph=gacc, color=color.red, label="a2")

pos3 = gcurve(graph=gpos, color=color.green, label="x3")
vel3 = gcurve(graph=gvel, color=color.green, label="v3")
acc3 = gcurve(graph=gacc, color=color.green, label="a3")

# Function to start the simulation
def start_simulation():
    run_button.config(state='disabled', text='Waiting for Simulation')
    global terminated
    global paused
    # Bind the pause function to mouse click
    scene.bind('click', pause_simulation)
    scene.bind('keydown', handle_keydown)
    clear_scene_and_plots()

    # Get values from sliders
    initial_x1 = float(slider_x1.get()) if slider_x1.get() else 0.0
    initial_x2 = float(slider_x2.get()) if slider_x2.get() else 0.0
    initial_x3 = float(slider_x3.get()) if slider_x3.get() else 0.0
    initial_v1 = float(slider_v1.get()) if slider_v1.get() else 0.0
    initial_v2 = float(slider_v2.get()) if slider_v2.get() else 0.0
    initial_v3 = float(slider_v3.get()) if slider_v3.get() else 0.0

    initial_m1 = float(slider_m1.get()) if slider_m1.get() else 0.2
    initial_m2 = float(slider_m2.get()) if slider_m2.get() else 0.2
    initial_m3 = float(slider_m3.get()) if slider_m3.get() else 0.2
    initial_k1 = float(slider_k1.get()) if slider_k1.get() else 10.0
    initial_k2 = float(slider_k2.get()) if slider_k2.get() else 5.0
    initial_k3 = float(slider_k3.get()) if slider_k3.get() else 5.0
    initial_k4 = float(slider_k4.get()) if slider_k4.get() else 10.0


    # System parameters
    m1, m2, m3 = initial_m1, initial_m2, initial_m3
    k1, k2, k3, k4 = initial_k1, initial_k2, initial_k3, initial_k4
    L = 0.4
    dL = L / 4

    # Initial conditions
    x1, x2, x3 = initial_x1, initial_x2, initial_x3
    x1dot, x2dot, x3dot = initial_v1, initial_v2, initial_v3

    # Create the visual elements
    left_wall = box(pos=vector(-L/2, 0, 0), size=vector(0.01, 0.1, 0.1), color=color.white)
    right_wall = box(pos=vector(L/2, 0, 0), size=vector(0.01, 0.1, 0.1), color=color.white)

    mass1 = sphere(pos=vector(left_wall.pos.x + dL + x1, 0, 0), radius=0.02, color=color.blue)
    mass2 = sphere(pos=vector(left_wall.pos.x + 2 * dL + x2, 0, 0), radius=0.02, color=color.red)
    mass3 = sphere(pos=vector(left_wall.pos.x + 3 * dL + x3, 0, 0), radius=0.02, color=color.green)

    spring1 = helix(pos=left_wall.pos, axis=mass1.pos - left_wall.pos, radius=0.01, thickness=0.002, color=color.white)
    spring2 = helix(pos=mass1.pos, axis=mass2.pos - mass1.pos, radius=0.01, thickness=0.002, color=color.white)
    spring3 = helix(pos=mass2.pos, axis=mass3.pos - mass2.pos, radius=0.01, thickness=0.002, color=color.white)
    spring4 = helix(pos=mass3.pos, axis=right_wall.pos - mass3.pos, radius=0.01, thickness=0.002, color=color.white)

    # Simulation parameters
    t = 0
    dt = 0.01

    # Initialize lists to store data points
    data_time = []
    data_x1, data_x2, data_x3 = [], [], []
    data_v1, data_v2, data_v3 = [], [], []
    data_a1, data_a2, data_a3 = [], [], []

    # Define the time window for the plots
    time_window = 5
    num_initial_points = int(time_window / dt)

    while t < 10:
        rate(50)  # Sets the simulation rate

        if terminated:
            terminated = False
            break

        if paused:
            continue

        # Calculate forces
        F1 = -k1 * x1 - k2 * (x1 - x2)
        F2 = -k3 * (x2 - x3) - k2 * (x2 - x1)
        F3 = -k3 * (x3 - x2) - k4 * x3

        # Update accelerations
        x1ddot = F1 / m1
        x2ddot = F2 / m2
        x3ddot = F3 / m3

        # Update velocities
        x1dot += x1ddot * dt
        x2dot += x2ddot * dt
        x3dot += x3ddot * dt

        # Update positions
        x1 += x1dot * dt
        x2 += x2dot * dt
        x3 += x3dot * dt

        # Update the visual elements
        mass1.pos.x = left_wall.pos.x + dL + x1
        mass2.pos.x = left_wall.pos.x + 2 * dL + x2
        mass3.pos.x = left_wall.pos.x + 3 * dL + x3

        spring1.axis = mass1.pos - left_wall.pos
        spring2.pos = mass1.pos
        spring2.axis = mass2.pos - mass1.pos
        spring3.pos = mass2.pos
        spring3.axis = mass3.pos - mass2.pos
        spring4.pos = mass3.pos
        spring4.axis = right_wall.pos - mass3.pos

        # Store the data points
        data_time.append(t)
        data_x1.append(x1)
        data_x2.append(x2)
        data_x3.append(x3)
        data_v1.append(x1dot)
        data_v2.append(x2dot)
        data_v3.append(x3dot)
        data_a1.append(x1ddot)
        data_a2.append(x2ddot)
        data_a3.append(x3ddot)

        # Determine the range of data points to plot
        start_index = 0 if t <= time_window else next(i for i, time_value in enumerate(data_time) if time_value > t - time_window)

        # Update the plots
        pos1.data = list(zip(data_time[start_index:], data_x1[start_index:]))
        vel1.data = list(zip(data_time[start_index:], data_v1[start_index:]))
        acc1.data = list(zip(data_time[start_index:], data_a1[start_index:]))

        pos2.data = list(zip(data_time[start_index:], data_x2[start_index:]))
        vel2.data = list(zip(data_time[start_index:], data_v2[start_index:]))
        acc2.data = list(zip(data_time[start_index:], data_a2[start_index:]))

        pos3.data = list(zip(data_time[start_index:], data_x3[start_index:]))
        vel3.data = list(zip(data_time[start_index:], data_v3[start_index:]))
        acc3.data = list(zip(data_time[start_index:], data_a3[start_index:]))

        t += dt

    run_button.config(state='normal', text='Run Simulation')


# Button to run the simulation
run_button = ttk.Button(mainframe, text="Run Simulation", command=start_simulation)
run_button.grid(column=0, row=13, columnspan=3, pady=10)

# Help button
help_button = ttk.Button(mainframe, text="Help", command=show_help)
help_button.grid(column=0, row=14, columnspan=3, pady=10)

# Bind key press events
root.bind('<KeyPress>', on_key_press)

# Run the GUI event loop
root.mainloop()
