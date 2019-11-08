import imgui
print("begin")
imgui.create_context()
imgui.get_io().display_size = 100, 100
imgui.get_io().fonts.get_tex_data_as_rgba32()


imgui.new_frame()
imgui.begin("Window", True)
imgui.text("HelloWorld")
imgui.end()

imgui.render()
imgui.end_frame()
print("end")
