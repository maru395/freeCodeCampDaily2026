def mix_paint(bucket1, bucket2):
    total = bucket1["fullness"] + bucket2["fullness"]
    if total == 0:
        return [0, 0, 0]  

    rgb = []
    for i in range(3):
        weighted = (bucket1["color"][i] * bucket1["fullness"] +
                    bucket2["color"][i] * bucket2["fullness"]) / total
        rgb.append(int(weighted + 0.5)) 

    return rgb


