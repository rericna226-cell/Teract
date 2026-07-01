from pathlib import Path

BASE = Path("/Users/Renata/Desktop/PANORAMICA/Páginas Webs/TERACT")


def read(name: str) -> str:
    return (BASE / name).read_text(encoding="utf-8")


def write(name: str, text: str) -> None:
    (BASE / name).write_text(text, encoding="utf-8")


def apply_replacements(text: str, replacements: list[tuple[str, str]]) -> str:
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def insert_lang_assets(text: str, current_lang: str, es_file: str, en_file: str, theme: str) -> str:
    if 'id="langSwitcher"' in text:
        return text

    desktop_css_dark = """    .lang-switcher {
      position: relative;
      margin-left: 18px;
    }

    .lang {
      appearance: none;
      height: 42px;
      padding: 0 14px;
      border-radius: 999px;
      border: 1px solid rgba(255,255,255,0.14);
      background: rgba(255,255,255,0.1);
      color: inherit;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-weight: 700;
      font-size: 14px;
      letter-spacing: 0.02em;
      cursor: pointer;
    }

    .lang-caret {
      color: rgba(255,255,255,0.68);
      font-size: 12px;
      transition: transform 0.15s ease;
    }

    .lang-switcher.open .lang-caret {
      transform: rotate(180deg);
    }

    .lang-menu {
      position: absolute;
      top: calc(100% + 10px);
      right: 0;
      min-width: 180px;
      padding: 8px;
      border-radius: 18px;
      border: 1px solid rgba(12,20,34,0.12);
      background: rgba(255,255,255,0.98);
      box-shadow: 0 24px 80px rgba(0,0,0,0.18);
      display: grid;
      gap: 6px;
      z-index: 110;
    }

    .lang-menu a {
      display: flex;
      align-items: center;
      padding: 12px;
      border-radius: 14px;
      color: #0c1422;
      font-size: 14px;
      font-weight: 700;
      border: 1px solid transparent;
      background: transparent;
    }

    .lang-menu a:hover,
    .lang-menu a.active {
      background: rgba(12,20,34,0.04);
      border-color: rgba(12,20,34,0.06);
    }
"""

    desktop_css_light = """    .lang-switcher {
      position: relative;
      margin-left: 18px;
    }

    .lang {
      appearance: none;
      height: 42px;
      padding: 0 14px;
      border-radius: 999px;
      border: 1px solid rgba(12,20,34,0.12);
      background: rgba(255,255,255,0.42);
      color: inherit;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-weight: 700;
      font-size: 14px;
      letter-spacing: 0.02em;
      cursor: pointer;
    }

    .lang-caret {
      color: rgba(12,20,34,0.56);
      font-size: 12px;
      transition: transform 0.15s ease;
    }

    .lang-switcher.open .lang-caret {
      transform: rotate(180deg);
    }

    .lang-menu {
      position: absolute;
      top: calc(100% + 10px);
      right: 0;
      min-width: 180px;
      padding: 8px;
      border-radius: 18px;
      border: 1px solid rgba(12,20,34,0.12);
      background: rgba(255,255,255,0.98);
      box-shadow: 0 24px 80px rgba(0,0,0,0.18);
      display: grid;
      gap: 6px;
      z-index: 110;
    }

    .lang-menu a {
      display: flex;
      align-items: center;
      padding: 12px;
      border-radius: 14px;
      color: #0c1422;
      font-size: 14px;
      font-weight: 700;
      border: 1px solid transparent;
      background: transparent;
    }

    .lang-menu a:hover,
    .lang-menu a.active {
      background: rgba(12,20,34,0.04);
      border-color: rgba(12,20,34,0.06);
    }
"""

    mobile_css_dark = """    .mobile-menu .lang-switcher {
      width: 100%;
      margin-left: 0;
    }

    .mobile-menu .lang {
      width: 100%;
      justify-content: space-between;
      height: auto;
      padding: 12px;
      border-radius: 14px;
      font-size: 15px;
      color: inherit;
      background: rgba(255,255,255,0.04);
      border: 1px solid rgba(255,255,255,0.08);
    }

    .mobile-menu .lang-caret {
      color: rgba(255,255,255,0.56);
    }

    .mobile-menu .lang-menu {
      position: static;
      min-width: 0;
      padding: 8px 0 0;
      border-radius: 0;
      border: 0;
      background: transparent;
      box-shadow: none;
      gap: 8px;
    }

    .mobile-menu .lang-menu a {
      color: inherit;
      background: rgba(255,255,255,0.04);
      border: 1px solid rgba(255,255,255,0.08);
    }
"""

    mobile_css_light = """    .mobile-menu .lang-switcher {
      width: 100%;
      margin-left: 0;
    }

    .mobile-menu .lang {
      width: 100%;
      justify-content: space-between;
      height: auto;
      padding: 12px;
      border-radius: 14px;
      font-size: 15px;
      color: #0c1422;
      background: rgba(12,20,34,0.03);
      border: 1px solid rgba(12,20,34,0.06);
    }

    .mobile-menu .lang-caret {
      color: rgba(12,20,34,0.56);
    }

    .mobile-menu .lang-menu {
      position: static;
      min-width: 0;
      padding: 8px 0 0;
      border-radius: 0;
      border: 0;
      background: transparent;
      box-shadow: none;
      gap: 8px;
    }

    .mobile-menu .lang-menu a {
      color: #0c1422;
      background: rgba(12,20,34,0.03);
      border: 1px solid rgba(12,20,34,0.06);
    }
"""

    lang_script = """
    (() => {
      function initLang(switcherId, toggleId, menuId) {
        const switcher = document.getElementById(switcherId);
        const toggle = document.getElementById(toggleId);
        const menu = document.getElementById(menuId);

        if (!switcher || !toggle || !menu) return;

        function close() {
          menu.hidden = true;
          switcher.classList.remove("open");
          toggle.setAttribute("aria-expanded", "false");
        }

        function open() {
          menu.hidden = false;
          switcher.classList.add("open");
          toggle.setAttribute("aria-expanded", "true");
        }

        toggle.addEventListener("click", (event) => {
          event.stopPropagation();
          if (menu.hidden) open();
          else close();
        });

        document.addEventListener("click", (event) => {
          if (!switcher.contains(event.target)) close();
        });

        document.addEventListener("keydown", (event) => {
          if (event.key === "Escape") close();
        });
      }

      initLang("langSwitcher", "langToggle", "langMenu");
      initLang("langSwitcherMobile", "langToggleMobile", "langMenuMobile");
    })();
"""

    text = text.replace(
        "    .nav-toggle {",
        (desktop_css_dark if theme == "dark" else desktop_css_light) + "    .nav-toggle {",
        1,
    )
    text = text.replace(
        "    .mobile-backdrop[hidden],\n    .mobile-menu[hidden] {",
        "    .mobile-backdrop[hidden],\n    .mobile-menu[hidden],\n    .lang-menu[hidden] {",
        1,
    )
    text = text.replace(
        "    section { padding:",
        (mobile_css_dark if theme == "dark" else mobile_css_light) + "    section { padding:",
        1,
    )
    text = text.replace(
        "      .nav-links {\n        display: none;\n      }",
        "      .nav-links,\n      .navbar > .lang-switcher {\n        display: none;\n      }",
        1,
    )

    if current_lang == "es":
        aria = "Seleccionar idioma"
        current_code = "ES"
        es_link = f'<a href="{es_file}" class="active">\n          <span>Español</span>\n        </a>'
        en_link = f'<a href="{en_file}">\n          <span>English</span>\n        </a>'
    else:
        aria = "Select language"
        current_code = "EN"
        es_link = f'<a href="{es_file}">\n          <span>Español</span>\n        </a>'
        en_link = f'<a href="{en_file}" class="active">\n          <span>English</span>\n        </a>'

    desktop_html = f"""    <div class="lang-switcher" id="langSwitcher">
      <button class="lang" type="button" aria-label="{aria}" aria-haspopup="true" aria-expanded="false" aria-controls="langMenu" id="langToggle">
        <span>{current_code}</span>
        <span class="lang-caret" aria-hidden="true">⌄</span>
      </button>
      <div class="lang-menu" id="langMenu" hidden>
        {es_link}
        {en_link}
      </div>
    </div>
"""

    mobile_html = f"""    <div class="lang-switcher mobile" id="langSwitcherMobile">
      <button class="lang" type="button" aria-label="{aria}" aria-haspopup="true" aria-expanded="false" aria-controls="langMenuMobile" id="langToggleMobile">
        <span>{current_code}</span>
        <span class="lang-caret" aria-hidden="true">⌄</span>
      </button>
      <div class="lang-menu" id="langMenuMobile" hidden>
        {es_link}
        {en_link}
      </div>
    </div>
"""

    text = text.replace(
        '    <button class="nav-toggle" id="navToggle"',
        desktop_html + '    <button class="nav-toggle" id="navToggle"',
        1,
    )

    if "  </div>\n\n  <!-- HERO -->" in text:
        text = text.replace("  </div>\n\n  <!-- HERO -->", mobile_html + "  </div>\n\n  <!-- HERO -->", 1)
    else:
        text = text.replace("  </div>\n\n  <section class=\"hero\">", mobile_html + "  </div>\n\n  <section class=\"hero\">", 1)

    text = text.replace("  </script>", lang_script + "  </script>", 1)
    return text


