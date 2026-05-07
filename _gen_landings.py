#!/usr/bin/env python3
"""
One-shot generator for the 5 sector landing pages.
Each page is self-contained, on-brand with index.html, and SEO/AEO-ready.
"""

import os
import urllib.parse

PHONE_LOCAL = "643 199 580"
PHONE_E164  = "+34643199580"
WA_BASE     = "https://wa.me/34643199580?text="

SECTORS = [
    {
        "slug": "chatbot-peluquerias-madrid",
        "sector_lc": "peluquerías",
        "title": "Chatbot IA para Peluquerías en Madrid | WhiteMoon",
        "h1": "Chatbot IA para peluquerías en Madrid",
        "meta_desc": (
            "Chatbot IA con reservas automáticas para peluquerías en Madrid. "
            "Atiende citas 24/7 por WhatsApp. Majadahonda, Las Rozas, Boadilla. "
            "Desde 149€/mes."
        ),
        "service_name": "Chatbot IA para peluquerías en Madrid",
        "service_desc": (
            "Chatbot conversacional con IA para peluquerías y salones de belleza en Madrid. "
            "Reservas automáticas, recordatorios por WhatsApp, catálogo de servicios y "
            "atención 24/7. Servicio presencial en el noroeste de Madrid (Majadahonda, "
            "Las Rozas de Madrid, Boadilla del Monte, Pozuelo de Alarcón) y remoto en toda España."
        ),
        "wa_msg": "Hola WHITEMOON, tengo una peluquería en Madrid y me interesa el chatbot IA con reservas automáticas",
        "intro": (
            "Si tienes una peluquería en <strong>Majadahonda</strong>, <strong>Las Rozas de "
            "Madrid</strong>, <strong>Boadilla del Monte</strong>, <strong>Pozuelo de Alarcón</strong> o "
            "<strong>Madrid capital</strong>, sabes que las llamadas para pedir cita siempre "
            "entran en el peor momento: con tijeras en la mano, lavando, o secando. WhiteMoon "
            "instala un chatbot con inteligencia artificial que responde a tus clientes 24/7, "
            "reserva citas directamente en tu agenda y libera a tu equipo de la recepción."
        ),
        "pains": [
            ("📞", "Llamadas en hora punta",
             "Cada vez que suena el teléfono mientras estás cortando, pierdes concentración o "
             "cuelgas a un cliente. El chatbot atiende todas las consultas en paralelo, sin "
             "interrumpir tu trabajo."),
            ("⏰", "Citas perdidas fuera de horario",
             "El 40% de las reservas se piden de noche o fines de semana, cuando el salón está "
             "cerrado. Si no respondes, la cliente se va a la competencia o lo deja para luego "
             "y se olvida."),
            ("🚪", "No-shows y huecos vacíos",
             "Cancelaciones de última hora sin aviso significan horas pagadas a tu equipo sin "
             "facturación. El chatbot envía recordatorios automáticos y gestiona lista de "
             "espera para llenar huecos."),
        ],
        "use_cases": [
            ("📅", "Reservas automáticas 24/7",
             "El cliente escribe por WhatsApp, el chatbot consulta hueco en tu Google Calendar "
             "y confirma la cita al instante. Sin formularios, sin llamadas."),
            ("🔔", "Recordatorios y confirmaciones",
             "Aviso 24h antes pidiendo confirmación. Si la cliente cancela, el sistema ofrece "
             "el hueco a otra persona en lista de espera."),
            ("💇", "Catálogo de servicios y precios",
             "Color, mechas, alisado, tratamientos… El chatbot conoce tu carta y responde "
             "precios y duraciones sin que tengas que repetirlo cada vez."),
            ("🗓️", "Horarios, festivos y vacaciones",
             "Cierres por puente, días de descanso o vacaciones de verano: el chatbot avisa "
             "automáticamente y propone días alternativos."),
        ],
        "faqs": [
            ("¿El chatbot puede integrarse con mi agenda actual?",
             "Sí. Conectamos con Google Calendar, Outlook, sistemas POS de peluquería como "
             "Phorest o Treatwell, y la mayoría de agendas online del sector. Si usas papel "
             "o un Excel, también podemos automatizarlo."),
            ("¿Funciona si tengo varios estilistas con agendas distintas?",
             "Sí. El chatbot pregunta al cliente con quién quiere ir, comprueba la disponibilidad "
             "real de cada estilista y reserva en la agenda correcta. Sin solapes."),
            ("¿Y si la clienta quiere modificar o cancelar su cita?",
             "Lo hace por el mismo WhatsApp: el chatbot identifica la reserva, pregunta si "
             "quiere cambiar día/hora o cancelar, y libera el hueco automáticamente para que "
             "lo ocupe otra persona."),
            ("¿Cuánto cuesta para una peluquería pequeña?",
             "El pack Spark (149€/mes sin setup) cubre perfectamente una peluquería con 1-3 "
             "estilistas. Sin permanencia, baja cuando quieras. Operativo en 5-7 días desde la "
             "contratación."),
        ],
    },
    {
        "slug": "chatbot-talleres-mecanicos-madrid",
        "sector_lc": "talleres mecánicos",
        "title": "Chatbot IA para Talleres Mecánicos Madrid | WhiteMoon",
        "h1": "Chatbot IA para talleres mecánicos en Madrid",
        "meta_desc": (
            "Chatbot IA para talleres mecánicos en Madrid: presupuestos, estado del "
            "coche y citas 24/7 por WhatsApp. Majadahonda, Las Rozas, Pozuelo. Desde 149€/mes."
        ),
        "service_name": "Chatbot IA para talleres mecánicos en Madrid",
        "service_desc": (
            "Chatbot con inteligencia artificial para talleres mecánicos y de chapa-pintura en "
            "Madrid. Solicitud de presupuesto con foto, estado del vehículo, recordatorios de "
            "ITV/revisiones y citas automáticas. Servicio presencial en Majadahonda, Las Rozas "
            "de Madrid, Boadilla del Monte y Pozuelo de Alarcón. Remoto en toda España."
        ),
        "wa_msg": "Hola WHITEMOON, tengo un taller mecánico en Madrid y me interesa el chatbot IA",
        "intro": (
            "Si llevas un taller mecánico en <strong>Majadahonda</strong>, <strong>Las Rozas</strong>, "
            "<strong>Boadilla del Monte</strong>, <strong>Pozuelo de Alarcón</strong> o "
            "<strong>Madrid capital</strong>, conoces el problema: WhatsApp lleno de "
            "fotos de coches, preguntas por presupuestos y clientes que llaman para saber si "
            "su vehículo está listo. WhiteMoon implanta un chatbot IA que automatiza todo eso "
            "y te devuelve horas de productividad cada semana."
        ),
        "pains": [
            ("💬", "WhatsApp saturado de presupuestos",
             "Diez fotos al día de coches con la misma pregunta: «¿cuánto me costaría?». "
             "Responder uno a uno te quita tiempo del taller. El chatbot pre-cualifica y "
             "te pasa solo los casos serios."),
            ("📲", "«¿Está ya mi coche?»",
             "Llamadas constantes de clientes preguntando por el estado de su vehículo. El "
             "chatbot informa automáticamente: en diagnóstico, esperando piezas, listo para "
             "recoger."),
            ("📆", "ITV y revisiones que el cliente olvida",
             "Tus mejores clientes son los que vuelven. El chatbot envía recordatorios de "
             "ITV, cambio de aceite o revisión de los 30.000 km y propone cita directa."),
        ],
        "use_cases": [
            ("📸", "Presupuestos con foto",
             "El cliente envía foto del problema, el chatbot pregunta marca/modelo/año y "
             "deriva al mecánico con un brief listo para presupuestar."),
            ("🔧", "Estado del vehículo en tiempo real",
             "Actualizaciones automáticas: llegada al taller, diagnóstico realizado, piezas "
             "pedidas, reparación completa. El cliente sabe siempre dónde está su coche."),
            ("📅", "Citas para diagnóstico",
             "Reserva automática en el calendario del taller con tipo de servicio "
             "(diagnóstico, cambio aceite, ITV previa) y duración estimada."),
            ("🧾", "Recordatorios de servicio",
             "ITV, cambio de aceite, neumáticos. El chatbot recuerda al cliente cuándo toca "
             "y le ofrece cita directa sin tener que llamar."),
        ],
        "faqs": [
            ("¿Puede dar presupuestos cerrados sin verme el coche?",
             "Para reparaciones simples y mantenimiento sí (cambio de aceite, neumáticos, "
             "ITV previa). Para reparaciones complejas el chatbot da una horquilla orientativa "
             "y agenda diagnóstico físico para presupuesto cerrado."),
            ("¿Cómo funciona con piezas no estándar?",
             "El chatbot detecta cuando el caso requiere consulta humana (piezas de importación, "
             "averías raras, vehículos antiguos) y te lo escala con todo el contexto recopilado."),
            ("¿Avisa al cliente cuando el coche está listo?",
             "Sí. Cuando marcas la reparación como completada en tu sistema, el chatbot envía "
             "un mensaje al cliente con la factura, hora de recogida y cómo pagar."),
            ("¿Sirve para talleres pequeños de 2-3 mecánicos?",
             "Perfectamente. El pack Spark (149€/mes sin setup) es el más demandado por "
             "talleres pequeños del noroeste de Madrid. Sin permanencia."),
        ],
    },
    {
        "slug": "chatbot-clinicas-dentales-madrid",
        "sector_lc": "clínicas dentales",
        "title": "Chatbot IA para Clínicas Dentales Madrid | WhiteMoon",
        "h1": "Chatbot IA para clínicas dentales en Madrid",
        "meta_desc": (
            "Chatbot IA para clínicas dentales en Madrid: citas automáticas, triaje de "
            "urgencias y recordatorios por WhatsApp. Majadahonda, Pozuelo. Desde 149€/mes."
        ),
        "service_name": "Chatbot IA para clínicas dentales en Madrid",
        "service_desc": (
            "Chatbot IA para clínicas dentales y odontológicas en Madrid. Gestión automática "
            "de citas, triaje de urgencias dentales, recordatorios pre-cita y respuesta a "
            "dudas frecuentes (precios, mutuas, tratamientos). Servicio en Majadahonda, "
            "Las Rozas de Madrid, Boadilla del Monte, Pozuelo de Alarcón y Madrid capital."
        ),
        "wa_msg": "Hola WHITEMOON, tengo una clínica dental en Madrid y me interesa el chatbot IA con triaje de urgencias",
        "intro": (
            "Tu clínica dental en <strong>Majadahonda</strong>, <strong>Las Rozas de Madrid</strong>, "
            "<strong>Boadilla del Monte</strong>, <strong>Pozuelo de Alarcón</strong> o "
            "<strong>Madrid capital</strong> tiene un cuello de botella claro: la recepción. "
            "Limpiezas, urgencias, dudas sobre mutuas, pacientes que llaman para preguntar "
            "el precio de un blanqueamiento. WhiteMoon implanta un chatbot con IA que filtra, "
            "agenda y responde 24/7, dejando a tu recepcionista libre para lo importante."
        ),
        "pains": [
            ("☎️", "Recepción colapsada con dudas básicas",
             "«¿Cuánto cuesta una limpieza?», «¿trabajáis con Adeslas?», «¿abrís sábados?». "
             "El chatbot responde estas preguntas instantáneamente y solo escala cuando hace "
             "falta un humano."),
            ("🦷", "Urgencias fuera de horario sin canalizar",
             "Un paciente con dolor agudo a las 22:00 no debería tener que esperar al día "
             "siguiente. El chatbot hace triaje y avisa al dentista de guardia si la urgencia "
             "es real."),
            ("📵", "No-shows que matan tu agenda",
             "Cada hueco vacío son 80-200€ perdidos. El chatbot envía recordatorios "
             "automáticos 24h y 4h antes de la cita y reduce los no-shows hasta un 60%."),
        ],
        "use_cases": [
            ("📅", "Reserva de primera consulta o limpieza",
             "El paciente elige tipo de cita (revisión, limpieza, urgencia, ortodoncia), el "
             "chatbot ofrece huecos y reserva en tu sistema."),
            ("🚨", "Triaje de urgencias dentales",
             "Distingue entre dolor agudo, flemón, traumatismo o consulta no urgente. Si es "
             "real, escala al dentista de guardia con todo el contexto."),
            ("⏰", "Recordatorios pre-cita",
             "Mensajes automáticos 24h y 4h antes con instrucciones (no comer 2h antes en "
             "ciertos tratamientos, traer informes previos, etc.)."),
            ("💳", "Mutuas y precios orientativos",
             "El chatbot conoce con qué mutuas trabajáis (Sanitas, Adeslas, DKV, Mapfre…) y "
             "da precios orientativos para tratamientos privados habituales."),
        ],
        "faqs": [
            ("¿El chatbot cumple RGPD con datos de salud?",
             "Sí. No almacenamos historiales clínicos en el chatbot: solo datos de contacto y "
             "preferencia de cita. El triaje médico se limita a categorizar urgencia, no a "
             "diagnosticar. Cumplimos RGPD y normativa sanitaria española."),
            ("¿Distingue una urgencia real de una cita normal?",
             "Sí. El chatbot hace preguntas clínicas básicas (¿dolor del 1 al 10?, ¿flemón?, "
             "¿sangrado?, ¿traumatismo?) y clasifica en rojo (avisa al dentista), amarillo "
             "(cita 24h) o verde (agenda normal)."),
            ("¿Se integra con software como Dentalink, Klinic Cloud o Gesden?",
             "Sí, integramos con los principales sistemas de gestión odontológica. Si usáis "
             "uno menos común, lo conectamos vía API o automatizamos por email."),
            ("¿Qué pack me recomendáis para una clínica con 2 dentistas?",
             "El pack Core (1.800€ + 199€/mes) es el más equilibrado: web profesional + "
             "chatbot IA + reservas + integración con vuestro software. Operativo en 5-7 días."),
        ],
    },
    {
        "slug": "chatbot-gestorias-madrid",
        "sector_lc": "gestorías",
        "title": "Chatbot IA para Gestorías en Madrid | WhiteMoon",
        "h1": "Chatbot IA para gestorías en Madrid",
        "meta_desc": (
            "Chatbot IA para gestorías en Madrid: cualifica leads, responde dudas "
            "fiscales y agenda citas 24/7 por WhatsApp. Majadahonda, Las Rozas. Desde 149€/mes."
        ),
        "service_name": "Chatbot IA para gestorías en Madrid",
        "service_desc": (
            "Chatbot con inteligencia artificial para gestorías, asesorías fiscales y "
            "laborales en Madrid. Cualificación de leads (autónomo, pyme, particular), "
            "respuesta a dudas fiscales frecuentes, recordatorios de plazos AEAT y agenda "
            "automática de citas. Servicio en Majadahonda, Las Rozas de Madrid, Boadilla "
            "del Monte, Pozuelo de Alarcón y Madrid capital."
        ),
        "wa_msg": "Hola WHITEMOON, tengo una gestoría en Madrid y me interesa el chatbot IA para cualificar leads",
        "intro": (
            "Tu gestoría en <strong>Majadahonda</strong>, <strong>Las Rozas</strong>, "
            "<strong>Boadilla del Monte</strong>, <strong>Pozuelo de Alarcón</strong> o "
            "<strong>Madrid capital</strong> recibe a diario consultas que se repiten: "
            "«soy autónomo nuevo, ¿cuánto cuesta?», «¿hacéis IRPF?», «¿qué papeles necesito "
            "para una pyme?». WhiteMoon instala un chatbot con IA que cualifica al cliente, "
            "responde lo evidente y agenda solo a quien encaja realmente con tu cartera."
        ),
        "pains": [
            ("🔁", "Dudas fiscales repetidas todo el día",
             "Mismas preguntas sobre alta de autónomo, modelo 303, retenciones de IRPF. El "
             "chatbot responde lo estándar y solo escala lo que requiere asesoramiento real."),
            ("🎯", "Leads sin cualificar",
             "Particulares preguntando por declaraciones simples, pymes con potencial real, "
             "autónomos en alta… todos llegan al mismo email. El chatbot los segmenta antes "
             "de que entren en tu agenda."),
            ("📆", "Plazos AEAT que el cliente olvida",
             "Trimestres, modelos 111, 303, 130, declaración de la renta. El chatbot envía "
             "alertas automáticas a tus clientes con 7 días de antelación y les pide la "
             "documentación."),
        ],
        "use_cases": [
            ("🏷️", "Cualificación de leads",
             "Autónomo nuevo / pyme / sociedad / particular. El chatbot pregunta lo justo "
             "para clasificar y dirige al gestor adecuado con un brief."),
            ("📋", "Respuestas a dudas fiscales típicas",
             "Cuotas de autónomo en 2026, requisitos de tarifa plana, modelos trimestrales, "
             "diferencias entre estimación directa y módulos."),
            ("👤", "Agenda con el gestor adecuado",
             "Fiscal, laboral, contable, mercantil. El chatbot enruta a la persona "
             "especializada y reserva slot disponible."),
            ("⏳", "Alertas de plazos y documentación",
             "Recordatorios automáticos de fin de trimestre, modelos pendientes y solicitud "
             "de la documentación que falta para presentar."),
        ],
        "faqs": [
            ("¿El chatbot tiene acceso a los datos contables del cliente?",
             "No, por seguridad. El chatbot trabaja con información pública (plazos AEAT, "
             "tipos impositivos, requisitos generales) y datos del propio cliente que él mismo "
             "introduce. No accede a tus expedientes ni a software contable."),
            ("¿Distingue trimestres y plazos AEAT por tipo de cliente?",
             "Sí. Conoce el calendario fiscal completo (trimestrales 303, 111, 130, anuales "
             "390, 100, 200) y avisa según el régimen del cliente: estimación directa, "
             "módulos, sociedad limitada."),
            ("¿Cómo funcionan las alertas a mi equipo?",
             "Cuando un lead supera un umbral de potencial (pyme con +10 empleados, "
             "consultas complejas), el chatbot avisa por email o WhatsApp al socio o gestor "
             "responsable."),
            ("¿Qué pack encaja con una gestoría pequeña-mediana?",
             "Para gestorías de 2-5 personas, Core (1.800€ + 199€/mes). Para gestorías "
             "establecidas con cartera grande y muchos documentos propios, Scale RAG "
             "(3.500€ + 349€/mes), que entrena la IA con vuestros propios procedimientos."),
        ],
    },
    {
        "slug": "chatbot-abogados-madrid",
        "sector_lc": "despachos de abogados",
        "title": "Chatbot IA para Abogados en Madrid | WhiteMoon",
        "h1": "Chatbot IA para abogados en Madrid",
        "meta_desc": (
            "Chatbot IA para abogados en Madrid: triage legal, agenda de consultas y "
            "respuesta 24/7 por WhatsApp. Majadahonda, Las Rozas, Pozuelo. Desde 149€/mes."
        ),
        "service_name": "Chatbot IA para despachos de abogados en Madrid",
        "service_desc": (
            "Chatbot con inteligencia artificial para despachos de abogados en Madrid. "
            "Triage legal automático por área (civil, penal, laboral, familia, mercantil, "
            "bancario), clasificación de urgencia, agenda de consulta y respuesta 24/7. "
            "Servicio en Majadahonda, Las Rozas de Madrid, Boadilla del Monte, Pozuelo "
            "de Alarcón y Madrid capital."
        ),
        "wa_msg": "Hola WHITEMOON, tengo un despacho de abogados en Madrid y me interesa el chatbot IA con triage legal",
        "intro": (
            "Tu despacho en <strong>Majadahonda</strong>, <strong>Las Rozas de Madrid</strong>, "
            "<strong>Boadilla del Monte</strong>, <strong>Pozuelo de Alarcón</strong> o "
            "<strong>Madrid capital</strong> recibe consultas de áreas muy distintas: una "
            "separación, un despido improcedente, un conflicto bancario, una sucesión. "
            "WhiteMoon implanta un chatbot IA que hace triage legal automático, clasifica "
            "la urgencia y deriva al abogado especializado con un brief listo. Sin que tú "
            "tengas que filtrar todas las llamadas."
        ),
        "pains": [
            ("⚖️", "Cualificación manual del caso",
             "El cliente cuenta su problema, alguien tiene que decidir si es civil, laboral, "
             "penal o si encaja con vuestra especialidad. Horas de filtro que no se "
             "facturan."),
            ("🚨", "Urgencias mezcladas con consultas frías",
             "Un detenido a las 23:00 y una pregunta sobre un alquiler tienen igual peso en "
             "tu bandeja. El chatbot las separa: rojo (urgente), amarillo (24h), verde (cita "
             "en agenda)."),
            ("💼", "Casos fuera de tu especialidad",
             "Mucha consulta inicial no encaja con tu cartera. El chatbot identifica esos "
             "casos antes de que lleguen a la primera entrevista, ahorrándote tiempo y "
             "dándole al cliente una respuesta útil."),
        ],
        "use_cases": [
            ("🏛️", "Triage por área legal",
             "Familia, laboral, penal, civil, mercantil, bancario, revolving, microcréditos. "
             "El chatbot hace 4-6 preguntas y clasifica con precisión."),
            ("🚦", "Clasificación de urgencia",
             "Rojo (intervención inmediata: detención, embargo, plazo procesal a punto de "
             "vencer), amarillo (24-48h), verde (cita agendada en semana)."),
            ("📅", "Cita con abogado especializado",
             "Una vez clasificado, el chatbot agenda con el socio/asociado del área "
             "correspondiente y envía un brief con los datos clave."),
            ("📑", "Información sobre honorarios típicos",
             "Provisión de fondos, minuta orientativa por tipo de procedimiento, posibles "
             "vías de cobro (asistencia jurídica gratuita, segunda opinión, etc.)."),
        ],
        "faqs": [
            ("¿El chatbot cumple con el secreto profesional?",
             "Sí. La conversación se almacena cifrada y solo accede el abogado asignado al "
             "caso. No usamos los datos del cliente para entrenar la IA. Cumplimos RGPD y la "
             "normativa colegial sobre confidencialidad."),
            ("¿Cómo deriva al abogado correcto si tenemos varios socios?",
             "Configuramos reglas de routing por área de especialidad. Si tienes un socio "
             "especialista en penal y otra en familia, el chatbot lo sabe y enruta el caso "
             "a la persona correcta con todo el contexto recogido."),
            ("¿Se puede integrar con sistemas como Sentinel, Lex-On o Iurik?",
             "Sí. Integramos con los principales sistemas de gestión jurídica españoles vía "
             "API o webhooks. Las consultas entran ya creadas como expediente preliminar."),
            ("¿Qué pack es el más adecuado para un despacho boutique?",
             "Para despachos de 2-6 abogados sin documentación masiva, Core (1.800€ + 199€/mes). "
             "Si tenéis un volumen alto de jurisprudencia y procedimientos propios, "
             "Scale RAG (3.500€ + 349€/mes) entrena la IA con vuestros documentos."),
        ],
    },
]


