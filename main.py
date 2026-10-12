import sys
from pathlib import Path

# Inyectar el directorio raíz del proyecto al path de Python
project_root = Path(__file__).resolve().parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

import json
from src.llm_parser import MoldingReportParser

def main():
    raw_text_path = "data/raw_sample.txt"
    print("=== INICIANDO PIPELINE ETL LOCAL CON OLLAMA ===")
    
    try:
        with open(raw_text_path, "r", encoding="utf-8") as f:
            raw_text = f.read()
        print(f"📄 Texto de entrada ({raw_text_path}):")
        print(f"'{raw_text}'\n")
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo '{raw_text_path}'.")
        return

    print("🤖 Procesando con el modelo local 'qwen2.5:3b'...")
    parser = MoldingReportParser(model_name="qwen2.5:3b")

    try:
        report = parser.parse_text(raw_text)
        json_result = report.model_dump_json(indent=2)
        
        print("\n✅ Extracción exitosa. JSON Resultante:")
        print(json_result)

        output_path = "data/output.json"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(json_result)
            
        print(f"\n💾 Guardado exitosamente en '{output_path}'")

    except Exception as e:
        print(f"\n❌ Error durante el procesamiento o validación: {e}")

if __name__ == "__main__":
    main()
