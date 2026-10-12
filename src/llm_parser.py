import json
from typing import Dict, Any
import ollama
from src.config.schema import MoldingReport

class MoldingReportParser:
    def __init__(self, model_name: str = "qwen2.5:3b"):
        self.model_name = model_name

    def parse_text(self, raw_text: str) -> MoldingReport:
        system_prompt = (
            "Eres un sistema experto de extracción de datos en plantas de moldeo. "
            "Extrae la información clave del reporte de entrada. "
            "Si un dato no está presente en el texto, asigna null o lista vacía según corresponda."
        )

        response = ollama.chat(
            model=self.model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": raw_text}
            ],
            format=MoldingReport.model_json_schema(),
            options={"temperature": 0.0}
        )

        raw_json = response['message']['content']
        validated_report = MoldingReport.model_validate_json(raw_json)
        return validated_report
