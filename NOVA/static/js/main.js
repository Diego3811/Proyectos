document.addEventListener('DOMContentLoaded', () => {
    const startBtn = document.getElementById('start-btn');
    const aiResponse = document.getElementById('ai-response');
    const coreCircle = document.querySelector('.core-circle');
    const container = document.querySelector('.ai-interface');
    let isListening = false;
    
    // Configurar síntesis de voz
    const synth = window.speechSynthesis;
    let voice = null;

    // Seleccionar voz en español
    function setSpanishVoice() {
        const voices = synth.getVoices();
        voice = voices.find(v => v.lang.includes('es')) || voices[0];
    }

    // Esperar a que las voces estén disponibles
    speechSynthesis.onvoiceschanged = setSpanishVoice;
    
    // Función para hacer hablar a NOVA
    function speak(text) {
        if (synth.speaking) {
            synth.cancel();
        }
        
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.voice = voice;
        utterance.rate = 1.0;
        utterance.pitch = 1.0;
        utterance.volume = 1.0;
        synth.speak(utterance);
    }

    // Inicialización
    speak('NOVA está lista para ayudarte');
    aiResponse.textContent = 'NOVA está lista para ayudarte...';

    startBtn.addEventListener('click', () => {
        container.classList.add('transitioning');
        
        if (!isListening) {
            startListening();
        } else {
            stopListening();
        }
        
        setTimeout(() => {
            container.classList.remove('transitioning');
        }, 1000);
    });

    function startListening() {
        isListening = true;
        startBtn.textContent = 'Detener';
        const message = '🎤 NOVA te está escuchando...';
        fadeText(aiResponse, message);
        speak('Te escucho');
        coreCircle.classList.add('listening');
        startBtn.classList.add('listening');
    }

    function stopListening() {
        isListening = false;
        startBtn.textContent = 'Iniciar';
        const message = 'NOVA está esperando...';
        fadeText(aiResponse, message);
        speak('Esperando nuevas instrucciones');
        coreCircle.classList.remove('listening');
        startBtn.classList.remove('listening');
    }

    function fadeText(element, newText) {
        element.style.opacity = '0';
        setTimeout(() => {
            element.textContent = newText;
            element.style.opacity = '1';
        }, 300);
    }
});