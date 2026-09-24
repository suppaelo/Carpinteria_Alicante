import re
import os

with open(r'g:\Seo\carpinteria web\index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract header and footer
parts1 = index_content.split('<main>')
head_and_header = parts1[0] + '<main>'

parts2 = index_content.split('<!-- ═══════════════════ FOOTER ═══════════════════ -->')
footer_and_scripts = '<!-- ═══════════════════ FOOTER ═══════════════════ -->' + parts2[1]

# Modify head meta tags
hh = head_and_header
hh = re.sub(r'<title>.*?</title>', '<title>Carpintería de Aluminio en Alicante | Ventanas y Cerramientos</title>', hh)
hh = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="Especialistas en aluminios en Alicante. Instalación de ventanas de aluminio, PVC, cerramientos y mosquiteras.">', hh)
hh = re.sub(r'<link rel="canonical" href=".*?">', '<link rel="canonical" href="https://carpinteriaalicante.com/carpinteria-aluminio-pvc.html">', hh)

wa_link = 'https://wa.me/34600000000?text=Hola,%20necesito%20presupuesto%20para%20aluminios/PVC'
hh = re.sub(r'https://wa\.me/34600000000\?text=[^"]+', wa_link, hh)
fs = footer_and_scripts
fs = re.sub(r'https://wa\.me/34600000000\?text=[^"]+', wa_link, fs)

main_content = f"""
    <!-- ═══════════════════ HERO INTERNO ═══════════════════ -->
    <section class="relative pt-24 lg:pt-32 pb-16 lg:pb-24 flex items-center justify-center min-h-[50vh] overflow-hidden">
        <div class="absolute inset-0">
            <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&q=80" alt="Carpintería de Aluminio y PVC" class="w-full h-full object-cover object-center hero-bg" loading="eager">
            <div class="absolute inset-0 bg-black/50"></div>
        </div>

        <div class="relative z-10 w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center reveal">
            <h1 class="font-display text-4xl md:text-5xl lg:text-7xl font-bold text-white tracking-tight mb-6 drop-shadow-lg">
                Carpintería de Aluminio y PVC
            </h1>
            <p class="text-xl text-white/90 max-w-2xl mx-auto drop-shadow-md">
                Fabricación e instalación de ventanas, puertas, cerramientos y mosquiteras con la máxima eficiencia energética en Alicante.
            </p>
        </div>
    </section>

    <!-- ═══════════════════ CONTENIDO Y SIDEBAR (GRID 12) ═══════════════════ -->
    <section class="py-16 relative bg-wood-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
                
                <!-- Columna Izquierda (70% -> col-span-8) -->
                <div class="lg:col-span-8">
                    <article class="prose prose-lg prose-wood max-w-none text-wood-800 reveal">
                        <h2 class="font-display text-3xl font-bold text-wood-950 mb-6">Fabricantes e Instaladores de Aluminios en Alicante</h2>
                        
                        <p class="mb-6 leading-relaxed">
                            Si buscas <strong>aluminios Alicante</strong> de máxima calidad, somos tu mejor opción. Nos especializamos en la fabricación y montaje de soluciones a medida tanto en aluminio como en PVC, ofreciendo el equilibrio perfecto entre estética, durabilidad y aislamiento térmico.
                        </p>
                        
                        <p class="mb-8 leading-relaxed">
                            Como expertos en <strong>carpinteria de aluminio en alicante</strong>, sabemos que una buena ventana o un cerramiento bien instalado no solo mejora el aspecto de tu hogar, sino que reduce drásticamente tus facturas de luz y gas al aislar la vivienda del frío, el calor y el ruido exterior.
                        </p>

                        <div class="bg-white p-8 rounded-2xl shadow-sm border border-wood-100 mb-10">
                            <h3 class="font-bold text-2xl text-wood-950 mb-6 border-b pb-4">Ventajas de nuestras Ventanas de Aluminio y PVC</h3>
                            <ul class="space-y-6 list-none pl-0 m-0">
                                <li class="flex items-start gap-4">
                                    <div class="w-12 h-12 rounded-full bg-wood-100 text-wood-600 flex items-center justify-center shrink-0 shadow-sm border border-wood-200">
                                        <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"/></svg>
                                    </div>
                                    <div>
                                        <strong class="text-wood-950 block text-lg mb-1">Eficiencia Energética (RPT)</strong>
                                        <span class="text-wood-700 leading-relaxed text-sm">Aislamiento total con Rotura de Puente Térmico que mantiene la temperatura ideal de tu casa todo el año.</span>
                                    </div>
                                </li>
                                <li class="flex items-start gap-4">
                                    <div class="w-12 h-12 rounded-full bg-wood-100 text-wood-600 flex items-center justify-center shrink-0 shadow-sm border border-wood-200">
                                        <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15.536 8.464a5 5 0 010 7.072M18.364 5.636a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z"/></svg>
                                    </div>
                                    <div>
                                        <strong class="text-wood-950 block text-lg mb-1">Aislamiento Acústico</strong>
                                        <span class="text-wood-700 leading-relaxed text-sm">Cristales Climalit de alto rendimiento para disfrutar del silencio total en el interior, sin molestias del tráfico.</span>
                                    </div>
                                </li>
                                <li class="flex items-start gap-4">
                                    <div class="w-12 h-12 rounded-full bg-wood-100 text-wood-600 flex items-center justify-center shrink-0 shadow-sm border border-wood-200">
                                        <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
                                    </div>
                                    <div>
                                        <strong class="text-wood-950 block text-lg mb-1">Alta Durabilidad</strong>
                                        <span class="text-wood-700 leading-relaxed text-sm">Materiales ultra resistentes a la humedad, al sol y a la corrosión marina, perfectos para la costa alicantina.</span>
                                    </div>
                                </li>
                                <li class="flex items-start gap-4">
                                    <div class="w-12 h-12 rounded-full bg-wood-100 text-wood-600 flex items-center justify-center shrink-0 shadow-sm border border-wood-200">
                                        <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4 5a1 1 0 011-1h14a1 1 0 011 1v2a1 1 0 01-1 1H5a1 1 0 01-1-1V5zM4 13a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H5a1 1 0 01-1-1v-6zM16 13a1 1 0 011-1h2a1 1 0 011 1v6a1 1 0 01-1 1h-2a1 1 0 01-1-1v-6z"/></svg>
                                    </div>
                                    <div>
                                        <strong class="text-wood-950 block text-lg mb-1">Diseño a Medida</strong>
                                        <span class="text-wood-700 leading-relaxed text-sm">Diferentes aperturas (correderas, abatibles, oscilobatientes) y colores (imitación madera, lacados RAL).</span>
                                    </div>
                                </li>
                            </ul>
                        </div>

                        <p class="mb-6 leading-relaxed">
                            No solo instalamos <strong>ventanas de aluminio</strong>; también diseñamos e instalamos cerramientos para terrazas, mamparas de baño, persianas motorizadas y mosquiteras a medida. Trabajamos con marcas líderes para garantizarte una inversión que durará toda la vida.
                        </p>
                    </article>
                </div>

                <!-- Columna Derecha (30% -> col-span-4) -->
                <aside class="lg:col-span-4 relative">
                    <!-- Sidebar Sticky Flotante de WhatsApp -->
                    <div class="sticky top-24 bg-white rounded-3xl p-8 shadow-2xl border border-gray-100 text-center reveal transform transition hover:-translate-y-1 duration-300">
                        <div class="w-20 h-20 bg-whatsapp/10 rounded-full flex items-center justify-center mx-auto mb-6">
                            <svg class="w-10 h-10 text-whatsapp" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
                        </div>
                        <h3 class="font-display text-2xl font-bold text-wood-950 mb-3">¿Hablamos de tu proyecto?</h3>
                        <p class="text-wood-600 mb-8 leading-relaxed text-sm">
                            No esperes más. Consigue un precio cerrado sin sorpresas.
                        </p>
                        <a href="{wa_link}" target="_blank" rel="noopener noreferrer"
                           class="w-full inline-flex items-center justify-center gap-3 bg-whatsapp hover:bg-whatsapp-hover text-white font-bold text-lg px-6 py-4 rounded-xl shadow-lg shadow-whatsapp/30 transition-all active:scale-95">
                            Pedir Presupuesto
                        </a>
                        
                        <div class="mt-6 pt-5 border-t border-wood-100 flex flex-col gap-2 text-sm text-wood-500 font-medium">
                            <span class="flex items-center justify-center gap-2">
                                <svg class="w-4 h-4 text-whatsapp" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                                Presupuesto 100% Gratis
                            </span>
                            <span class="flex items-center justify-center gap-2">
                                <svg class="w-4 h-4 text-whatsapp" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                                Respuesta en menos de 10 min
                            </span>
                        </div>
                    </div>
                </aside>

            </div>
        </div>
    </section>
"""

full_html = hh + main_content + fs

with open(r'g:\Seo\carpinteria web\carpinteria-aluminio-pvc.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print('Regenerado carpinteria-aluminio-pvc.html con diseño perfecto.')
