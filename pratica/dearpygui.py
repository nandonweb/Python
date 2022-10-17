import dearpygui.dearpygui as dpg

def save_callback():
    print("Save Clicked")

with dpg.window(label="Example Window"):
    dpg.add_text("Hello, world")
    dpg.add_button(label="Save", callback=save_callback)
    dpg.add_input_text(label="string", default_value="Quick brown fox")
    dpg.add_slider_float(label="float", default_value=0.273, max_value=1)
dpg.start_dearpygui()