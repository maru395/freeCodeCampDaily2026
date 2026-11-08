conversion = {
    "B" : 1,
    "KB" : 1000,
    "MB" : 1000000,
    "GB" : 1000000000,
    "TB" : 1000000000000
}
valid_video = {"B", "KB", "MB", "GB"}
valid_drive = {"GB", "TB"}

def number_of_videos(video_size, video_unit, drive_size, drive_unit):
    if video_unit not in valid_video:
        return "Invalid video unit"
    if drive_unit not in valid_drive:
        return "Invalid drive unit"
    return (drive_size * conversion[drive_unit]) // (video_size * conversion[video_unit])
