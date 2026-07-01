from pathlib import Path

BASE = Path("/Users/Renata/Desktop/PANORAMICA/Páginas Webs/TERACT")


def read(name: str) -> str:
    return (BASE / name).read_text(encoding="utf-8")


def write(name: str, text: str) -> None:
    (BASE / name).write_text(text, encoding="utf-8")


def fix_en_switcher(text: str, es_file: str, en_file: str) -> str:
    text = text.replace('aria-label="Seleccionar idioma"', 'aria-label="Select language"')
    text = text.replace("<span>ES</span>", "<span>EN</span>", 2)
    text = text.replace(
        f'<a href="{es_file}" class="active">\n          <span>Español</span>\n        </a>\n        <a href="{en_file}">\n          <span>English</span>\n        </a>',
        f'<a href="{es_file}">\n          <span>Español</span>\n        </a>\n        <a href="{en_file}" class="active">\n          <span>English</span>\n        </a>',
    )
    return text


def apply(name: str, es_file: str, en_file: str, replacements: list[tuple[str, str]]) -> None:
    text = read(name)
    text = fix_en_switcher(text, es_file, en_file)
    for old, new in replacements:
        text = text.replace(old, new)
    write(name, text)


apply(
    "index-en.html",
    "index.html",
    "index-en.html",
    [
        ("Validación, pruebas comparativas y acuerdos bajo NDA.", "Validation, comparative testing and NDA-based agreements."),
    ],
)

apply(
    "rtn-null-cell-en.html",
    "rtn-null-cell.html",
    "rtn-null-cell-en.html",
    [
        ("Explora RTN-Null Cell bajo colaboración técnica", "Explore RTN-Null Cell under technical collaboration"),
        ("Hablemos de validación, NDA o colaboración técnica", "Let us talk about validation, NDA or technical collaboration"),
        ("Solicitudes de whitepaper, NDA o validación conjunta.", "Requests for whitepaper, NDA or joint validation."),
        ("Ruta de integración posterior al transistor", "Post-transistor integration path"),
    ],
)

apply(
    "hypergate-en.html",
    "hypergate.html",
    "hypergate-en.html",
    [
        ("Integración con high-k", "Integration with high-k"),
        ("Ruta hacia nodos avanzados", "Path toward advanced nodes"),
        ("Explora HyperGate V40 bajo colaboración técnica", "Explore HyperGate V40 under technical collaboration"),
        ("Hablemos de evaluación, integración o colaboración técnica", "Let us talk about evaluation, integration or technical collaboration"),
        ("Solicitudes de whitepaper, NDA o revisión técnica.", "Requests for whitepaper, NDA or technical review."),
    ],
)

apply(
    "rtn-null-cell-detalle-en.html",
    "rtn-null-cell-detalle.html",
    "rtn-null-cell-detalle-en.html",
    [
        ("Ruta compatible con manufactura CMOS BEOL.", "Path compatible with CMOS BEOL manufacturing."),
        ("Arquitectura funcional del dispositivo", "Functional device architecture"),
    ],
)

apply(
    "hypergate-detalle-en.html",
    "hypergate-detalle.html",
    "hypergate-detalle-en.html",
    [
        ("Ruta pensada para nodos sub-2nm y era Ángstrom.", "Path conceived for sub-2nm nodes and the Angstrom era."),
        ("Arquitectura funcional de compuerta", "Functional gate architecture"),
    ],
)
