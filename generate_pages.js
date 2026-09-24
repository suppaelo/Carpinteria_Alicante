const fs = require('fs');
const path = require('path');

const indexFile = path.join(__dirname, 'index.html');
const indexContent = fs.readFileSync(indexFile, 'utf8');

// Extract header and footer
const parts1 = indexContent.split('<main>');
if (parts1.length < 2) {
    console.error("Error: Could not find <main> in index.html");
    process.exit(1);
}
const headAndHeader = parts1[0] + '<main>';

const parts2 = indexContent.split('<!-- ═══════════════════ FOOTER ═══════════════════ -->');
if (parts2.length < 2) {
    console.error("Error: Could not find FOOTER comment in index.html");
    process.exit(1);
}
const footerAndScripts = '<!-- ═══════════════════ FOOTER ═══════════════════ -->' + parts2[1];

function generatePage(config) {
    let hh = headAndHeader;
    
    // Replace Meta Tags & Title
    hh = hh.replace(/<title>.*?<\/title>/g, `<title>${config.title}</title>`);
    hh = hh.replace(/<meta name="description" content=".*?">/g, `<meta name="description" content="${config.description}">`);
    hh = hh.replace(/<link rel="canonical" href=".*?">/g, `<link rel="canonical" href="https://carpinteriaalicante.com/${config.slug}.html">`);
    hh = hh.replace(/<meta property="og:title" content=".*?">/g, `<meta property="og:title" content="${config.title}">`);
    hh = hh.replace(/<meta property="og:description" content=".*?">/g, `<meta property="og:description" content="${config.description}">`);
    hh = hh.replace(/<meta property="og:url" content=".*?">/g, `<meta property="og:url" content="https://carpinteriaalicante.com/${config.slug}.html">`);
    hh = hh.replace(/<meta property="og:image" content=".*?">/g, `<meta property="og:image" content="https://carpinteriaalicante.com/${config.hero_image}">`);

    // Replace WhatsApp links in the header and footer
    hh = hh.replace(/https:\/\/wa\.me\/(?:34)?\d+\?text=[^"]+/g, config.wa_link);
    let fs_content = footerAndScripts.replace(/https:\/\/wa\.me\/(?:34)?\d+\?text=[^"]+/g, config.wa_link);

    const mainContent = `
    <!-- ═══════════════════ HERO INTERNO ═══════════════════ -->
    <section class="relative pt-24 lg:pt-32 pb-16 lg:pb-24 flex items-center justify-center min-h-[40vh] overflow-hidden">
        <!-- Background -->
        <div class="absolute inset-0">
            <img src="${config.hero_image}" alt="${config.h1}" class="w-full h-full object-cover object-center hero-bg" loading="eager">
            <div class="absolute inset-0 bg-wood-950/70 mix-blend-multiply"></div>
            <div class="absolute inset-0 bg-gradient-to-t from-wood-50 via-transparent to-transparent"></div>
        </div>

        <div class="relative z-10 w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center reveal">
            <h1 class="font-display text-4xl md:text-5xl lg:text-6xl font-bold text-white tracking-tight mb-4 leading-tight">
                ${config.h1}
            </h1>
            <p class="text-lg md:text-xl text-white/80 max-w-2xl mx-auto">
                ${config.hero_subtitle}
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
                        <h2 class="font-display text-3xl font-bold text-wood-950 mb-6">${config.h2}</h2>
                        
                        ${config.content_html}
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
                            <svg class="w-8 h-8 text-whatsapp" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
                            </svg>
                        </div>
                        <h3 class="font-display text-2xl font-bold text-wood-950 mb-3">¿Necesitas presupuesto?</h3>
                        <p class="text-wood-600 mb-6 text-sm leading-relaxed">
                            Contáctanos ahora y recibe una valoración sin compromiso para tu proyecto.
                        </p>
                        <a href="${config.wa_link}" target="_blank" rel="noopener noreferrer"
                           class="wa-glow w-full inline-flex items-center justify-center gap-3 bg-whatsapp hover:bg-whatsapp-hover text-white font-bold text-lg px-6 py-4 rounded-2xl shadow-xl shadow-whatsapp/30 transition-all active:scale-95">
                            Pedir Presupuesto WhatsApp
                        </a>
                        <a href="tel:+34603087323"
                           class="mt-3 w-full inline-flex items-center justify-center gap-2 bg-wood-100 hover:bg-wood-200 text-wood-950 font-bold text-base px-6 py-3.5 rounded-2xl transition-colors">
                            <svg class="w-5 h-5 text-wood-700" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 002.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 01-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 00-1.091-.852H4.5A2.25 2.25 0 002.25 4.5v2.25z"/></svg>
                            Llamar: 603 08 73 23
                        </a>
                        <div class="mt-6 pt-4 border-t border-wood-100 flex flex-col gap-2.5 text-xs text-wood-600 font-medium text-left">
                            <span class="flex items-center gap-2">
                                <svg class="w-4 h-4 text-whatsapp shrink-0" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                                <span>Sin intermediarios — Trato directo</span>
                            </span>
                            <span class="flex items-center gap-2">
                                <svg class="w-4 h-4 text-whatsapp shrink-0" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                                <span>Calidad profesional garantizada</span>
                            </span>
                            <span class="flex items-center gap-2">
                                <svg class="w-4 h-4 text-whatsapp shrink-0" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1115 0z"/></svg>
                                <span>C. del Cid, 22, 3F, 03001 Alicante</span>
                            </span>
                        </div>
                    </div>
                </aside>

            </div>
        </div>
    </section>
    `;

    const fullHtml = hh + mainContent + fs_content;
    const destPath = path.join(__dirname, `${config.slug}.html`);
    fs.writeFileSync(destPath, fullHtml, 'utf8');
    console.log(`Generated: ${config.slug}.html`);
}

// ═══════════════════ PAGES CONFIGURATION ═══════════════════

const pages = [
    {
        slug: "muebles-a-medida",
        title: "Muebles a Medida en Alicante | Carpintería de Madera Personalizada",
        description: "Diseño y fabricación de muebles a medida en Alicante. Salones, librerías, vestidores, armarios y mobiliario auxiliar con acabados excelentes.",
        h1: "Muebles a Medida en Alicante",
        h2: "Diseño y Fabricación de Mobiliario de Madera a Medida",
        hero_subtitle: "Diseñamos y fabricamos muebles a medida que se adaptan a tu espacio, estilo y presupuesto.",
        hero_image: "img/muebles-medida.png",
        wa_link: "https://wa.me/34603087323?text=Hola,%20necesito%20presupuesto%20para%20muebles%20a%20medida",
        content_html: `
            <p class="mb-6 leading-relaxed">
                Si buscas aprovechar al máximo cada centímetro de tu casa u oficina, nuestro servicio de <strong>muebles a medida en Alicante</strong> es la solución perfecta. Fabricamos todo tipo de mobiliario en madera, combinando técnicas artesanales con maquinaria moderna para lograr acabados impecables y de alta durabilidad.
            </p>
            <p class="mb-8 leading-relaxed">
                Nos adaptamos completamente a tus gustos y necesidades. Diseñamos desde modernos muebles de salón, librerías y estanterías integradas, hasta dormitorios completos, mesas de comedor y muebles auxiliares. Trabajamos con maderas nobles, tableros de alta densidad y una gran variedad de lacados.
            </p>
            
            <div class="rounded-2xl overflow-hidden shadow-lg border border-wood-100 my-8">
                <img src="img/muebles-medida-interior.jpg" alt="Muebles a medida en Alicante" class="w-full h-64 md:h-96 object-cover object-center hover:scale-105 transition-transform duration-700">
            </div>

            <div class="bg-white p-8 rounded-3xl shadow-sm border border-wood-100 mb-10">
                <h3 class="font-bold text-2xl text-wood-950 mb-6 flex items-center gap-3">
                    <svg class="w-8 h-8 text-whatsapp" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/></svg>
                    ¿Qué nos diferencia?
                </h3>
                <ul class="space-y-4 list-none pl-0 m-0">
                    <li class="flex items-start gap-4">
                        <div class="w-8 h-8 rounded-full bg-whatsapp/10 flex items-center justify-center shrink-0 mt-0.5">
                            <svg class="w-5 h-5 text-whatsapp-dark" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                        </div>
                        <span class="text-wood-700 leading-relaxed"><strong class="text-wood-950">Ajuste de Precisión:</strong> Tomamos medidas al milímetro para que tus muebles encajen perfectamente en paredes, rincones o bajo techos abuhardillados.</span>
                    </li>
                    <li class="flex items-start gap-4">
                        <div class="w-8 h-8 rounded-full bg-whatsapp/10 flex items-center justify-center shrink-0 mt-0.5">
                            <svg class="w-5 h-5 text-whatsapp-dark" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                        </div>
                        <span class="text-wood-700 leading-relaxed"><strong class="text-wood-950">Materiales de Calidad:</strong> Utilizamos tableros resistentes, herrajes de marcas líderes con cierre suave y maderas tratadas.</span>
                    </li>
                    <li class="flex items-start gap-4">
                        <div class="w-8 h-8 rounded-full bg-whatsapp/10 flex items-center justify-center shrink-0 mt-0.5">
                            <svg class="w-5 h-5 text-whatsapp-dark" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                        </div>
                        <span class="text-wood-700 leading-relaxed"><strong class="text-wood-950">Diseño Personalizado:</strong> Elige la distribución de cajones, baldas, tipos de puertas (batientes, correderas) y tiradores a tu gusto.</span>
                    </li>
                </ul>
            </div>
        `
    },
    {
        slug: "puertas-madera",
        title: "Puertas en Alicante | Puertas de Paso, Blindadas y Acorazadas",
        description: "Instaladores de puertas en Alicante. Amplio catálogo en puertas de interior de madera, puertas blindadas y acorazadas de seguridad.",
        h1: "Instalación de Puertas en Alicante",
        h2: "Puertas de Interior y de Seguridad a Medida",
        hero_subtitle: "Aporta calidez, estilo y máxima seguridad a tu hogar con nuestras puertas instaladas por profesionales.",
        hero_image: "img/puertas-madera.png",
        wa_link: "https://wa.me/34603087323?text=Hola,%20necesito%20presupuesto%20para%20puertas",
        content_html: `
            <p class="mb-6 leading-relaxed">
                Si buscas renovar las puertas de tu vivienda o negocio, somos especialistas en la <strong>instalación de puertas en Alicante</strong>. Contamos con un extenso catálogo de puertas de paso de madera (macizas y semi-macizas) y soluciones acorazadas o blindadas para proteger tu hogar.
            </p>
            <p class="mb-8 leading-relaxed">
                Nuestras puertas no solo destacan por su elegancia y variedad de acabados (roble, nogal, lacados en blanco), sino que también mejoran sensiblemente el aislamiento acústico y térmico entre habitaciones, proporcionando mayor privacidad y confort.
            </p>
            
            <div class="rounded-2xl overflow-hidden shadow-lg border border-wood-100 my-8">
                <img src="img/puertas-interior.jpg" alt="Instalación de puertas en Alicante" class="w-full h-64 md:h-96 object-cover object-center hover:scale-105 transition-transform duration-700">
            </div>

            <div class="bg-white p-8 rounded-3xl shadow-sm border border-wood-100 mb-10">
                <h3 class="font-bold text-2xl text-wood-950 mb-6 flex items-center gap-3">
                    <svg class="w-8 h-8 text-whatsapp" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/></svg>
                    Nuestras Soluciones de Portajes
                </h3>
                <ul class="space-y-4 list-none pl-0 m-0">
                    <li class="flex items-start gap-4">
                        <div class="w-8 h-8 rounded-full bg-whatsapp/10 flex items-center justify-center shrink-0 mt-0.5">
                            <svg class="w-5 h-5 text-whatsapp-dark" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                        </div>
                        <span class="text-wood-700 leading-relaxed"><strong class="text-wood-950">Puertas de Paso:</strong> Diseños modernos, clásicos o lacados en blanco liso con fresados personalizados y manivelas de diseño.</span>
                    </li>
                    <li class="flex items-start gap-4">
                        <div class="w-8 h-8 rounded-full bg-whatsapp/10 flex items-center justify-center shrink-0 mt-0.5">
                            <svg class="w-5 h-5 text-whatsapp-dark" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                        </div>
                        <span class="text-wood-700 leading-relaxed"><strong class="text-wood-950">Puertas Blindadas y Acorazadas:</strong> Refuerzos de acero, bisagras de seguridad antipalanca y cerraduras multipunto de alta seguridad.</span>
                    </li>
                    <li class="flex items-start gap-4">
                        <div class="w-8 h-8 rounded-full bg-whatsapp/10 flex items-center justify-center shrink-0 mt-0.5">
                            <svg class="w-5 h-5 text-whatsapp-dark" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                        </div>
                        <span class="text-wood-700 leading-relaxed"><strong class="text-wood-950">Montaje y Remate Profesional:</strong> Retiramos los marcos viejos e instalamos tapajuntas y guarniciones perfectas sin dañar la pintura.</span>
                    </li>
                </ul>
            </div>
        `
    },
    {
        slug: "armarios-empotrados",
        title: "Armarios Empotrados en Alicante | Vestidores a Medida",
        description: "Diseño y fabricación de armarios empotrados y vestidores a medida en Alicante. Puertas correderas o batientes y distribución interior personalizada.",
        h1: "Armarios Empotrados en Alicante",
        h2: "Armarios y Vestidores a Medida con Interiores Personalizados",
        hero_subtitle: "Maximiza tu capacidad de almacenaje con soluciones inteligentes adaptadas a tus prendas.",
        hero_image: "img/armarios-empotrados.png",
        wa_link: "https://wa.me/34603087323?text=Hola,%20necesito%20presupuesto%20para%20armarios%20o%20vestidores",
        content_html: `
            <p class="mb-6 leading-relaxed">
                Un armario bien distribuido marca la diferencia en el orden diario de tu hogar. Como especialistas en <strong>armarios empotrados en Alicante</strong>, diseñamos, fabricamos e instalamos armarios a medida y vestidores abiertos o cerrados que aprovechan al máximo el espacio disponible.
            </p>
            <p class="mb-8 leading-relaxed">
                Tanto si prefieres puertas correderas (ideales para habitaciones pequeñas) como puertas batientes clásicas, nos encargamos de forrar y distribuir el interior de tu armario con cajoneras, baldas ajustables, pantaloneros extraíbles e iluminación LED integrada.
            </p>

            <div class="rounded-2xl overflow-hidden shadow-lg border border-wood-100 my-8">
                <img src="img/armarios-interior.jpg" alt="Armarios a medida en Alicante" class="w-full h-64 md:h-96 object-cover object-center hover:scale-105 transition-transform duration-700">
            </div>

            <div class="bg-white p-8 rounded-3xl shadow-sm border border-wood-100 mb-10">
                <h3 class="font-bold text-2xl text-wood-950 mb-6 flex items-center gap-3">
                    <svg class="w-8 h-8 text-whatsapp" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/></svg>
                    Opciones de Personalización
                </h3>
                <ul class="space-y-4 list-none pl-0 m-0">
                    <li class="flex items-start gap-4">
                        <div class="w-8 h-8 rounded-full bg-whatsapp/10 flex items-center justify-center shrink-0 mt-0.5">
                            <svg class="w-5 h-5 text-whatsapp-dark" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                        </div>
                        <span class="text-wood-700 leading-relaxed"><strong class="text-wood-950">Puertas Exteriores:</strong> Correderas de suave deslizamiento, batientes o plegables en lacados, madera natural, espejo o cristal templado.</span>
                    </li>
                    <li class="flex items-start gap-4">
                        <div class="w-8 h-8 rounded-full bg-whatsapp/10 flex items-center justify-center shrink-0 mt-0.5">
                            <svg class="w-5 h-5 text-whatsapp-dark" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                        </div>
                        <span class="text-wood-700 leading-relaxed"><strong class="text-wood-950">Interiores a Medida:</strong> Cajones con frente de cristal o madera, zapateros extraíbles, barras abatibles y baldas a diferentes alturas.</span>
                    </li>
                    <li class="flex items-start gap-4">
                        <div class="w-8 h-8 rounded-full bg-whatsapp/10 flex items-center justify-center shrink-0 mt-0.5">
                            <svg class="w-5 h-5 text-whatsapp-dark" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                        </div>
                        <span class="text-wood-700 leading-relaxed"><strong class="text-wood-950">Vestidores Completos:</strong> Soluciones abiertas tipo boutique con acabados de lujo para organizar toda tu ropa y complementos.</span>
                    </li>
                </ul>
            </div>
        `
    },
    {
        slug: "cocinas-a-medida",
        title: "Cocinas a Medida en Alicante | Muebles de Cocina y Baño",
        description: "Fabricación e instalación de cocinas a medida y muebles de baño en Alicante. Diseños modernos y funcionales de gran calidad y durabilidad.",
        h1: "Cocinas a Medida en Alicante",
        h2: "Fabricación de Mobiliario de Cocina y Baño Moderno y Funcional",
        hero_subtitle: "Creamos cocinas y baños confortables, ergonómicos y con materiales resistentes a la humedad y al uso diario.",
        hero_image: "img/cocinas-medida.png",
        wa_link: "https://wa.me/34603087323?text=Hola,%20necesito%20presupuesto%20para%20cocinas%20o%20ba%C3%B1os",
        content_html: `
            <p class="mb-6 leading-relaxed">
                La cocina es el corazón del hogar. Por eso, en nuestro servicio de <strong>cocinas a medida en Alicante</strong>, combinamos estética y ergonomía para crear un espacio donde dé gusto cocinar y convivir. Diseñamos muebles de cocina resistentes que optimizan las zonas de trabajo y almacenamiento.
            </p>
            <p class="mb-8 leading-relaxed">
                Del mismo modo, diseñamos <strong>muebles de baño</strong> a medida, suspendidos o apoyados, con acabados antihumedad para asegurar una larga vida útil. Nos encargamos de todo el proceso de carpintería y montaje coordinando los detalles al milímetro.
            </p>

            <div class="rounded-2xl overflow-hidden shadow-lg border border-wood-100 my-8">
                <img src="img/cocinas-interior.jpg" alt="Cocinas a medida en Alicante" class="w-full h-64 md:h-96 object-cover object-center hover:scale-105 transition-transform duration-700">
            </div>

            <div class="bg-white p-8 rounded-3xl shadow-sm border border-wood-100 mb-10">
                <h3 class="font-bold text-2xl text-wood-950 mb-6 flex items-center gap-3">
                    <svg class="w-8 h-8 text-whatsapp" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/></svg>
                    Calidad y Resistencia
                </h3>
                <ul class="space-y-4 list-none pl-0 m-0">
                    <li class="flex items-start gap-4">
                        <div class="w-8 h-8 rounded-full bg-whatsapp/10 flex items-center justify-center shrink-0 mt-0.5">
                            <svg class="w-5 h-5 text-whatsapp-dark" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                        </div>
                        <span class="text-wood-700 leading-relaxed"><strong class="text-wood-950">Materiales de Alta Gama:</strong> Maderas macizas tratadas, estratificados de alta presión (HPL) y lacados con resistencia UV.</span>
                    </li>
                    <li class="flex items-start gap-4">
                        <div class="w-8 h-8 rounded-full bg-whatsapp/10 flex items-center justify-center shrink-0 mt-0.5">
                            <svg class="w-5 h-5 text-whatsapp-dark" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                        </div>
                        <span class="text-wood-700 leading-relaxed"><strong class="text-wood-950">Herrajes Premium:</strong> Guías amortiguadas de gran capacidad de carga y bisagras regulables de alta durabilidad.</span>
                    </li>
                    <li class="flex items-start gap-4">
                        <div class="w-8 h-8 rounded-full bg-whatsapp/10 flex items-center justify-center shrink-0 mt-0.5">
                            <svg class="w-5 h-5 text-whatsapp-dark" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                        </div>
                        <span class="text-wood-700 leading-relaxed"><strong class="text-wood-950">Aprovechamiento de Espacio:</strong> Rinconeras extraíbles, cajoneras cuberteras dobles y despenseros extraíbles en columna.</span>
                    </li>
                </ul>
            </div>
        `
    },
    {
        slug: "suelos-tarima-parquet",
        title: "Instalación de Parquet y Tarima en Alicante | Suelos de Madera",
        description: "Instaladores de tarima flotante, parquet y suelos laminados en Alicante. Instalación rápida, limpia y con excelentes acabados.",
        h1: "Suelos y Tarimas en Alicante",
        h2: "Instalación Profesional de Tarima Flotante, Parquet y Laminados",
        hero_subtitle: "Cambia la imagen y la calidez de tus habitaciones con suelos de madera de alta calidad.",
        hero_image: "img/suelos-tarima.png",
        wa_link: "https://wa.me/34603087323?text=Hola,%20necesito%20presupuesto%20para%20suelos%20o%20tarimas",
        content_html: `
            <p class="mb-6 leading-relaxed">
                Pocos elementos cambian tanto la sensación de confort de un hogar como el suelo. Nos especializamos en la <strong>instalación de tarima en Alicante</strong>, ofreciendo suelos laminados, vinílicos e impermeables y parquets tradicionales de madera natural.
            </p>
            <p class="mb-8 leading-relaxed">
                Realizamos un montaje profesional, asegurando la perfecta nivelación, el correcto sellado acústico mediante bases aislantes de calidad y la colocación de rodapiés a juego para un acabado impecable y duradero frente a golpes y rozaduras.
            </p>

            <div class="rounded-2xl overflow-hidden shadow-lg border border-wood-100 my-8">
                <img src="img/suelos-interior.jpg" alt="Instalación de tarimas y suelos en Alicante" class="w-full h-64 md:h-96 object-cover object-center hover:scale-105 transition-transform duration-700">
            </div>

            <div class="bg-white p-8 rounded-3xl shadow-sm border border-wood-100 mb-10">
                <h3 class="font-bold text-2xl text-wood-950 mb-6 flex items-center gap-3">
                    <svg class="w-8 h-8 text-whatsapp" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/></svg>
                    Nuestros Suelos de Madera y Sintéticos
                </h3>
                <ul class="space-y-4 list-none pl-0 m-0">
                    <li class="flex items-start gap-4">
                        <div class="w-8 h-8 rounded-full bg-whatsapp/10 flex items-center justify-center shrink-0 mt-0.5">
                            <svg class="w-5 h-5 text-whatsapp-dark" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                        </div>
                        <span class="text-wood-700 leading-relaxed"><strong class="text-wood-950">Tarima Flotante:</strong> Parquet multicapa de madera real. Combina la belleza natural con una gran estabilidad térmica.</span>
                    </li>
                    <li class="flex items-start gap-4">
                        <div class="w-8 h-8 rounded-full bg-whatsapp/10 flex items-center justify-center shrink-0 mt-0.5">
                            <svg class="w-5 h-5 text-whatsapp-dark" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                        </div>
                        <span class="text-wood-700 leading-relaxed"><strong class="text-wood-950">Suelos Laminados (AC4 y AC5):</strong> Identidad y altísima dureza, ideales para hogares con mascotas y alto tránsito.</span>
                    </li>
                    <li class="flex items-start gap-4">
                        <div class="w-8 h-8 rounded-full bg-whatsapp/10 flex items-center justify-center shrink-0 mt-0.5">
                            <svg class="w-5 h-5 text-whatsapp-dark" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                        </div>
                        <span class="text-wood-700 leading-relaxed"><strong class="text-wood-950">Suelos de Vinilo (SPC):</strong> Suelos 100% resistentes al agua y a la humedad, aptos para baños, cocinas y locales comerciales.</span>
                    </li>
                </ul>
            </div>
        `
    },
    {
        slug: "carpinteria-aluminio-pvc",
        title: "Carpintería de Aluminio en Alicante | Ventanas y Cerramientos",
        description: "Especialistas en aluminios en Alicante. Instalación de ventanas de aluminio, PVC, cerramientos y mosquiteras. Máxima eficiencia energética.",
        h1: "Carpintería de Aluminio y PVC en Alicante",
        h2: "Fabricación e Instalación de Ventanas y Cerramientos a Medida",
        hero_subtitle: "Fabricación propia y montaje limpio con rotura de puente térmico para aislar tu vivienda del frío y del calor.",
        hero_image: "img/aluminio-pvc.png",
        wa_link: "https://wa.me/34603087323?text=Hola,%20necesito%20presupuesto%20para%20aluminio/PVC",
        content_html: `
            <p class="mb-6 leading-relaxed">
                Si buscas <strong>aluminios en Alicante</strong>, te ofrecemos perfiles de máxima calidad en aluminio y PVC. Nos especializamos en la fabricación y montaje de ventanas de apertura oscilobatiente, correderas de alta estanqueidad y cerramientos herméticos para balcones y porches.
            </p>
            <p class="mb-8 leading-relaxed">
                Trabajar con perfiles de aluminio con Rotura de Puente Térmico (RPT) o PVC multicámara reduce considerablemente el consumo energético en aire acondicionado y calefacción, aislando el interior de tu hogar del clima exterior y los ruidos de la calle.
            </p>

            <div class="rounded-2xl overflow-hidden shadow-lg border border-wood-100 my-8">
                <img src="img/aluminio-interior.jpg" alt="Ventanas de aluminio y PVC en Alicante" class="w-full h-64 md:h-96 object-cover object-center hover:scale-105 transition-transform duration-700">
            </div>

            <div class="bg-white p-8 rounded-3xl shadow-sm border border-wood-100 mb-10">
                <h3 class="font-bold text-2xl text-wood-950 mb-6 flex items-center gap-3">
                    <svg class="w-8 h-8 text-whatsapp" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/></svg>
                    Aislamiento y Ahorro
                </h3>
                <ul class="space-y-4 list-none pl-0 m-0">
                    <li class="flex items-start gap-4">
                        <div class="w-8 h-8 rounded-full bg-whatsapp/10 flex items-center justify-center shrink-0 mt-0.5">
                            <svg class="w-5 h-5 text-whatsapp-dark" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                        </div>
                        <span class="text-wood-700 leading-relaxed"><strong class="text-wood-950">Aislamiento Térmico RPT:</strong> Perfiles aislados interiormente que impiden la transferencia de calor y evitan la condensación.</span>
                    </li>
                    <li class="flex items-start gap-4">
                        <div class="w-8 h-8 rounded-full bg-whatsapp/10 flex items-center justify-center shrink-0 mt-0.5">
                            <svg class="w-5 h-5 text-whatsapp-dark" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                        </div>
                        <span class="text-wood-700 leading-relaxed"><strong class="text-wood-950">Acristalamiento Doble o Triple:</strong> Cristales inteligentes tipo Climalit con filtros solares bajo emisivos de gran rendimiento acústico.</span>
                    </li>
                    <li class="flex items-start gap-4">
                        <div class="w-8 h-8 rounded-full bg-whatsapp/10 flex items-center justify-center shrink-0 mt-0.5">
                            <svg class="w-5 h-5 text-whatsapp-dark" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                        </div>
                        <span class="text-wood-700 leading-relaxed"><strong class="text-wood-950">Resistencia Climatológica:</strong> Materiales duraderos frente a la exposición solar, el viento salino y la corrosión costera.</span>
                    </li>
                </ul>
            </div>
        `
    },
    {
        slug: "ebanisteria-restauracion",
        title: "Ebanistería en Alicante | Restauración y Creaciones de Madera",
        description: "Servicios de ebanistería artística y restauración de muebles en Alicante. Talla de madera, barnizado tradicional y recuperación de piezas antiguas.",
        h1: "Ebanistería y Restauración en Alicante",
        h2: "Ebanistería Artesanal y Recuperación de Muebles Antiguos",
        hero_subtitle: "Ebanistas experimentados en la talla, barnizados a muñequilla y carpintería fina artesanal.",
        hero_image: "img/ebanisteria.png",
        wa_link: "https://wa.me/34603087323?text=Hola,%20necesito%20presupuesto%20para%20ebanister%C3%ADa%20o%20restauraci%C3%B3n",
        content_html: `
            <p class="mb-6 leading-relaxed">
                La ebanistería es un arte y un oficio que requiere paciencia, mimo y profundo conocimiento de las vetas y comportamiento de cada tipo de madera. En nuestro taller de <strong>ebanistería en Alicante</strong>, realizamos trabajos de carpintería fina y restauramos muebles con valor histórico o sentimental.
            </p>
            <p class="mb-8 leading-relaxed">
                Utilizamos técnicas tradicionales como el encolado orgánico, el barnizado de goma laca aplicado a muñequilla, tintes naturales y ceras de abeja, devolviendo el esplendor original a cajoneras, mesas antiguas, portones y tallas clásicas deterioradas por el paso de los años.
            </p>

            <div class="rounded-2xl overflow-hidden shadow-lg border border-wood-100 my-8">
                <img src="img/ebanisteria-interior.jpg" alt="Trabajo de ebanistería y restauración en Alicante" class="w-full h-64 md:h-96 object-cover object-center hover:scale-105 transition-transform duration-700">
            </div>

            <div class="bg-white p-8 rounded-3xl shadow-sm border border-wood-100 mb-10">
                <h3 class="font-bold text-2xl text-wood-950 mb-6 flex items-center gap-3">
                    <svg class="w-8 h-8 text-whatsapp" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/></svg>
                    Oficio y Técnica
                </h3>
                <ul class="space-y-4 list-none pl-0 m-0">
                    <li class="flex items-start gap-4">
                        <div class="w-8 h-8 rounded-full bg-whatsapp/10 flex items-center justify-center shrink-0 mt-0.5">
                            <svg class="w-5 h-5 text-whatsapp-dark" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                        </div>
                        <span class="text-wood-700 leading-relaxed"><strong class="text-wood-950">Restauración Reversible:</strong> Respetamos el carácter e historia del mueble usando adhesivos y métodos reversibles no agresivos.</span>
                    </li>
                    <li class="flex items-start gap-4">
                        <div class="w-8 h-8 rounded-full bg-whatsapp/10 flex items-center justify-center shrink-0 mt-0.5">
                            <svg class="w-5 h-5 text-whatsapp-dark" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                        </div>
                        <span class="text-wood-700 leading-relaxed"><strong class="text-wood-950">Tratamiento de Carcoma:</strong> Curación y prevención biológica activa frente a plagas que dañan y debilitan la estructura interna.</span>
                    </li>
                    <li class="flex items-start gap-4">
                        <div class="w-8 h-8 rounded-full bg-whatsapp/10 flex items-center justify-center shrink-0 mt-0.5">
                            <svg class="w-5 h-5 text-whatsapp-dark" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                        </div>
                        <span class="text-wood-700 leading-relaxed"><strong class="text-wood-950">Barnizado Tradicional:</strong> Acabados clásicos sedosos de alta calidad a base de gomalaca o ceras naturales protectoras.</span>
                    </li>
                </ul>
            </div>
        `
    }
];

// Generate all pages
pages.forEach(generatePage);
console.log("All pages compiled successfully in perfect symbiosis with index.html");
