from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Chromeのオプション設定
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")  # ヘッドレスモード（新しい方式）
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# ChromeDriverのパスを明示的に指定
service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

# **新しいタブでColabを開く**
colab_url = "https://colab.research.google.com/drive/12E2d5Rcx4xUFLw1Uj5uQwWSp0cjh3uGb"
driver.execute_script(f"window.open('{colab_url}', '_blank');")

print("Colabを新しいタブで開きました")

# 10秒待機（デバッグ用）
import time
time.sleep(10)

# ブラウザを閉じる
driver.quit()
