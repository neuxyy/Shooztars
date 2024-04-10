function changeLanguage(lang) {
    
    if (lang === 'BG') {
        // Code to switch the website to Bulgarian
    } else if (lang === 'EN') {
        // Code to switch the website to English
    }
    document.cookie = "django_language=" + lang;

    location.reload();
}