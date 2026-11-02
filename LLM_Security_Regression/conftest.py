import sys
from pathlib import Path

# เพิ่ม path ของโฟลเดอร์ปัจจุบัน (root) เข้าไปใน Python path
sys.path.insert(0, str(Path(__file__).parent))