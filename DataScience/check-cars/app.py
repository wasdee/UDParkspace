import streamlit as st
import cv2
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2 import model_zoo
from deep_sort_realtime.deepsort_tracker import DeepSort  # Assumed available

# Initialize detectron2 model for instance segmentation
cfg = get_cfg()
cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"))
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5  # set threshold for this model
cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml")
predictor = DefaultPredictor(cfg)

st.title('Biggest Instance Identifier with Deep SORT')

uploaded_file = st.file_uploader("Choose a video file...", type=["mp4", "avi"])

def initialize_deep_sort():
    return DeepSort(max_age=5)  # Initialize DeepSort with max_age parameter

def process_video(video_file, deep_sort):
    vid = cv2.VideoCapture(video_file.name)
    frame_idx = 0
    biggest_instance = None
    biggest_area = -1

    while vid.isOpened():
        ret, frame = vid.read()
        if not ret:
            break

        # Apply instance segmentation
        outputs = predictor(frame)
        instances = outputs["instances"].to("cpu")

        # Format detections for Deep SORT
        bbs = []
        object_chips = []
        for i in range(len(instances)):
            bbox = instances.pred_boxes[i].tensor.numpy()[0]
            score = instances.scores[i].item()
            x, y, x2, y2 = bbox
            bbs.append(([x, y, x2-x, y2-y], score, None))  # Assuming class is not used
            object_chips.append(frame[int(y):int(y2), int(x):int(x2)])  # Crop the chip

        # Dummy embedder for example
        # Replace with actual logic to generate embeddings from chips
        embeds = [chip.mean(axis=None) for chip in object_chips]  # Dummy embedding

        # Update tracks with new frame detections
        tracks = deep_sort.update_tracks(bbs, embeds=embeds)

        for track in tracks:
            if not track.is_confirmed():
                continue

            ltrb = track.to_ltrb()
            area = (ltrb[2]-ltrb[0]) * (ltrb[3]-ltrb[1])
            if area > biggest_area:
                biggest_area = area
                biggest_instance = frame[int(ltrb[1]):int(ltrb[3]), int(ltrb[0]):int(ltrb[2])]
                biggest_frame_idx = frame_idx

        frame_idx += 1

    vid.release()
    return biggest_instance, biggest_frame_idx

if uploaded_file is not None:
    deep_sort = initialize_deep_sort()
    biggest_instance, biggest_frame_idx = process_video(uploaded_file, deep_sort)
    if biggest_instance is not None:
        st.image(biggest_instance, caption=f"Biggest Instance at Frame: {biggest_frame_idx}")
        st.write(f"Frame Index: {biggest_frame_idx}")
        st.write(f"File Name: {uploaded_file.name}")
