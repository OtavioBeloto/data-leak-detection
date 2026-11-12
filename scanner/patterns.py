import re

PADROES = {
    "email": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    "cpf": re.compile(r"\b(?:\d{11}|\d{3}\.\d{3}\.\d{3}-\d{2})\b"),
    "senha": re.compile(r"(?i)\b(?:senha|password|passwd|pwd)\s*[:=]\s*\S+")
}