# Newsletter Agent

LangGraph 기반 뉴스레터 에이전트. 같은 코드(`graph.py`)가 `AUDIENCE_CONFIG`
환경변수로 지정한 설정 파일(`audience.yaml`=AI 주제, `audience_security.yaml`=
보안 주제)에 따라 다른 분야의 뉴스레터를 수집·선별·요약·검수·발행한다.

이번 제출/리뷰 대상은 **보안 브리핑**이다 — 자세한 내용은 **[REPORT.md](REPORT.md)**
참고 (분야·독자 정의, 소스 채택표, 선별 로직, 파이프라인 구조도, 실행 기록,
이메일 채널 지원, 회고).

```bash
pip install -r requirements.txt
AUDIENCE_CONFIG=audience_security.yaml python run.py --dry-run
```

자동 실행: `.github/workflows/security.yml`(보안, 매일 07:40 KST) /
`.github/workflows/daily.yml`(AI, 매일 07:30 KST)