def build_en(
    src_name: str,
    dst_name: str,
    theme: str,
    title: str,
    extra_replacements: list[tuple[str, str]],
) -> None:
    text = read(src_name)
    text = apply_replacements(
        text,
        [
            ('<html lang="es">', '<html lang="en">'),
            ('href="index.html"', 'href="index-en.html"'),
            ('href="rtn-null-cell.html"', 'href="rtn-null-cell-en.html"'),
            ('href="hypergate.html"', 'href="hypergate-en.html"'),
            ('href="rtn-null-cell-detalle.html"', 'href="rtn-null-cell-detalle-en.html"'),
            ('href="hypergate-detalle.html"', 'href="hypergate-detalle-en.html"'),
            ('href="politica-privacidad.html"', 'href="politica-privacidad-en.html"'),
            ('>Inicio<', '>Home<'),
            ('>Contáctanos<', '>Contact<'),
            ('aria-label="Abrir menú"', 'aria-label="Open menu"'),
            ('Política de Privacidad', 'Privacy Notice'),
            ('Puebla, México', 'Puebla, Mexico'),
            ('TERACT Semiconductores', 'TERACT Semiconductors'),
            ('© 2026 TERACT Semiconductores. Todos los derechos reservados.', '© 2026 TERACT Semiconductors. All rights reserved.'),
            ('<title>', f'<title>{title}'),
        ]
        + extra_replacements,
    )
    text = insert_lang_assets(text, "en", src_name, dst_name, theme)
    write(dst_name, text)


