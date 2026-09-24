import re
import os

with open(r'g:\Seo\carpinteria web\index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract header and footer
parts1 = index_content.split('<main>')
head_and_header = parts1[0] + '<main>'

parts2 = index_content.split('<!-- ═══════════════════ FOOTER ═══════════════════ -->')
footer_and_scripts = '<!-- ═══════════════════ FOOTER ═══════════════════ -->' + parts2[1]

def generate_page(config):
    # Clone header and modify metas
    hh = head_and_header
    hh = re.sub(r'<title>.*?</title>', f'<title>{config["title"]}</title>', hh)
    hh = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{config["description"]}">', hh)
    hh = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="https://carpinteriaalicante.com/{config["slug"]}">', hh)
    hh = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{config["title"]}">', hh)
    hh = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{config["description"]}">', hh)
    hh = re.sub(r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="https://carpinteriaalicante.com/{config["slug"]}">', hh)
    hh = re.sub(r'<meta property="og:image" content=".*?">', f'<meta property="og:image" content="{config["hero_image"]}">', hh)

    # Replace all WA links
    hh = re.sub(r'https://wa\.me/34600000000\?text=[^"]+', config['wa_link'], hh)
    fs = footer_and_scripts
    fs = re.sub(r'https://wa\.me/34600000000\?text=[^"]+', config['wa_link'], fs)

    main_content = f"""
    <!-- ═══════════════════ HERO INTERNO ═══════════════════ -->
    <section class="relative pt-24 lg:pt-32 pb-16 lg:pb-24 flex items-center justify-center min-h-[40vh] overflow-hidden">
        <!-- Background -->
        <div class="absolute inset-0">
            <img src="{config['hero_image']}" alt="{config['h1']}" class="w-full h-full object-cover object-center hero-bg" loading="eager">
            <div class="absolute inset-0 bg-black/60"></div>
            <!-- Subtle gradient to blend with the white section below -->
            <div class="absolute inset-0 bg-gradient-to-t from-wood-50 via-transparent to-transparent"></div>
        </div>

        <div class="relative z-10 w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center reveal">
            <h1 class="font-display text-4xl md:text-5xl lg:text-6xl font-bold text-white tracking-tight mb-4 leading-tight drop-shadow-lg">
                {config['h1']}
            </h1>
            <p class="text-lg md:text-xl text-white/90 max-w-2xl mx-auto drop-shadow-md">
                {config['hero_subtitle']}
            </p>
        </div>
    </section>

    <!-- ═══════════════════ CONTENIDO Y SIDEBAR ═══════════════════ -->
    <section class="py-16 lg:py-24 relative bg-wood-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex flex-col lg:flex-row gap-12 lg:gap-16">
                
                <!-- Contenido principal (70%) -->
                <div class="w-full lg:w-[70%]">
                    <article class="prose prose-lg prose-wood max-w-none text-wood-800 reveal">
                        <h2 class="font-display text-3xl md:text-4xl font-bold text-wood-950 mb-8 tracking-tight">{config['h2']}</h2>
                        
                        {config['content_html']}
                    </article>

                    <!-- FAQS / Método -->
                    <div class="mt-16 reveal border-t border-wood-200/60 pt-12">
                        <h3 class="font-display text-2xl font-bold text-wood-950 mb-8">Nuestro método de trabajo</h3>
                        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                            <div class="bg-white p-8 rounded-3xl shadow-sm border border-wood-100 relative hover:shadow-md transition-shadow">
                                <div class="absolute -top-5 -left-5 w-12 h-12 bg-wood-800 text-white flex items-center justify-center font-bold text-xl rounded-full shadow-lg">1</div>
                                <h4 class="font-bold text-wood-900 mb-2 mt-2">Contáctanos</h4>
                                <p class="text-sm text-wood-600 leading-relaxed">Escríbenos por WhatsApp o llámanos. Cuéntanos qué necesitas (medidas aproximadas, fotos).</p>
                            </div>
                            <div class="bg-white p-8 rounded-3xl shadow-sm border border-wood-100 relative hover:shadow-md transition-shadow">
                                <div class="absolute -top-5 -left-5 w-12 h-12 bg-wood-800 text-white flex items-center justify-center font-bold text-xl rounded-full shadow-lg">2</div>
                                <h4 class="font-bold text-wood-900 mb-2 mt-2">Medimos y Presupuestamos</h4>
                                <p class="text-sm text-wood-600 leading-relaxed">Un técnico se desplazará a tu domicilio para tomar medidas exactas y darte un presupuesto cerrado, sin sorpresas.</p>
                            </div>
                            <div class="bg-white p-8 rounded-3xl shadow-sm border border-wood-100 relative hover:shadow-md transition-shadow">
                                <div class="absolute -top-5 -left-5 w-12 h-12 bg-whatsapp text-white flex items-center justify-center font-bold text-xl rounded-full shadow-lg">3</div>
                                <h4 class="font-bold text-wood-900 mb-2 mt-2">Instalación Limpia</h4>
                                <p class="text-sm text-wood-600 leading-relaxed">Fabricamos a medida y montamos de forma rápida y limpia. Retiramos el material antiguo si es necesario.</p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Sidebar Sticky (30%) -->
                <aside class="w-full lg:w-[30%] relative">
                    <div class="sticky top-28 bg-white rounded-3xl p-8 shadow-2xl shadow-wood-900/10 border border-wood-100 text-center reveal transition-transform hover:-translate-y-1 duration-300">
                        <div class="w-20 h-20 bg-gradient-to-br from-whatsapp-light to-whatsapp/20 rounded-full flex items-center justify-center mx-auto mb-6">
                            <svg class="w-10 h-10 text-whatsapp-dark" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
                        </div>
                        <h3 class="font-display text-3xl font-bold text-wood-950 mb-4">¿Necesitas este servicio?</h3>
                        <p class="text-wood-600 mb-8 leading-relaxed text-lg">
                            Pide tu <strong>presupuesto rápido, gratis y sin compromiso</strong> en menos de 5 minutos.
                        </p>
                        <a href="{config['wa_link']}" target="_blank" rel="noopener noreferrer"
                           class="wa-glow w-full inline-flex items-center justify-center gap-3 bg-whatsapp hover:bg-whatsapp-hover text-white font-bold text-xl px-8 py-5 rounded-2xl shadow-xl shadow-whatsapp/30 transition-all active:scale-95">
                            Pedir Presupuesto
                        </a>
                        
                        <div class="mt-8 pt-6 border-t border-wood-100 flex flex-col gap-3 text-sm text-wood-600 font-medium">
                            <span class="flex items-center justify-center gap-2">
                                <svg class="w-5 h-5 text-whatsapp" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                                Trato directo, sin intermediarios
                            </span>
                            <span class="flex items-center justify-center gap-2">
                                <svg class="w-5 h-5 text-whatsapp" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                                Calidad garantizada
                            </span>
                        </div>
                    </div>
                </aside>

            </div>
        </div>
    </section>
    """

    full_html = hh + main_content + fs
    
    file_path = fr'g:\Seo\carpinteria web\{config["slug"]}.html'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f'Generado {config["slug"]}.html')

# 1. Regenerate Aluminio
aluminio_content = """
<p class="mb-6 leading-relaxed">
    Si buscas <strong>aluminios Alicante</strong> de máxima calidad, somos tu mejor opción. Nos especializamos en la fabricación y montaje de soluciones a medida tanto en aluminio como en PVC, ofreciendo el equilibrio perfecto entre estética, durabilidad y aislamiento térmico.
</p>

<p class="mb-8 leading-relaxed">
    Como expertos en <strong>carpinteria de aluminio en alicante</strong>, sabemos que una buena ventana o un cerramiento bien instalado no solo mejora el aspecto de tu hogar, sino que reduce drásticamente tus facturas de luz y gas al aislar la vivienda del frío, el calor y el ruido exterior.
</p>

<div class="bg-white p-8 rounded-3xl shadow-sm border border-wood-100 mb-10">
    <h3 class="font-bold text-2xl text-wood-950 mb-6 flex items-center gap-3">
        <svg class="w-8 h-8 text-whatsapp" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/></svg>
        Ventajas de nuestras Ventanas de Aluminio y PVC
    </h3>
    <ul class="space-y-4 list-none pl-0 m-0">
        <li class="flex items-start gap-4">
            <div class="w-8 h-8 rounded-full bg-whatsapp/10 flex items-center justify-center shrink-0 mt-0.5">
                <svg class="w-5 h-5 text-whatsapp-dark" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
            </div>
            <span class="text-wood-700 leading-relaxed"><strong class="text-wood-950">Eficiencia Energética (Rotura de Puente Térmico):</strong> Aislamiento total que mantiene la temperatura ideal de tu casa todo el año.</span>
        </li>
        <li class="flex items-start gap-4">
            <div class="w-8 h-8 rounded-full bg-whatsapp/10 flex items-center justify-center shrink-0 mt-0.5">
                <svg class="w-5 h-5 text-whatsapp-dark" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
            </div>
            <span class="text-wood-700 leading-relaxed"><strong class="text-wood-950">Aislamiento Acústico:</strong> Cristales Climalit de alto rendimiento para disfrutar del silencio total en el interior.</span>
        </li>
        <li class="flex items-start gap-4">
            <div class="w-8 h-8 rounded-full bg-whatsapp/10 flex items-center justify-center shrink-0 mt-0.5">
                <svg class="w-5 h-5 text-whatsapp-dark" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
            </div>
            <span class="text-wood-700 leading-relaxed"><strong class="text-wood-950">Alta Durabilidad:</strong> Materiales resistentes a la humedad, al sol y a la corrosión marina (ideal para zonas de costa).</span>
        </li>
        <li class="flex items-start gap-4">
            <div class="w-8 h-8 rounded-full bg-whatsapp/10 flex items-center justify-center shrink-0 mt-0.5">
                <svg class="w-5 h-5 text-whatsapp-dark" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
            </div>
            <span class="text-wood-700 leading-relaxed"><strong class="text-wood-950">Diseño a Medida:</strong> Diferentes aperturas (correderas, abatibles, oscilobatientes) y colores (imitación madera, lacados RAL).</span>
        </li>
    </ul>
</div>

<p class="mb-6 leading-relaxed">
    No solo instalamos <strong>ventanas de aluminio</strong>; también diseñamos e instalamos cerramientos para terrazas, mamparas de baño, persianas motorizadas y mosquiteras a medida. Trabajamos con marcas líderes para garantizarte una inversión que durará toda la vida.
</p>
"""

generate_page({
    "slug": "carpinteria-aluminio-pvc",
    "title": "Carpintería de Aluminio en Alicante | Ventanas y Cerramientos",
    "description": "Especialistas en aluminios en Alicante. Instalación de ventanas de aluminio, PVC, cerramientos y mosquiteras. Pide presupuesto por WhatsApp.",
    "h1": "Carpintería de Aluminio y PVC en Alicante",
    "h2": "Fabricantes e Instaladores de Aluminios en Alicante",
    "hero_subtitle": "Fabricación e instalación de ventanas, puertas, cerramientos y mosquiteras con la máxima eficiencia energética.",
    "hero_image": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&q=80",
    "wa_link": "https://wa.me/34600000000?text=Hola,%20necesito%20presupuesto%20para%20aluminios/PVC",
    "content_html": aluminio_content
})

# 2. Generate Puertas
puertas_content = """
<p class="mb-6 leading-relaxed">
    Si estás buscando cambiar las puertas de tu vivienda o negocio, somos especialistas en la <strong>instalación de puertas en alicante</strong>. Contamos con un amplio catálogo que abarca desde puertas de paso clásicas y modernas, hasta soluciones acorazadas de máxima seguridad.
</p>

<p class="mb-8 leading-relaxed">
    Nuestras <strong>puertas de madera</strong> están fabricadas con materiales nobles y acabados impecables que aportan calidez y elegancia a cualquier estancia. Además, no solo cuidan la estética de tu hogar, sino que nuestras puertas mejoran significativamente el aislamiento térmico y acústico de las habitaciones.
</p>

<div class="bg-white p-8 rounded-3xl shadow-sm border border-wood-100 mb-10">
    <h3 class="font-bold text-2xl text-wood-950 mb-6 flex items-center gap-3">
        <svg class="w-8 h-8 text-whatsapp" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/></svg>
        ¿Por qué elegir nuestras puertas?
    </h3>
    <ul class="space-y-4 list-none pl-0 m-0">
        <li class="flex items-start gap-4">
            <div class="w-8 h-8 rounded-full bg-whatsapp/10 flex items-center justify-center shrink-0 mt-0.5">
                <svg class="w-5 h-5 text-whatsapp-dark" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
            </div>
            <span class="text-wood-700 leading-relaxed"><strong class="text-wood-950">Máxima Seguridad:</strong> Protege a tu familia con puertas blindadas y acorazadas de última tecnología con cerraduras antibumping.</span>
        </li>
        <li class="flex items-start gap-4">
            <div class="w-8 h-8 rounded-full bg-whatsapp/10 flex items-center justify-center shrink-0 mt-0.5">
                <svg class="w-5 h-5 text-whatsapp-dark" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
            </div>
            <span class="text-wood-700 leading-relaxed"><strong class="text-wood-950">Aislamiento Acústico Superior:</strong> Puertas macizas y semi-macizas que evitan ruidos indeseados entre habitaciones, garantizando tu descanso.</span>
        </li>
        <li class="flex items-start gap-4">
            <div class="w-8 h-8 rounded-full bg-whatsapp/10 flex items-center justify-center shrink-0 mt-0.5">
                <svg class="w-5 h-5 text-whatsapp-dark" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
            </div>
            <span class="text-wood-700 leading-relaxed"><strong class="text-wood-950">Diseños Exclusivos:</strong> Desde lacadas en blanco que aportan luz, hasta maderas naturales (roble, nogal, haya) para dar ese toque premium.</span>
        </li>
        <li class="flex items-start gap-4">
            <div class="w-8 h-8 rounded-full bg-whatsapp/10 flex items-center justify-center shrink-0 mt-0.5">
                <svg class="w-5 h-5 text-whatsapp-dark" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
            </div>
            <span class="text-wood-700 leading-relaxed"><strong class="text-wood-950">Instalación Profesional:</strong> Nos encargamos de todo. Retiramos tus puertas viejas y dejamos las nuevas perfectamente selladas y ajustadas.</span>
        </li>
    </ul>
</div>

<p class="mb-6 leading-relaxed">
    Tanto si buscas <strong>puertas alicante</strong> para una reforma integral como si quieres actualizar las de tu salón, nuestro equipo de carpinteros montadores te asesorará sin compromiso para encontrar el modelo perfecto que encaje con el estilo decorativo de tu hogar.
</p>
"""

generate_page({
    "slug": "puertas-madera",
    "title": "Puertas en Alicante | Puertas de Paso, Blindadas y Acorazadas",
    "description": "Instaladores de puertas en Alicante. Amplio catálogo en puertas de madera a medida, de interior y exterior. Seguridad y diseño.",
    "h1": "Instalación de Puertas en Alicante",
    "h2": "Puertas de Madera a Medida para tu Hogar",
    "hero_subtitle": "Diseño, seguridad y calidez para tu hogar. Puertas de interior y exterior a medida.",
    "hero_image": "https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&q=80",
    "wa_link": "https://wa.me/34600000000?text=Hola,%20necesito%20presupuesto%20para%20puertas",
    "content_html": puertas_content
})

