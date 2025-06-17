document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('prompt-form');
    const promptInput = document.getElementById('prompt');
    const temperatureSlider = document.getElementById('temperature');
    const tempValue = document.getElementById('temp-value');
    const generateBtn = document.getElementById('generate-btn');
    const outputDiv = document.getElementById('output');
    const loadingDiv = document.getElementById('loading');

    // Update temperature value display
    temperatureSlider.addEventListener('input', () => {
        tempValue.textContent = temperatureSlider.value;
    });

    // Handle form submission
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        // Get form values
        const prompt = promptInput.value.trim();
        const temperature = parseFloat(temperatureSlider.value);
        
        // Validate input
        if (!prompt) {
            alert('Please enter a prompt');
            return;
        }
        
        // Show loading state
        generateBtn.disabled = true;
        loadingDiv.classList.remove('hidden');
        outputDiv.textContent = '';
        
        try {
            // Send request to backend
            const response = await fetch('/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ prompt, temperature })
            });
            
            const data = await response.json();
            
            // Handle error
            if (data.error) {
                outputDiv.textContent = `Error: ${data.error}`;
                outputDiv.style.color = '#e11d48';
            } else {
                // Display output
                outputDiv.textContent = data.output;
                outputDiv.style.color = '#333';
            }
        } catch (error) {
            outputDiv.textContent = `An error occurred: ${error.message}`;
            outputDiv.style.color = '#e11d48';
        } finally {
            // Hide loading state
            generateBtn.disabled = false;
            loadingDiv.classList.add('hidden');
        }
    });
});