PAGES_ES = [
    ("index.html", "index-en.html", "dark"),
    ("rtn-null-cell.html", "rtn-null-cell-en.html", "light"),
    ("hypergate.html", "hypergate-en.html", "light"),
    ("rtn-null-cell-detalle.html", "rtn-null-cell-detalle-en.html", "dark"),
    ("hypergate-detalle.html", "hypergate-detalle-en.html", "dark"),
]

for es_name, en_name, theme in PAGES_ES:
    write(es_name, insert_lang_assets(read(es_name), "es", es_name, en_name, theme))

privacy_en = read("politica-privacidad-en.html")
privacy_en = apply_replacements(
    privacy_en,
    [
        ('href="index.html#contacto"', 'href="index-en.html#contacto"'),
        ('href="index.html"', 'href="index-en.html"'),
        ('href="rtn-null-cell.html"', 'href="rtn-null-cell-en.html"'),
        ('href="hypergate.html"', 'href="hypergate-en.html"'),
        ('<a class="btn btn-primary" href="index.html">Back to TERACT</a>', '<a class="btn btn-primary" href="index-en.html">Back to TERACT</a>'),
        ('<a class="btn btn-secondary" href="mailto:contacto@teract.com">Email contacto@teract.com</a>', '<a class="btn btn-secondary" href="index-en.html#contacto">Go to contact form</a>'),
    ],
)
write("politica-privacidad-en.html", privacy_en)

