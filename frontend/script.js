document.getElementById('convertBtn').addEventListener('click', async () => {
  const fileInput = document.getElementById('imageInput');
  const formatSelect = document.getElementById('formatSelect');
  const resultDiv = document.getElementById('result');

  if (!fileInput.files.length) {
    alert('Please select an image file');
    return;
  }

  const formData = new FormData();
  formData.append('image', fileInput.files[0]);
  formData.append('format', formatSelect.value);

  resultDiv.textContent = 'Converting...';

  try {
    const response = await fetch('http://localhost:5000/convert', {
      method: 'POST',
      body: formData
    });

    if (!response.ok) {
      const error = await response.json();
      resultDiv.textContent = 'Error: ' + (error.error || 'Unknown error');
      return;
    }

    const blob = await response.blob();
    const url = URL.createObjectURL(blob);
    resultDiv.innerHTML = `<a href="${url}" download="converted.${formatSelect.value}">Download converted image</a>`;
  } catch (err) {
    resultDiv.textContent = 'Error: ' + err.message;
  }
});
