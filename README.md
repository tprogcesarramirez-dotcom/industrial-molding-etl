# Automated Molding Report ETL via Ollama & Pydantic Validation

Pipeline de automatización e ingesta de datos no estructurados (ETL) para procesar reportes diarios del área de Moldeo e integrarlos a sistemas de reporte como Excel y Smartsheet, garantizando la calidad de los datos y la privacidad local.

---

## Arquitectura del Sistema

```text
[Texto No Estructurado]
          |
          v
[Ollama - qwen2.5:3b]
          |
          v
[Validación Pydantic]
          |
          v
[JSON Limpio]
          |
          v
[Data Store / Excel]
```

### Flujo de procesamiento

1. **Ingesta:** Captura de texto no estructurado enviado por supervisores vía correo o chat.
2. **Extracción:** Inferencia local con `qwen2.5:3b` mediante un esquema JSON definido.
3. **Validación:** Uso de **Pydantic v2** para validar los tipos de datos (`int`, `str`, `List`) antes de almacenarlos.
4. **Carga:** Generación de datos estructurados listos para insertarse en una base de datos o exportarse a tablas internas.

---

## Stack Técnico y Privacidad

- **LLM Engine:** [Ollama](https://ollama.com/) (`qwen2.5:3b`)
- **Validación de datos:** Pydantic v2
- **Lenguaje:** Python 3.10+
- **Formato de salida:** JSON

### Ventajas principales

- **Privacidad local:** El modelo puede ejecutarse localmente, evitando enviar los reportes a APIs externas durante la inferencia.
- **Sin costos por tokens:** No requiere pagar por cada llamada a una API externa; el hardware y el consumo eléctrico sí generan costos.
- **Ejecución local:** El procesamiento no depende de una conexión a internet una vez instalados el modelo y las dependencias.

---

## Guía de Instalación y Ejecución

### Prerrequisitos

- Python 3.10 o superior.
- [Ollama](https://ollama.com/) instalado y disponible en el sistema.
- Git instalado.
- Archivo `requirements.txt` con las dependencias del proyecto.

### 1. Clonar el repositorio

```bash
git clone https://github.com/tprogcesarramirez-dotcom/industrial-molding-etl.git
cd industrial-molding-etl
```

### 2. Descargar el modelo de Ollama

```bash
ollama pull qwen2.5:3b
```

### 3. Crear y activar el entorno virtual

En Linux o macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

En Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 4. Instalar las dependencias

```bash
python -m pip install -r requirements.txt
```

### 5. Ejecutar el pipeline ETL

```bash
PYTHONPATH=. python main.py
```

En Windows PowerShell, si `PYTHONPATH` no está configurado:

```powershell
$env:PYTHONPATH = "."
python main.py
```

---

## Esquema JSON Esperado

El pipeline busca generar una estructura de datos similar a la siguiente:

```json
{
  "machine_id": "M102",
  "downtime_minutes": 45,
  "approved_parts": 1200,
  "rejected_parts": 15,
  "reasons": [
    "defectos estéticos"
  ],
  "shift_leader": "Juan Pérez"
}
```

### Descripción de los campos

| Campo | Tipo | Descripción |
|---|---|---|
| `machine_id` | `str` | Identificador de la máquina |
| `downtime_minutes` | `int` | Minutos de inactividad |
| `approved_parts` | `int` | Cantidad de piezas aprobadas |
| `rejected_parts` | `int` | Cantidad de piezas rechazadas |
| `reasons` | `List[str]` | Motivos de rechazo o incidencias |
| `shift_leader` | `str` | Nombre del responsable del turno |

---

## Propuesta de Optimización de Procesos

Aunque esta solución demuestra el uso de modelos de lenguaje (LLMs) para extraer información de texto libre, una estrategia de ingeniería eficiente debe considerar la calidad de los datos desde su origen.

### Canal primario: captura estructurada

Implementar un formulario estandarizado mediante Microsoft Forms o Power Apps, con campos obligatorios y validaciones para reducir errores de captura y procesamiento innecesario.

### Canal secundario: extracción mediante IA

Mantener el pipeline con Ollama y Pydantic para procesar mensajes informales, correos, reportes de contingencia o texto libre.

### Beneficios esperados

- Mayor consistencia en los reportes de producción.
- Reducción de errores de captura manual.
- Validación de datos antes de su almacenamiento.
- Menor dependencia de servicios externos de IA.
- Integración futura con Excel, Smartsheet o bases de datos.

---

## Consideraciones de Seguridad y Calidad

- Validar los datos extraídos antes de almacenarlos.
- Gestionar correctamente los errores y las respuestas incompletas del modelo.
- Evitar incluir información confidencial en registros de depuración.
- Verificar que el modelo y sus dependencias estén instalados correctamente.
- Mantener protegidos los archivos de configuración y las credenciales.
- Considerar que la inferencia local no garantiza por sí sola la seguridad de todos los datos del sistema.

---

## Estado del Proyecto

Proyecto de automatización ETL enfocado en la extracción, validación y estructuración de reportes industriales mediante modelos de lenguaje ejecutados localmente.

**Objetivo:** transformar texto no estructurado en datos consistentes y listos para su integración en sistemas de análisis y reporte.
