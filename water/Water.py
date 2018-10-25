class Water:
    height_scale_factor = 800 / 65335

    def __init__(self, height: float, x_axis_flow_rate: float, z_axis_flow_rate: float, material_check: int,
                 material_index: int):
        self.height = height
        self.x_axis_flow_rate = x_axis_flow_rate
        self.z_axis_flow_rate = z_axis_flow_rate
        self.material_check = material_check
        self.material_index = material_index

    @staticmethod
    def actual_height(height: int) -> float:
        return height * Water.height_scale_factor

    @staticmethod
    def to_int(height: float) -> int:
        return round(height / Water.height_scale_factor)

    @staticmethod
    def normalize_flow(flow: int) -> float:
        return ((flow / 65335) * 2) - 1

    @staticmethod
    def denormalize_flow(flow: float) -> int:
        return round(((flow + 1) / 2) * 65335)
