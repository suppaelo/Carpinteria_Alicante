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
hh = re.sub(r'<title>.*?</title>', '<title>Carpintería de Aluminio en Alicante | Ventanas y Cerramientos a Medida</title>', hh)
hh = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="Especialistas en aluminios en Alicante. Instalación de ventanas de aluminio, PVC, cerramientos y mosquiteras. Pide tu presupuesto cerrado en minutos.">', hh)
hh = re.sub(r'<link rel="canonical" href=".*?">', '<link rel="canonical" href="https://carpinteriaalicante.com/carpinteria-aluminio-pvc.html">', hh)

wa_link = 'https://wa.me/34600000000?text=Hola,%20necesito%20presupuesto%20para%20aluminios/PVC'
hh = re.sub(r'https://wa\.me/34600000000\?text=[^"]+', wa_link, hh)
fs = footer_and_scripts
fs = re.sub(r'https://wa\.me/34600000000\?text=[^"]+', wa_link, fs)

main_content = f"""
    <!-- 1. HERO SECTION -->
    <section class="relative pt-24 lg:pt-32 pb-16 lg:pb-24 flex items-center justify-center min-h-[45vh] lg:min-h-[55vh] overflow-hidden">
        <div class="absolute inset-0">
            <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&q=80" alt="Carpintería de Aluminio en Alicante" class="w-full h-full object-cover object-center hero-bg" loading="eager">
            <div class="absolute inset-0 bg-black/60"></div>
            <!-- Subtle gradient to blend with the white section below -->
            <div class="absolute inset-0 bg-gradient-to-t from-wood-50 via-transparent to-transparent"></div>
        </div>

        <div class="relative z-10 w-full max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 text-center reveal">
            <h1 class="font-display text-4xl md:text-5xl lg:text-6xl font-bold text-white tracking-tight mb-6 leading-tight drop-shadow-xl">
                Carpintería de Aluminio en Alicante: <span class="text-wood-200">Ventanas y Cerramientos a Medida</span>
            </h1>
            <p class="text-lg md:text-xl text-gray-200 max-w-3xl mx-auto drop-shadow-md mb-10 font-light">
                Fabricación propia e instalación rápida de sistemas de aluminio y PVC de alta eficiencia energética. Pide tu presupuesto cerrado en minutos.
            </p>
            
            <div class="flex flex-col sm:flex-row items-center justify-center gap-5">
                <a href="tel:+34600000000" class="w-full sm:w-auto inline-flex justify-center items-center gap-3 bg-blue-600 hover:bg-blue-700 text-white font-bold text-lg px-8 py-4 rounded-full shadow-lg transition-transform hover:scale-105">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
                    Llamar Ahora: 600 000 000
                </a>
                <a href="{wa_link}" target="_blank" rel="noopener noreferrer" class="w-full sm:w-auto inline-flex justify-center items-center gap-3 bg-whatsapp hover:bg-whatsapp-hover text-white font-bold text-lg px-8 py-4 rounded-full shadow-lg transition-transform hover:scale-105">
                    <svg class="w-6 h-6" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
                    WhatsApp
                </a>
            </div>
        </div>
    </section>

    <!-- 2. BLOQUE DE INTRODUCCIÓN SEO -->
    <section class="py-16 bg-wood-50">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center reveal">
            <h2 class="font-display text-3xl md:text-4xl font-bold text-wood-950 mb-8">Especialistas en Aluminios en Alicante para Hogares y Negocios</h2>
            <div class="prose prose-lg prose-wood mx-auto text-wood-800">
                <p class="leading-relaxed">
                    A la hora de renovar los cerramientos de una vivienda, contar con una <strong>carpinteria de aluminio en alicante</strong> experta marca la diferencia. Diseñamos e instalamos sistemas que no solo mejoran radicalmente la estética de tus espacios, sino que garantizan un aislamiento térmico y acústico superior, transformando tu hogar en un lugar mucho más confortable.
                </p>
                <p class="leading-relaxed mt-4">
                    Al elegir nuestros <strong>aluminios alicante</strong>, estás invirtiendo en eficiencia energética. Nuestras <strong>ventanas de aluminio</strong> con Rotura de Puente Térmico (RPT) y perfiles de alta calidad impiden que el calor del verano o el frío del invierno penetren en tu casa, lo que se traduce en un ahorro drástico en tus facturas de luz y climatización mensual.
                </p>
                <p class="leading-relaxed mt-4">
                    Como empresa líder de <strong>carpinteria aluminio alicante</strong>, fabricamos a medida para asegurar la máxima durabilidad frente a la humedad, el salitre y las altas temperaturas de la Costa Blanca. Nuestro equipo de instaladores propios se encarga de realizar un montaje rápido, limpio y con unos acabados que simplemente hablan por sí solos.
                </p>
            </div>
        </div>
    </section>

    <!-- 3. TIPOS DE SOLUCIONES Y MATERIALES -->
    <section class="py-20 bg-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <h2 class="font-display text-3xl md:text-4xl font-bold text-wood-950 mb-12 text-center reveal">Nuestras Soluciones en Cerramientos y Perfiles</h2>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
                <!-- Tarjeta 1 -->
                <div class="bg-wood-50 rounded-2xl overflow-hidden shadow-lg border border-wood-100 flex flex-col hover:-translate-y-2 transition-transform duration-300 group reveal">
                    <div class="h-48 overflow-hidden relative">
                        <img src="https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&q=80" alt="Ventanas de Aluminio RPT" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                    </div>
                    <div class="p-6 flex flex-col flex-grow">
                        <h3 class="font-bold text-xl text-wood-950 mb-3">Ventanas de Aluminio RPT</h3>
                        <p class="text-wood-700 text-sm leading-relaxed mb-6 flex-grow">
                            Con Rotura de Puente Térmico para aislar del frío y del calor de Alicante. Diseños elegantes y alta resistencia.
                        </p>
                        <a href="{wa_link}" target="_blank" rel="noopener noreferrer" class="w-full inline-flex justify-center items-center gap-2 bg-white border-2 border-whatsapp text-whatsapp hover:bg-whatsapp hover:text-white font-bold py-2.5 rounded-xl transition-colors">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"/></svg>
                            Consultar Precio
                        </a>
                    </div>
                </div>

                <!-- Tarjeta 2 -->
                <div class="bg-wood-50 rounded-2xl overflow-hidden shadow-lg border border-wood-100 flex flex-col hover:-translate-y-2 transition-transform duration-300 group reveal">
                    <div class="h-48 overflow-hidden relative">
                        <img src="https://images.unsplash.com/photo-1560185007-c5ca9d2c014d?auto=format&fit=crop&q=80" alt="Cerramientos de Terrazas" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                    </div>
                    <div class="p-6 flex flex-col flex-grow">
                        <h3 class="font-bold text-xl text-wood-950 mb-3">Cerramientos de Terrazas</h3>
                        <p class="text-wood-700 text-sm leading-relaxed mb-6 flex-grow">
                            Estructuras herméticas fijas o correderas para aprovechar balcones, áticos y porches durante todo el año.
                        </p>
                        <a href="{wa_link}" target="_blank" rel="noopener noreferrer" class="w-full inline-flex justify-center items-center gap-2 bg-white border-2 border-whatsapp text-whatsapp hover:bg-whatsapp hover:text-white font-bold py-2.5 rounded-xl transition-colors">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"/></svg>
                            Consultar Precio
                        </a>
                    </div>
                </div>

                <!-- Tarjeta 3 -->
                <div class="bg-wood-50 rounded-2xl overflow-hidden shadow-lg border border-wood-100 flex flex-col hover:-translate-y-2 transition-transform duration-300 group reveal">
                    <div class="h-48 overflow-hidden relative">
                        <img src="https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&q=80" alt="Puertas y Ventanas de PVC" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                    </div>
                    <div class="p-6 flex flex-col flex-grow">
                        <h3 class="font-bold text-xl text-wood-950 mb-3">Puertas y Ventanas de PVC</h3>
                        <p class="text-wood-700 text-sm leading-relaxed mb-6 flex-grow">
                            Máximo aislamiento acústico y estanqueidad con perfiles multi-cámara de última generación. Silencio y confort.
                        </p>
                        <a href="{wa_link}" target="_blank" rel="noopener noreferrer" class="w-full inline-flex justify-center items-center gap-2 bg-white border-2 border-whatsapp text-whatsapp hover:bg-whatsapp hover:text-white font-bold py-2.5 rounded-xl transition-colors">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"/></svg>
                            Consultar Precio
                        </a>
                    </div>
                </div>

                <!-- Tarjeta 4 -->
                <div class="bg-wood-50 rounded-2xl overflow-hidden shadow-lg border border-wood-100 flex flex-col hover:-translate-y-2 transition-transform duration-300 group reveal">
                    <div class="h-48 overflow-hidden relative">
                        <img src="https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&q=80" alt="Mosquiteras e Integraciones" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                    </div>
                    <div class="p-6 flex flex-col flex-grow">
                        <h3 class="font-bold text-xl text-wood-950 mb-3">Mosquiteras e Integraciones</h3>
                        <p class="text-wood-700 text-sm leading-relaxed mb-6 flex-grow">
                            Sistemas enrollables, plisados y correderas a medida para proteger tu hogar de insectos sin perder estilo.
                        </p>
                        <a href="{wa_link}" target="_blank" rel="noopener noreferrer" class="w-full inline-flex justify-center items-center gap-2 bg-white border-2 border-whatsapp text-whatsapp hover:bg-whatsapp hover:text-white font-bold py-2.5 rounded-xl transition-colors">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"/></svg>
                            Consultar Precio
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 4. FAQS -->
    <section class="py-20 bg-wood-50">
        <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 reveal">
            <h2 class="font-display text-3xl md:text-4xl font-bold text-wood-950 mb-10 text-center">Preguntas Frecuentes sobre Carpintería de Aluminio</h2>
            
            <div class="space-y-4">
                <!-- FAQ 1 -->
                <details class="group bg-white rounded-2xl shadow-sm border border-wood-100 overflow-hidden open:ring-2 open:ring-wood-200 transition-all">
                    <summary class="flex justify-between items-center font-bold text-wood-900 cursor-pointer p-6 hover:bg-wood-50 transition-colors">
                        <span class="pr-6">¿Cuánto se tarda en instalar unas ventanas de aluminio en Alicante?</span>
                        <span class="transition group-open:rotate-180">
                            <svg class="w-6 h-6 text-wood-500" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/></svg>
                        </span>
                    </summary>
                    <div class="p-6 pt-0 text-wood-700 leading-relaxed bg-white">
                        <p>La fabricación suele tardar entre 2 y 3 semanas, y la instalación en la vivienda se realiza habitualmente en 1 o 2 días sin necesidad de obras molestas.</p>
                    </div>
                </details>

                <!-- FAQ 2 -->
                <details class="group bg-white rounded-2xl shadow-sm border border-wood-100 overflow-hidden open:ring-2 open:ring-wood-200 transition-all">
                    <summary class="flex justify-between items-center font-bold text-wood-900 cursor-pointer p-6 hover:bg-wood-50 transition-colors">
                        <span class="pr-6">¿Qué es mejor para el aislamiento, el aluminio o el PVC?</span>
                        <span class="transition group-open:rotate-180">
                            <svg class="w-6 h-6 text-wood-500" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/></svg>
                        </span>
                    </summary>
                    <div class="p-6 pt-0 text-wood-700 leading-relaxed bg-white">
                        <p>Ambos materiales ofrecen un rendimiento excelente hoy en día. El PVC destaca por su aislamiento acústico natural, mientras que el aluminio con Rotura de Puente Térmico (RPT) permite perfiles más finos y una mayor entrada de luz.</p>
                    </div>
                </details>

                <!-- FAQ 3 -->
                <details class="group bg-white rounded-2xl shadow-sm border border-wood-100 overflow-hidden open:ring-2 open:ring-wood-200 transition-all">
                    <summary class="flex justify-between items-center font-bold text-wood-900 cursor-pointer p-6 hover:bg-wood-50 transition-colors">
                        <span class="pr-6">¿Cómo puedo solicitar un presupuesto para un cerramiento?</span>
                        <span class="transition group-open:rotate-180">
                            <svg class="w-6 h-6 text-wood-500" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/></svg>
                        </span>
                    </summary>
                    <div class="p-6 pt-0 text-wood-700 leading-relaxed bg-white">
                        <p>El proceso es inmediato. Haz clic en nuestros botones de llamada o WhatsApp, facilítanos unas medidas aproximadas o fotos de la zona, y te daremos una valoración sin compromiso en menos de 10 minutos.</p>
                    </div>
                </details>
            </div>
        </div>
    </section>

    <!-- 5. CTA AGRESIVO -->
    <section class="py-24 bg-gradient-to-br from-wood-800 to-wood-950 text-white relative overflow-hidden">
        <!-- Decoración de fondo -->
        <div class="absolute inset-0 opacity-10 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-wood-100 via-transparent to-transparent"></div>
        
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10 reveal">
            <h2 class="font-display text-4xl md:text-5xl font-bold mb-10 drop-shadow-lg">¿Quieres mejorar el aislamiento de tu casa hoy mismo?</h2>
            
            <div class="flex flex-col sm:flex-row items-center justify-center gap-6">
                <a href="tel:+34600000000" class="w-full sm:w-auto inline-flex justify-center items-center gap-3 bg-white text-wood-950 hover:bg-wood-50 font-bold text-xl px-10 py-5 rounded-full shadow-2xl transition-transform hover:scale-105 border-2 border-white">
                    <svg class="w-7 h-7 text-blue-600" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
                    Llamar al 600 000 000
                </a>
                <a href="{wa_link}" target="_blank" rel="noopener noreferrer" class="w-full sm:w-auto inline-flex justify-center items-center gap-3 bg-whatsapp hover:bg-whatsapp-hover text-white font-bold text-xl px-10 py-5 rounded-full shadow-2xl transition-transform hover:scale-105 border-2 border-whatsapp hover:border-whatsapp-hover">
                    <svg class="w-7 h-7" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
                    Presupuesto por WhatsApp
                </a>
            </div>
        </div>
    </section>
"""

full_html = hh + main_content + fs

with open(r'g:\Seo\carpinteria web\carpinteria-aluminio-pvc.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print('Regenerado carpinteria-aluminio-pvc.html con la nueva super landing premium.')
