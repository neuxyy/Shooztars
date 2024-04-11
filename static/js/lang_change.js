function changeLanguage(lang) {
    if (lang === 'BG') {

        document.getElementById('bgButton').innerText = 'New BG Text';

    } else if (lang === 'EN') {

        document.getElementById('enButton').innerText = 'New EN Text';
        
    }
    document.cookie = "django_language=" + lang;
    location.reload();
}