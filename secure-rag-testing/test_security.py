from security import (
    secure_retrieve,
    validate_tool,
    validate_output,
)


# ---------- secure_retrieve ----------

def test_authorized_user():
    result = secure_retrieve("alice", "DOC-01")
    assert result is not None
    assert result["owner"] == "alice"


def test_unauthorized_user():
    result = secure_retrieve("bob", "DOC-01")
    assert result is None


def test_unknown_user():
    result = secure_retrieve("unknown", "DOC-01")
    assert result is None


def test_unknown_document():
    result = secure_retrieve("alice", "DOC-99")
    assert result is None


# ---------- validate_tool ----------

def test_allowed_tool():
    assert validate_tool("get_report") is True


def test_unknown_tool():
    assert validate_tool("delete_all") is False


# ---------- validate_output ----------

def test_safe_output():
    assert validate_output("CPU usage is 80%.") is True


def test_secret_output():
    text = "API key: sk-demo-ABCDEF1234567890"
    assert validate_output(text) is False


def test_short_secret_suffix_is_safe():
    # น้อยกว่า 12 ตัวอักษร ไม่ถือว่าเป็น secret
    assert validate_output("sk-demo-ABC") is True