index_extra = [
    ("TERACT Semiconductores", "TERACT Semiconductors"),
    ("Semiconductores · Memristor · Transistor", "Semiconductors · Memristor · Transistor"),
    ("Infraestructura Semiconductor para la Próxima Era del Cómputo", "Semiconductor Infrastructure for the Next Era of Computing"),
    ("Desarrollamos arquitecturas avanzadas para memoria y transistores,", "We develop advanced architectures for memory and transistors,"),
    ("enfocadas en estabilidad, eficiencia energética y escalabilidad para", "focused on stability, energy efficiency and scalability for"),
    ("sistemas de alto rendimiento.", "high-performance systems."),
    (">Explorar tecnologías<", ">Explore technologies<"),
    (">Contactar<", ">Contact us<"),
    ("Infraestructura para IA", "Infrastructure for AI"),
    ("La base física del cómputo moderno está cambiando", "The physical foundation of modern computing is changing"),
    ("Nuestras tecnologías", "Our technologies"),
    (">Ver RTN-Null Cell<", ">See RTN-Null Cell<"),
    (">Ver HyperGate<", ">See HyperGate<"),
    ("Ecosistema TERACT", "TERACT Ecosystem"),
    (">Iniciar conversación<", ">Start the conversation<"),
    ("Nuestra Dirección Tecnológica", "Our Technology Direction"),
    ("Rendimiento Escalable", "Scalable Performance"),
    ("Eficiencia Energética", "Energy Efficiency"),
    ("Compatibilidad Industrial", "Industrial Compatibility"),
    ("Validación Conjunta", "Joint Validation"),
    ("Estructuración Comercial Flexible", "Flexible Commercial Structuring"),
    ("Proceso de colaboración", "Collaboration process"),
    ("Primero entendemos el caso. Después definimos la ruta.", "We first understand the case. Then we define the path."),
    ("Diagnóstico técnico y estratégico", "Technical and strategic diagnosis"),
    ("Validación controlada", "Controlled validation"),
    ("Estructuración comercial flexible", "Flexible commercial structuring"),
    ("Integración o transferencia acordada", "Agreed integration or transfer"),
    ("Divulgación progresiva:", "Progressive disclosure:"),
    ("Validación y colaboración", "Validation and collaboration"),
    ("De la arquitectura matemática a la validación física", "From mathematical architecture to physical validation"),
    (">Solicitar conversación técnica<", ">Request a technical conversation<"),
    ("Contáctanos", "Contact us"),
    ("Hablemos de colaboración técnica", "Let us talk about technical collaboration"),
    ("Solicita una conversación", "Request a conversation"),
    ("Nombre", "Name"),
    ("Empresa o institución", "Company or institution"),
    ("Rol / cargo", "Role / title"),
    ("Etapa", "Stage"),
    ("Selecciona una etapa", "Select a stage"),
    ('value="explorando"', 'value="exploring"'),
    ('value="evaluando"', 'value="evaluating"'),
    ('value="listo-validar"', 'value="ready-to-validate"'),
    ("Explorando", "Exploring"),
    ("Evaluando", "Evaluating"),
    ("Listo para validar", "Ready to validate"),
    ("Interés", "Interest"),
    ("Selecciona una opción", "Select an option"),
    ("Validación técnica", "Technical validation"),
    ("Explorar estructura comercial", "Explore commercial structure"),
    ("Inversión deep-tech", "Deep-tech investment"),
    ("Alianza estratégica", "Strategic partnership"),
    ("Conversación técnica", "Technical conversation"),
    ("Otro", "Other"),
    ("Mensaje", "Message"),
    ("Oficina Central", "Head Office"),
    ("Arquitecturas avanzadas para memoria, transistor y cómputo de próxima generación.", "Advanced architectures for memory, transistor and next-generation computing."),
    ("Validacion tecnica - TERACT", "Technical validation - TERACT"),
    ("Explorar estructura comercial - TERACT", "Explore commercial structure - TERACT"),
    ("Interes de inversion deep-tech - TERACT", "Deep-tech investment interest - TERACT"),
    ("Alianza estrategica - TERACT", "Strategic partnership - TERACT"),
    ("Conversacion tecnica - TERACT", "Technical conversation - TERACT"),
    ("Consulta general - TERACT", "General inquiry - TERACT"),
    ("Empresa o institucion: ", "Company or institution: "),
    ("Rol / cargo: ", "Role / title: "),
    ("Etapa: ", "Stage: "),
    ("Interes: ", "Interest: "),
    ("Abriendo tu cliente de correo...", "Opening your email client..."),
]

