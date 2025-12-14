📦 Pill Image Search

AI 기반 실사 의약품 이미지 검색 + 복약 정보 관리 서비스
(개인 포트폴리오용 정리본)

<br>
📌 프로젝트 개요

실제 의약품 이미지를 업로드하면 YOLO를 통한 객체 검출 → CLIP 임베딩 검색을 통해 가장 유사한 약품을 찾아주는 서비스입니다.
사용자는 약품을 검색하고, 북마크를 저장하며, 복약 관리 도구를 사용할 수 있습니다.

본 저장소는 팀 프로젝트를 기반으로 하되, 제가 담당한 핵심 기능을 중심으로 리팩토링한 개인 포트폴리오 버전입니다.

<br>
🧩 기술 스택
Backend

Django REST Framework

Python

PostgreSQL

JWT Authentication (Access / Refresh)

AI / ML

YOLOv8 (CPU 최적화)

OpenAI CLIP (이미지 임베딩 → 벡터 검색)

🎯 제가 담당한 주요 기능
🔐 1. Auth / JWT 커스텀 인증

Refresh Token 직접 구현 (토큰 만료/예외 처리 포함)

Login/Logout/Token Refresh 엔드포인트 설계

DRF Permission 기반 접근 제어

⭐ 2. 북마크 기능 전체

모델 & 시리얼라이저 & View(APIView → ViewSet 리팩토링)

북마크 추가/삭제/조회 API

Response 포맷을 팀 요구사항에 맞게 커스텀

{
  "success": true,
  "message": "약품이 북마크에 추가되었습니다.",
  "current_count": 7
}

📷 3. 이미지 검색 기능 구조 설계

YOLO 모델 로딩 실패 문제 해결

GPU → CPU 환경에 맞는 ONNX 변환 수행

CLIP 벡터 저장 및 검색 구조 제안

API의 응답 속도를 위한 비동기 스케줄러 구성

🗂 4. 전체 URL 구조 리팩토링

/auth/, /pills/, /bookmarks/ RESTful하게 재설계

Query Parameter 기반 검색 API 개선
(두 글자 이상 + 초성 검색 지원)

🧪 5. 테스트/유틸 구조 개선

pytest 기반 단위 테스트 추가

의약품 데이터 수집 스크립트 개선

Redis 없이, 서버에서 시간마다 이미지 검색 처리를 하도록, 검색 서버를 별도로 구현 

🗺 시연 PPT
https://docs.google.com/presentation/d/1BKcQu7VAuFIlppJSzQg8yMZ0Rw7T2qOT/edit?slide=id.g3a69ba4f913_2_1#slide=id.g3a69ba4f913_2_1

📌 API 명세

자세한 API 목록은 docs/api_spec.md 참고

📝 개발 중 해결한 핵심 문제들
1) YOLO의 names 속성 setter 에러

→ onnxmetadata 및 직접 매핑 테이블로 해결

2) DRF JSON decode error

→ 업로드 시기별 처리 분리 (Image/form-data → JSON 분리)

3) Refresh Token NameError

→ status 모듈 import 누락 해결

4) SQL & VS Code 연동

→ Docker 기반 DB → Remote Explorer 설정 문서화

📄 라이선스

개인 포트폴리오용으로만 사용됩니다.