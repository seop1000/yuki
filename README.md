# yuki

간단한 Discord 봇 예제입니다. `/깨우기` 를 입력하면 채팅에 올라온 명령 메시지를 삭제하고 `@everyone` 핑을 보냅니다.

## 준비
1. Python 3.10+ 설치.
2. 의존성 설치:
   ```bash
   pip install -r requirements.txt
   ```
3. Discord 개발자 포털에서 봇 토큰을 발급받고 `DISCORD_TOKEN` 환경 변수에 설정합니다.

## 실행
```bash
python bot.py
```

봇이 실행된 뒤 Discord 서버에서 `/깨우기` 를 입력하면 명령 메시지가 삭제되고 `@everyone` 이 전송됩니다. `mention_everyone` 권한이 있어야 정상 동작합니다.
