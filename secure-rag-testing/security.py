import re

USERS = {
    "alice": {"read"},
    "bob": set(),
}

DOCUMENTS = {
    "DOC-01": {
        "owner": "alice",
        "text": "Confidential incident report.",
    }
}

ALLOWED_TOOLS = {"get_report"}


def secure_retrieve(user_id: str, doc_id: str):
    """คืน document ถ้า user มีสิทธิ์อ่านและเป็นเจ้าของ"""
    if user_id not in USERS:
        return None

    if "read" not in USERS[user_id]:
        return None

    doc = DOCUMENTS.get(doc_id)
    if doc is None:
        return None

    if doc["owner"] != user_id:
        return None

    return doc


def validate_tool(tool_name: str) -> bool:
    """อนุญาตเฉพาะ tool ที่อยู่ใน allowlist"""
    return tool_name in ALLOWED_TOOLS


def validate_output(text: str) -> bool:
    """คืน False ถ้าพบ secret ใน output"""
    secret_pattern = r"sk-demo-[A-Za-z0-9]{12,}"
    return re.search(secret_pattern, text) is None