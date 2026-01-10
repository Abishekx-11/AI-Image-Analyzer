const uploadImageBtn = document.getElementById('uploadImageBtn');
const uploadSection = document.getElementById('uploadSection');
const mainButtons = document.getElementById('mainButtons')

uploadImageBtn.addEventListener('click', function()
{
    mainButtons.classList.add('hidden');
    uploadSection.classList.remove('hidden');
})