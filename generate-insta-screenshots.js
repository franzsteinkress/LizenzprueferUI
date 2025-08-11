// Copyright (c) 2025 Franz Steinkress
// Licensed under the MIT License - see LICENSE file for details
//

const puppeteer = require("puppeteer");
const fs = require("fs");
const path = require("path");

const outputDir = path.join(__dirname, "insta-visuals/screenshots");
if (!fs.existsSync(outputDir)) fs.mkdirSync(outputDir);

// Liste der Bilddateien
const images = [
    "flatly.png", "flatly_midblue.png", "journal.png", "cyborg.png", "vapor.png",
    "solar.png", "superhero.png", "darkly.png", "litera.png", "litera_midblue.png",
    "lumen.png", "cosmo.png", "minty.png", "pulse.png", "united.png",
    "yeti.png", "yeti_midblue.png", "neon.png", "glass.png", "neumo.png",
    "claymo.png", "aurora.png", "neo.png"
];

const titles = [
    "Flatly (Material Design)", "Flatly (Mid Blue)", "Journal (Minimal UI)", "Cyborg (Dark Mode)",
    "Vapor (Modern Flat)", "Solar (Retro)", "Superhero (Neo-Brutal)", "Darkly (Dark Flat)",
    "Litera (Clean Light)", "Litera (Mid Blue)", "Lumen (Soft Light)", "Cosmo (Modern Light)",
    "Minty (Fresh Light)", "Pulse (Vibrant)", "United (Bold)", "Yeti (Soft Blue)",
    "Yeti (Mid Blue)", "Dark Neon Mode", "Glassmorphism", "Neumorphism",
    "Claymorphism", "Aurora Art Style", "Neo-Brutal (Gelb)"
];

const descriptions = [
    "Material-inspiriertes Design mit klaren Linien", 
    "Variante mit mittlerem Blauton für moderne Wirkung", 
    "Leichtes, fast papierhaftes Interface für fokussierte Inhalte", 
    "Dunkler Style im Tech-Look mit hohem Kontrast", 
    "Zeitgenössisches Flat-Design mit weichen Farben", 
    "Nostalgisches Retro-Feeling mit warmem Farbschema", 
    "Kraftvolles, kantiges Theme mit plakativem Stil", 
    "Minimalistisches Dark Theme mit dezentem Auftritt", 
    "Aufgeräumtes, klares Design für Lesbarkeit", 
    "Litera mit kühlerem Blauton für sachlichere Darstellung", 
    "Helles Theme mit sanften Kontrasten und flächigem Weiß", 
    "Modernes Interface mit strukturierter Farbgebung", 
    "Frisches, lebendiges UI mit Minzgrün-Akzenten", 
    "Kraftvolles Design mit auffälliger Farbgebung", 
    "Stabiles, farbkräftiges Theme mit politischem Touch", 
    "Kühles, ruhiges UI mit weichen Blautönen", 
    "Yeti in kräftigerem Blau - sachlich und modern", 
    "Dunkles Theme mit Neonfarben für visuelle Spannung", 
    "Transparente Ebenen mit weichen Lichtreflexen", 
    "Weiche Schatten und plastische Tiefe durch Light UI", 
    "Plastisches, rundes Design mit plastilinartiger Wirkung", 
    "Leuchtende Farben und Lichtverläufe wie Polarlichter", 
    "Kontrastreiches, plakatives Theme mit Fokus auf Gelb"
];

const dominantColors = [
    "#2d74b2", "#225b94", "#777", "#121212", "#91d6ff",
    "#ffde88", "#ff3377", "#2f2f2f", "#f9f9f9", "#87b9f7",
    "#f4f4f4", "#e6e6e6", "#d5f5e3", "#f56cb5", "#e95420",
    "#d0e7f9", "#89c2e3", "#1bfffc", "#ffffffcc", "#ebebeb",
    "#dadada", "#f2f2f2", "#f5e342"
];

const fontColors = [
    "#f5f5f5", "#f5f5f5", "#f5f5f5", "#f5f5f5", "#333", 
    "#333", "#333", "#f5f5f5", "#333", "#333", 
    "#333", "#333", "#333", "#333", "#f5f5f5", 
    "#333", "#333", "#333", "#333", "#333", 
    "#333", "#333", "#333"
];

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    await page.setViewport({
        width: 1080,
        height: 1920,
        deviceScaleFactor: 1,
    });

    await page.goto("file://" + __dirname + "/insta-visuals/index.html");

    for (let i = 0; i < images.length; i++) {
        const imageName = images[i];
        const titleName = titles[i];
        const descript = descriptions[i];
        const domColor = dominantColors[i];
        const fontColor = fontColors[i];
        console.log("Verarbeite Bild:", imageName, "Index:", i);

        // Dynamisches Setzen des Bildes und Textes
        await page.evaluate((imgSrc, idx, total, titleName, descript, domColor, fontColor) => {
            try {
                // Bildquelle aktualisieren
                const imgElement = document.querySelector("img");
                if (imgElement) {
                    imgElement.src = `./assets/${imgSrc}`;
                }

                // Text für den Button oder Rahmen aktualisieren
                const textElement = document.querySelector("#closeBtn") || document.querySelector(".frame > div:first-child");
                if (textElement) {
                    textElement.textContent = `Bild ${idx + 1} von ${total}`;
                }

                const textLine1 = document.querySelector("#title.line1")
                if (textLine1) {
                    textLine1.textContent = `${titleName}`;
                }

                const textLine2 = document.querySelector("#description.line2")
                if (textLine2) {
                    textLine2.textContent = `${descript}`;
                }

                const overlayBox = document.querySelector("#overlayBox");
                if (overlayBox) {
                    overlayBox.style.backgroundColor = `${domColor}`;
                    overlayBox.style.color = `${fontColor}`;
                    overlayBox.style.outline = `${domColor}`;
                }
            } catch (error) {
                console.error("Fehler in page.evaluate:", error);
            }
        }, imageName, i, images.length, titleName, descript, domColor, fontColor);

        // Warten, bis das Bild vollständig geladen ist
        await page.waitForFunction(() => {
            const img = document.querySelector("img");
            return img && img.complete && img.naturalHeight > 0;
        });

        // Kurze Verzögerung für Stabilität
        await new Promise(resolve => setTimeout(resolve, 300));

        const filename = `img${i + 1}-${imageName}`;
        const filepath = path.join(outputDir, `${filename}`);
        await page.screenshot({ path: filepath, omitBackground: false });
        console.log("Screenshot gespeichert:", filename);
    }

    await browser.close();
})();