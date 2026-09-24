import re
import os

with open(r'g:\Seo\carpinteria web\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Split around <main> and FOOTER
parts1 = content.split('<main>')
head_and_header = parts1[0] + '<main>'

parts2 = content.split('<!-- ═══════════════════ FOOTER ═══════════════════ -->')
footer_and_scripts = '<!-- ═══════════════════ FOOTER ═══════════════════ -->' + parts2[1]

# Modify head meta tags
head_and_header = re.sub(
    r'<title>.*?</title>',
    '<title>Carpintería de Aluminio en Alicante | Ventanas y Cerramientos</title>',
    head_and_header
)
head_and_header = re.sub(
    r'<meta name="description" content=".*?">',
    '<meta name="description" content="Especialistas en aluminios en Alicante. Instalación de ventanas de aluminio, PVC, cerramientos y mosquiteras. Pide presupuesto por WhatsApp.">',
    head_and_header
)
head_and_header = re.sub(
    r'<link rel="canonical" href=".*?">',
    '<link rel="canonical" href="https://carpinteriaalicante.com/carpinteria-aluminio-pvc">',
    head_and_header
)
head_and_header = re.sub(
    r'<meta property="og:title" content=".*?">',
    '<meta property="og:title" content="Carpintería de Aluminio en Alicante | Ventanas y Cerramientos">',
    head_and_header
)
head_and_header = re.sub(
    r'<meta property="og:description" content=".*?">',
    '<meta property="og:description" content="Especialistas en aluminios en Alicante. Instalación de ventanas de aluminio, PVC, cerramientos y mosquiteras. Pide presupuesto por WhatsApp.">',
    head_and_header
)
head_and_header = re.sub(
    r'<meta property="og:url" content=".*?">',
    '<meta property="og:url" content="https://carpinteriaalicante.com/carpinteria-aluminio-pvc">',
    head_and_header
)
head_and_header = re.sub(
    r'<meta property="og:image" content=".*?">',
    '<meta property="og:image" content="https://carpinteriaalicante.com/img/aluminio-pvc.png">',
    head_and_header
)

# Update WhatsApp links in the entire document to pre-fill the requested text
wa_link = 'https://wa.me/34600000000?text=Hola,%20necesito%20presupuesto%20para%20aluminios/PVC'
head_and_header = re.sub(r'https://wa\.me/34600000000\?text=[^"]+', wa_link, head_and_header)
footer_and_scripts = re.sub(r'https://wa\.me/34600000000\?text=[^"]+', wa_link, footer_and_scripts)

main_content = """
    <!-- ═══════════════════ HERO INTERNO ═══════════════════ -->
    <section class="relative pt-24 lg:pt-32 pb-16 lg:pb-24 flex items-center justify-center min-h-[40vh] overflow-hidden">
        <!-- Background -->
        <div class="absolute inset-0">
            <img src="img/aluminio-pvc.png" alt="Carpintería de aluminio y PVC en Alicante" class="w-full h-full object-cover object-center hero-bg">
            <div class="absolute inset-0 bg-wood-950/70 mix-blend-multiply"></div>
            <div class="absolute inset-0 bg-gradient-to-t from-wood-50 via-transparent to-transparent"></div>
        </div>

        <div class="relative z-10 w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center reveal">
            <h1 class="font-display text-4xl md:text-5xl lg:text-6xl font-bold text-white tracking-tight mb-4 leading-tight">
                Carpintería de Aluminio y PVC en Alicante
            </h1>
            <p class="text-lg md:text-xl text-white/80 max-w-2xl mx-auto">
                Fabricación e instalación de ventanas, puertas, cerramientos y mosquiteras con la máxima eficiencia energética.
            </p>
        </div>
    </section>

    <!-- ═══════════════════ CONTENIDO Y SIDEBAR ═══════════════════ -->
    <section class="py-12 lg:py-20 relative bg-wood-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex flex-col lg:flex-row gap-12 lg:gap-16">
                
                <!-- Contenido principal (70%) -->
                <div class="w-full lg:w-[65%]">
                    <article class="prose prose-lg prose-wood max-w-none text-wood-800 reveal">
                        <h2 class="font-display text-3xl font-bold text-wood-950 mb-6">Fabricantes e Instaladores de Aluminios en Alicante</h2>
                        
                        <p class="mb-6 leading-relaxed">
                            Si buscas <strong>aluminios Alicante</strong> de máxima calidad, somos tu mejor opción. Nos especializamos en la fabricación y montaje de soluciones a medida tanto en aluminio como en PVC, ofreciendo el equilibrio perfecto entre estética, durabilidad y aislamiento térmico.
                        </p>
                        
                        <p class="mb-6 leading-relaxed">
                            Como expertos en <strong>carpinteria de aluminio en alicante</strong>, sabemos que una buena ventana o un cerramiento bien instalado no solo mejora el aspecto de tu hogar, sino que reduce drásticamente tus facturas de luz y gas al aislar la vivienda del frío, el calor y el ruido exterior.
                        </p>

                        <h3 class="font-bold text-xl text-wood-900 mt-8 mb-4">Ventajas de nuestras Ventanas de Aluminio y PVC</h3>
                        <ul class="space-y-3 mb-8 list-none pl-0">
                            <li class="flex items-start gap-3">
                                <svg class="w-6 h-6 text-whatsapp shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                                <span><strong>Eficiencia Energética (Rotura de Puente Térmico):</strong> Aislamiento total que mantiene la temperatura ideal de tu casa todo el año.</span>
                            </li>
                            <li class="flex items-start gap-3">
                                <svg class="w-6 h-6 text-whatsapp shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                                <span><strong>Aislamiento Acústico:</strong> Cristales Climalit de alto rendimiento para disfrutar del silencio total en el interior.</span>
                            </li>
                            <li class="flex items-start gap-3">
                                <svg class="w-6 h-6 text-whatsapp shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                                <span><strong>Alta Durabilidad:</strong> Materiales resistentes a la humedad, al sol y a la corrosión marina (ideal para zonas de costa).</span>
                            </li>
                            <li class="flex items-start gap-3">
                                <svg class="w-6 h-6 text-whatsapp shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                                <span><strong>Diseño a Medida:</strong> Diferentes aperturas (correderas, abatibles, oscilobatientes) y colores (imitación madera, lacados RAL).</span>
                            </li>
                        </ul>

                        <div class="rounded-2xl overflow-hidden shadow-lg mb-8">
                            <img src="img/aluminio-pvc.png" alt="Instalación de ventanas de aluminio en Alicante" class="w-full h-auto object-cover hover:scale-105 transition-transform duration-700">
                        </div>

                        <p class="mb-6 leading-relaxed">
                            No solo instalamos <strong>ventanas de aluminio</strong>; también diseñamos e instalamos cerramientos para terrazas, mamparas de baño, persianas motorizadas y mosquiteras a medida. Trabajamos con marcas líderes para garantizarte una inversión que durará toda la vida.
                        </p>
                    </article>

                    <!-- FAQS / Método -->
                    <div class="mt-16 reveal border-t border-wood-200 pt-10">
                        <h3 class="font-display text-2xl font-bold text-wood-950 mb-8">Nuestro método de trabajo (Simple y Rápido)</h3>
                        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                            <div class="bg-white p-6 rounded-2xl shadow-sm border border-wood-100 relative">
                                <div class="absolute -top-4 -left-4 w-10 h-10 bg-wood-800 text-white flex items-center justify-center font-bold text-xl rounded-full shadow-lg">1</div>
                                <h4 class="font-bold text-wood-900 mb-2 mt-2">Contáctanos</h4>
                                <p class="text-sm text-wood-600">Escríbenos por WhatsApp o llámanos. Cuéntanos qué necesitas (medidas aproximadas, fotos).</p>
                            </div>
                            <div class="bg-white p-6 rounded-2xl shadow-sm border border-wood-100 relative">
                                <div class="absolute -top-4 -left-4 w-10 h-10 bg-wood-800 text-white flex items-center justify-center font-bold text-xl rounded-full shadow-lg">2</div>
                                <h4 class="font-bold text-wood-900 mb-2 mt-2">Medimos y Presupuestamos</h4>
                                <p class="text-sm text-wood-600">Un técnico se desplazará a tu domicilio para tomar medidas exactas y darte un presupuesto cerrado, sin sorpresas.</p>
                            </div>
                            <div class="bg-white p-6 rounded-2xl shadow-sm border border-wood-100 relative">
                                <div class="absolute -top-4 -left-4 w-10 h-10 bg-whatsapp text-white flex items-center justify-center font-bold text-xl rounded-full shadow-lg">3</div>
                                <h4 class="font-bold text-wood-900 mb-2 mt-2">Instalación Limpia</h4>
                                <p class="text-sm text-wood-600">Fabricamos a medida y montamos de forma rápida y limpia. Retiramos el material antiguo si es necesario.</p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Sidebar Sticky (30%) -->
                <aside class="w-full lg:w-[35%] relative">
                    <div class="sticky top-32 bg-white rounded-3xl p-8 shadow-xl shadow-wood-900/5 border border-wood-100 text-center reveal">
                        <div class="w-16 h-16 bg-whatsapp/10 rounded-full flex items-center justify-center mx-auto mb-6">
                            <svg class="w-8 h-8 text-whatsapp" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
                        </div>
                        <h3 class="font-display text-2xl font-bold text-wood-950 mb-3">¿Necesitas este servicio?</h3>
                        <p class="text-wood-600 mb-8 leading-relaxed">
                            No esperes más. Pide tu <strong>presupuesto rápido, gratis y sin compromiso</strong> en menos de 5 minutos.
                        </p>
                        <a href="https://wa.me/34600000000?text=Hola,%20necesito%20presupuesto%20para%20aluminios/PVC" target="_blank" rel="noopener noreferrer"
                           class="wa-glow w-full inline-flex items-center justify-center gap-3 bg-whatsapp hover:bg-whatsapp-hover text-white font-bold text-lg px-8 py-4 rounded-xl shadow-lg transition-all active:scale-95">
                            WhatsApp Rápido
                        </a>
                        
                        <div class="mt-6 flex flex-col gap-2 text-sm text-wood-500 font-medium">
                            <span class="flex items-center justify-center gap-2">
                                <svg class="w-4 h-4 text-wood-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                                Trato directo, sin intermediarios
                            </span>
                            <span class="flex items-center justify-center gap-2">
                                <svg class="w-4 h-4 text-wood-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                                Calidad garantizada
                            </span>
                        </div>
                    </div>
                </aside>

            </div>
        </div>
    </section>
    
    </main>
"""

full_html = head_and_header + main_content + footer_and_scripts

with open(r'g:\Seo\carpinteria web\carpinteria-aluminio-pvc.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print('Regenerated carpinteria-aluminio-pvc.html correctly.')
