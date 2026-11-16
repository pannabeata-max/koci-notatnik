(() => {
  const dialog = document.getElementById('photo-dialog');
  const photo = document.getElementById('photo-full');
  const caption = document.getElementById('photo-caption');
  if (!dialog || !photo || !caption || typeof dialog.showModal !== 'function') return;
  let opener;
  document.querySelectorAll('.gallery-open').forEach(button => {
    button.addEventListener('click', () => {
      opener = button;
      photo.src = button.dataset.photo;
      photo.alt = button.querySelector('img').alt;
      caption.textContent = button.dataset.caption;
      dialog.showModal();
    });
  });
  dialog.querySelector('.photo-close').addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', event => {
    if (event.target !== dialog) return;
    const box = dialog.getBoundingClientRect();
    if (event.clientX < box.left || event.clientX > box.right || event.clientY < box.top || event.clientY > box.bottom) dialog.close();
  });
  dialog.addEventListener('close', () => { if (opener) opener.focus(); });
})();
