def tire_status(pressure_psi, range_bar):
  bar = 14.5038
  return ["high" if t > range_bar*bar else "low" for t in pressure_psi]
