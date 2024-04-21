function openWindow(name, imageUrl, descriptionEN, descriptionBG) {

    var overlay = document.createElement('div');
    overlay.style.position = 'fixed';
    overlay.style.top = 0;
    overlay.style.left = 0;
    overlay.style.width = '100%';
    overlay.style.height = '100%';
    overlay.style.backgroundColor = 'rgba(0,0,0,0.5)';
    overlay.style.display = 'flex';
    overlay.style.justifyContent = 'center';
    overlay.style.alignItems = 'center';

    var modal = document.createElement('div');
    modal.style.position = 'relative';
    modal.style.backgroundColor = 'rgba(255, 255, 255, 0.8)';
    modal.style.padding = '50px';
    modal.style.width = '50%';
    modal.style.maxWidth = '100%';
    modal.style.display = 'flex';

    var img = document.createElement('img');
    img.src = imageUrl;
    img.style.width = '32%';
    img.style.height = 'auto';
    img.style.transform = 'scale(1.2)';
    img.style.transition = 'transform 0.25s ease, margin-right 0.25s ease';
    img.style.cursor = 'zoom-in';
    img.style.objectFit = 'cover';
    setTimeout(function() {
        img.style.transform = 'scale(1)';
        img.style.marginRight = '20px';
    }, 250);
    modal.appendChild(img);

    img.addEventListener('mouseover', function() {
        img.style.transform = 'scale(1.4) translateX(-15%)';
    });
    img.addEventListener('mouseout', function() {
        img.style.transform = 'scale(1.2)';
    });

    var content = document.createElement('div');
    content.style.width = '60%';
    content.style.paddingLeft = '20px';

    var title = document.createElement('h1');
    title.textContent = name;
    content.appendChild(title);

    var buttonElementEN = document.createElement('button');
    buttonElementEN.textContent = 'EN  ';
    buttonElementEN.id = 'buttonEN';
    buttonElementEN.style.outline = 'none';
    buttonElementEN.addEventListener('click', function() {
        var descriptionTextEN = document.getElementById('descriptionTextEN');
        descriptionTextEN.style.display = descriptionTextEN.style.display === 'block' ? 'none' : 'block';
    });
    content.appendChild(buttonElementEN);
    
    var descriptionElementEN = document.createElement('p');
    descriptionElementEN.textContent = "⠀⠀" + descriptionEN;
    descriptionElementEN.id = 'descriptionTextEN';
    descriptionElementEN.style.display = 'none';
    content.appendChild(descriptionElementEN);
    
    var buttonElementBG = document.createElement('button');
    buttonElementBG.textContent = 'BG  ';
    buttonElementBG.id = 'buttonBG';
    buttonElementBG.style.outline = 'none';

    buttonElementBG.addEventListener('click', function() {
        var descriptionTextBG = document.getElementById('descriptionTextBG');
        descriptionTextBG.style.display = descriptionTextBG.style.display === 'block' ? 'none' : 'block';
    });
    content.appendChild(buttonElementBG);
    
    var descriptionElementBG = document.createElement('p');
    descriptionElementBG.textContent = "⠀⠀" + descriptionBG;
    descriptionElementBG.id = 'descriptionTextBG';
    descriptionElementBG.style.display = 'none';
    content.appendChild(descriptionElementBG);

    var closeButton = document.createElement('button');
    closeButton.textContent = '✘';
    closeButton.style.position = 'absolute';
    closeButton.style.top = '10px';
    closeButton.style.right = '10px';
    closeButton.style.border = 'none';
    closeButton.style.background = 'none';
    closeButton.style.fontSize = '20px';    
    closeButton.style.cursor = 'pointer';
    closeButton.style.outline = '0';

    closeButton.addEventListener('click', function(event) {
        event.stopPropagation();
        document.body.removeChild(overlay);
    });

    modal.appendChild(content);
    modal.appendChild(closeButton);

    closeButton.addEventListener('click', function(event) {
        event.stopPropagation();
        document.body.removeChild(overlay);
    });

    overlay.appendChild(modal);
    document.body.appendChild(overlay);
}

window.openWindow = openWindow;