def render_landing(s):
    canonical = f"https://whitemoon.es/{s['slug']}"
    wa_link = WA_BASE + urllib.parse.quote(s["wa_msg"])

    pains_html = "\n".join([
        f"""        <div class="card">
          <div class="card-icon">{icon}</div>
          <h3>{title}</h3>
          <p>{text}</p>
        </div>""" for icon, title, text in s["pains"]
    ])

    cases_html = "\n".join([
        f"""        <div class="card card-purple">
          <div class="card-icon">{icon}</div>
          <h3>{title}</h3>
          <p>{text}</p>
        </div>""" for icon, title, text in s["use_cases"]
    ])

    faqs_html = "\n".join([
        f"""        <details class="faq-item">
          <summary>{q}</summary>
          <p>{a}</p>
        </details>""" for q, a in s["faqs"]
    ])

    faq_jsonld = ",\n      ".join([
        f'{{ "@type": "Question", "name": {jsonstr(q)}, "acceptedAnswer": {{ "@type": "Answer", "text": {jsonstr(a)} }} }}'
        for q, a in s["faqs"]
    ])

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{s['title']}</title>
  <meta name="description" content="{s['meta_desc']}">
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
  <meta name="author" content="WhiteMoon Agencia IA">
  <meta name="geo.region" content="ES-MD">
  <meta name="geo.placename" content="Majadahonda, Madrid, España">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="es" href="{canonical}">
  <link rel="icon" type="image/png" href="../logo.png">

  <meta property="og:type" content="website">
  <meta property="og:locale" content="es_ES">
  <meta property="og:url" content="{canonical}">
  <meta property="og:title" content="{s['title']}">
  <meta property="og:description" content="{s['meta_desc']}">
  <meta property="og:image" content="https://whitemoon.es/og-image.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{s['title']}">
  <meta name="twitter:description" content="{s['meta_desc']}">

  <!-- ── SCHEMA SERVICE ── -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Service",
    "name": {jsonstr(s['service_name'])},
    "serviceType": "Chatbot con inteligencia artificial",
    "description": {jsonstr(s['service_desc'])},
    "provider": {{ "@id": "https://whitemoon.es/#negocio" }},
    "areaServed": [
      {{ "@type": "City", "name": "Majadahonda", "sameAs": "https://www.wikidata.org/wiki/Q493529" }},
      {{ "@type": "City", "name": "Las Rozas de Madrid", "sameAs": "https://www.wikidata.org/wiki/Q492816" }},
      {{ "@type": "City", "name": "Boadilla del Monte", "sameAs": "https://www.wikidata.org/wiki/Q493041" }},
      {{ "@type": "City", "name": "Pozuelo de Alarcón", "sameAs": "https://www.wikidata.org/wiki/Q492591" }},
      {{ "@type": "City", "name": "Madrid", "sameAs": "https://www.wikidata.org/wiki/Q2807" }}
    ],
    "availableChannel": {{
      "@type": "ServiceChannel",
      "serviceUrl": "https://whitemoon.es",
      "servicePhone": "{PHONE_E164}"
    }},
    "offers": [
      {{
        "@type": "Offer",
        "name": "Spark",
        "description": "Chatbot IA conversacional sin setup. Operativo en 48h.",
        "price": "149",
        "priceCurrency": "EUR",
        "priceSpecification": {{ "@type": "RecurringCharge", "billingPeriod": "P1M" }},
        "availability": "https://schema.org/InStock"
      }},
      {{
        "@type": "Offer",
        "name": "Core",
        "description": "Web profesional + chatbot IA + reservas. Operativo en 5-7 días.",
        "price": "199",
        "priceCurrency": "EUR",
        "priceSpecification": [
          {{ "@type": "RecurringCharge", "billingPeriod": "P1M" }},
          {{ "@type": "PriceSpecification", "name": "Setup", "price": "1800", "priceCurrency": "EUR" }}
        ],
        "availability": "https://schema.org/InStock"
      }},
      {{
        "@type": "Offer",
        "name": "Scale",
        "description": "Chatbot RAG con tus documentos para empresas medianas.",
        "price": "349",
        "priceCurrency": "EUR",
        "priceSpecification": [
          {{ "@type": "RecurringCharge", "billingPeriod": "P1M" }},
          {{ "@type": "PriceSpecification", "name": "Setup", "price": "3500", "priceCurrency": "EUR" }}
        ],
        "availability": "https://schema.org/InStock"
      }}
    ]
  }}
  </script>

  <!-- ── SCHEMA FAQ ── -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {faq_jsonld}
    ]
  }}
  </script>

  <!-- ── SCHEMA BREADCRUMB ── -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{ "@type": "ListItem", "position": 1, "name": "Inicio",  "item": "https://whitemoon.es/" }},
      {{ "@type": "ListItem", "position": 2, "name": "Sectores","item": "https://whitemoon.es/#servicios" }},
      {{ "@type": "ListItem", "position": 3, "name": {jsonstr(s['h1'])}, "item": "{canonical}" }}
    ]
  }}
  </script>

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

  <style>
    *,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
    html{{scroll-behavior:smooth}}
    :root{{
      --p:#7c4dff;--p2:#9d70ff;--g:#00d4aa;--wa:#25D366;--wa-dark:#128C7E;
      --bg:#08080d;--bg2:#0e0e16;--card:#111118;
      --border:rgba(124,77,255,.22);--border-soft:rgba(124,77,255,.12);
      --text:#f0f0f5;--muted:#8888a0;--max:1100px;--r:14px;
    }}
    body{{font-family:'Inter',-apple-system,BlinkMacSystemFont,sans-serif;background:var(--bg);color:var(--text);line-height:1.6;-webkit-font-smoothing:antialiased}}
    a{{color:inherit;text-decoration:none}}
    .wrap{{max-width:var(--max);margin:0 auto;padding:0 24px}}
    h1,h2,h3{{line-height:1.2;letter-spacing:-.01em}}
    p{{color:var(--muted)}}

    /* NAV */
    .nav{{position:sticky;top:0;z-index:50;background:rgba(8,8,13,.85);backdrop-filter:blur(12px);border-bottom:1px solid var(--border-soft)}}
    .nav-inner{{display:flex;align-items:center;justify-content:space-between;padding:14px 0}}
    .nav-logo img{{height:40px;width:auto}}
    .nav-back{{font-size:.85rem;color:var(--muted);display:inline-flex;align-items:center;gap:8px;transition:color .2s}}
    .nav-back:hover{{color:var(--p2)}}
    .nav-cta{{display:inline-flex;align-items:center;gap:8px;padding:10px 18px;background:linear-gradient(135deg,var(--p),#5b21b6);color:#fff;border-radius:10px;font-size:.85rem;font-weight:600}}
    .nav-cta:hover{{box-shadow:0 8px 24px rgba(124,77,255,.4)}}

    /* HERO */
    .hero{{padding:80px 0 60px;background:radial-gradient(ellipse at 20% 30%,rgba(124,77,255,.12),transparent 60%),radial-gradient(ellipse at 80% 70%,rgba(0,212,170,.08),transparent 60%)}}
    .hero h1{{font-size:clamp(2rem,4.5vw,3.2rem);font-weight:800;margin-bottom:18px;color:#fff;background:linear-gradient(135deg,#fff 0%,#c9b6ff 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent}}
    .hero .lead{{font-size:1.05rem;line-height:1.7;color:var(--muted);max-width:720px;margin-bottom:32px}}
    .hero .lead strong{{color:#fff;font-weight:600}}
    .hero-ctas{{display:flex;flex-wrap:wrap;gap:14px}}
    .btn-wa{{display:inline-flex;align-items:center;gap:10px;padding:14px 24px;background:var(--wa);color:#fff;border-radius:12px;font-weight:700;font-size:.95rem;transition:all .25s;box-shadow:0 8px 24px rgba(37,211,102,.3)}}
    .btn-wa:hover{{background:var(--wa-dark);box-shadow:0 12px 32px rgba(37,211,102,.45);transform:translateY(-1px)}}
    .btn-ghost{{display:inline-flex;align-items:center;gap:10px;padding:14px 24px;background:transparent;border:1px solid var(--border);color:var(--text);border-radius:12px;font-weight:600;font-size:.9rem;transition:all .25s}}
    .btn-ghost:hover{{background:rgba(124,77,255,.08);border-color:var(--p2)}}

    /* SECTIONS */
    .sec{{padding:70px 0;border-top:1px solid var(--border-soft)}}
    .sec-lbl{{display:inline-block;padding:5px 14px;background:rgba(124,77,255,.1);border:1px solid var(--border);border-radius:20px;font-size:.7rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--p2);margin-bottom:14px}}
    .sec h2{{font-size:clamp(1.5rem,3vw,2.1rem);font-weight:800;color:#fff;margin-bottom:14px}}
    .sec .sub{{font-size:1rem;color:var(--muted);max-width:640px;margin-bottom:36px}}

    .grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}}
    .grid-4{{display:grid;grid-template-columns:repeat(2,1fr);gap:18px}}
    @media(max-width:780px){{.grid,.grid-4{{grid-template-columns:1fr}}}}
    .card{{background:var(--card);border:1px solid var(--border);border-radius:var(--r);padding:24px;transition:transform .25s,border-color .25s}}
    .card:hover{{transform:translateY(-2px);border-color:var(--p2)}}
    .card-icon{{font-size:1.6rem;margin-bottom:12px}}
    .card h3{{font-size:1rem;font-weight:700;color:#fff;margin-bottom:8px}}
    .card p{{font-size:.9rem;line-height:1.6;color:var(--muted);margin:0}}
    .card-purple{{background:linear-gradient(180deg,rgba(124,77,255,.06),rgba(124,77,255,.02));border-color:rgba(124,77,255,.28)}}

    /* PACKS */
    .packs{{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:8px}}
    @media(max-width:780px){{.packs{{grid-template-columns:1fr}}}}
    .pack{{background:var(--card);border:1px solid var(--border);border-radius:18px;padding:28px;position:relative}}
    .pack.featured{{border-color:var(--p2);box-shadow:0 12px 40px rgba(124,77,255,.2)}}
    .pack-name{{font-size:1.2rem;font-weight:800;color:#fff;margin-bottom:6px}}
    .pack-desc{{font-size:.82rem;color:var(--muted);margin-bottom:16px}}
    .pack-price{{font-size:1.6rem;font-weight:800;color:#fff;margin-bottom:4px}}
    .pack-price .small{{font-size:.95rem;color:var(--muted);font-weight:400}}
    .pack-setup{{font-size:.78rem;color:var(--muted);margin-bottom:16px}}
    .pack ul{{list-style:none;padding:0;margin:0 0 18px}}
    .pack li{{font-size:.85rem;color:var(--text);padding:5px 0;display:flex;gap:8px}}
    .pack li::before{{content:'✓';color:var(--g);font-weight:700;flex-shrink:0}}
    .pack-cta{{display:block;text-align:center;padding:11px;background:rgba(124,77,255,.1);border:1px solid var(--border);border-radius:10px;color:var(--p2);font-size:.85rem;font-weight:600;transition:all .2s}}
    .pack-cta:hover{{background:var(--p);color:#fff;border-color:var(--p)}}

    /* FAQ */
    .faq-list{{max-width:760px}}
    .faq-item{{background:rgba(124,77,255,.04);border:1px solid var(--border-soft);border-radius:12px;padding:18px 22px;margin-bottom:10px}}
    .faq-item summary{{font-weight:600;font-size:.95rem;color:#fff;cursor:pointer;list-style:none}}
    .faq-item summary::-webkit-details-marker{{display:none}}
    .faq-item summary::after{{content:'+';float:right;color:var(--p2);font-weight:700;transition:transform .2s}}
    .faq-item[open] summary::after{{transform:rotate(45deg)}}
    .faq-item p{{margin-top:14px;font-size:.9rem;line-height:1.7;color:var(--muted)}}

    /* CTA FINAL */
    .cta-final{{background:linear-gradient(135deg,rgba(124,77,255,.12),rgba(0,212,170,.06));border:1px solid var(--border);border-radius:20px;padding:48px;text-align:center;margin:30px 0}}
    .cta-final h2{{font-size:1.8rem;color:#fff;margin-bottom:12px}}
    .cta-final p{{font-size:1rem;color:var(--muted);margin-bottom:28px;max-width:520px;margin-left:auto;margin-right:auto}}

    /* FOOTER */
    footer{{padding:50px 0 30px;border-top:1px solid var(--border-soft);background:#06060a;margin-top:60px}}
    .foot-grid{{display:grid;grid-template-columns:1.5fr 1fr 1fr;gap:40px;margin-bottom:28px}}
    @media(max-width:780px){{.foot-grid{{grid-template-columns:1fr;gap:28px}}}}
    .foot-grid h4{{font-size:.7rem;font-weight:700;text-transform:uppercase;letter-spacing:.14em;color:var(--p2);margin-bottom:14px}}
    .foot-grid p,.foot-grid a{{font-size:.85rem;color:var(--muted);line-height:1.7;display:block}}
    .foot-grid a:hover{{color:var(--p2)}}
    .foot-bottom{{padding-top:24px;border-top:1px solid var(--border-soft);font-size:.78rem;color:var(--muted);display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px}}
    .foot-bottom a{{color:var(--p2)}}
  </style>
</head>
<body>

<nav class="nav">
  <div class="wrap nav-inner">
    <a href="https://whitemoon.es/" class="nav-logo" aria-label="Volver a WhiteMoon">
      <img src="../logo.png" alt="WhiteMoon Agencia IA" width="180" height="82" loading="eager">
    </a>
    <a href="https://whitemoon.es/" class="nav-back">← Volver a whitemoon.es</a>
    <a href="{wa_link}" class="nav-cta" target="_blank" rel="noopener">WhatsApp</a>
  </div>
</nav>

<header class="hero">
  <div class="wrap">
    <span class="sec-lbl">Sector · {s['sector_lc'].title()}</span>
    <h1>{s['h1']}</h1>
    <p class="lead">{s['intro']}</p>
    <div class="hero-ctas">
      <a class="btn-wa" href="{wa_link}" target="_blank" rel="noopener">
        <svg width="18" height="18" viewBox="0 0 32 32" fill="currentColor"><path d="M16 2C8.268 2 2 8.268 2 16c0 2.49.638 4.83 1.757 6.865L2 30l7.331-1.724A13.916 13.916 0 0016 30c7.732 0 14-6.268 14-14S23.732 2 16 2z"/></svg>
        Hablar por WhatsApp · {PHONE_LOCAL}
      </a>
      <a class="btn-ghost" href="https://whitemoon.es/#precios">Ver packs y precios</a>
    </div>
  </div>
</header>

<section class="sec">
  <div class="wrap">
    <span class="sec-lbl">Problema</span>
    <h2>Lo que pasa hoy en {s['sector_lc']} sin un chatbot IA</h2>
    <p class="sub">Tres cuellos de botella que oímos cada semana en despachos del noroeste de Madrid.</p>
    <div class="grid">
{pains_html}
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <span class="sec-lbl">Casos de uso</span>
    <h2>Lo que automatiza nuestro chatbot en {s['sector_lc']}</h2>
    <p class="sub">Sin scripts rígidos. La IA entiende lenguaje natural y se adapta a cómo escriben tus clientes.</p>
    <div class="grid-4">
{cases_html}
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <span class="sec-lbl">Por qué WhiteMoon</span>
    <h2>Agencia local de IA en el noroeste de Madrid</h2>
    <p class="sub">WhiteMoon es una agencia española de inteligencia artificial fundada en 2023, con sede en Calle Madrid 9, Majadahonda. Atendemos presencialmente <strong style="color:#fff">Majadahonda</strong>, <strong style="color:#fff">Las Rozas de Madrid</strong>, <strong style="color:#fff">Boadilla del Monte</strong>, <strong style="color:#fff">Pozuelo de Alarcón</strong> y <strong style="color:#fff">Madrid capital</strong>. Implementación en 5-7 días laborables, sin permanencia, soporte directo por WhatsApp.</p>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <span class="sec-lbl">Precios</span>
    <h2>Tres packs según tu tamaño</h2>
    <p class="sub">Todos los precios sin IVA. Sin permanencia.</p>
    <div class="packs">
      <div class="pack">
        <div class="pack-name">Spark</div>
        <div class="pack-desc">Chatbot IA conversacional para negocios pequeños.</div>
        <div class="pack-price">149€<span class="small">/mes</span></div>
        <div class="pack-setup">Sin setup · Sin permanencia · Operativo en 48h</div>
        <ul>
          <li>Chatbot IA en tu web o WhatsApp</li>
          <li>Reservas y captación de leads</li>
          <li>Actualizaciones incluidas</li>
        </ul>
        <a class="pack-cta" href="{wa_link}" target="_blank" rel="noopener">Solicitar Spark</a>
      </div>
      <div class="pack featured">
        <div class="pack-name">Core ⭐</div>
        <div class="pack-desc">Web profesional + chatbot IA + reservas. La opción más completa.</div>
        <div class="pack-price">1.800€<span class="small"> setup</span></div>
        <div class="pack-setup">+ 199€/mes · Operativo en 5-7 días</div>
        <ul>
          <li>Web profesional con dominio incluido</li>
          <li>Chatbot IA conversacional</li>
          <li>Sistema de reservas integrado</li>
          <li>SEO básico configurado</li>
        </ul>
        <a class="pack-cta" href="{wa_link}" target="_blank" rel="noopener">Solicitar Core</a>
      </div>
      <div class="pack">
        <div class="pack-name">Scale</div>
        <div class="pack-desc">Chatbot RAG entrenado con tus documentos. Para empresas medianas.</div>
        <div class="pack-price">3.500€<span class="small"> setup</span></div>
        <div class="pack-setup">+ 349€/mes · Operativo en 7-10 días</div>
        <ul>
          <li>RAG sobre 200+ documentos propios</li>
          <li>2.000 consultas/mes</li>
          <li>Captura de leads + analíticas</li>
          <li>Soporte prioritario</li>
        </ul>
        <a class="pack-cta" href="{wa_link}" target="_blank" rel="noopener">Solicitar Scale</a>
      </div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <span class="sec-lbl">FAQ</span>
    <h2>Preguntas frecuentes sobre {s['sector_lc']}</h2>
    <div class="faq-list">
{faqs_html}
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="cta-final">
      <h2>Hablemos de tu {s['sector_lc'][:-1] if s['sector_lc'].endswith('s') else s['sector_lc']}</h2>
      <p>Sin formularios, sin esperas. Te contamos en 5 minutos cómo encajaría el chatbot en tu día a día y qué pack tiene más sentido para tu volumen.</p>
      <a class="btn-wa" href="{wa_link}" target="_blank" rel="noopener" style="font-size:1rem;padding:16px 32px">
        <svg width="18" height="18" viewBox="0 0 32 32" fill="currentColor"><path d="M16 2C8.268 2 2 8.268 2 16c0 2.49.638 4.83 1.757 6.865L2 30l7.331-1.724A13.916 13.916 0 0016 30c7.732 0 14-6.268 14-14S23.732 2 16 2z"/></svg>
        Escribir a {PHONE_LOCAL}
      </a>
    </div>
  </div>
</section>

<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <h4>WhiteMoon Agencia IA</h4>
        <p>Agencia de inteligencia artificial en Majadahonda y Madrid. Chatbots, RAG y automatización para pymes y autónomos.</p>
        <p style="margin-top:12px"><a href="https://whitemoon.es/">← Volver a whitemoon.es</a></p>
      </div>
      <div>
        <h4>Contacto</h4>
        <a href="tel:{PHONE_E164}">{PHONE_LOCAL}</a>
        <a href="mailto:comercial@whitemoon.es">comercial@whitemoon.es</a>
        <p style="margin-top:6px">Calle Madrid 9, 2ºB<br>28220 Majadahonda, Madrid</p>
      </div>
      <div>
        <h4>Otras landings</h4>
        <a href="/chatbot-peluquerias-madrid">Peluquerías</a>
        <a href="/chatbot-talleres-mecanicos-madrid">Talleres mecánicos</a>
        <a href="/chatbot-clinicas-dentales-madrid">Clínicas dentales</a>
        <a href="/chatbot-gestorias-madrid">Gestorías</a>
        <a href="/chatbot-abogados-madrid">Abogados</a>
      </div>
    </div>
    <div class="foot-bottom">
      <span>© WhiteMoon Agencia IA · Majadahonda, Madrid</span>
      <a href="https://whitemoon.es/">whitemoon.es</a>
    </div>
  </div>
</footer>

</body>
</html>
"""


def jsonstr(s):
    """JSON-encode a string, including the surrounding quotes."""
    import json as _json
    return _json.dumps(s, ensure_ascii=False)


def main():
    for s in SECTORS:
        d = s["slug"]
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(render_landing(s))
        print(f"wrote {d}/index.html")


if __name__ == "__main__":
    main()
