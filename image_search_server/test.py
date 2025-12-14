import time
import requests
from io import BytesIO
from PIL import Image
from ultralytics import YOLO

# 모델 로드 (CPU 전용)
# best.pt 경로를 settings.py와 동일하게 맞춰주세요
MODEL_PATH = "yolo_pill_v7/best.pt"
model = YOLO(MODEL_PATH)

def run_test_image(url: str):
    print(f"Downloading test image from {url}")
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    img = Image.open(BytesIO(resp.content)).convert("RGB")

    start = time.time()
    results = model(img)  # Ultralytics가 내부적으로 NMS, confidence filtering 다 해줌
    elapsed_ms = (time.time() - start) * 1000.0

    print(f"Inference finished in {elapsed_ms:.2f} ms")

    detections = []
    if len(results[0].boxes) > 0:
        for box in results[0].boxes:
            cls_id = int(box.cls.item())
            conf = float(box.conf.item())
            label = results[0].names.get(cls_id, f"class_{cls_id}")
            detections.append({
                "label": label,
                "confidence": conf,
                "bbox": box.xyxy.tolist()[0]  # [x1, y1, x2, y2]
            })

    print("Detections:", detections)

if __name__ == "__main__":
    # 테스트용 이미지 URL
    test_url = "https://media.discordapp.net/attachments/1194914826858790972/1440914977991950396/19334.jpg?ex=691fe425&is=691e92a5&hm=2eb39d0403a5d016428d35bef3c10124ce3795c2a84d65be347600c60d4cfb23&=&format=webp&width=721&height=541"
    run_test_image(test_url)
