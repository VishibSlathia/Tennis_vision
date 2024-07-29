from ultralytics import YOLO

model = YOLO('yolov')

result = model.predict('input_videos/input_video.mp4',conf = 0.2,save = True)


