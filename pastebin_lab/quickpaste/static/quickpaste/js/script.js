document.addEventListener('DOMContentLoaded', function() {
    const saveBtn = document.querySelector('.btn-primary');
    const linkContainer = document.querySelector('.link-container');
    const languageSelect = document.querySelector('.language-select');
    const textarea = document.querySelector('.paste-textarea');

    if (saveBtn && linkContainer) {
        saveBtn.addEventListener('click', function() {
            // Показываем блок с ссылкой при нажатии на "Сохранить"
            linkContainer.style.display = 'block';

            // Здесь будет логика сохранения и получения ссылки
            // В демо-версии просто показываем блок
        });

        // Обработчик для кнопки "Копировать"
        const copyBtn = document.querySelector('.btn-copy');
        if (copyBtn) {
            copyBtn.addEventListener('click', function() {
                const linkUrl = document.querySelector('.link-url').textContent;
                navigator.clipboard.writeText(linkUrl).then(() => {
                    copyBtn.textContent = 'Скопировано!';
                    setTimeout(() => {
                        copyBtn.textContent = 'Копировать';
                    }, 2000);
                });
            });
        }
    }
    if (languageSelect && textarea) {
        languageSelect.addEventListener('change', function() {
            // Здесь можно добавить логику подсветки синтаксиса
            console.log('Выбран язык:', this.value);
        });
    }
});