rtn_extra = [
    ("RTN-Null Cell: Arquitectura ReRAM para Estabilidad de Lectura", "RTN-Null Cell: ReRAM Architecture for Read Stability"),
    ("Memristor · Redefiniendo la pureza de la señal", "Memristor · Redefining signal purity"),
    (">Explorar tecnología<", ">Explore technology<"),
    (">Solicitar whitepaper<", ">Request whitepaper<"),
    ("El problema", "The problem"),
    ("La solución", "The solution"),
    ("Ventajas esperadas", "Expected advantages"),
    ("Manufactura", "Manufacturing"),
    ("HfO₂ mediante ALD", "HfO2 via ALD"),
    ("Modulación de estequiometría", "Stoichiometry modulation"),
    ("Integración BEOL", "BEOL integration"),
    ("Proceso compatible con flujo industrial", "Industrial-flow-compatible process"),
    ("Ruta de validación", "Validation path"),
    ("Whitepaper y contacto técnico", "Whitepaper and technical contact"),
    (">Ver detalle técnico<", ">See technical detail<"),
    ("Contacto técnico", "Technical contact"),
    ("Solicita información técnica", "Request technical information"),
    ("Nombre", "Name"),
    ("Empresa o institución", "Company or institution"),
    ("Rol / cargo", "Role / title"),
    ("Etapa", "Stage"),
    ("Selecciona una etapa", "Select a stage"),
    ('value="explorando"', 'value="exploring"'),
    ('value="evaluando"', 'value="evaluating"'),
    ('value="listo-validar"', 'value="ready-to-validate"'),
    ("Explorando", "Exploring"),
    ("Evaluando", "Evaluating"),
    ("Listo para validar", "Ready to validate"),
    ("Interés", "Interest"),
    ("Selecciona una opción", "Select an option"),
    ("Revisar whitepaper", "Review whitepaper"),
    ("Solicitud de NDA", "NDA request"),
    ("Validación técnica ReRAM", "ReRAM technical validation"),
    ("Explorar estructura comercial", "Explore commercial structure"),
    ("Conversación técnica", "Technical conversation"),
    ("Otro", "Other"),
    ("Mensaje", "Message"),
    ("Oficina Central", "Head Office"),
    ("Solicitud de whitepaper - RTN-Null Cell", "Whitepaper request - RTN-Null Cell"),
    ("Solicitud de NDA - RTN-Null Cell", "NDA request - RTN-Null Cell"),
    ("Validacion tecnica ReRAM - RTN-Null Cell", "ReRAM technical validation - RTN-Null Cell"),
    ("Explorar estructura comercial - RTN-Null Cell", "Explore commercial structure - RTN-Null Cell"),
    ("Conversacion tecnica - RTN-Null Cell", "Technical conversation - RTN-Null Cell"),
    ("Consulta tecnica - RTN-Null Cell", "Technical inquiry - RTN-Null Cell"),
    ("Empresa o institucion: ", "Company or institution: "),
    ("Rol / cargo: ", "Role / title: "),
    ("Etapa: ", "Stage: "),
    ("Interes: ", "Interest: "),
    ("Abriendo tu cliente de correo...", "Opening your email client..."),
]

