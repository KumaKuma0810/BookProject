document.getElementById("toggleButton").onclick = function() {
    var moreText = document.getElementById("moreText");
    
    if (moreText.style.display === "none") {
        moreText.style.display = "block"; // Показываем текст
        this.innerHTML = "Скрыть"; // Меняем текст кнопки
    } else {
        moreText.style.display = "none"; // Скрываем текст
        this.innerHTML = "Показать больше"; // Меняем текст кнопки обратно
    }
};