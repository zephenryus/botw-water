class Water:
    def __init__(self, height: float, x_axis_flow_rate: float, z_axis_flow_rate: float, material_check: int,
                 material_index: int):
        self.height = height
        self.x_axis_flow_rate = x_axis_flow_rate
        self.z_axis_flow_rate = z_axis_flow_rate
        self.material_check = material_check
        self.material_index = material_index
