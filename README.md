# Newsletter Agent

LangGraph 기반 뉴스레터 에이전트. 같은 코드(`graph.py`)가 `AUDIENCE_CONFIG`
환경변수로 지정한 설정 파일(`audience.yaml`=AI 주제, `audience_security.yaml`=
보안 주제)에 따라 다른 분야의 뉴스레터를 수집·선별·요약·검수·발행한다.

이번 제출/리뷰 대상은 **보안 브리핑**이다 — 자세한 내용은 **[REPORT.md](REPORT.md)**
참고 (분야·독자 정의, 소스 채택표, 선별 로직, 파이프라인 구조도, 실행 기록,
이메일 채널 지원, 회고).

```bash
pip install -r requirements.txt
export OPENAI_API_KEY=sk-...        # 필수 (선별·요약·검수 전부 이 키를 씀)
AUDIENCE_CONFIG=audience_security.yaml python run.py --dry-run
```

**환경변수**:

| 변수 | 필수 여부 | 용도 |
|---|---|---|
| `OPENAI_API_KEY` | 필수 | 선별(②)·요약(③)·검수(④) 전부 |
| `DISCORD_WEBHOOK_URL` | 선택 | `--dry-run` 없이 Discord로 실제 발행할 때만 |
| `PUBLISH_CHANNEL=email` | 선택 | 지정하면 Discord 대신 이메일 노드로 발행 |
| `SMTP_HOST`/`SMTP_USER`/`SMTP_PASS`/`MAIL_TO` | 선택 | 이메일을 실제로 발송할 때만 (없으면 dry-run처럼 본문만 출력) |

`--dry-run`(또는 `DRY_RUN=1`)이면 `OPENAI_API_KEY`만 있어도 전체 파이프라인이
끝까지 돌고, 실제 발행(Discord/이메일) 없이 로그로 결과를 확인할 수 있다.

자동 실행: `.github/workflows/security.yml`(보안, 매일 07:40 KST) /
`.github/workflows/daily.yml`(AI, 매일 07:30 KST)
