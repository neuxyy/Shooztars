function changeLanguage(lang) {
    
    if (lang === 'BG') {
    
    } else if (lang === 'EN') {
    
    }
    document.cookie = "django_language=" + lang;

    location.reload();
}