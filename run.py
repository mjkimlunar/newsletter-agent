import os
import sys
from graph import run                 # graph.py 에 있는 그 run()

if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # Windows 콘솔 대비 (Actions/리눅스에선 무해)
    except Exception:
        pass
    # 플래그 유무로 반드시 양쪽 다 명시한다 — 안 그러면 graph.py의 기본값("1", dry-run)이
    # 계속 남아 있어서 --dry-run을 안 줘도 실제 발행이 안 되는 조용한 실패가 난다.
    os.environ["DRY_RUN"] = "1" if "--dry-run" in sys.argv else "0"
    out = run()
    for line in out["log"]:
        print(line)                    # 이 출력이 Actions 로그에 그대로 남는다