hyper_extra = [
    ("HyperGate V40: Gate Stack para la Era Sub-2nm", "HyperGate V40: Gate Stack for the Sub-2nm Era"),
    ("Transistor · Una nueva dimensión de rendimiento", "Transistor · A new dimension of performance"),
    (">Explorar tecnología<", ">Explore technology<"),
    (">Solicitar whitepaper<", ">Request whitepaper<"),
    ("El problema", "The problem"),
    ("La solución", "The solution"),
    ("Ventajas esperadas", "Expected advantages"),
    ("Mercado objetivo", "Target market"),
    ("Diseñadores fabless", "Fabless designers"),
    ("IA y HPC", "AI and HPC"),
    ("Ruta de validación", "Validation path"),
    ("Caracterización C-V", "C-V characterization"),
    ("Mediciones I-V", "I-V measurements"),
    ("Lote de control", "Control lot"),
    ("Whitepaper y contacto técnico", "Whitepaper and technical contact"),
    (">Ver detalle técnico<", ">See technical detail<"),
    ("Contacto técnico", "Technical contact"),
    ("Solicita información técnica", "Request technical information"),
    ("Nombre", "Name"),
    ("Empresa o institución", "Company or institution"),
    ("Rol / cargo", "Role / title"),
    ("Etapa", "Stage"),
    ("Selecciona una etapa", "Select a stage"),
    ('value="explorando"', 'value="exploring"'),
    ('value="evaluando"', 'value="evaluating"'),
    ('value="listo-validar"', 'value="ready-to-validate"'),
    ("Explorando", "Exploring"),
    ("Evaluando", "Evaluating"),
    ("Listo para validar", "Ready to validate"),
    ("Interés", "Interest"),
    ("Selecciona una opción", "Select an option"),
    ("Revisar whitepaper", "Review whitepaper"),
    ("Solicitud de NDA", "NDA request"),
    ("Validación GAA-FET", "GAA-FET validation"),
    ("Integración con foundry o fabless", "Foundry or fabless integration"),
    ("Conversación técnica", "Technical conversation"),
    ("Otro", "Other"),
    ("Mensaje", "Message"),
    ("Oficina Central", "Head Office"),
    ("Solicitud de whitepaper - HyperGate V40", "Whitepaper request - HyperGate V40"),
    ("Solicitud de NDA - HyperGate V40", "NDA request - HyperGate V40"),
    ("Validacion GAA-FET - HyperGate V40", "GAA-FET validation - HyperGate V40"),
    ("Integracion con foundry o fabless - HyperGate V40", "Foundry or fabless integration - HyperGate V40"),
    ("Conversacion tecnica - HyperGate V40", "Technical conversation - HyperGate V40"),
    ("Consulta tecnica - HyperGate V40", "Technical inquiry - HyperGate V40"),
    ("Empresa o institucion: ", "Company or institution: "),
    ("Rol / cargo: ", "Role / title: "),
    ("Etapa: ", "Stage: "),
    ("Interes: ", "Interest: "),
    ("Abriendo tu cliente de correo...", "Opening your email client..."),
]

