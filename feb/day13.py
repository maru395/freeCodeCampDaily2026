def get_fastest_speed(times):
    segments = [320, 280, 350, 300, 250]
    best_lap = segments[0]/times[0]
    segment_number = 1
    for i in range(len(segments)):
        if segments[i]/times[i] > best_lap:
            best_lap = segments[i]/times[i]
            segment_number = i + 1
    return f"The luger's fastest speed was {round(best_lap, 2)} m/s on segment {segment_number}."
