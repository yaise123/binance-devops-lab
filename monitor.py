import os
import requests
import time

#配置
CONTAINER_NAME = "web-server"
URL = "http://localhost:8080"

def check_status():
    print(f"[{time.strftime('%X')}] 正在檢察系統狀態")

    docker_status = os.popen(f"docker inspect -f '{{{{.State.Running}}}}' {CONTAINER_NAME} 2>/dev/null").read().strip()

    if docker_status != "true":
        return "❌ 錯誤：Docker 容器已停止工作！"

    try:
        response = requests.get(URL,timeout=3)
        if response.status_code ==200:
            return "✅ 正常：容器運作中且網頁可正常訪問。"
        else:
            return f"⚠️ 警告：容器在跑，但網頁回傳錯誤代碼: {response.status_code                }"
    except:
        return "❌ 錯誤：無法連線到網頁，服務可能崩潰了。"
if __name__ == "__main__":
    result = check_status()
    print(result)