detail_rtn_extra = [
    ("Detalle ampliado de arquitectura y validación", "Extended architecture and validation detail"),
    ("Principio de diseño", "Design principle"),
    ("Esquema del stack", "Stack scheme"),
    ("Capa superior", "Top layer"),
    ("Electrodo superior", "Top electrode"),
    ("Región activa", "Active region"),
    ("Región de soporte", "Support region"),
    ("Subcapa de switching", "Switching sublayer"),
    ("Subcapa bulk aislante", "Insulating bulk sublayer"),
    ("Capa inferior", "Bottom layer"),
    ("Electrodo inferior", "Bottom electrode"),
    ("KPIs esperados", "Expected KPIs"),
    ("Métricas objetivo, sujetas a validación", "Target metrics, subject to validation"),
    ("A validar", "To validate"),
    ("Estabilidad de lectura", "Read stability"),
    ("Ruido reducido", "Reduced noise"),
    ("Ruta multinivel", "Multilevel path"),
    ("Ruta experimental ampliada", "Expanded experimental path"),
    ("Secuencia de evaluación propuesta", "Proposed evaluation sequence"),
    ("1. Lote comparativo inicial", "1. Initial comparative lot"),
    ("2. Caracterización eléctrica", "2. Electrical characterization"),
    ("3. Análisis de ruido", "3. Noise analysis"),
    ("4. Evaluación de integración", "4. Integration assessment"),
    ("Siguiente paso", "Next step"),
    ("Solicita whitepaper o conversación técnica", "Request whitepaper or technical conversation"),
    (">Solicitar whitepaper<", ">Request whitepaper<"),
    (">Volver a RTN-Null Cell<", ">Back to RTN-Null Cell<"),
]

detail_hyper_extra = [
    ("Detalle ampliado de arquitectura y validación", "Extended architecture and validation detail"),
    ("Principio de diseño", "Design principle"),
    ("Esquema del stack", "Stack scheme"),
    ("Región superior", "Upper region"),
    ("Región dieléctrica", "Dielectric region"),
    ("Capa high-k de soporte", "Supporting high-k layer"),
    ("Interfaz crítica", "Critical interface"),
    ("Capa interfacial calibrada", "Calibrated interfacial layer"),
    ("Región activa", "Active region"),
    ("KPIs esperados", "Expected KPIs"),
    ("Métricas objetivo, sujetas a validación", "Target metrics, subject to validation"),
    ("A validar", "To validate"),
    ("Leakage reducido", "Reduced leakage"),
    ("Control electrostático", "Electrostatic control"),
    ("Eficiencia energética", "Energy efficiency"),
    ("Ruta experimental ampliada", "Expanded experimental path"),
    ("Secuencia de evaluación propuesta", "Proposed evaluation sequence"),
    ("1. Test wafer inicial", "1. Initial test wafer"),
    ("2. Barridos C-V", "2. C-V sweeps"),
    ("3. Barridos I-V", "3. I-V sweeps"),
    ("4. Benchmark contra control", "4. Benchmark against control"),
    ("Siguiente paso", "Next step"),
    ("Solicita whitepaper o conversación técnica", "Request whitepaper or technical conversation"),
    (">Solicitar whitepaper<", ">Request whitepaper<"),
    (">Volver a HyperGate V40<", ">Back to HyperGate V40<"),
]

build_en("index.html", "index-en.html", "dark", "TERACT Semiconductors</title>", index_extra)
build_en("rtn-null-cell.html", "rtn-null-cell-en.html", "light", "RTN-Null Cell | TERACT Semiconductors</title>", rtn_extra)
build_en("hypergate.html", "hypergate-en.html", "light", "HyperGate V40 | TERACT Semiconductors</title>", hyper_extra)
build_en("rtn-null-cell-detalle.html", "rtn-null-cell-detalle-en.html", "dark", "RTN-Null Cell Detail | TERACT</title>", detail_rtn_extra)
build_en("hypergate-detalle.html", "hypergate-detalle-en.html", "dark", "HyperGate V40 Detail | TERACT</title>", detail_hyper_extra)
