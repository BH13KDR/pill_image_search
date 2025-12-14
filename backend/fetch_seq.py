import requests
from urllib.parse import quote

API_KEY = "S2EwY+1X17CjDD9b0ECOAznTouqL6fc1bf89TGQ4BGQMHQ1o0jiOtjeYvDfRLeIVVC0vV1eS5ryaEHE15Kldtw=="
BASE_URL = "https://apis.data.go.kr/1471000/DrbEasyDrugInfoService/getDrbEasyDrugList"


def fetch_item_seq(name: str):
    params = {
        "serviceKey": API_KEY,
        "type": "json",
        "pageNo": 1,
        "numOfRows": 30,
        "itemName": name,
    }

    resp = requests.get(BASE_URL, params=params, timeout=10)

    try:
        data = resp.json()
    except:
        print("JSON decode error:", resp.text)
        return []

    # 응답 구조 표준화
    body = data.get("body") \
        or data.get("response", {}).get("body") \
        or {}

    items = body.get("items") or []

    seq_list = []
    for it in items:
        seq = it.get("itemSeq") or it.get("ITEM_SEQ")
        nm = it.get("itemName") or it.get("ITEM_NAME")
        if seq:
            seq_list.append((nm, seq))

    return seq_list


if __name__ == "__main__":
    drug_list = [
        "오피큐탄",
        "웰러드연질캡슐",
        "멀티큐텐플러스정",
        "유니테리드",
        "유니카민정",
        "뉴글리아정",
        "게스타렌투엑스정",
        "디아셀캡슐",
        "아펜탈CR서방정",
        "카나가바로틴캡슐",
        "세바코에이치씨티정",
        "경동파니틴정",
        "아나콕스캡슐",
        "라자렉트정",
        "레비에필정",
        "브이타민정",
        "티뮤즈연질캡슐",
        "동성라베프라졸정",
        "토바스트정",
        # 여기에 22개 리스트 추가
    ]

    for drug in drug_list:
        seqs = fetch_item_seq(drug)
        print(f"🔍 {drug} 검색 결과:")

        if not seqs:
            print("  ➜ 검색 결과 없음\n")
            continue

        for nm, seq in seqs:
            print(f"  • {nm} → {seq}")
        print()
