const featureSections = document.querySelectorAll('.feature');

featureSections.forEach(section => {
  section.addEventListener('click', () => {
    const link = section.id;
    window.open(link, '_blank');
  });
});
const dockerButton = document.getElementById('docker-button');

dockerButton.addEventListener('click', () => {
  window.open('docker.html', '_blank');
});

