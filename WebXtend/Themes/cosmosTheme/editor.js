document.addEventListener('DOMContentLoaded', () => {
    let isEditing = false;

    const editBtn = document.getElementById('edit-toggle');
    const allLinks = document.querySelectorAll('.link-card');

    editBtn.addEventListener('click', () => {
      isEditing = !isEditing;
      document.body.classList.toggle('editing-mode', isEditing);

      if (isEditing) {
        editBtn.innerHTML = '<i class="fas fa-check"></i> Done';
      } else {
        editBtn.innerHTML = '<i class="fas fa-edit"></i> Edit';
      }
    });

    allLinks.forEach(linkCard => {
      linkCard.addEventListener('click', (e) => {
        if (!isEditing) return;

        e.preventDefault(); // Prevent link navigation in edit mode

        const nameEl = linkCard.querySelector('.link-name');
        const iconEl = linkCard.querySelector('.link-icon i');

        const currentName = nameEl.textContent;
        const currentURL = linkCard.href;
        const currentIcon = Array.from(iconEl.classList).join(' ');

        const newName = prompt('Enter new link name:', currentName);
        const newURL = prompt('Enter new URL:', currentURL);
        const newIcon = prompt('Enter new Font Awesome class:', currentIcon); // example: "fab fa-google"

        if (newName) nameEl.textContent = newName;
        if (newURL) linkCard.href = newURL;
        if (newIcon) iconEl.className = newIcon;
      });
    });
  });
